class Celular:
    def __init__(self, marca, modelo, polegadas, armazenamento, mem_ram):
        # Atributos principais
        self.marca = marca
        self.modelo = modelo
        self.polegadas = polegadas
        self.armazenamento = armazenamento
        self.mem_ram = mem_ram
        
        # Atributos internos de status
        self.status_celular = "Desligado"  # Status do celular (Desligado ou Ligado)
        self.status_chamada = None  # Status da chamada (Nenhuma chamada ou número de telefone)

    def ligar(self):
        if self.status_celular == "Desligado":
            self.status_celular = "Ligado"
            print(f'{self.modelo} agora está ligado.')
        else:
            print(f'{self.modelo} já está ligado.')

    def desligar(self):
        if self.status_celular == "Ligado":
            self.status_celular = "Desligado"
            self.status_chamada = None  # Desliga a chamada se houver
            print(f'{self.modelo} agora está desligado.')
        else:
            print(f'{self.modelo} já está desligado.')

    def fazer_chamada(self, numero):
        if self.status_celular == "Ligado":
            if self.status_chamada is None:
                self.status_chamada = numero
                print(f'Chamando {numero}...')
            else:
                print(f'Já existe uma chamada em andamento para {self.status_chamada}.')
        else:
            print(f'{self.modelo} precisa estar ligado para fazer uma chamada.')

    def encerrar_chamada(self):
        if self.status_chamada is not None:
            print(f'Chamada para {self.status_chamada} encerrada.')
            self.status_chamada = None
        else:
            print(f'Não há chamada em andamento para encerrar.')

# Instanciando um celular
celular = Celular(marca="Samsung", modelo="Galaxy S23", polegadas=6.1, armazenamento=128, mem_ram=8)

# Testando os métodos
celular.ligar()
celular.fazer_chamada("987654321")
celular.fazer_chamada("912345678")  # Tentando fazer outra chamada enquanto uma está em andamento
celular.encerrar_chamada()
celular.fazer_chamada("912345678")  # Agora pode fazer a segunda chamada
celular.desligar()