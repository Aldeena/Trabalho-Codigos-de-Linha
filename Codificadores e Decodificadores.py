from base64 import encode
from opcode import opname
from cryptography.fernet import Fernet

def index_in_list(a_list, index):     
    return index < len(a_list)

def binaryDecode(array):
    #printar grafico aqui
    string_ints = []
    for i in array:
        string_ints.append(str(i))

    string_ints = ''.join(string_ints)
    
    values = []
    # splits the string into an array containing substrings with the fixed length of (size of 1 byte)
    ascii_array =  [string_ints[i:i+8] for i in range(0, len(string_ints), 8)] 
    print(ascii_array)
    for i in ascii_array:
        values.append(int(i,2))
    return values


'''def paraBin(array):

    msg = []
    for palavra in range(0, len(array)):
        msg = msg + array[palavra]

    l, m= [], []

    for i in msg:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m
    '''

def asciiEncode(array):
    values = []
    for char in array:
        values.append(f'{ord(char)}')

    return values

def asciiDecode(array):

    res = ""

    for i in array:
        res = res + chr(i)

    return res

def binEncode(array):
    values = []
    for i in array:
        i = int(i)
        values.append(bin(i)[2:].zfill(8))

    print (values)

    values = list(''.join(values))
    bit_array = []
    for bit in values:
        bit_array.append(int(bit))
    return bit_array


def encrypt(array):
    values = []

    for i in array:
        i = int(i)

        if i%2 != 0:
            i = i+128
            
        if i > 255:
            i = i-255
        
        values.append(i)

    return values

def decrypt(array):

    values = []

    for i in array:
        i = int(i)

        if i%2 != 0:
            i = i-128

        if i < 0:
            i = i + 255

        values.append(i)

    return values


'''def convertPokemon(array):

    arquivo = open("Pokedex.txt", "r")
    pokemons = arquivo.readlines()
    #print(pokemons)

    criptografia = []

    values = []

    for char in array:
        values.append(ord(char))

    print(values)

    for j in range(0, len(array)):
        criptografia.append(pokemons[values[j]])

    arquivo.close()

    return criptografia	
    '''

def encodeMLT3(array):
    states = ['+' , '0', '-', '0']
    sinal = []

    index = 3
    i = 0

    for i in range(0, len(array)):
        if array[i] == 1:
            index = (index + 1) % 4
        #print(states[index])
        sinal.append(states[index])

    return sinal
    

def DecodeMLT3(array):
    mensagem = []

    if array[0] != '0':
        mensagem.append(1)
    else:
        mensagem.append(0)
       
    for i in range(len(array)):
        if index_in_list(array, i+1):
            if array[i] != array[i+1]:
                mensagem.append(1)

            else:
                mensagem.append(0)

    return mensagem


    """
    Essa é uma função para convertar para binário
    
    print(num+"\n")
    vet_bin = [] * 8
    i = 0
    while num > 0:
        vet_bin[i] = num % 2
        i += 1
        num = num/2

    vet_bin.reverse()

    for j in vet_bin:
        print(vet_bin[j])

    print("\n")

    """

# Thomas e seus amigos

mensagem = ('Jesus')
print(mensagem)

#key = Fernet.generate_key()

#fernet = Fernet(key)

asciiString = asciiEncode(mensagem)
print(asciiString)

criptografado = encrypt(asciiString) #fernet.encrypt(mensagem.encode())
print(criptografado)

#criptografia = convertPokemon(mensagem)
#print(criptografia)

values = binEncode(list(criptografado))
print(values)

sinal = encodeMLT3(values)
print(sinal)

decodificado = DecodeMLT3(sinal)
print(decodificado)

bitsRefeitos = binaryDecode(decodificado)
print(bitsRefeitos)

codificado = decrypt(criptografado)#fernet.decrypt(criptografado).decode()
print(codificado)

final = asciiDecode(codificado)
print(final)