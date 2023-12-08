import fake_useragent
import requests
from bs4 import BeautifulSoup


user = fake_useragent.UserAgent().random
headers = {
    'Accept': 'image/avif,image/webp,*/*',
    'user-agent': user
}


def get_day_periods(url: str) -> list:
    src = requests.get(url, headers=headers).text

    soup = BeautifulSoup(src, 'lxml')
    weather_info = soup.find('div', class_='cols__column__item cols__column__item_2-1 cols__column__item_2-1_ie8')
    all_day_periods = weather_info.find_all('div', class_='day day_period')

    return all_day_periods


def get_weather(url: str) -> str:
    periods = get_day_periods(url)
    for period in periods:
        date = period.find('div', class_='day__date').text
        temperature = period.find('div', class_='day__temperature').text
        description = period.find('div', class_='day__description').find('span').text

        yield f'    {date}: {temperature} {description}'
