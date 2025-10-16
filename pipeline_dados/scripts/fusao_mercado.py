# Importações
from processamento_dados import Dados



# Parâmetros de path file
path_json ='/home/daniel/Documentos/Alura - Engenharia da Dados/pipeline_dados/data_raw/dados_empresaA.json'
path_csv ='/home/daniel/Documentos/Alura - Engenharia da Dados/pipeline_dados/data_raw/dados_empresaB.csv'

# Extract
dados_empresaA = Dados(path_json, 'json')
print(f"Log Extract: Nome das colunas json: {dados_empresaA.nomes_colunas}")
print(f"Log Extract: Quantidade linhas json: [{dados_empresaA.qtd_linhas}]")

dados_empresaB = Dados(path_csv, 'csv')
print(f"Log Extract: Nome das colunas csv: {dados_empresaB.nomes_colunas}")
print(f"Log Extract: Quantidade linhas csv: [{dados_empresaB.qtd_linhas}]")
print(f"Log Extract: Quantidade de linhas total [{dados_empresaB.qtd_linhas + dados_empresaA.qtd_linhas}]")

# Transform

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(F"Log Transform: Nome das colunas json: {dados_empresaB.nomes_colunas}")

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f"Log Transform: Nome das colunas fusão: {dados_fusao.nomes_colunas}")
print(f"Log Transform: Quantidade de linhas pré-fusão [{dados_empresaB.qtd_linhas + dados_empresaA.qtd_linhas}]")
print(f"Log Transform: Quantidade de linhas fusão: [{dados_fusao.qtd_linhas}]")

# Load
path_dados_combinados = '/home/daniel/Documentos/Alura - Engenharia da Dados/pipeline_dados/data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(path_dados_combinados)

