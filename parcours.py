import os
from os.path import abspath


class Aroborescence:
    def __init__(self, dossier):
        self.dossier = dossier

    def parcours(self):
        dir_path=abspath(self.dossier)
        for dirPath, dirName, fileNames in os.walk(dir_path):
            for files in fileNames: 
                if files.lower().endswith(".mp3"):
                    print(files)
        
        
musique= Aroborescence("./chanson")
musique.parcours()