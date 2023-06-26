import os
import msvcrt
import time
from colorama import Back, Style

def mainInterface():

    print("                                    text editor by @mxz")

    print("/n        options :")
    print("/n/n        [1] - open file")
    print("            [2] - create file")
    print("            [3] - exit")

    select = input("/n/nselect :")

    if select == "1":
        createFile()
    if elif select == "2":
        openFile()
    if elif select == "3":
        print("aurevoir")
        time.sleep(1)
        exit(0)
    

def createFile():
   
    os.system("cls")

    file = input("Nom du fichier : ")

    with open(file, 'r+') as file_to_write:
        lignes = file_to_write.readlines()
        lignes_backup = lignes.copy()

    current_line = 0

    while True:
        os.system("cls")
        for numero, ligne in enumerate(lignes, 1):
            num = Back.LIGHTBLUE_EX + str(numero) + Style.RESET_ALL
            if numero - 1 == current_line:
                print(f"> {num} {ligne.strip()}")
            else:
                print(f"  {num} {ligne.strip()}")

        key = ord(msvcrt.getch())

        if key == 224: 
            key = ord(msvcrt.getch())

            if key == 80: 
                current_line = min(current_line + 1, len(lignes) - 1)
            elif key == 72:
                current_line = max(current_line - 1, 0)

        elif key == 13:  # touche entrer
            new_text = input("Nouveau texte : ")
            lignes[current_line] = new_text + '\n'

        elif key == 26:  # touche retour
            if current_line < len(lignes):
                lignes[current_line] = lignes_backup[current_line]

        elif key == 19:  # touche sauvegarde
            with open(file, 'w') as file_to_write:
                file_to_write.writelines(lignes)
            break

        elif key == 27: # touche quitter
            print("en cours de sauvegarde...")
            time.sleep(0.5)
            print("aurevoir...")
            break


if __name__ == "__main__":
    mainInterface()
