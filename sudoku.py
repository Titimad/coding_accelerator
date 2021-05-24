#!/usr/bin/python3

import sys

#ouvrir les fichiers sources

fichier1 = open(sys.argv[1], 'r')

list_sudoku = fichier1.readlines()

#supprimer les \n de list_list_sudoku

for i in range(len(list_sudoku)):

    list_sudoku[i] = list(list_sudoku[i][0:len(list_sudoku[i]) - 1])

    for j in range(list_sudoku[i].count('|')):
        list_sudoku[i].remove('|')

    for j in range(list_sudoku[i].count('-')):
        list_sudoku[i].remove('-')

    for j in range(list_sudoku[i].count('+')):
        list_sudoku[i].remove('+')

#sys.exit()
#lire la ligne
for line_number in range(11):

    nbr_ = list_sudoku[line_number].count('_')
    line = list_sudoku[line_number]
#s'il y a qu'un chiffre manquant --> le combler

    if nbr_ == 1:

        #index de '_'
        index_ = list_sudoku[line_number].index('_')

        #supprimer le '_' et les '|' de la liste

        del line[index_]

#convertir la liste de caractères en liste de chiffre et l'ordonner

        for i in range(8):
            line[i] = int(line[i])

#déterminer le chiffre manquant

        list_sudoku[line_number].insert(index_, 45 - sum(line))

    elif nbr_ == 0 and len(list_sudoku[line_number]) != 0:
#
        for i in range(9):
            line[i] = int(line[i])

#s'il y a 2 chiffres manquants
for i in range(len(list_sudoku)):
    nbr_ = list_sudoku[i].count('_')
    if nbr_ == 2:
        j = 0
        while j <= 1:

            #index de '_'
            index_ = list_sudoku[i].index('_')

            list1 = []
            for line_number in range(11):
                if line_number != i and line_number != 3 and line_number != 7:
                    list1.append(list_sudoku[line_number][index_])

                    #déterminer le chiffre manquant
                    del list_sudoku[i][index_]
                    list_sudoku[i].insert(index_, 45 - sum(list1))
            j = j + 1

#convertir la liste de string en int
        for k in range(9):
            list_sudoku[i][k] = int(list_sudoku[i][k])

#mettre en forme le tableau final
for i in range(len(list_sudoku)):
    if i != 3 and i != 7:
        for k in range (9):
            list_sudoku[i][k] = str(list_sudoku[i][k])
        list_sudoku[i].insert(3, '|')
        list_sudoku[i].insert(7, '|')
        list_sudoku[i].insert(11, '\n')
        list_sudoku[i] = ''.join(list_sudoku[i])

    else:
        list_sudoku [i] = "---+---+---\n"

#print(list_sudoku)

print(''.join(list_sudoku))


#afficher le sudoku résolu


fichier1.close()
