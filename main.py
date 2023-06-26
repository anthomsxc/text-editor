import os
import msvcrt
from colorama import Back, Style

def createFile():
    dir_path = os.path.dirname(os.path.realpath('__file__'))
    os.system("cls")

    file = input("Nom du fichier à créer : ")

    lignes = ['']

    current_line = 0

    while True:
        os.system("cls")
        for numero, ligne in enumerate(lignes, 1):
            num = Back.LIGHTBLUE_EX + str(numero) + Style.RESET_ALL
            if numero - 1 == current_line:
                # Highlight the current line
                print(f"> {num} {ligne}")
            else:
                print(f"  {num} {ligne}")

        key = ord(msvcrt.getch())

        if key == 224:  # Special keys (arrow keys, function keys, etc.)
            key = ord(msvcrt.getch())  # Get the actual key code

            if key == 80:  # Down arrow
                current_line = min(current_line + 1, len(lignes) - 1)
            elif key == 72:  # Up arrow
                current_line = max(current_line - 1, 0)

        elif key == 13:  # Enter key
            new_text = input("Nouveau texte : ")
            lignes[current_line] = new_text

        elif key == 19:  # Ctrl+S
            with open(file, 'w') as file_to_write:
                file_to_write.write('\n'.join(lignes))
            print("Fichier créé et sauvegardé !")
            break

        elif key == 27:  # Escape key
            break
