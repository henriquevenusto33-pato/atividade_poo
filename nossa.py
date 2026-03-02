class Jogo():
    def __init__(self, nome, tipo, desenvolvedora):
        self.nome = nome
        self.tipo = tipo
        self.desenvolvedora = desenvolvedora
    def comprar(self):
        return f"{self.nome} da {self.desenvolvedora} foi comprado"
    
    def baixar(self):
        return f"{self.nome} esta classificado como {self.tipo}"
    
jogo1 = Jogo("hollow kight", "Metroidvania", "Team Cherry")
jogo2 = Jogo("Elden Ring", "Soulsborne", "Fromsoftware")
jogo3 = Jogo("minecraft", "rpg,mundo aberto", "mojang")

print(jogo1.comprar())
print(jogo1.baixar())
print(jogo2.comprar())
print(jogo2.baixar())
print(jogo3.comprar())
print(jogo3.baixar())