import requests
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
elements_with_class = soup.find_all(class_="external text")

for element in elements_with_class:
    print(element.text)

