# Criação de um objeto para armazenar os dados do herói
class Heroi:
    def __init__(self, name, exp):
        self.name = name
        self.exp = int(exp)

# Variáveis para receber o nome e experiência do personagem
name = input("Informe o nome do seu herói: ")
exp = input("Informe a experiência do seu herói: ")

# Cria o objeto heroi com os dados fornecidos
heroi = Heroi(name, exp)

# Verificar nível do herói
nivel = None
# Se XP for menor do que 1.000 = Ferro
if heroi.exp <= 1000:
    nivel = "Ferro"
# Se XP for entre 1.001 e 2.000 = Bronze
elif heroi.exp > 1000 and heroi.exp <= 2000:
    nivel = "Bronze"
# Se XP for entre 2.001 e 5.000 = Prata
elif heroi.exp > 2000 and heroi.exp <= 5000:
    nivel = "Prata"
# Se XP for entre 5.001 e 7.000 = Ouro
elif heroi.exp > 5000 and heroi.exp <= 7000:
    nivel = "Ouro"
# Se XP for entre 7.001 e 8.000 = Platina
elif heroi.exp > 7000 and heroi.exp <= 8000:
    nivel = "Platina"
# Se XP for entre 8.001 e 9.000 = Ascendente
elif heroi.exp > 8000 and heroi.exp <= 9000:
    nivel = "Ascendente"
# Se XP for entre 9.001 e 10.000= Imortal
elif heroi.exp > 9000 and heroi.exp <= 10000:
    nivel = "Imortal"
# Se XP for maior ou igual a 10.001 = Radiante
elif heroi.exp > 10000:
    nivel = "Radiante"

# Exibe as informações do herói
print(f"O Herói de nome **{heroi.name}** está no nível de **{nivel}**")
