from opcode import opname

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

def convertBin(array):
    #binary_string = paraBin(array)
    values = []
    for char in array:
        values.append(f'{ord(char):08b}'.format(8))
    
    values = list(''.join(values))
    bit_array = []
    for bit in values:
        bit_array.append(int(bit))
    return bit_array


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

mensagem = ('ü')
print(mensagem)

#criptografia = convertPokemon(mensagem)
#print(criptografia)

values = convertBin(mensagem)

print(values)

sinal = encodeMLT3(values)
print(sinal)

decodificado = DecodeMLT3(sinal)
print(decodificado)
#print(binaryDecode(values))

