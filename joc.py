import random

class Erou:
    def __init__(self,viata,agilitate,noroc,magie,forta,inteligenta,numerar):
        self.viata=viata
        self.agilitate=agilitate
        self.noroc=noroc
        self.forta=forta
        self.inteligenta=inteligenta
        self.numerar=numerar
        self.magie=magie
    def scadehp(self,nr):
        self.viata-=nr
    def crestehp(self,nr):
        self.viata+=nr

class Soldat(Erou):
    def __init__(self, viata, agilitate, noroc, magie, forta, inteligenta,numerar):
        super().__init__(viata, agilitate, noroc, forta, magie, inteligenta,numerar)

class Vrajitor(Erou):
    def __init__(self, viata, agilitate, noroc, magie, forta, inteligenta, numerar):
        super().__init__(viata, agilitate, noroc, magie, forta, inteligenta, numerar)

class Savant(Erou):
    def __init__(self, viata, agilitate, noroc, magie, forta, inteligenta, numerar):
        super().__init__(viata, agilitate, noroc, magie, forta, inteligenta, numerar)
    
class Asasin(Erou):
    def __init__(self, viata, agilitate, noroc, magie, forta, inteligenta, numerar):
        super().__init__(viata, agilitate, noroc, magie, forta, inteligenta, numerar)

print("Bine ai venit! Introdu numele pe care vrei sa il aiba eroul")
nume=input()
print("Actiunea se petrece in vremuri demult apuse, pe taramuri din basme\nPovestea incepe cu eroul nostru {}, un tanar dintr-un sat indepatat care se hotaraste sa plece din casa parintilor lui ca sa-si gaseasca menirea. El se hotaraste sa mearga la hanul din sat prima data ca sa se gandeasca unde sa plece si ce sa faca. Acolo apare o clarvazatoare batrana care ii spune ca ii va ghici destinul, iar tanarul {} accepta.".format(nume,nume))
tip=random.randrange(1,5)
if(tip==1):
    print("Batrana crede ca vei fi soldat bun!")
elif(tip==2):
    print("Batrana crede ca ai anumite puteri magice si ca vei deveni vrajitor!")
elif(tip==3):
    print("Batrana crede ca vei fi un savant bun!")
else:
    print("Batrana crede ca vei fi un asasin bun!")
print("Accepti soarta pe care ti-a dat-o batrana(Decizia implica ca {} va devenii clasa data de batrana)?\nIntrodu 1 pentru da sau 2 pentru nu".format(nume))
while(1):
    acceptare=input()
    if(acceptare=='1' or acceptare=='2'):
        break
    print("optiune incorecta")
erou=nume
while(1):
    if(acceptare=='1'):
        if(tip==1):
            erou=Soldat(100,80,random.randrange(70,101),0,85,50,0)
            print("{} este soldat!".format(nume))
            break
        elif(tip==2):
            erou=Vrajitor(100,75,random.randrange(50,101),90,40,80,0)
            print("{} este vrajitor!".format(nume))
            break
        elif(tip==3):
            erou=Savant(100,75,random.randrange(50,101),80,50,85,0)
            print("{} este savant!".format(nume))
            break
        else:
            erou=Asasin(100,85,random.randrange(50,101),70,80,65,0)
            print("{} este asasin!".format(nume))
            break
    else:
        while(1):
            print("Introdu clasa pe care vrei sa o aiba eroul 1 pentru soldat, 2 pentru vrajitor, 3 pentru savant si 4 pentru asasin\nSoldatul are ca atribut principal fort, vrajitorul magia, savantul inteligenta si asasinul agilitatea")
            tip=input()
            if(tip=='1' or tip=='2' or tip=='3' or tip=='4'):
                break
            else:
                print("optiune incorecta")
        if(tip=='1'):
            erou=Soldat(100,65,random.randrange(50,101),0,85,50,0)
            print("Ai ales clasa soldat!")
            break
        elif(tip=='2'):
            erou=Vrajitor(100,65,random.randrange(50,101),90,40,80,0)
            print("Ai ales clasa vrajitor!")
            break
        elif(tip=='3'):
            erou=Savant(100,60,random.randrange(50,101),80,40,85,0)
            print("Ai ales clasa savant!")
            break
        else:
            erou=Asasin(100,85,random.randrange(50,101),70,75,65,0)
            print("Ai ales clasa asasin!")
            break    
print("Batrana ii mai da tanarului {} o harta a unui taram indepartat numit Eldoria, unde se spune ca s-ar afla elixirul nemuririi\nAstfel, {} pleaca spre Eldoria si ajunge intr-o padure fermecata unde vede o ciuperca atragatoare, {} fiind infometat.".format(nume,nume,nume))
print("Vrei sa mananci ciuperca ? Introdu 1 pentru da sau 2 pentru nu")
while(1):
    alegere=input()
    if(alegere=='1' or alegere=='2'):
        break
    print("optiune incorecta")








