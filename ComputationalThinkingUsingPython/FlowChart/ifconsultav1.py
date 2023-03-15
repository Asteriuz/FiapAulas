nome: str = "Augusto"
idade: int = 56
peso: float = 105
altura: float = 1.80
imc: float = peso / (altura * altura)
tipo_sanguineo: str = "O+"
is_contagioso: bool = False
batimentos: int = 65
# pressao: int = 120
temperatura: float = 36.6
has_plano_saude: bool = True
nome_plano_saude: str = "Unimed"


if (imc <= 15 or imc > 40) or (batimentos <= 45 or batimentos > 140) or (temperatura < 34 or temperatura > 40) or (idade < 2 or idade > 60):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (45 < batimentos <= 60 or 115 < batimentos <= 140) and (34 < temperatura <= 36 or 38 < temperatura <= 40):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (45 < batimentos <= 60 or 115 < batimentos <= 140) and (2 < idade <= 10 or 50 < idade <= 60):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (34 < temperatura <= 36 or 38 < temperatura <= 40) and (2 < idade <= 10 or 50 < idade <= 60):
    print('Emergente')
elif (45 < batimentos <= 60 or 115 < batimentos <= 140) and (34 < temperatura <= 36 or 38 < temperatura <= 40) and (2 < idade <= 10 or 50 < idade <= 60):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (45 < batimentos <= 60 or 115 < batimentos <= 140) and (25 < imc <= 32.5) and (100 < batimentos <= 115):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (45 < batimentos <= 60 or 115 < batimentos <= 140) and (25 < imc <= 32.5) and (37 < temperatura <= 38):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (45 < batimentos <= 60 or 115 < batimentos <= 140) and (25 < imc <= 32.5) and (10 < idade <= 30):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (45 < batimentos <= 60 or 115 < batimentos <= 140) and (100 < batimentos <= 115) and (37 < temperatura <= 38):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (45 < batimentos <= 60 or 115 < batimentos <= 140) and (100 < batimentos <= 115) and (10 < idade <= 30):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (45 < batimentos <= 60 or 115 < batimentos <= 140) and (37 < temperatura <= 38) and (10 < idade <= 30):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (34 < temperatura <= 36 or 38 < temperatura <= 40) and (25 < imc <= 32.5) and (100 < batimentos <= 115):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (34 < temperatura <= 36 or 38 < temperatura <= 40) and (25 < imc <= 32.5) and (37 < temperatura <= 38):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (34 < temperatura <= 36 or 38 < temperatura <= 40) and (25 < imc <= 32.5) and (10 < idade <= 30):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (34 < temperatura <= 36 or 38 < temperatura <= 40) and (100 < batimentos <= 115) and (37 < temperatura <= 38):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (34 < temperatura <= 36 or 38 < temperatura <= 40) and (100 < batimentos <= 115) and (10 < idade <= 30):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (34 < temperatura <= 36 or 38 < temperatura <= 40) and (37 < temperatura <= 38) and (10 < idade <= 30):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (2 < idade <= 10 or 50 < idade <= 60) and (25 < imc <= 32.5) and (100 < batimentos <= 115):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (2 < idade <= 10 or 50 < idade <= 60) and (25 < imc <= 32.5) and (37 < temperatura <= 38):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (2 < idade <= 10 or 50 < idade <= 60) and (25 < imc <= 32.5) and (10 < idade <= 30):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (2 < idade <= 10 or 50 < idade <= 60) and (100 < batimentos <= 115) and (37 < temperatura <= 38):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (2 < idade <= 10 or 50 < idade <= 60) and (100 < batimentos <= 115) and (10 < idade <= 30):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (2 < idade <= 10 or 50 < idade <= 60) and (37 < temperatura <= 38) and (10 < idade <= 30):
    print('Emergente')
elif (45 < batimentos <= 60 or 115 < batimentos <= 140) and (34 < temperatura <= 36 or 38 < temperatura <= 40) and (25 < imc <= 32.5) and (100 < batimentos <= 115):
    print('Emergente')
elif (45 < batimentos <= 60 or 115 < batimentos <= 140) and (34 < temperatura <= 36 or 38 < temperatura <= 40) and (25 < imc <= 32.5) and (37 < temperatura <= 38):
    print('Emergente')
elif (45 < batimentos <= 60 or 115 < batimentos <= 140) and (34 < temperatura <= 36 or 38 < temperatura <= 40) and (25 < imc <= 32.5) and (10 < idade <= 30):
    print('Emergente')
elif (45 < batimentos <= 60 or 115 < batimentos <= 140) and (34 < temperatura <= 36 or 38 < temperatura <= 40) and (100 < batimentos <= 115) and (37 < temperatura <= 38):
    print('Emergente')
elif (45 < batimentos <= 60 or 115 < batimentos <= 140) and (34 < temperatura <= 36 or 38 < temperatura <= 40) and (100 < batimentos <= 115) and (10 < idade <= 30):
    print('Emergente')
elif (45 < batimentos <= 60 or 115 < batimentos <= 140) and (34 < temperatura <= 36 or 38 < temperatura <= 40) and (37 < temperatura <= 38) and (10 < idade <= 30):
    print('Emergente')
elif (45 < batimentos <= 60 or 115 < batimentos <= 140) and (2 < idade <= 10 or 50 < idade <= 60) and (25 < imc <= 32.5) and (100 < batimentos <= 115):
    print('Emergente')
elif (45 < batimentos <= 60 or 115 < batimentos <= 140) and (2 < idade <= 10 or 50 < idade <= 60) and (25 < imc <= 32.5) and (37 < temperatura <= 38):
    print('Emergente')
elif (45 < batimentos <= 60 or 115 < batimentos <= 140) and (2 < idade <= 10 or 50 < idade <= 60) and (25 < imc <= 32.5) and (10 < idade <= 30):
    print('Emergente')
elif (45 < batimentos <= 60 or 115 < batimentos <= 140) and (2 < idade <= 10 or 50 < idade <= 60) and (100 < batimentos <= 115) and (37 < temperatura <= 38):
    print('Emergente')
elif (45 < batimentos <= 60 or 115 < batimentos <= 140) and (2 < idade <= 10 or 50 < idade <= 60) and (100 < batimentos <= 115) and (10 < idade <= 30):
    print('Emergente')
elif (45 < batimentos <= 60 or 115 < batimentos <= 140) and (2 < idade <= 10 or 50 < idade <= 60) and (37 < temperatura <= 38) and (10 < idade <= 30):
    print('Emergente')
elif (34 < temperatura <= 36 or 38 < temperatura <= 40) and (2 < idade <= 10 or 50 < idade <= 60) and (25 < imc <= 32.5) and (100 < batimentos <= 115):
    print('Emergente')
elif (34 < temperatura <= 36 or 38 < temperatura <= 40) and (2 < idade <= 10 or 50 < idade <= 60) and (25 < imc <= 32.5) and (37 < temperatura <= 38):
    print('Emergente')
elif (34 < temperatura <= 36 or 38 < temperatura <= 40) and (2 < idade <= 10 or 50 < idade <= 60) and (25 < imc <= 32.5) and (10 < idade <= 30):
    print('Emergente')
elif (34 < temperatura <= 36 or 38 < temperatura <= 40) and (2 < idade <= 10 or 50 < idade <= 60) and (100 < batimentos <= 115) and (37 < temperatura <= 38):
    print('Emergente')
elif (34 < temperatura <= 36 or 38 < temperatura <= 40) and (2 < idade <= 10 or 50 < idade <= 60) and (100 < batimentos <= 115) and (10 < idade <= 30):
    print('Emergente')
elif (34 < temperatura <= 36 or 38 < temperatura <= 40) and (2 < idade <= 10 or 50 < idade <= 60) and (37 < temperatura <= 38) and (10 < idade <= 30):
    print('Emergente')
elif (imc <= 20 or 32.5 < imc <= 40) and (45 < batimentos <= 60 or 115 < batimentos <= 140):
    print('Muito Urgente')
elif (imc <= 20 or 32.5 < imc <= 40) and (34 < temperatura <= 36 or 38 < temperatura <= 40):
    print('Muito Urgente')
elif (imc <= 20 or 32.5 < imc <= 40) and (2 < idade <= 10 or 50 < idade <= 60):
    print('Muito Urgente')
elif (45 < batimentos <= 60 or 115 < batimentos <= 140) and (34 < temperatura <= 36 or 38 < temperatura <= 40):
    print('Muito Urgente')
elif (45 < batimentos <= 60 or 115 < batimentos <= 140) and (2 < idade <= 10 or 50 < idade <= 60):
    print('Muito Urgente')
elif (34 < temperatura <= 36 or 38 < temperatura <= 40) and (2 < idade <= 10 or 50 < idade <= 60):
    print('Muito Urgente')
elif (imc <= 20 or 32.5 < imc <= 40) and (25 < imc <= 32.5) and (100 < batimentos <= 115):
    print('Muito Urgente')
elif (imc <= 20 or 32.5 < imc <= 40) and (25 < imc <= 32.5) and (37 < temperatura <= 38):
    print('Muito Urgente')
elif (imc <= 20 or 32.5 < imc <= 40) and (25 < imc <= 32.5) and (10 < idade <= 30):
    print('Muito Urgente')
elif (imc <= 20 or 32.5 < imc <= 40) and (100 < batimentos <= 115) and (37 < temperatura <= 38):
    print('Muito Urgente')
elif (imc <= 20 or 32.5 < imc <= 40) and (100 < batimentos <= 115) and (10 < idade <= 30):
    print('Muito Urgente')
elif (imc <= 20 or 32.5 < imc <= 40) and (37 < temperatura <= 38) and (10 < idade <= 30):
    print('Muito Urgente')
elif (45 < batimentos <= 60 or 115 < batimentos <= 140) and (25 < imc <= 32.5) and (100 < batimentos <= 115):
    print('Muito Urgente')
elif (45 < batimentos <= 60 or 115 < batimentos <= 140) and (25 < imc <= 32.5) and (37 < temperatura <= 38):
    print('Muito Urgente')
elif (45 < batimentos <= 60 or 115 < batimentos <= 140) and (25 < imc <= 32.5) and (10 < idade <= 30):
    print('Muito Urgente')
elif (45 < batimentos <= 60 or 115 < batimentos <= 140) and (100 < batimentos <= 115) and (37 < temperatura <= 38):
    print('Muito Urgente')
elif (45 < batimentos <= 60 or 115 < batimentos <= 140) and (100 < batimentos <= 115) and (10 < idade <= 30):
    print('Muito Urgente')
elif (45 < batimentos <= 60 or 115 < batimentos <= 140) and (37 < temperatura <= 38) and (10 < idade <= 30):
    print('Muito Urgente')
elif (34 < temperatura <= 36 or 38 < temperatura <= 40) and (25 < imc <= 32.5) and (100 < batimentos <= 115):
    print('Muito Urgente')
elif (34 < temperatura <= 36 or 38 < temperatura <= 40) and (25 < imc <= 32.5) and (37 < temperatura <= 38):
    print('Muito Urgente')
elif (34 < temperatura <= 36 or 38 < temperatura <= 40) and (25 < imc <= 32.5) and (10 < idade <= 30):
    print('Muito Urgente')
elif (34 < temperatura <= 36 or 38 < temperatura <= 40) and (100 < batimentos <= 115) and (37 < temperatura <= 38):
    print('Muito Urgente')
elif (34 < temperatura <= 36 or 38 < temperatura <= 40) and (100 < batimentos <= 115) and (10 < idade <= 30):
    print('Muito Urgente')
elif (34 < temperatura <= 36 or 38 < temperatura <= 40) and (37 < temperatura <= 38) and (10 < idade <= 30):
    print('Muito Urgente')
elif (2 < idade <= 10 or 50 < idade <= 60) and (25 < imc <= 32.5) and (100 < batimentos <= 115):
    print('Muito Urgente')
elif (2 < idade <= 10 or 50 < idade <= 60) and (25 < imc <= 32.5) and (37 < temperatura <= 38):
    print('Muito Urgente')
elif (2 < idade <= 10 or 50 < idade <= 60) and (25 < imc <= 32.5) and (10 < idade <= 30):
    print('Muito Urgente')
elif (2 < idade <= 10 or 50 < idade <= 60) and (100 < batimentos <= 115) and (37 < temperatura <= 38):
    print('Muito Urgente')
elif (2 < idade <= 10 or 50 < idade <= 60) and (100 < batimentos <= 115) and (10 < idade <= 30):
    print('Muito Urgente')
elif (2 < idade <= 10 or 50 < idade <= 60) and (37 < temperatura <= 38) and (10 < idade <= 30):
    print('Muito Urgente')
elif (imc <= 20 or 32.5 < imc <= 40) or (45 < batimentos <= 60 or 115 < batimentos <= 140) or (34 < temperatura <= 36 or 38 < temperatura <= 40) or (2 < idade <= 10 or 50 < idade <= 60):
    print('Pouco Urgente')
elif (25 < imc <= 32.5) and (100 < batimentos <= 115):
    print('Pouco Urgente')
elif (25 < imc <= 32.5) and (37 < temperatura <= 38):
    print('Pouco Urgente')
elif (25 < imc <= 32.5) and (10 < idade <= 30):
    print('Pouco Urgente')
elif (100 < batimentos <= 115) and (37 < temperatura <= 38):
    print('Pouco Urgente')
elif (100 < batimentos <= 115) and (10 < idade <= 30):
    print('Pouco Urgente')
elif (37 < temperatura <= 38) and (10 < idade <= 30):
    print('Pouco Urgente')
else:
    print('Não Urgente')
