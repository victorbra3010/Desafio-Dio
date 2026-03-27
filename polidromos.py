palavra = input("Digite um palíndromo: ").lower().replace(" ", "")

if palavra == palavra[::-1]:
    print("É palíndromo")
else:
    print("Não é palíndromo")