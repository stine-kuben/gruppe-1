# Oppgave 1. testing:
def tell_tegn (tegn, tekst):
    teller = 0
    for i in tekst: 
        if i == tegn:
            teller += 1
    return teller

def erLik(tall1, tall2, tall3):
    if tall1 == tall2 and tall2 == tall3:
        return True
    else:
        return False
    
print(erLik(5, 5, 5))
print(erLik(5, 3, 5))