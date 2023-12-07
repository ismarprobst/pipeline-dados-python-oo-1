import json
import csv

# Variaveis
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'
path_dados_combinados = 'data_processed/dados_combinados.csv'


# Funcoes
def leitura_json(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    return dados_json
 
def leitura_csv(path_csv):
    dados_csv = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            dados_csv.append(row)
    return dados_csv

def leitura_dados(path, tipo_arquivo):
    dados = []
    if tipo_arquivo =='csv':
        dados = leitura_csv(path)
    elif tipo_arquivo == 'json':
        dados = leitura_json(path)    
    return dados

def get_columns(dados):
    return list(dados[-1].keys())

def rename_columns(dados, key_mapping):
    new_dados_csv = []
    # Utilizando dict comprehension
    new_dados_csv = [{key_mapping.get(old_key): value for old_key, value in old_dict.items()} for old_dict in dados]
    return new_dados_csv

def size_data(dados):
    return len(dados)

def join(dados_a, dados_b):
    combined_list = []
    combined_list.extend(dados_a)
    combined_list.extend(dados_b)
    return combined_list

def data_to_table(dados, nomes_colunas):
    data_to_table = [nomes_colunas]
    for row in dados:
        linha = []
        for coluna in nomes_colunas:
            linha.append(row.get(coluna, 'Indisponível'))
        data_to_table.append(linha)
    return data_to_table

def salvando_dados(dados, path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(dados)

# Iniciando a leitura dos arquivos
dados_json = leitura_dados(path_json, 'json')
nome_colunas_json = get_columns(dados_json)
tamanho_dados_json = size_data(dados_json)

dados_csv = leitura_dados(path_csv, 'csv')
nome_colunas_csv = get_columns(dados_csv)
tamanho_dados_csv = size_data(dados_csv)

#DE PARA colunas
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}


# Transformacao dos dados
    
dados_csv = rename_columns(dados_csv, key_mapping)
nome_colunas_csv = get_columns(dados_csv)

dados_fusao = join(dados_json, dados_csv)
nome_colunas_fusao = get_columns(dados_fusao)
tamanho_dados_fusao = size_data(dados_fusao)

# Salvando os dados

dados_fusao_tabela = data_to_table(dados_fusao, nome_colunas_fusao)

salvando_dados(dados_fusao_tabela, path_dados_combinados)
