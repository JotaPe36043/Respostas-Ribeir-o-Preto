def inverte(palavra):
    invertida = ""
    for l in range(len(palavra) - 1, -1, -1):
        invertida += palavra[l]
    return invertida

palavra = input("Digite uma palavra: ")
print(f"A palavra {palavra} invertida fica :",  inverte(palavra))