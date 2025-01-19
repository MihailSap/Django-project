# СДЕЛАНО
import pandas as pd
import matplotlib.pyplot as plt
import requests
from datetime import datetime
from xml.etree import ElementTree as ET
import csv
from tqdm import tqdm
from collections import defaultdict
import numpy as np

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

city_counts = df['area_name'].value_counts()
total_vacancies = len(df)
df['city_percent'] = df['area_name'].map(city_counts) / total_vacancies
df = df[df['city_percent'] > 0.01]
salary_by_city = df.groupby('area_name')['salary_rub'].mean().sort_values(ascending=False)

top_20_cities = salary_by_city

plt.figure(figsize=(12, 6))
bars = plt.bar(top_20_cities.index, top_20_cities.values, color=['red'] * (len(top_20_cities) // 2 + 1), label='Средняя зарплата')

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.0f}', ha='center', va='bottom')

plt.title('Уровень зарплат по топ-20 городам', fontsize=16)
plt.xlabel('Город', fontsize=14)
plt.ylabel('Средняя зарплата (руб)', fontsize=14)
plt.xticks(rotation=90)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.savefig('salary_cities.png', format='png')
plt.show()
