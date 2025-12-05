class NaveModelo:
    def __init__(self, denominacao, cor, perda_energia, simbolo):
        self.denominacao = denominacao
        self.cor = cor
        self.energia = 100
        self.perda_energia = perda_energia
        self.simbolo = simbolo

    def perder_energia(self):
        self.energia -= self.perda_energia
        if self.energia < 0:
            self.energia = 0
        return self.energia


class NaveEspecial(NaveModelo):
    def __init__(self, denominacao, cor, perda_energia, simbolo, energia_extra):
        super().__init__(denominacao, cor, perda_energia, simbolo)
        self.energia_extra = energia_extra

    def mostrar_dados(self):
        # Exibe os dados da nave com a cor especificada (simples)
        print(f"{self.cor}{self.simbolo} - {self.denominacao} - Energia: {self.energia}\033[0m")

    def adicionar_energia_extra(self):
        self.energia += self.energia_extra
        if self.energia > 100:
            self.energia = 100
