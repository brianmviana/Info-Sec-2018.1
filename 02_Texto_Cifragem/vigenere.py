alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    msg = (open('texto_cifrado_amor.txt','r')).read()
    arquivo = open('lista.txt', 'r')
    texto = open('teste.txt', 'a')

    for chave in arquivo:
        textoDescriptografado = descriptografar(chave.rstrip(), msg)
        if textoDescriptografado.find("amor") != -1:
            texto.writelines(textoDescriptografado + "\n")
            print(chave, " - ", textoDescriptografado)

    arquivo.close()
    texto.close()

def descriptografar(chave, mensagem):

    texto = []
    chaveIndex = 0
    chave = chave.upper()

    for letra in mensagem:
        index = alfabeto.find(letra.upper())
        if index != -1:
            index -= alfabeto.find(chave[chaveIndex])
            index %= len(alfabeto)
            if letra.isupper():
                texto.append(alfabeto[index])
            elif letra.islower():
                texto.append(alfabeto[index].lower())

            chaveIndex += 1
            if chaveIndex == len(chave):
                chaveIndex = 0
        else:
            texto.append(letra)
    return ''.join(texto)


if __name__ == '__main__':
    main()
