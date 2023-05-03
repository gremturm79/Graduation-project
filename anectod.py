import requests
from bs4 import BeautifulSoup
import random


class Parent:

    @staticmethod
    def drug():
        url = requests.get('https://anekdoty.ru/pro-narkomanov/').text
        soup = BeautifulSoup(url, parser='html', features='lxml')
        test = soup.find_all('div', class_='holder-body')
        lst = []
        for i in test:
            lst.append(i.text)
        lst1 = [random.choices(lst, k=3)]
        print(' '.join(*lst1))

    @staticmethod
    def shpion():
        url = requests.get('https://anekdoty.ru/pro-shtirlica/').text
        soup = BeautifulSoup(url, parser='html', features='lxml')
        test = soup.find_all('div', class_='holder-body')
        lst = []
        for i in test:
            lst.append(i.text)
        lst1 = [random.choices(lst, k=3)]
        print(' '.join(*lst1))

    @staticmethod
    def gitler():
        url = requests.get('https://anekdoty.ru/pro-gitlera/').text
        soup = BeautifulSoup(url, parser='html', features='lxml')
        test = soup.find_all('div', class_='holder-body')
        lst = []
        for i in test:
            lst.append(i.text)
        lst1 = [random.choices(lst, k=3)]
        print(' '.join(*lst1))

    @staticmethod
    def vovochka():
        url = requests.get('https://anekdoty.ru/pro-vovochku/').text
        soup = BeautifulSoup(url, parser='html', features='lxml')
        test = soup.find_all('div', class_='holder-body')
        lst = []
        for i in test:
            lst.append(i.text)
        lst1 = [random.choices(lst, k=3)]
        print(' '.join(*lst1))

    @staticmethod
    def programmer():
        url = requests.get('https://anekdoty.ru/pro-programmistov/').text
        soup = BeautifulSoup(url, parser='html', features='lxml')
        test = soup.find_all('div', class_='holder-body')
        lst = []
        for i in test:
            lst.append(i.text)
        lst1 = [random.choices(lst, k=3)]
        print(' '.join(*lst1))

    @staticmethod
    def avram():
        url = requests.get('https://anekdoty.ru/pro-evreev/').text
        soup = BeautifulSoup(url, parser='html', features='lxml')
        test = soup.find_all('div', class_='holder-body')
        lst = []
        for i in test:
            lst.append(i.text)
        lst1 = [random.choices(lst, k=3)]
        print(' '.join(*lst1))

drug_jokes = Parent()
# drug_jokes.drug()
# drug_jokes.shpion()
# drug_jokes.gitler()
# drug_jokes.vovochka()
# drug_jokes.programmer()
drug_jokes.avram()




