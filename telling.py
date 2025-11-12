def summertall(tall1, tall2):
    return tall1 + tall2
summertall(6, 7)

#Kommentar

def erLik(tall1, tall2, tall3):
    if tall1 == tall2 and tall2 == tall3:
        return True
    else:
        return False
    
print(erLik(5, 5, 5))
print(erLik(5, 3, 5))