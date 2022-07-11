"""
CIPHER ESCOLHIDA Base64 Cipher
me guiei usando apenas o algoritmo de encodificiação e decodificação, sei que o base64 usa um ultimo char "=" 
para validaçoes de partiçoes onde existam grupos que tem menos de 6bytes porém não apliquei essa ultima validação
visto que não achei literatura descrevendo esse processo
"""
#trazendo todos os elementos da tabela ascii usados no algoritmo de base64, mais pode ser visto nesse site https://base64.guru/learn/base64-characters
CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

class myBase64(object):
#Particiona a minha lista de bytes quando chamado
    def particiona(self,data, length):
        array_particionado = [data[i:i+length] for i in range(0, len(data), length)]
        array_balanceado = ""
        for index,item in enumerate(array_particionado):
            if len(item) < 6:
                item = item+'00'
                array_particionado[index] = item
            else:
                pass
        return array_particionado


    # Encodificação
    def encode(self,data):
        string = data
        group_bytes = ''.join('{0:08b}'.format(ord(x), 'b') for x in string)
        # depois daqui vou dividir em grupos de 6 characteres ( se o ultimo tiver menos então preenchemos com zero)
        dividestrings = self.particiona(group_bytes, 6)
        #vou pegar o resultado e adicionar mais 2 bytes a cada uma das strings para ficar com grupos de 8bytes
        for index_element,item_element in enumerate(dividestrings):
            item_element='00'+item_element
            dividestrings[index_element]=item_element
        # agora é so mente fazer a conversão para decimal para achar o correspondente na tabela ascii
        encoded_string = ""
        for element in dividestrings:
            encoded_string += CHARS[int(element, 2)]
        
        return encoded_string

    # Decodificação
    def decode(self,data):
        binstring = ""
        for char in data:
            #dessa forma já removo os 00bytes do começo e converto para binario a partir de um int chat do meu alfabeto
            binstring += "{:0>6b}".format(CHARS.index(char))        
        oitopartes = self.particiona(binstring, 8)
        decoded_string = b""
        for parte in oitopartes:
            decoded_string += bytes([int(parte, 2)])
        
        return decoded_string[0:-1]


#instanciando
teste = myBase64()
print(teste.decode(teste.encode("hello")))