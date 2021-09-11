import requests
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd
import numpy as np

url = 'https://api.hh.ru/vacancies?industry=7&per_page=1&page=0'
#url = 'https://quotes.toscrape.com/'

def main():
    response = requests.get(url)
    #pprint(response.json())


    vacancy_id = response.json()['items'][0]['alternate_url'].replace('https://hh.ru/vacancy/','')
    vacancy_url = 'https://api.hh.ru/vacancies/' + vacancy_id
    request = requests.get(vacancy_url)
    pprint(request.json())


#soup = BeautifulSoup(response.text, 'lxml')
    #quotes = soup.find_all('span', class_='text')

    #for quote in quotes:
    #    print(quote.text)


if __name__ == '__main__':
    main()
