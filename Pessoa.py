class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.falando = False
        self.comendo = False

    def falar(self, subject):
        if not self.falando:
            self.falando = True
            return f'Estou falando sobre {subject}'


    def pararDeFalar(self):
        if self.falando:
            self.falando = False
            return 'Estou parando de falar'
        else:
            return 'Eu não posso parar, pois não estava falando'


    def comer(self, comida):
        if not self.comendo:
            self.comendo = True
            return f'Estou comendo {comida}'
        else:
            return 'Já estou comendo!!'