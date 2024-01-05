sim = ['s', 'sim', 'si', 'Sim']
nao = ['n', 'nao', 'não', 'ñ', 'Não']
num_id = ['1', '2', '3', '4', '5', '6', '7']

# informacoes = [
#     '1': [
#         {
#         'id_usu': '1',
#         'nome:': 'Lucas',
#         'conta': 3457
#         }  
#     ],
#     {
#         'id_usu': '2',
#         'nome': 'Maria',
#         'conta': 2307
#     },
#     {
#         'id_usu': '3',
#         'nome': 'Carlos',
#         'conta': 124
#     }
# ]

informacoes  = [

    '1' = {
            'nome': 'Lucas'
    }
]   

def name():
    msg = input('Digite seu nome: ')
    return msg


def é_número(arg1):
    if arg1.isnumeric() is True:
        return arg1
    else:
        while arg1 is not True:
            msg = input('Digite novamente, apenas números: ')
            arg1 = msg.isnumeric()
        return msg


def na_lista(arg1, arg2=num_id):
    if arg1 not in arg2:
        return arg1
    else:
        print('Esse usuário já existe')
        parar = arg1
        while parar in arg2:
            arg1 = input('Digite novamente: ')
            parar = arg1
        return parar


def sorn(arg1):
    arg1 = arg1.lower()
    if arg1 in sim:
        msg = 'sim'
        return msg
    elif arg1 in nao:
        msg = 'nao'
        return msg
    else:
        while arg1 not in sim or nao:
            arg1 = input('Digite novamente. Sim ou não: ')
            if arg1 in sim:
                msg = 'sim'
                return msg
            elif arg1 in nao:
                msg = 'nao'
                return msg
            else:
                print('Ausência de sucesso')


def consulta_conta(arg1):
    voltar = informacoes[arg1]['nome']
    return voltar


class usuario:
    def __init__(self) -> None:
        pass

# algo = consulta_conta(1)
# print(algo)


# verif = na_lista(d,num_id)
#
# print(verif)
#
# if verif.isnumeric():
#     num_id.append(verif)
#     print(num_id)
# else:
#     print('Erro no if')


#  Tentativa de verificação de sim ou não
# if resposta in sim:
#         msg = True
#         return msg
#     elif resposta in nao:
#         msg = False
#         return msg
#     elif resposta not in sim or nao:
#         parar = False
#         while parar == False:
#             continua = input('Digite novamente. Sim ou não: ').lower()
#             if continua not in sim or nao:
#                 print('Algo')
#             else:
#                 print(f'Sua resposta foi: {continua}')
#                 continua = True
#             msg = continua
#             return msg
#     else:
#         msg = 'bom é isso'
#         return msg

# def s_or_n(arg1):
#     arg1 = arg1.lower()
#     if arg1 in sim:
#         return True
#     elif arg1 in nao:
#         return True
#     else:
#         while arg1 not in sim or nao:
#             arg1 = input('Digita dnv: ').lower()
#             if arg1 in sim:
#                 print('Sucesso')
#                 break
#             elif arg1 in nao:
#                 print('Sucesso. Vez do não')
#                 break
#             else:
#                 print('Ausência de sucesso')
#         return True
