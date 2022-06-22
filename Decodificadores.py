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
