letrasParaBinario = {'A': 1100001, 'B': 1100010 , 'C': 1100011 , 'D': 1100100 , 'E': 1100101 , 'F': 1000110 , 'G': 1100111 , 'H': 1101000 , 'I': 1001001, 'J': 1001010 , 'K': 1101011 , 'L': 1001100 ,
                       'M': 1001101 , 'N': 1101110 , 'O': 1101111, 'P': 1110000 , 'Q': 1110001, 'R': 1010010 , 'S': 1010011 , 'T': 1010100 , 'U': 1010101 , 'V' : 1010110 , 'W': 1110111 , 'X' : 1111000 , 'Y' : 1011001 , 'Z' : 1011010 }


letrasParaNumeros = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
                       'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19}



def criptografarCaracter (frase):
    palavra = input("Digite uma palavra")
    mensagem = palavra
    for i in frase:
        mensagem = mensagem + chr(ord(i)) + 5
        return mensagem
    
   


#def criptografarNumero(){
    palavra = input("Digite uma palavra para ser alterada para número")
#}

#def criptografaBinario(){
    palavra = input("Digite uma palavra para ser alterada para binario")
#}




print('\033[36m'"------------------BEM VINDO A CRIPTOGRAFIA-----------------")

print("QUAL METODO DE CRIPTOGRAFIA")
print('1- Palavra')
print('2- Numérico')


metodoCripto = int(input("Digite um método de criptografia: "))


if metodoCripto == 1:
    print('1- Mudança de caracter')
    print('2- Binário')
    print('3- Número')
    palavraCripto = int(input("Digite qual tipo de criptografia deseja: "))
    if palavraCripto == 1:
        print('O método desejado foi Mudança de Caracter')
        print(criptografarCaracter(frase = 1))
    elif palavraCripto == 2:
        print('O método desejado foi Binário')
    elif palavraCripto == 3:
        print('O metodo desejado foi Número')
elif metodoCripto == 2:
    print('1- Alterar numeros da senha')


