#conectando a main com a control
from ControlCalculadora import ControlCalculadora

if __name__ == "__main__":
    controle = ControlCalculadora()
    controle.operacao()#chamando o metodo de operação de dados da classe control
