from DateModel import Model

#Criado por Vinicius Tessis Cruz
#Disciplina - Algoritmos e Programação III
#Professora: Eduarda Rodrigues Monteiro

teste = Model()

dataPronta = teste.lerData()
 
if teste.verificarBissexto(dataPronta) == 1:
    bissexto = "é"
else:
    bissexto = "não é"

print("O ano", dataPronta.year, bissexto, "bissexto")

pascoa = teste.verificarPascoa(dataPronta.year)

print("A data da páscoa é:", teste.escreverExtenso(pascoa))