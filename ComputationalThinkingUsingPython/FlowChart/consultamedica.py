from itertools import combinations
from pprint import pp, pprint

# Consulta médica

nome: str = "Augusto"
idade: int = 20
peso: float = 70.5
altura: float = 1.70
imc: float = peso / (altura * altura)
tipo_sanguineo: str = "O+"
is_contagioso: bool = False
batimentos: int = 65
# pressao: int = 120
temperatura: float = 36.5
has_plano_saude: bool = True
nome_plano_saude: str = "Unimed"


""" 
Classficação de Risco - Protocolo Manchester (Versão Reduzida)
Vermelho = Emergente     = 0 min   = Hospital
Laranja  = Muito Urgente = 20 min  = Hospital ou Unidade de Pronto-Atendimento 24h (UPA)
Verde    = Pouco Urgente = 100 min = Unidade de Pronto-Atendimento 24h (UPA) ou Atendimento ambulatorial em Unidades Básicas de Saúde ou Unidades de Saúde da Família
Azul     = Não Urgente   = 240 min = Atendimento ambulatorial em Unidades Básicas de Saúde ou Unidades de Saúde da Família
"""

"""
Pontos de Risco
!       Vermelho = 10
TODO    Laranja  = 5
*       Verde    = 1
?       Azul     = 0

Classificação 
Emergente     = (10 <= pontos)
Muito Urgente = (5 <= pontos < 10)
Pouco Urgente = (2 <= pontos < 5)
Não Urgente   = (0 <= pontos < 2)

Combinações
1) 1 Vermelho = Emergente
2) 2 Laranja  = Emergente
3) 1 Laranja = Muito Urgente
4) 2 Verde = Pouco Urgente
else: Não Urgente




"""
Vermelho = []
Laranja = []
Verde = []
Azul = []


# IMC
Vermelho.append("(imc <= 15 or imc > 40)")
Laranja.append("(imc <= 18 or 32.5 < imc <= 40)")
Verde.append("(18 < imc <= 19.9 or 25 < imc <= 32.5)")
Azul.append("(19.9 < imc <= 25)")


# Batimentos
Vermelho.append("(batimentos <= 45 or batimentos > 140)")
Laranja.append("(45 < batimentos <= 50 or 115 < batimentos <= 140)")
Verde.append("(50 < batimentos <= 59 or 100 < batimentos <= 115)")
Azul.append("(59 < batimentos <= 100)")


# Temperatura
Vermelho.append("(temperatura <= 34 or temperatura > 40.5)")
Laranja.append("(34 < temperatura <= 35 or 38 < temperatura <= 40.5)")
Verde.append("(35 < temperatura <= 35.9 or 37 < temperatura <= 38)")
Azul.append("(35.9 < temperatura <= 37)")

# Idade
Vermelho.append("(idade <= 1 or idade > 70)")
Laranja.append("(1 < idade <= 8 or 50 < idade <= 70)")
Verde.append("(8 < idade <= 18) or (40 < idade <= 50)")
Azul.append("(18 < idade <= 40)")


if is_contagioso:
    print("Isolamento")


print("\n")

teste = []

# Verificar se o paciente é emergente
emergentes = []
muitourgentes = []
poucourgentes = []
naourgentes = []

# 1)
condition = []
conditiontxt = ""
for i in list(combinations(Vermelho, 1)):
    condition.append(i[0])
    conditiontxt = " or ".join(condition)
emergentes.append(conditiontxt)

# 2)
for i in list(combinations(Laranja, 2)):
    emergentes.append(" and ".join(i))

# 3)
condition = []
conditiontxt = ""
for i in list(combinations(Laranja, 1)):
    condition.append(i[0])
    conditiontxt = " or ".join(condition)
muitourgentes.append(conditiontxt)

# 4)
for i in list(combinations(Verde, 2)):
    poucourgentes.append(" and ".join(i))

first = True
for x in emergentes:
    if first == True:
        print(f"if {x}:")
        first = False
    else:
        print(f"elif {x}:")
    print("    print('Emergente')")
for x in muitourgentes:
    print(f"elif {x}:")
    print("    print('Muito Urgente')")
for x in poucourgentes:
    print(f"elif {x}:")
    print("    print('Pouco Urgente')")
print("else:")
print("    print('Não Urgente')")

ifstotal = len(emergentes) + len(muitourgentes) + len(poucourgentes)
print(f"\nNúmero de Ifs: {ifstotal}")
