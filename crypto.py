letrasParaBinario = {'A': 1100001, 'B': 1100010 , 'C': 1100011 , 'D': 1100100 , 'E': 1100101 , 'F': 1000110 , 'G': 1100111 , 'H': 1101000 , 'I': 1001001, 'J': 1001010 , 'K': 1101011 , 'L': 1001100 ,
                       'M': 1001101 , 'N': 1101110 , 'O': 1101111, 'P': 1110000 , 'Q': 1110001, 'R': 1010010 , 'S': 1010011 , 'T': 1010100 , 'U': 1010101 , 'V' : 1010110 , 'W': 1110111 , 'X' : 1111000 , 'Y' : 1011001 , 'Z' : 1011010 }




def criptografar (frase):
    mensagem = ''

    for i in frase: 
        mensagem = mensagem + chr (ord(i) + 9)

    return mensagem


print(criptografar('Elvis'))