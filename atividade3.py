# Parte 1 -  escreva uma função em python que recebe um texto limpo, isto é, sem acentos nem números e nem caracteres especiais
import random
stringRaw = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using , making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like). Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33'
key = random.randint(0,26) #Gerando chave aleatoriamente
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def onlyCharLetters(string):
    result = ""
    for index in string:
        if index.isalpha():
            result= "".join([result,index])
    return result.lower()

def cifraDeslocamento(message, key):
    result = ''
    for char in message:
        try:
            temp = (alphabet.index(char) + key) % 26
            result += alphabet[temp]
        except ValueError:
            result += char
    return result.upper()


cifra = cifraDeslocamento(onlyCharLetters(stringRaw),key)
print(key)
print(cifra)