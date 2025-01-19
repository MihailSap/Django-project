# ГОТОВО!!! УРА!!!
import pandas as pd
import matplotlib.pyplot as plt
import csv
from collections import Counter

file_path = 'vacancies_2024.csv'
data = []

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
df['published_at'] = pd.to_datetime(df['published_at'], format='%Y-%m-%dT%H:%M:%S%z', errors='coerce', utc=True)
df = df.dropna(subset=['published_at'])
df['year'] = df['published_at'].dt.year

for year in range(2003, 2024 + 1):
    df_year = df[df['year'] == year]
    if df_year.empty:
        print(f"No data for year {year}")
        continue
    df_year = df_year.dropna(subset=['key_skills'])
    skills = df_year['key_skills'].str.split('\n').explode().dropna()
    skills = skills[skills != '']
    skill_counts = Counter(skills)
    top_skills = skill_counts.most_common(20)

    if not top_skills:
        print(f"No skills data for year {year}")
        continue

    skill_names, skill_values = zip(*top_skills)

    plt.figure(figsize=(12, 8))
    plt.barh(skill_names, skill_values, color='red')
    plt.xlabel('Частота', fontsize=14)
    plt.ylabel('Навыки', fontsize=14)
    plt.title(f'Топ-20 навыков в вакансиях за {year} год', fontsize=16)
    plt.gca().invert_yaxis()

    for i, v in enumerate(skill_values):
        plt.text(v + 1, i, str(v), va='center', fontsize=10)

    plt.tight_layout()
    plt.savefig(f'skills_{year}.png')
    plt.show()
