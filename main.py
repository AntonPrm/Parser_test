import requests
from bs4 import BeautifulSoup


url = 'https://quotes.toscrape.com/'

def main():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('span', class_='text')

    for quote in quotes:
        print(quote.text)


if __name__ == '__main__':
    main()
