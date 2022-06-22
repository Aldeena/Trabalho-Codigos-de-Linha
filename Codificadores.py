def index_in_list(a_list, index):     
    return index < len(a_list)

def convertBin(array):
    #Função para codificar o sinal, para uma codificação em
    values = []
    for char in array:
        values.append(f'{ord(char):08b}'.format(8))
    
    values = list(''.join(values))
    bit_array = []
    for bit in values:
        bit_array.append(int(bit))
    return bit_array

def encodeMLT3(array):
    #Função pra codificar o sinal, de acordo com o algoritmo de código de linha MLT-3
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


'''

Função desnecessária criada para converter uma string em uma lista de pokemons, sendo um pra cada
caracter

def convertPokemon(array):

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

'''


    char states[4] = { '+', '0', '-', '0' };
    int index = 3;
    int b = 0x97;         // OP example
    int i;
    for (i=0; i<8; i++) {
        if (b & 0x80)
            index = (index + 1) % 4;
        printf ("%c", states[index]);
        b <<= 1;
    }
    printf("\n");
    return 0;

    int direction = 1;//1: upto, -1: downto
    int state = 0;
    char seq = "10010111";
    while(seq){
        if(*seq == '1'){
            state += direction;
            if(state == 1 || state == -1)
                direction = -direction;//reversal of direction
        }
        switch(state){//putchar("-0+"[state+1]);
        case 1: putchar('+');break;
        case 0: putchar('0');break;
        case -1: putchar('-');break;
        }
        ++seq;
    }
    '''