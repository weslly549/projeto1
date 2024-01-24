#Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
#depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito 
#através do calculo (vitórias - derrotas
#Se vitórias for menor do que 10 = Ferro
#Se vitórias for entre 11 e 20 = Bronze
#Se vitórias for entre 21 e 50 = Prata
#Se vitórias for entre 51 e 80 = Ouro
#Se vitórias for entre 81 e 90 = Diamante
#Se vitórias for entre 91 e 100= Lendário
#Se vitórias for maior ou igual a 101 = Imortal


def quant_vitórias(vitórias):

    if vitórias < 10:
        print("O Herói tem de saldo de "+str(vitórias)+" está no nível de ferro!")
    
    elif 11 <= vitórias <= 20:
        print("O Herói tem de saldo de "+str(vitórias)+" está no nível de bronze!")

    elif 21 <= vitórias <= 50:
        print("O Herói tem de saldo de "+str(vitórias)+" está no nível de prata!")

    elif 51 <= vitórias <= 80: 
        print("O Herói tem de saldo de "+str(vitórias)+" está no nível de ouro!")

    elif 81 <= vitórias <= 90:
        print("O Herói tem de saldo de "+str(vitórias)+" está no nível de diamante!")

    elif 91 <= vitórias <= 100:
        print("O Herói tem de saldo de "+str(vitórias)+" está no nível de lendário!")

    elif vitórias > 101:
        print("O Herói tem de saldo de "+str(vitórias)+" está no nível de imoral!") 


a = int(input("Digite a quantidade de vitórias que o herói  possui: "))

quant_vitórias(a)