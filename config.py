COLUMNS_CNPJ_EMPRESA = ['cnpj_basico',
                        'razao_social', 
                        'natureza_juridica', 
                        'qualificacao_do_responsavel',
                        'capital_social_da_empresa', 
                        'porte_da_empresa', 
                        'ente_federativo_responsavel']

COLUMNS_CNPJ_ESTABELECIMENTO = ['cnpj_basico',
                                'cnpj_ordem', 
                                'cnpj_dv', 
                                'identificador_matriz_filia',
                                'nome_fantasia', 
                                'situacao_cadastral',
                                'motivo_situacao_cadastral',
                                'nome_cidade_exterior', 
                                'pais', 
                                'data_inicio_atividade', 
                                'cnae_fiscal_principal',
                                'cnae_fiscal_secundario', 
                                'tipo_logradouro', 
                                'logradouro','numero', 
                                'complemento', 
                                'bairro', 
                                'cep', 
                                'uf', 
                                'municipio', 
                                'ddd_1', 
                                'telefone_1', 
                                'ddd_2',
                                'telefone_2', 
                                'ddd_fax', 
                                'fax',
                                'correio_eletronico', 
                                'situacao_especial', 
                                'data_situacao_especial']

COLUMNS_CNPJ_SOCIO = ['cnpj_basico', 
                     'identificador_socio', 
                     'nome_socio_razao_social', 
                     'cpf_cnpj_socio', 
                     'qualificacao_socio', 
                     'data_entrada_sociedade', 
                     'pais', 
                     'representante_legal', 
                     'nome_representante', 
                     'qualificacao_representante_legal', 
                     'faixa_etaria']

URL = 'https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj'

FILETYPE_EMPRESA = 'EMPRECSV.zip'
FILETYPE_ESTABELECIMENTO = 'ESTABELE.zip'
FILETYPE_SOCIO = 'SOCIOCSV.zip'

FILENAME_EMPRESA = 'EMPRECSV'
FILENAME_ESTABELECIMENTO = 'ESTABELE'
FILENAME_SOCIO = 'SOCIOCSV'

NAME_DATABASE = 'database.db'

TABLE_EMPRESA = 'empresa'
TABLE_ESTABELECIMENTO = 'estabelecimento'
TABLE_SOCIO = 'socio'

DTYPE_EMPRESA = {'ente_federativo_responsavel':str, 'porte_da_empresa':str}
DTYPE_ESTABELECIMENTO = {'situacao_especial':str,'fax':str, 'pais':str,'nome_cidade_exterior':str, 'cep':str, 'ddd_1':str, 'telefone_1':str, 'telefone_2':str}
DTYPE_SOCIO = {'nome_representante':str}
