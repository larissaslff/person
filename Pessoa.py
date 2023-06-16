class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.falando = False
        self.comendo = False

    def falar(self, subject):
        if not self.falando and not self.comendo:
            self.falando = True
        if self.comendo:
            return 'Não posso falar porque estou comendo'

        return f'Estou falando sobre {subject}'

    def pararDeFalar(self):
        if self.falando:
            self.falando = False
            return 'Estou parando de falar'
        else:
            return 'Eu não posso parar de falar, pois não estava falando'


    def comer(self, comida):
        if not self.comendo and not self.falando:
            self.comendo = True
            return f'Estou comendo {comida}'
        if self.falando:
            return 'Não posso falar de boca cheia!'
        else:
            return 'Já estou comendo!!'


    def paraDeComer(self):
        if self.comendo:
            self.comendo = False
            return 'Parei de comer'