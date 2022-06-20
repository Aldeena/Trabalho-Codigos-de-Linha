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

def convertBin(array):
    values = []
    for char in array:
        values.append(f'{ord(char):08b}'.format(8))
    
    values = list(''.join(values))
    bit_array = []
    for bit in values:
        bit_array.append(int(bit))
    return bit_array
    
    """
    Essa é uma função para convertar para binário
    """

    
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

# Thomas e seus amigos

vet_poke = list('Thomas e seus amigos')
print(vet_poke)
values = convertBin(vet_poke)

print(values)
print(binaryDecode(values))

