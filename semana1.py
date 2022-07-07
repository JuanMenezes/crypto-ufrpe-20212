#Geração de caracteres de c1 até c2 (incluindo ambos)

def charRange(c1,c2):
    lista = []
    for c in range(ord(c1), ord(c2)+1):
        lista = lista + [chr(c)]
    return lista

print(charRange("a","k"))



#CIFRA DE DESLOCAMENTO - VERSÃO 1 ( O TEXTO CONTÉM APENAS LETRAS)
#TODO - precisamos implementar isso no futuro
deslocamento('MarceloGama',3)



#CIFRAS DE DESLOCAMENTO - VERSÃO2 ( MANTÉM CACTERES QUE NÃO SAÃO LETRAS EM SUAS POSIÇÕES ORIGINAIS)
#TODO - precisaremos imnplementar isso no futuro
deslocamentochat('Rua Cifrada, 125 - Recife ****',4)



#LIMPAR TEXTO - ELIMINA CARACTERES QUE NÃO SÃO LETRAS (INCLUSIVE ESPAÇOS)
#TODO - também iremos precisar dessa função
texto = 'Marcelo Gama - Rua 1233, %$@$@dfe'
limpartexto(texto)


#UTILIDADES
#1) posição de um elementos em uma lista lista.index(elemento)
letras = ['a','b','c','d','e']
letras.index('c')


#2) Atenção ao procurar letras em uma lista (lower, upper)
letras = ['A','B','C','D','E']
letras.index('d'.upper())


#3 Saber se um elemento está em uma lista (count)
letras=['a','b','c']
letras.count('a')
