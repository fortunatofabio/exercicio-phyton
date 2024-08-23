eleitores = int(input("Digite a quantidade de eleitores: "))
votosbrancos = int(input("Digite quantos votos brancos tiveram: "))
votosnulos = int(input("Digite a quantidade de votos nulos: "))
votosvalidos = int(input("Digite a quantidade total de votos válidos: ")) 

eleitores = eleitores
votosbrancos = (votosbrancos/eleitores)*100
votosnulos = (votosnulos/eleitores)*100
votosvalidos = (votosvalidos/eleitores)*100

print("O percentual de votos válidos são:", votosvalidos, "%")
print("O percentual de votos brancos são:", votosbrancos, "%")
print("O percentual de votos nulos são:", votosnulos, "%")

