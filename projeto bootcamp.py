


nome = input("Digite seu nome, herói: ")

nivel = int(input("Digite seu nível, herói: "))


if nivel <= 1000:
    print("O herói de nome "+nome+" está no nível de ferro!") 

elif 1001 <= nivel <= 2000:
    print("O herói de nome "+nome+" está no nível de bronze!")

elif 2001 <= nivel <= 5000:
    print("O herói de nome "+nome+" está no nível de prata!")

elif 5001 <= nivel <= 7000:
    print("O herói de nome "+nome+" está no nível de ouro!")

elif 7001 <= nivel <= 8000:
    print("O herói de nome "+nome+" está no nível de platina!")

elif 8001 <= nivel <= 9000:
    print("O herói de nome "+nome+" está no nível de ascendente!")

elif 9001 <= nivel <= 10000:
    print("O herói de nome "+nome+" está no nível de imoral!")

elif nivel >= 10001:
    print("O herói de nome "+nome+" está no nível de radiante!")





