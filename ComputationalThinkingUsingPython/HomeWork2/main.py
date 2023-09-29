nomeList = ["Augusto", "Albérico", "Ranieri"]
senhaList = ["Dart123", "Python456", "Java789"]

while True:
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    if usuario in nomeList:
        if senha == senhaList[nomeList.index(usuario)]:
            print("Usuário e senha corretos, Login Realizado")
            exit()
        else:
            print("Senha Incorreta")
    else:
        print("Esse usuário não existe")
