class Cachorro:
    def __init__(self,nome,raça,idade):
        self.nome = nome
        self.raça = raça
        self.idade = idade

cachorro = Cachorro(nome="Petra",raça="Bulldog",idade=5 )

print(cachorro.nome)
print(cachorro.raça)
print(cachorro.idade)