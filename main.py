from numpy import dtype
from utils import *
from config import *
import pandas as pd
from os import listdir
from dask import dataframe as dd
import os

link_empresa = files_link(URL, FILETYPE_EMPRESA)[0]
link_estabelecimento = files_link(URL, FILETYPE_ESTABELECIMENTO)[0]
link_socio = files_link(URL, FILETYPE_SOCIO)[0]

if not os.path.exists('download'):
    os.mkdir('download')

download_save_file('./download/'+FILETYPE_EMPRESA,link_empresa)
download_save_file('./download/'+FILETYPE_ESTABELECIMENTO,link_estabelecimento)
download_save_file('./download/'+FILETYPE_SOCIO,link_socio)


print(extract_file('./download/'+FILETYPE_EMPRESA, 'src'))
print(extract_file('./download/'+FILETYPE_ESTABELECIMENTO, 'src'))
print(extract_file('./download/'+FILETYPE_SOCIO, 'src'))


path_csv_empresa = None
path_csv_estabelecimento = None
path_csv_socio = None

for namefile in listdir('src'):
    if FILENAME_EMPRESA in namefile:
        path_csv_empresa = './src/'+namefile

    if FILENAME_ESTABELECIMENTO in namefile:
        path_csv_estabelecimento = './src/'+namefile

    if FILENAME_SOCIO in namefile:
        path_csv_socio = './src/'+namefile

engine = conection_database(NAME_DATABASE)
chunk = 10**2

if path_csv_empresa:
    try:
        df_empresa = dd.read_csv(path_csv_empresa, names=COLUMNS_CNPJ_EMPRESA, dtype=DTYPE_EMPRESA ,sep=';', encoding_errors='ignore')
        dd.to_sql(df=df_empresa, name=TABLE_EMPRESA,uri=str(engine.url), chunksize=chunk, if_exists='replace')
        print('Dados das empresas inseridos no banco')
    except:
        print('Arquivo não suportado')
else:
    print('Arquivo não encontrado')

if path_csv_estabelecimento:
    try:
        df_estabelecimento = dd.read_csv(path_csv_estabelecimento, names=COLUMNS_CNPJ_ESTABELECIMENTO , dtype=DTYPE_ESTABELECIMENTO, sep=';', encoding_errors='ignore')
        dd.to_sql(df=df_estabelecimento, name=TABLE_ESTABELECIMENTO,uri=str(engine.url),chunksize=chunk, if_exists='replace')
        print('Dados dos estabelecimentos inseridos no banco')
    except:
        print('Arquivo não suportado')
else:
    print('Arquivo não encontrado')

if path_csv_socio:
    try:
        df_socio = dd.read_csv(path_csv_socio, names=COLUMNS_CNPJ_SOCIO, dtype=DTYPE_SOCIO, sep=';', encoding_errors='ignore')
        dd.to_sql(df=df_socio, name=TABLE_SOCIO,uri=str(engine.url), chunksize=chunk, if_exists='replace')
        print('Dados dados do socio inseridos no banco')
    except:
        print('Arquivo não suportado')
else:
    print('Arquivo não encontrado')