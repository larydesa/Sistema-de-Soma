print("===== SISTEMA DE SOMA =====\n")
soma = 0
lista_numeros = []
while True:
  numero = int(input("Digite um número (ou 0 para sair): "))
  if numero == 0:
    print("\nEncerrando o programa...")
    break
  else:
    soma += numero
    list.append(numero)

print("\nQuantidade de números digitados: ", len(lista_numeros))
print("Soma total: ", soma)
print("\n Obrigado por usar o sistema!")
