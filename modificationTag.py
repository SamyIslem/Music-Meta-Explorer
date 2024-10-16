import os
from os.path import abspath
from mutagen.mp3 import MP3
from mutagen.id3 import TIT2, TPE1, TALB, TCON, TYER, ID3
from mutagen.flac import FLAC


tagsModifiable = {1: 'Title',
                  2: 'Artist',
                  3: 'Album',
                  4: 'Genre',
                  5: 'date'}


class gestionTags:
    def __init__(self, fichier):
        self.fichier = fichier

    def modifierTag(self):
        print(tagsModifiable)
        print("")
        a = int(
            input("Veuillez introduire l'index du tag que vous voudriez changer\n"))
        while (a not in [1, 2, 3, 4, 5]):
            a = int(
                input("Veuillez introduire une valeur comprise entre 1 et 5\n"))

        # if (a == 5):
        #     try:
        #         x = int(input("veuillez intorduire la nouvelle valeur\n"))
        #     except ValueError:
        #         print(
        #             "Oops!  Valeur non valide, la nouvelle valeur doit impérativement etre un entier.")
        #         return

        else:
            x = input("veuillez intorduire la nouvelle valeur\n")

        if (self.fichier.lower().endswith(".mp3")):
            audio = MP3(self.fichier, ID3=ID3)
            if (a == 1):
                audio["TIT2"] = TIT2(encoding=3, text=x)
            elif (a == 2):
                audio["TPE1"] = TIT2(encoding=3, text=x)
            elif (a == 3):
                audio["TALB"] = TIT2(encoding=3, text=x)
            elif (a == 4):
                audio["TCON"] = TIT2(encoding=3, text=x)
            else:
                audio["TYER"] = TIT2(encoding=3, text=x)

            audio.save()

        elif self.fichier.lower().endswith(".flac"):
            audio = FLAC(self.fichier)
            audio[tagsModifiable[a]] = x
            audio.save()

        else:
            print(
                "Format de fichier non supporté. Veuillez utiliser un fichier MP3 ou FLAC.")


musique = gestionTags("chanson/Leo-Das-Entry.mp3")
musique.modifierTag()
