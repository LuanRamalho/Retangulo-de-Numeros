# Solicita ao usuário a largura e a altura do retângulo
altura = int(input("Digite a altura do retângulo: "))
largura = int(input("Digite a largura do retângulo: "))

# Exibe o retângulo de números
for i in range(altura):
    for j in range(largura):
        print(j + 1, end=" ")  # Imprime o número com espaço no final
    print()  # Nova linha no final de cada linha do retângulo
input()