import pandas as pd

# Caminho do arquivo CSV
arquivo = 'C:\\Users\\lbecker\\AppData\\Local\\Programs\\Python\\Python312\\camara_ur.csv'

# Lê o arquivo CSV com o separador correto
df = pd.read_csv(arquivo, delimiter=';', encoding='latin1')

# Limpa espaços dos nomes das colunas
df.columns = df.columns.str.strip()

# Converte a coluna 'Valor' para float
df['Valor'] = df['Valor'].astype(str).str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)

# Converte a coluna 'Emissão' para datetime
df['Emissao'] = pd.to_datetime(df['Emissao'], dayfirst=True)

# Cria colunas de ano e mês
df['Ano'] = df['Emissao'].dt.year
df['Mês'] = df['Emissao'].dt.month

# Agrupa e soma os valores por ano e mês
resumo = df.groupby(['Ano', 'Mês'])['Valor'].sum().reset_index()

# Formata os valores como 000,00 (vírgula como separador decimal)
resumo['Valor'] = resumo['Valor'].apply(lambda x: f'{x:,.2f}'.replace('.', 'X').replace(',', '.').replace('X', ','))

# Salva o resultado em um novo arquivo
arquivo_saida = 'C:\\Users\\lbecker\\AppData\\Local\\Programs\\Python\\Python312\\resumo_Durs.csv'
resumo.to_csv(arquivo_saida, index=False, sep=';', encoding='latin1')

print("Resumo gerado com sucesso e salvo em:", arquivo_saida)

