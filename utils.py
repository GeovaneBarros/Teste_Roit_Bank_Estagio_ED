import requests
from bs4 import BeautifulSoup as bs
from zipfile import ZipFile
import sqlite3

def download_file(name_file, url):
    with open(name_file, 'wb') as file:
        response = requests.get(url)
        file.write(response.content)

def get_soup(url):
    return bs(requests.get(url).text, 'html.parser')

def files_link(url):
    links = []
    for link in get_soup(url).find_all('a'):
        file_link = link.get('href')
        if '.zip' in file_link:
            links.append(file_link)
            
def extract_file(name_zip, dir_result):
    with ZipFile(name_zip, 'r') as zip_ref:
        zip_ref.extractall(dir_result)

def conection_database(name_database):
    con = sqlite3.connect(name_database)
    return con
