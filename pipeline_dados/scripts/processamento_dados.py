import json
import csv

class Dados:
    # Método construtor
    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dados()
        self.nome_colunas = self.get_columns()
        self.qtd_linhas = self.size_data()
    
    
    # Métodos da classe, recebe self pois ja tem esses valores como seus atributos 
    def leitura_json(self):
        dados_json = []
        with open(self.path, 'r') as file:
            dados_json = json.load(file)
        return dados_json
 
    def leitura_csv(self):
        dados_csv = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv

    def leitura_dados(self):
        dados = []
        if self.tipo_dados =='csv':
            dados = self.leitura_csv()
        elif self.tipo_dados == 'json':
            dados = self.leitura_json()
        elif self.tipo_dados == 'list':
            dados = self.path
            self.path = 'lista em memória' 
        return dados
    
    def get_columns(self):
        return list(self.dados[-1].keys())
    
    def rename_columns(self, key_mapping):
        new_dados = []
        # Utilizando dict comprehension
        new_dados = [{key_mapping.get(old_key): value for old_key, value in old_dict.items()} for old_dict in self.dados]
        
        self.dados = new_dados
        self.nome_colunas = self.get_columns()
          
    def size_data(self):
        return len(self.dados)
    # Metodo estático, nao receberá caracteristicas da classe
    def join(dados_a, dados_b):
        combined_list = []
        combined_list.extend(dados_a.dados)
        combined_list.extend(dados_b.dados)
        
        return Dados(combined_list, 'list')
    
    def data_to_table(self):
        data_to_table = [self.nome_colunas]
        for row in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna, 'Indisponível'))
            data_to_table.append(linha)
        return data_to_table
    
    def salvando_dados(self, path):
        
        dados_combinado_tabela = self.data_to_table()
        
        with open(path, 'w') as file:
            writer = csv.writer(file, delimiter = ";")
            writer.writerows(dados_combinado_tabela)