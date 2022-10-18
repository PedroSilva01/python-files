from random import randint
from time import sleep


VALOR_PEDAGIO_CARRO = 3.5
VALOR_PEDAGIO_MOTO = 2.75
VALOR_KM_RODADO_CARRO = 1.5
VALOR_KM_RODADO_MOTO = 1


class Automovel():
    def __init__(self, montadora, modelo, alugado):
        self.montadora = montadora
        self.modelo = modelo
        self.alugado = alugado
        self.valor_fatura = 0
        self.nome_cliente = ""
        print(f"Automovél {self.montadora} {self.modelo} adquirido pela Locadora.")

    def alugar(self, nome_cliente):
        self.alugado = True
        self.nome_cliente = nome_cliente
        print(f'O automóvel {self.montadora} {self.modelo} foi alugado por {self.nome_cliente}')

    def devolver_automovel(self):
        self.alugado = False
        print(f'O automovel {self.montadora} {self.modelo} foi devolvido por {self.nome_cliente}.')
        self.nome_cliente = ""


    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        raise NotImplementedError
    


#As classes que vão herdar de automovel agora:

class Carro(Automovel): #indicando que vai herdar da classe automoveis
    '''Quando se está criando um construtor em uma classe que já está herdando o construtor de outra classe automaticamente
    "que é o padrão" devemos explicitar o chamado, e se faz isso com o super()'''


    def __init__(self, montadora, modelo, alugado):
        super(Carro, self).__init__(montadora, modelo, alugado) 
        '''
        Ela está pegando a classe superior à que  está referenciando no super() 
        ex.: super(Carro, self) vai pegar a classe superior à de Carro, que é a de automovel e chamando o construtor dela
        '''
        print(f"O automovel adquirido foi um Carro")
    
    
        
    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        self.valor_fatura = numero_pedagios * VALOR_PEDAGIO_CARRO + km_rodados * VALOR_KM_RODADO_CARRO
        print(f'A fatura do carro {self.montadora} {self.modelo} é no valor de R$ {self.valor_fatura:.2f}')


class Moto(Automovel):
    def __init__(self, montadora, modelo, alugado):
        super(Moto, self).__init__(montadora, modelo, alugado) 
        '''
        Ela está pegando a classe superior à que  está referenciando no super() 
        ex.: super(Moto, self) vai pegar a classe superior à de Moto, que é a de automovel e chamando o construtor dela
        '''
        print(f"O automovel adquirido foi um Moto")


    def gerar_valor_fatura(self, numero_pedagios, km_rodados):
        self.valor_fatura = numero_pedagios * VALOR_PEDAGIO_MOTO + km_rodados * VALOR_KM_RODADO_MOTO
        print(f'A fatura do MOTO {self.montadora} {self.modelo} é no valor de R$ {self.valor_fatura:.2f}')


#-----------------------------------------------------------------------------------------------


fiesta = Carro("Ford", "Fiesta", False)
fiesta.alugar("João")

#Simulação do tempo de aluguel do automovel
sleep(randint(2,10))

fiesta.devolver_automovel()

fiesta.gerar_valor_fatura(numero_pedagios=5, km_rodados=750)