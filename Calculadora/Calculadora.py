class Calculadora:
        #metodo construtor
        def __init__(self):
            self.num1 = 0
            self.num2 = 0

        #metodos de acesso
        def getNum1(self):
            return self.num1

        def getNum2(self):
            return self.num2

        def setNum1(self, num1):
            self.num1 = num1

        def setNum2(self, num2):
            self.num2 = num2

        #metodos de operações:
        def soma(self, num1, num2):
            self.setNum1(num1)
            self.setNum2(num2)
            return (self.getNum1() + self.getNum2())

        def subtracao(self, num1, num2):
            self.setNum1(num1)
            self.setNum2(num2)
            return (self.getNum1() - self.getNum2())

        def divisao(self, num1, num2):
            self.setNum1(num1)
            self.setNum2(num2)
            return (self.getNum1() / self.getNum2())

        def multiplicacao(self, num1, num2):
            self.setNum1(num1)
            self.setNum2(num2)
            return (self.getNum1() * self.getNum2())
