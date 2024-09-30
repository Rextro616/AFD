from afd import AFD
import csv

def reportOccurrences(afd, patterns, text):
    occurrences = []
    for row_num, line in enumerate(text, start=1):
        for col_num, char in enumerate(line, start=1):
            if afd.run(char):
                occurrences.append({
                    'fila': row_num,
                    'columna': col_num,
                    'texto': char
                })
    return occurrences

def main():
    states = {0, 1, 2, 3} 
    alphabet = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~",
    " ", "\t"} 
    transitions = {(0, 'a'): 1, (1, 'b'): 2} 
    startState = 0
    acceptStates = {2}
    afd = AFD(states, alphabet, transitions, startState, acceptStates)
    patterns = 
    text = 
    occurrences = reportOccurrences(afd, patterns, text)
    return occurrences
