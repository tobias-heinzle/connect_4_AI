import numpy as np
import os

#gibt das spielfeld am bildschirm aus, dabei wird die bisherige ausgabe gelöscht
def display_state(state):
    os.system('cls||clear')
    print("0 1 2 3 4 5 6")
    for row in range(6):
        r = []
        for column in range(7):
            char = state[6*column + row]
            color = '\x1b[0m'
            if char == 'X':
                color = '\x1b[6;30;42m'
            elif char == 'O':
                color = '\x1b[6;30;41m'

            r.append(color + char +'\x1b[0m' + ' ' )
        print("".join(r))

#plaziert einen stein einer bestimmten farbe(char) in einer spalte(column)
#gibt das spielfeld und die position des plazierten steines zurück
def drop_piece(state,column,char):
        #pass state as string 
        tmp = list(state)
        for k in range(1,6):
            if tmp[6*column + k] != "_":
                tmp[6*column + k -1] = char 
                return ["".join(tmp), [column,k-1]]
        tmp[6*column + 5] = char
        return ["".join(tmp), [column,5]]

#konvertiert das spielfeld von string in einen numpy vektor mit länge 42
def str2vec(state):
    l = list(state)
    result = np.zeros(42)
    for i in range(42):
        if l[i] == 'X':
            result[i] = 1 
        if l[i] == 'O':
            result[i] = -1       
    return result