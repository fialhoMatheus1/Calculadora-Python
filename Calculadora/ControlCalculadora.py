#conectando control com model
from Calculadora import Calculadora

class ControlCalculadora:
    #metodo construtor
    def __init__(self):
        self.calculadora = Calculadora()#instanciando a classe calculadora
        self.opcao = -1

    def menu(self):
        print("Escolha uma das opções abaixo\n\n" +
              "1. Somar\n" +
              "2. Subtrair\n" +
              "3. Dividir\n" +
              "4. Multiplicar\n" +
              "0. Sair\n")
        self.opcao = int(input())

    def operacao(self):
        while(self.opcao != 0):
            self.menu()#chamando o menu
            if self.opcao == 0:
                print("Obrigado!")
            elif self.opcao == 1:
                print("Bem-vindo a soma!")
                print("Digite um número:")
                num1 = int(input())
                print("Digite outro número:")
                num2 = int(input())
                print(self.calculadora.soma(num1, num2))
            elif self.opcao == 2:
                print("Bem-vindo a subtração!")
                print("Digite um número:")
                num1 = int(input())
                print("Digite outro número:")
                num2 = int(input())
                print(self.calculadora.subtracao(num1, num2))

            elif self.opcao == 3:
                print("Bem-vindo a divisão!")
                print("Digite um número:")
                num1 = int(input())
                print("Digite outro número:")
                num2 = int(input())
                print(self.calculadora.divisao(num1, num2))
            elif self.opcao == 4:
                print("Bem-vindo a multiplicação!")
                print("Digite um número:")
                num1 = int(input())
                print("Digite outro número:")
                num2 = int(input())
                print(self.calculadora.multiplicacao(num1, num2))
            else:
                print("Opção inválida!")
