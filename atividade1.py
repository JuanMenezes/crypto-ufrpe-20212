"""
Escreva uma função em Python que recebe um texto e retira do mesmo todos os caracteres que não são letras, inclusive espaços. 
O resultado final deve conter apenas letras minúsculas que é uma espécie de "padrão" para mensagens que serão cifradas.
"""

string = 'Marcelo Gama - Rua 1233, %$@$@dfe'
def onlyCharLetters(string):
    result = ""
    for index in string:
        if index.isalpha():
            result= "".join([result,index])
    return result.lower()


print(onlyCharLetters(string))