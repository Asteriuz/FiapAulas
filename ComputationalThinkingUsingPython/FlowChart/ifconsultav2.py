nome: str = "Augusto"
idade: int = 45
peso: float = 105
altura: float = 1.80
imc: float = peso / (altura * altura)
print(imc)
batimentos: int = 62
temperatura: float = 36.5


if (
    (imc <= 15 or imc > 40)
    or (batimentos <= 45 or batimentos > 140)
    or (temperatura <= 34 or temperatura > 40.5)
    or (idade <= 1 or idade > 70)
):
    print("Emergente")
elif (imc <= 18 or 32.5 < imc <= 40) and (
    45 < batimentos <= 50 or 115 < batimentos <= 140
):
    print("Emergente")
elif (imc <= 18 or 32.5 < imc <= 40) and (
    34 < temperatura <= 35 or 38 < temperatura <= 40.5
):
    print("Emergente")
elif (imc <= 18 or 32.5 < imc <= 40) and (1 < idade <= 8 or 50 < idade <= 70):
    print("Emergente")
elif (45 < batimentos <= 50 or 115 < batimentos <= 140) and (
    34 < temperatura <= 35 or 38 < temperatura <= 40.5
):
    print("Emergente")
elif (45 < batimentos <= 50 or 115 < batimentos <= 140) and (
    1 < idade <= 8 or 50 < idade <= 70
):
    print("Emergente")
elif (34 < temperatura <= 35 or 38 < temperatura <= 40.5) and (
    1 < idade <= 8 or 50 < idade <= 70
):
    print("Emergente")
elif (
    (imc <= 18 or 32.5 < imc <= 40)
    or (45 < batimentos <= 50 or 115 < batimentos <= 140)
    or (34 < temperatura <= 35 or 38 < temperatura <= 40.5)
    or (1 < idade <= 8 or 50 < idade <= 70)
):
    print("Muito Urgente")
elif (18 < imc <= 19.9 or 25 < imc <= 32.5) and (
    50 < batimentos <= 59 or 100 < batimentos <= 115
):
    print("Pouco Urgente")
elif (18 < imc <= 19.9 or 25 < imc <= 32.5) and (
    35 < temperatura <= 35.9 or 37 < temperatura <= 38
):
    print("Pouco Urgente")
elif (18 < imc <= 19.9 or 25 < imc <= 32.5) and (8 < idade <= 18) or (40 < idade <= 50):
    print("Pouco Urgente")
elif (50 < batimentos <= 59 or 100 < batimentos <= 115) and (
    35 < temperatura <= 35.9 or 37 < temperatura <= 38
):
    print("Pouco Urgente")
elif (
    (50 < batimentos <= 59 or 100 < batimentos <= 115)
    and (8 < idade <= 18)
    or (40 < idade <= 50)
):
    print("Pouco Urgente")
elif (
    (35 < temperatura <= 35.9 or 37 < temperatura <= 38)
    and (8 < idade <= 18)
    or (40 < idade <= 50)
):
    print("Pouco Urgente")
else:
    print("Não Urgente")
