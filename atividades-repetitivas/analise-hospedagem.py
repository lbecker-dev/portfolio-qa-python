import pandas as pd
import os

def avaliar_hospedagem(df):
    # Converter colunas de data
    df["entrada"] = pd.to_datetime(df["entrada"], errors="coerce")
    df["saida"] = pd.to_datetime(df["saida"], errors="coerce")
    
    # Ordenar os dados por nome e data de entrada
    df = df.sort_values(by=["nome", "entrada"])
    
    # Criar lista para armazenar os resultados
    resultados = []
    
    for nome, grupo in df.groupby("nome"):
        grupo = grupo.sort_values(by="entrada")
        hospedagem_continua = True
        
        for i in range(1, len(grupo)):
            if grupo["entrada"].iloc[i] > grupo["saida"].iloc[i - 1] + pd.Timedelta(days=1):
                hospedagem_continua = False
                break
        
        resultados.append({
            "nome": nome,
            "total_internacoes": len(grupo),
            "hospedagem_continua": hospedagem_continua
        })
    
    return pd.DataFrame(resultados)

# Caminho do arquivo Excel
arquivo_entrada = r"C:\Users\lbecker\AppData\Local\Programs\Python\Python312\internafora.xlsx"
arquivo_saida = r"C:\Users\lbecker\AppData\Local\Programs\Python\Python312\resultado_hospedagem.xlsx"

# Verifica se o arquivo existe antes de tentar ler
if os.path.exists(arquivo_entrada):
    df = pd.read_excel(arquivo_entrada)
    
    # Processar os dados
    resultado = avaliar_hospedagem(df)
    
    # Salvar o resultado em um novo arquivo Excel
    resultado.to_excel(arquivo_saida, index=False)
    
    print(f"Arquivo processado com sucesso! Resultado salvo em: {arquivo_saida}")
else:
    print(f"Erro: O arquivo {arquivo_entrada} não foi encontrado.")
