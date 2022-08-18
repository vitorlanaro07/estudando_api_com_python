from pandas import read_csv
from concurrent.futures import ThreadPoolExecutor
import mysql.connector

pessoa_dataset = read_csv('AgeDataset-V1.csv', usecols=(1, 3, 4, 6))

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="354555",
  database="mydb"
)

mycursor = mydb.cursor()


def adiciona_pessoa_com_thread(index):
    nome = pessoa_dataset.values[index][0]
    sexo = pessoa_dataset.values[index][1]
    pais = pessoa_dataset.values[index][2]
    data_nascimento = pessoa_dataset.values[index][3]
    try:
        sql = "INSERT INTO pessoa (nome, sexo, pais, data_nascimento) VALUES (%s, %s, %s, %s)"
        mycursor.execute(sql, (nome, sexo, pais, data_nascimento))
        mydb.commit()
        print(f'adicionado {index}')
    except:
        print(f'erro {index}')
        pass


for index in range(100):
    adiciona_pessoa_com_thread(index)



mydb.commit()

print('ok')

