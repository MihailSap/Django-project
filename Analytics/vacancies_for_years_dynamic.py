import pandas as pd
import matplotlib.pyplot as plt
import csv

data = []
file_path = 'vacancies_2024.csv'

keywords = [
    'backend', 'бэкэнд', 'бэкенд', 'бекенд', 'бекэнд',
    'back end', 'бэк энд', 'бэк енд', 'django',
    'flask', 'laravel', 'yii', 'symfony'
]

i = 0
with open(file_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        if len(row) == 7:
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


vacancies_by_year = df['year'].value_counts().sort_index()
plt.figure(figsize=(12, 6))
bars = plt.bar(vacancies_by_year.index, vacancies_by_year.values, color='green', label='Количество вакансий')

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.0f}', ha='center', va='bottom')

plt.title('Динамика количества вакансий по годам', fontsize=16)
plt.xlabel('Год', fontsize=14)
plt.ylabel('Количество вакансий', fontsize=14)
plt.xticks(vacancies_by_year.index, rotation=45)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()
