import pandas as pd

arquivo = 'cars_raw.csv'
lista_de_carros = []
arquivo_carregado = pd.read_csv(arquivo, usecols=[0,1,2,4])

for index in range(100):
    lista_de_carros.append(
        {
             'ano' : f'{arquivo_carregado.values[index][0]}',
             'marca': f'{arquivo_carregado.values[index][1]}',
             'modelo': f'{arquivo_carregado.values[index][2]}',
             'preco': f'{arquivo_carregado.values[index][3]}'
        }
    )

