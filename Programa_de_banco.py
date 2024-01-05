import suporte
print('Sistema bancário')


nome = suporte.name()
print(f'Bom dia senhor(a) {nome}')
id_usu = input('Digite seu id para acessar o banco: ')
login = 'n'

# if id_usu.isnumeric():
#     pass
# else:
#     print('Erro. Deve-se digitar um número ao invés de texto no campo acima')
#     parar = id_usu
#     while parar is not True:
#         id_usu = input('Digite novamente: ')
#         parar = id_usu.isnumeric()
#         if not parar:
#             print(f'Está maluco {nome}? Não entendeu o que eu quis dizer? ESCREVA UM NÚMERO °_°')
#             # playsound.playsound(r'C:\Users\luqui\Downloads\20230830200628.mp3')
#         else:
#             pass

if suporte.é_número(id_usu):
    pass

if id_usu not in suporte.num_id:
    print('Id não encontrado. Deseja cadastrar-se no sistema?')
    resposta_usu = input('Sim ou não?: ').lower()
    if suporte.sorn(resposta_usu) == 'sim':
        resposta_usu_id = input('Digite o número pelo qual quer ser identificado: ')
        if resposta_usu_id.isnumeric():
            print('O número é válido')
            if resposta_usu_id in suporte.num_id:
                print('No entanto, esse número já está cadastrado.')
                parar = resposta_usu_id
                while parar in suporte.num_id:
                    resposta_usu_id = input('Tente outro: ')
                    parar = resposta_usu_id
            suporte.num_id.append(resposta_usu_id)
            login = 's'
        else:
            print('Digite um número, não uma letra.')
            parar = resposta_usu_id
            while parar is not True:
                resposta_usu_id = input('Digite novamente: ')
                parar = resposta_usu_id.isnumeric()
            suporte.num_id.append(resposta_usu_id)
            login = 's'
        print(suporte.num_id)
    elif sim_ou_nao == 'nao':
        print('Bom, é isso. Fim de sessão')
else:
    print('Usuário encontrado')
    login = 's'

if login == 's':
    id_usu = str(id_usu)
    print(f'Você está logado agora, {nome}!')
    print('Óleo de caminhão')
    info_usu = [
        {
            'id_usu': 1,
            'nome:': nome,
            'conta': 3457
        }
    ]
    print('O que deseja fazer?\n01.Consultar o valor da sua conta\n02.Transferir dinheiro para alguém')
    resposta_usu = input('Digite o número correspondente ao seu desejo: ')
    if suporte.é_número(resposta_usu):
        pass
    if resposta_usu == '1':
        print(f'Atualmente, você tem: R${info_usu[id_usu][]}.')

else:
    # print(f'O que? Erro no login senhor {nome}. O que aconteceu????????')
    print('É necessário estar logado para prosseguir')
    print(login)
