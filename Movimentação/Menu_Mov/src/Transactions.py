from src.database.connection import mycursor, mydb
import random
from datetime import datetime
from datetime import date


class Transactions:

    id = ''
    saldo = ''
    extrato = ''

    def __init__(self, parametro1):
        self.id = parametro1

    def create(self):  # PARA CRIAR USUÁRIOS FICTÍCIOS

        saldo_entrada = float(input("Digite o saldo: "))
        extrato_entrada = str(input("Digite o extrato:  "))

        values = (self.id, saldo_entrada, extrato_entrada,
                  datetime.utcnow(), datetime.utcnow())

        try:
            mycursor.execute(
                "INSERT INTO users(id, saldo, extrato, created_at, updated_at) VALUES(%s, %s, %s,%s,%s)", values)
            mydb.commit()
        except ConnectionError:
            print('Não foi possível cadastrar um novo usuário...     ')

        return 'Created', 201

    def query(self):
        query_id = mycursor.execute(
            f"SELECT id, saldo FROM users WHERE id={self.id}")
        origem_valores = mycursor.fetchall()
        for i in origem_valores:
            print(f"NÚMERO DA CONTA: {i[0]}\nSALDO: {i[1]}")
        return 200

    def transference(self):
        data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        destino = int(
            input("Digite o número da conta que deseja depositar...    "))

        if self.id == destino:
            print("Operação não permitida!")
            exit()

        query_id = mycursor.execute(
            f"SELECT id, saldo FROM users WHERE id={self.id}")
        origem_valores = mycursor.fetchall()

        query_id_receiver = mycursor.execute(
            f"SELECT id, saldo FROM users WHERE id={destino}")
        destino_valores = mycursor.fetchall()

        id_origem = ''
        saldo_origem = ''
        for i in origem_valores:
            id_origem = i[0]
            saldo_origem = i[1]

        id_destino = ''
        saldo_destino = ''
        for i in destino_valores:
            id_destino = i[0]
            saldo_destino = i[1]

        if self.id != id_origem or destino != id_destino:
            print("Conta informada não existente...     ")
            exit()

        valor_retirada = float(
            input("Qual será o valor da transferência?       "))

        if saldo_origem - valor_retirada < 0:
            print("Saldo insuficiente...        ")
        else:
            try:
                transfere = saldo_origem - valor_retirada
                mycursor.execute(
                    f"UPDATE users SET saldo={transfere} WHERE id={id_origem}")
                mycursor.execute(
                    f"INSERT INTO extrato(id_conta,id_origem,id_destino,valor,tipo,data_extrato) VALUES({id_origem},{id_origem},{id_destino},{valor_retirada},'Retirada','{data_atual}')"
                )

                saldo_final = saldo_destino + valor_retirada
                mycursor.execute(
                    f"UPDATE users SET saldo={saldo_final} WHERE id={id_destino}")
                mycursor.execute(
                    f"INSERT INTO extrato(id_conta,id_origem,id_destino,valor,tipo,data_extrato) VALUES({id_destino},{id_origem},{id_destino},{valor_retirada},'Entrada','{data_atual}')"
                )

                mydb.commit()

            except ConnectionError:
                print("Não foi possível realizar a operação...      ")

        return 'Updated', 201

    def statement(self):
        try:
            param = "SELECT id_origem, id_destino, valor, tipo, data_extrato from extrato where id_conta=" + \
                str(self.id)
            mycursor.execute(param)
            extratos = mycursor.fetchall()
            for row in extratos:
                print("--------------------------------")
                print("Conta Origem: ", row[0])
                print("Conta Destino: ", row[1])
                print("Valor: ", row[2])
                print("Tipo: ", row[3])
                print("Data: ", row[4].strftime('%d/%m/%Y %H:%M:%S'))
                print("--------------------------------\n")

        except ConnectionError:
            print("Não foi possível realizar a operação...      ")

        return 200

# ********************************************************************************************************************************************************


#objeto = Transactions(random.randint(10000000, 90000000))
# objeto.query()
# objeto.transference()
