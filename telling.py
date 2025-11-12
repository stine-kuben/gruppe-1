# Oppgave 1:
def tell_tegn (tegn, tekst):
    teller = 0
    for i in tekst: 
        if i == tegn:
            teller += 1
    return teller
