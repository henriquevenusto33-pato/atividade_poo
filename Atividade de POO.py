class Jogo:
    def __init__(self, nome, tipo, desenvolvedora):
        self.nome = nome
        self.tipo = tipo
        self.desenvolvedora = desenvolvedora

    def iniciar(self):
        return f"O jogo {self.nome} está iniciando..."

    def atualizar(self):
        return f"{self.nome} recebeu uma nova atualização!"
    

jogo1 = Jogo("Hollow Knight", "Metroidvania", "Team Cherry")
jogo2 = Jogo("Elden Ring", "Soulsborne", "FromSoftware")
jogo3 = Jogo("Minecraft", "RPG / Mundo Aberto", "Mojang")

print(jogo1.iniciar())
print(jogo1.atualizar())

print(jogo2.iniciar())
print(jogo2.atualizar())

print(jogo3.iniciar())
print(jogo3.atualizar())