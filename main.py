#Assimilação de variáveis
print("Digite o salário de Carlos")
salCarlos = float(input())
meses = int()
salJoao = float()
salJoao = salCarlos / 3
while True:
  salCarlos = salCarlos + (salCarlos * 0.02)
  salJoao = salJoao + (salJoao * 0.05)
  meses = meses + 1
  if(salJoao >= salCarlos):
    print("O total de meses que são precisos:", meses)
    break