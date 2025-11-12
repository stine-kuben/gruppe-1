from telling import *
#Oppgave 1. Testing
print(tell_tegn("b", "bananer"))

tallliste = [1, 2, 3, 4, 5]
def dobbel(liste):
    ny_liste = []
    for tall in liste:
        ny_liste.append(tall * 2)
    return ny_liste

print(tallliste)
print(dobbel(tallliste))


