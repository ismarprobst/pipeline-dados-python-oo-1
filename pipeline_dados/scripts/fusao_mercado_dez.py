from processamento_dados import Dados

 # Variaveis
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'
path_dados_combinados = 'data_processed/dados_combinados.csv'


#Extract
dados_empresaA = Dados(path_json, 'json');
print(f"Quantidade de linhas empresa A: {dados_empresaA.qtd_linhas}")

dados_empresaB = Dados(path_csv, 'csv');
print(f"Quantidade de linhas empresa B: {dados_empresaB.qtd_linhas}")


#Transform
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f"Nome das colunas da fusao: {dados_fusao.nome_colunas}")
print(f"Quantidade de linhas apos fusao: {dados_fusao.qtd_linhas}")


# Load
dados_fusao.salvando_dados(path_dados_combinados)
print(f"Arquivo criado em: {path_dados_combinados}")



