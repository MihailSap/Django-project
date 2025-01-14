import datetime
import requests

KEYWORDS = [
    'backend', 'бэкэнд', 'бэкенд', 'бекенд', 'бекэнд', 'back end', 'бэк энд', 'бэк енд',
    'django', 'flask', 'laravel', 'yii', 'symfony'
]


def clean_vacancy(vacancy):
    salary_from = vacancy['salary']['from'] if vacancy['salary'] else None
    salary_to = vacancy['salary']['to'] if vacancy['salary'] else None
    currency = vacancy['salary']['currency'] if vacancy['salary'] else None
    key_skills = ', '.join(x['name'] for x in vacancy['key_skills'])

    if salary_from is not None and salary_to is not None and salary_from != salary_to:
        salary_text = f"от {'{0:,}'.format(salary_from).replace(',', ' ')} до {'{0:,}'.format(salary_to).replace(',', ' ')} {currency}"
    elif salary_from is not None:
        salary_text = f"{'{0:,}'.format(salary_from).replace(',', ' ')} {currency}"
    elif salary_to is not None:
        salary_text = f"{'{0:,}'.format(salary_to).replace(',', ' ')} {currency}"
    else:
        salary_text = 'Нет данных'

    vacancy['salary'] = salary_text
    vacancy['key_skills'] = key_skills

    return vacancy


def matches_keywords(text):
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in KEYWORDS)


def get_vacancies():
    try:
        params = {
            'text': ' OR '.join(KEYWORDS),
            'specialization': 1,
            'page': 1,
            'per_page': 100,
        }
        data = []
        info = requests.get('https://api.hh.ru/vacancies', params=params).json()

        for row in info['items']:
            if row['salary'] and matches_keywords(row['name']):
                data.append({'id': row['id'], 'published_at': row['published_at']})

        data = sorted(data, key=lambda x: x['published_at'])
        vacancies = []

        for vacancy in data[-10:]:
            full_vacancy = requests.get(f'https://api.hh.ru/vacancies/{vacancy["id"]}').json()
            if matches_keywords(full_vacancy['description']):
                vacancies.append(clean_vacancy(full_vacancy))

        return vacancies
    except Exception as e:
        print(e)
        print(datetime.datetime.now())
        return []


if __name__ == "__main__":
    get_vacancies()
