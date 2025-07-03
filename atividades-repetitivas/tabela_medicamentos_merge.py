import pandas as pd

# Lê o arquivo de medicamentos (já conhecido)
materiais = pd.read_excel("materiais.xlsx", engine="openpyxl")
materiais.columns = materiais.columns.str.strip()

# Mostra colunas disponíveis (opcional)
#print("Colunas de medicamentos:", medicamentos.columns.tolist())

# Lê o segundo arquivo (deve ser fornecido pelo usuário)
tabela17 = pd.read_excel("Eventos17.xlsx", engine="openpyxl")
tabela17.columns = tabela17.columns.str.strip()

# Verifica colunas da tabela16 (opcional)
#print("Colunas de tabela16:", tabela16.columns.tolist())

tabela17.columns = tabela17.columns.str.strip()
materiais.columns = materiais.columns.str.strip()

if 'codevento' not in tabela17.columns:
    print("Coluna 'CODEVENTO' não encontrada em tabela17")

# Realiza a junção com base no código
resultado = pd.merge(
    tabela17,
    materiais[['Codigo', 'Nome', 'Valor', 'TISS']],
    left_on='CODEVENTO',
    right_on='Codigo',
    how='left'
)

# Substitui os valores da coluna TISS conforme regras
resultado['TISS'] = resultado['TISS'].replace({
    '20': '17',
    '00': '07'
})

# Remove a coluna 'Código' (opcional)
resultado.drop(columns=['Codigo'], inplace=True)

# Salva o resultado final
resultado.to_excel("resultado_com_descricao-materiais.xlsx", index=False)
print("✅ Arquivo 'resultado_com_descricao-materiais.xlsx' gerado com sucesso")
