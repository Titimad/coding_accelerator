#!/usr/bin/python3

import sys

#ouvrir les fichiers sources

fichier1 = open(sys.argv[1], 'r')
fichier2 = open(sys.argv[2], 'r')

list_lines1 = fichier1.readlines()
list_lines2 = fichier2.readlines()

#supprimer les \n de list_lines1

for i in range(len(list_lines1)):
    
    list_lines1[i] = list_lines1[i][0:len(list_lines1[i]) - 1]

#parcourir les fichier pour voir si l'un est contenu dans l'autre

nbr_lines1 = len(list_lines1)
nbr_lines2 = len(list_lines2)

if nbr_lines1 <= nbr_lines2:
    
    for line in range(nbr_lines2):

        if list_lines1[0] in list_lines2[line]:
            index_column = list_lines2[line].index(list_lines1[0])

            for line1 in range(1, nbr_lines1):
                if (list_lines1[line1] in list_lines2[line + line1]):
                    index_line = line

                else:
                    index_line = "not found"
                    break
                
#si oui, renseigner la position
            
            break
    
        else:
            index_column = "not found"
            pass

    if (index_column == "not found") or (index_line == "not found"):
        print("Le 1er carré n'est pas présent dans le 2nd.")
    else:
        print(index_column, ",", index_line)
    
else:
    print("Le 1er carré doit être plus petit ou de même dimension que le 2nd carré.")


#fermer les fichiers ouverts

fichier1.close()
fichier2.close()
