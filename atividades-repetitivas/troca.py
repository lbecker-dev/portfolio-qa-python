

# Nome do arquivo .lst de entrada e saída
arquivo_entrada = 'C:\\Users\lbecker\\AppData\\Local\\Programs\\Python\\Python312\\arquivo.lst'
arquivo_saida = 'C:\\Users\\lbecker\\AppData\Local\\Programs\Python\\Python312\\arquivo_sem_coluna10.lst'

# Função para substituir um número por outro em um arquivo
def substituir_numero(arquivo_entrada, arquivo_saida, numero_antigo, numero_novo):
    with open(arquivo_entrada, 'r', encoding='utf-8') as f_in, open(arquivo_saida, 'w', encoding='utf-8') as f_out:
        for linha in f_in:
            # Substituir o número antigo pelo número novo na linha
            nova_linha = linha.replace(numero_antigo, numero_novo)
            # Escrever a linha modificada no arquivo de saída
            f_out.write(nova_linha)

numero_antigo = '08898528000229'
numero_novo = '08898524000142'
            


# Abrir arquivo de entrada e criar arquivo de saída
with open(arquivo_entrada, 'r', encoding='utf-8') as f_in, open(arquivo_saida, 'w', encoding='utf-8') as f_out:
    for linha in f_in:
        # Dividir a linha em colunas usando espaço em branco ou tabulação como separador
        colunas = linha.strip().split(';')  # ou linha.split('\t') se o separador for tabulação
        
        # Verificar se há pelo menos 9 colunas
        if len(colunas) > 8:
            # Remover a nona coluna (índice 8)
            del colunas[8]
        
        # Escrever a linha modificada no arquivo de saída
        # Unir as colunas de volta em uma linha e escrever no arquivo
        f_out.write(';'.join(colunas) + '\n')

substituir_numero(arquivo_entrada, arquivo_saida, numero_antigo, numero_novo)

print(f'Coluna 9 removida com sucesso do arquivo {arquivo_entrada}.')
print(f'Arquivo modificado salvo em {arquivo_saida}.')
