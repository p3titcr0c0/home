import os

def compil(file,render):
    command="gcc -o " +str(render)+" "+str(file)
    os.system(command)
    
file=input("choisir un fichier: ")
render=input("choisir un nom de rendu: ")
compil(file,render)
