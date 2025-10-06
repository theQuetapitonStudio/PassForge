import random
import string

print("Seja bem vindo ao PassForge!")
print("Crie sua senha forte")

print("Opção 1: Criar senha")
print("Opção 2: sair")

opcao = int(input("Digite a opção: "))

def criarSenha():
    caracteres = string.ascii_letters + string.digits
    passWord = ''.join(random.choice(caracteres) for i in range(10))
    return passWord

if opcao == 1:
    senha = criarSenha()
    print("sua senha: " + senha)
else:
    print("Opção invalida! tente novamente!")

input("pressione ENTER para sair")