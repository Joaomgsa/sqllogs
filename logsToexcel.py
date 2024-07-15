import pandas as pd

# Caminho para o arquivo de entrada e saída
caminho_do_arquivo_finances = 'query.csv'
caminho_do_arquivo_saida = 'planilha.xlsx'


def logs_para_excel(caminho_do_arquivo_finances, caminho_do_arquivo_saida):
    # Abrir o arquivo e ler as linhas
    with open(caminho_do_arquivo_finances, 'r') as arquivo:
        linhas = arquivo.readlines()

    # Extrair os cabeçalhos
    cabecalhos = linhas[1].strip().split('|')[1:-1]
    cabecalhos = [cabecalho.strip() for cabecalho in cabecalhos]
    

    # Extrair os dados 
    data = []
    for linha in linhas[3:]:
        if linha.strip().startswith('+'):
            continue
        row = linha.strip().split('|')[1:-1]
        row = [celula.strip() for celula in row]
        data.append(row)

    # Criar um DataFrame com o conteúdo
    df = pd.DataFrame(data, columns=cabecalhos)

    # Salvar o DataFrame como uma planilha Excel
    df.to_excel(caminho_do_arquivo_saida, index=False)

    print(f'Planilha criada com sucesso em: {caminho_do_arquivo_saida}')
    
logs_para_excel(caminho_do_arquivo_finances, caminho_do_arquivo_saida)