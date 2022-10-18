import random
'''
    {
        Programação orientada a objetos.
        ela existe para facilitar a modelagem dp mundo real para a programação
        classe:{ 
            moldes para construção de objetos.
            elas definem quais serão os atributos "caracteristicas" que sera colocar na programação
        }
        objetos:{
            Objetos devem responder a 3 perguntas:[
                "1- Que coisas eu tenho?": ["caracteristicas", "atributos"],
                "2- Que coisas eu faço?": ["comportamento", "Métodos"],
                "3- Qual o meu estado atual?": ["ex.: tela ligada, desligada, bateria com 50%", "Estado"]
            ]
        }
        O processo de criação de um Objeto (forma concreta) através de uma Classe(molde) é chamada
        de instânciação.
        quando se tem a instânciação de uma classe, ele se torna um objeto
    }

    Classe ventilador:
        atributos{
            Fabricante: String,
            Marca: String,
            Modelo: String, 
            Nº pás: int,
            tipo: String
            tamanho: float
        }
        métodos{
            ligado_vel_1()
            legado_vel_2()
            legado_vel_3()
            desligado()
        }

    Classe notebook:
        atributos{
            Fabricante: String,
            Marca: String,
            Display: String,
            resolução: int,
            ram: int,
            hd: int
            velocidade_ram: int,
            touch: bool,
            camera_modelo: String,
            Microfone: String.
            Bateria: int
        }
        metodos{
            ligado()
            desligado()
            carregando()
            descarregando()
            salvar_em_disco()
        }

'''


'''
{
    Os 4 pilares de POO{
        1- Encapsulamento: Isolar/esconder dados em classe, evitando acesso externo direto aos dados
            desta Classe.
        2- Herança: é o pilar da POO que permite que Classes derivem de outras Classes para 
            aproveitar e reutlizar o codigo. ex.:{
                automovel{
                    carro,
                    caminhão,
                    Caminhonete,
                    Moto
                }
        }
        3- Polimofirsmo: É a caracteristica que métodos possuem de assumir várias (poli) formas (morfismo)
            ex.: suponha que voce tem que implementar o método gerar_fatura() para cada subtipo de 
            automovel do exemplo acima de herança, porem cada tipo de automovel tem um jeito diferente de
            calcular. 
        
        4-Abstração: Usuários das classes que você cria, não devem se preocupar com
            os detalhes internos desta classe. 
    }

}
'''


# Classe Celular:
#     Atributos:
#         Fabrincante: String
#         Modelo: String
#         Tela: Decimal
#         Armazenamento: Inteiro
#         Memória: Inteiro
#         Câmera: Inteiro
#         Bateria: Inteiro
#         Tela ligada: Booleano
#     Métodos: 
#         ligar_tela()
#         Salvar_em_disco()
#         carregar_aplicativo()
#         tirar_foto()
#         verificar_carga_bateria()

class Celular:
    def __init__(self, fabricante, modelo, tela, Armazenamento, Memoria, camera, bateria, tela_ligada): #construtor 
        self.fabricante = fabricante
        self.modelo = modelo
        self.tela = tela
        self.Armazenamento = Armazenamento
        self.Memoria = Memoria
        self.camera = camera
        self.bateria = bateria  
        self.tela_ligada = tela_ligada


    def ligar_tela(self): 
        '''
            O self ele segue uma convenção do python, onde o primeiro parâmetro vai receber o nome self
            e ele serve para referenciar a propria instância em que está tratando.
        '''
        self.tela_ligada = True

    def verificar_carga_bateria(self):
        carga = random(0,100)
        self.bateria = 3400
        carregamento = ((100 - carga) * self.bateria)/100
        print(f'O celular está com %s e {carregamento}mA sobrando' % (100 - carga))


    
celular_android = Celular("Samsung", "S10", 6.25, 128, 4, 21, 3400, False) #Instânciando a classe e criando um novo objeto.

print(celular_android.bateria)