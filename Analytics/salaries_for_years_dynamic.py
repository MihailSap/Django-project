import pandas as pd
import matplotlib.pyplot as plt
import requests
from datetime import datetime
from xml.etree import ElementTree as ET
import csv
from tqdm import tqdm
from collections import defaultdict
tqdm.pandas()

keywords = [
    'backend', 'бэкэнд', 'бэкенд', 'бекенд', 'бекэнд',
    'back end', 'бэк энд', 'бэк енд', 'django',
    'flask', 'laravel', 'yii', 'symfony'
]

file_path = 'vacancies_2024.csv'
data = []
with open(file_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        if len(row) == 7:
            first_column = row[0].split(',')[0].lower()
            if any(keyword.lower() in first_column for keyword in keywords):
                data.append(row)

df = pd.DataFrame(data, columns=header)

df['salary_from'] = pd.to_numeric(df['salary_from'], errors='coerce')
df['salary_to'] = pd.to_numeric(df['salary_to'], errors='coerce')
df = df[(df['salary_from'] < 10000000) & (df['salary_to'] < 10000000)]

df['published_at'] = pd.to_datetime(df['published_at'], format='%Y-%m-%dT%H:%M:%S%z', errors='coerce', utc=True)
df = df.dropna(subset=['published_at'])

currency_rate_cache = defaultdict(dict)

def fetch_currency_rates(year, month):
    """Загружает курсы валют для указанного месяца."""
    month_start_date = datetime(year, month, 1)
    date_str = month_start_date.strftime('%d/%m/%Y')
    url = f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={date_str}'
    response = requests.get(url)

    if response.status_code == 200:
        root = ET.fromstring(response.text)
        for child in root:
            char_code = child.find('CharCode').text
            value = float(child.find('Value').text.replace(',', '.'))
            nominal = float(child.find('Nominal').text)
            currency_rate_cache[(year, month)][char_code] = value / nominal


df['published_at'] = df['published_at'].dt.tz_convert(None)
unique_dates = df['published_at'].dt.to_period('M').drop_duplicates()
for date in tqdm(unique_dates, desc="Загрузка курсов валют"):
    fetch_currency_rates(date.year, date.month)


def convert_to_rub(row):
    if pd.isna(row['salary_from']) and pd.isna(row['salary_to']):
        return None

    salary_from = row['salary_from'] if not pd.isna(row['salary_from']) else row['salary_to']
    salary_to = row['salary_to'] if not pd.isna(row['salary_to']) else row['salary_from']
    avg_salary = (salary_from + salary_to) / 2

    year, month = row['published_at'].year, row['published_at'].month
    currency = row['salary_currency']

    rate = currency_rate_cache.get((year, month), {}).get(currency)
    if rate is None:
        return None

    return avg_salary * rate


df['salary_rub'] = df.progress_apply(convert_to_rub, axis=1)

df = df.dropna(subset=['salary_rub'])

df['year'] = df['published_at'].dt.year
salary_by_year = df.groupby('year')['salary_rub'].mean().sort_index()

plt.figure(figsize=(12, 6))
bars = plt.bar(salary_by_year.index, salary_by_year.values, color='red')

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.0f}', ha='center', va='bottom')

plt.title('Динамика уровня зарплат по годам', fontsize=16)
plt.xlabel('Год', fontsize=14)
plt.ylabel('Средняя зарплата (руб)', fontsize=14)
plt.xticks(salary_by_year.index, rotation=45)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('salary_trends.png', format='png')
plt.show()
