import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from zipfile import ZipFile
import sqlite3
from sqlalchemy import create_engine

def download_save_file(name_file, url):
    with open(name_file, 'wb') as file:
        print('download iniciado')
        response = requests.get(url)
        file.write(response.content)
        print('download concluído')

def files_link(url, filetype):
    soup = bs(requests.get(url).text, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        file_link = link.get('href')
        if filetype in file_link:
            links.append(file_link)
    return links

def extract_file(name_zip, dir_result):
    try:
        with ZipFile(name_zip, 'r') as zip_ref:
            zip_ref.extractall(dir_result)
        return 'Extração concluída'
    except:
        return 'Arquivo não encontrado'

def conection_database(name_database):
    return create_engine('sqlite:///'+name_database)
