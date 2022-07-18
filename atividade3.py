# Parte 1 -  escreva uma função em python que recebe um texto limpo, isto é, sem acentos nem números e nem caracteres especiais
import random,math
import matplotlib.pyplot as plt
from collections import Counter

stringRaw = 'Caros amigos, a execucao dos pontos do programa faz parte de um processo de gerenciamento das diversas correntes de pensamento. No mundo atual, o julgamento imparcial das eventualidades cumpre um papel essencial na formulacao dos paradigmas corporativos. A nivel organizacional, o consenso sobre a necessidade de qualificacao exige a precisao e a definicao das condicoes financeiras e administrativas exigidas. Por conseguinte, a expansao dos mercados mundiais nao pode mais se dissociar do sistema de participacao geral. As experiencias acumuladas demonstram que a hegemonia do ambiente politico apresenta tendencias no sentido de aprovar a manutencao das condicoes inegavelmente apropriadas. No entanto, nao podemos esquecer que a necessidade de renovacao processual afeta positivamente a correta previsao do levantamento das variaveis envolvidas. O incentivo ao avanco tecnologico, assim como o inicio da atividade geral de formacao de atitudes agrega valor ao estabelecimento das formas de acao. O que temos que ter sempre em mente e que o desafiador cenario globalizado representa uma abertura para a melhoria da gestao inovadora da qual fazemos parte. Por outro lado, a adocao de politicas descentralizadoras estende o alcance e a importancia das posturas dos orgaos dirigentes com relacao as suas atribuicoes.'
key = random.randint(0,26) #Gerando chave aleatoriamente
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_SIZE = len(ALPHABET)
LETTER_FREQUENCY_PTBR = {
                    'a': 14.63, 'b': 1.04, 'c': 3.88, 'd': 4.99,'e':12.57,'f':1.02,'g':1.30,'h':1.28,'i':6.18,'j':0.40,
                    'k':0.02,'l':2.78,'m':4.74,'n':5.05,'o':10.73,'p':2.52,'q':1.20,'r':6.53,'s':7.81,'t':4.34,'u':4.63,
                    'v':1.67,'w':0.01,'x':0.21,'y':0.01,'z':0.47
                    }


def onlyCharLetters(string):
    result = ""
    for index in string:
        if index.isalpha():
            result= "".join([result,index])
    return result.lower()

def cifraDeslocamento(message,key,decrypt):
    result = ''
    for char in message:
        if char not in ALPHABET:
            result += char
            continue
        index = ALPHABET.index(char.lower())
        if decrypt:
            new_char = ALPHABET[(index - key) % ALPHABET_SIZE]
        else:
            new_char = ALPHABET[(index + key) % ALPHABET_SIZE]
        result += new_char.upper() if char.isupper() else new_char
    return result


#basicamente a diferença entre a frequencia esperada e a frequencia da letter atual, isso tudo dividido pelo tamanho da mensagem
def difference(message):
    counter = Counter(message)
    return sum([abs(counter.get(letter, 0) * 100 / len(message) - LETTER_FREQUENCY_PTBR[letter]) for letter in
                ALPHABET]) / ALPHABET_SIZE


def break_cipher(cipher_text):
    lowest_difference = math.inf
    encryption_key = 0

    for key in range(1, ALPHABET_SIZE):
        current_plain_text = cifraDeslocamento(cipher_text, key, True)
        current_difference = difference(current_plain_text)

        if current_difference < lowest_difference:
            lowest_difference = current_difference
            encryption_key = key

    return encryption_key


cifra = cifraDeslocamento(onlyCharLetters(stringRaw),key,False)
decript = cifraDeslocamento(cifra,key,True)
print(key)
print(break_cipher(cifra))