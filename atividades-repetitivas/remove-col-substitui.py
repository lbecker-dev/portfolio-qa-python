import os

def remover_coluna_e_substituir_numero(arquivo_entrada, arquivo_saida, numero_antigo, numero_novo):
    with open(arquivo_entrada, 'r', encoding='utf-8') as f_in, open(arquivo_saida, 'w', encoding='utf-8') as f_out:
        for linha in f_in:
            # Dividir a linha em campos usando ';' como separador
            campos = linha.strip().split(';')
            
            # Verificar se há pelo menos 9 campos (índice 8 é o nono campo)
            if len(campos) > 8:
                # Remover o nono campo (índice 8)
                del campos[8]
            
            # Juntar os campos de volta em uma linha usando ';' como separador
            linha_sem_nono_campo = ';'.join(campos)
            
            # Substituir o número antigo pelo número novo na linha modificada
            linha_modificada = linha_sem_nono_campo.replace(numero_antigo, numero_novo)
            
            # Escrever a linha modificada no arquivo de saída
            f_out.write(linha_modificada + '\n')

    print(f'Arquivo modificado com sucesso. Veja em: {os.path.abspath(arquivo_saida)}')

# Exemplo de uso
# Nome do arquivo .lst de entrada e saída
arquivo_entrada = 'C:\\Users\lbecker\\AppData\\Local\\Programs\\Python\\Python312\\arquivo.lst'
arquivo_saida = 'C:\\Users\\lbecker\\AppData\Local\\Programs\Python\\Python312\\arquivo_sem_coluna11.lst'
numero_antigo = '08812346000223'
numero_novo = '088654326000142'

remover_coluna_e_substituir_numero(arquivo_entrada, arquivo_saida, numero_antigo, numero_novo)
