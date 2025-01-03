import pandas as pd
import matplotlib.pyplot as plt
import csv

from matplotlib import pyplot

keywords = [
    'backend', 'бэкэнд', 'бэкенд', 'бекенд', 'бекэнд',
    'back end', 'бэк энд', 'бэк енд', 'django',
    'flask', 'laravel', 'yii', 'symfony'
]

data = []
file_path = 'vacancies_2024.csv'


with open(file_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        if len(row) == 7:
            first_column = row[0].split(',')[0].lower()
            if any(keyword.lower() in first_column for keyword in keywords):
                data.append(row)
        else:
            print(row)

df = pd.DataFrame(data, columns=header)

df['salary_from'] = pd.to_numeric(df['salary_from'], errors='coerce')
df['salary_to'] = pd.to_numeric(df['salary_to'], errors='coerce')

df = df[(df['salary_from'] < 10000000) & (df['salary_to'] < 10000000)]

df['published_at'] = pd.to_datetime(df['published_at'], format='%Y-%m-%dT%H:%M:%S%z', errors='coerce', utc=True)
df = df.dropna(subset=['published_at'])
df['year'] = df['published_at'].dt.year

df['name'] = df['name'].str.lower()
df = df[df['name'].str.contains('|'.join(keywords), na=False)]

vacancies_by_city = df['area_name'].value_counts()

top_20_cities = vacancies_by_city.head(20)
other_cities_count = vacancies_by_city.iloc[20:].sum()
vacancies_with_other = pd.concat([top_20_cities, pd.Series({'Другие': other_cities_count})])

plt.figure(figsize=(12, 6))
vacancies_with_other.plot(kind='bar', color='blue')
plt.title('Топ-20 городов + остальные по количеству вакансий', fontsize=16)
plt.xlabel('Город', fontsize=14)
plt.ylabel('Количество вакансий', fontsize=14)
plt.xticks(rotation=90)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


colors = pyplot.get_cmap('tab20b', len(vacancies_with_other)).colors
plt.figure(figsize=(8, 8))
vacancies_with_other.plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    legend=False
)
plt.title('Доля вакансий по городам', fontsize=16)
plt.ylabel('')
plt.tight_layout()
plt.show()
