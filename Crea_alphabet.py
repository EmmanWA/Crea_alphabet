import string
import os


emplacement = os.path.dirname(__file__)

def Crea_alphabet(chemin):
    alphabet = string.ascii_uppercase
    chemin1 = os.path.join(emplacement,'Alphabet')
    if not os.path.exists(chemin1):
        os.makedirs(chemin1)

    for i in alphabet:
        chemin2 = os.path.join(chemin1,i)
        if not os.path.exists(chemin2):
            os.makedirs(chemin2)
    
Crea_alphabet(emplacement)



