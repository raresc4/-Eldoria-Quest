import random
import sys
import time
import os

def gameover():
    delay_print("Viata ta a ajuns la 0\nGAME OVER\n")
    sys.exit()

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

class Erou:
    def __init__(self,viata,agilitate,noroc,magie,forta,inteligenta,numerar):
        self.viata=viata
        self.agilitate=agilitate
        self.noroc=noroc
        self.forta=forta
        self.inteligenta=inteligenta
        self.numerar=numerar
        self.magie=magie
    def scadenumerar(self,nr):
        self.numerar-=nr
    def crestenoroc(self,nr):
        self.noroc+=nr
    def scadehp(self,nr):
        self.viata-=nr
    def crestehp(self,nr):
        self.viata+=nr
    def cresteagilitatea(self,nr):
        self.agilitate+=nr
    def cresteinteligenta(self,nr):
        self.inteligenta+=nr
    def statistici(self):
        return "viata : {}  agilitate: {}  noroc: {}  magie: {}  forta: {}  inteligenta: {}  numerar: {}".format(self.viata,self.agilitate,self.noroc,self.magie,self.forta,self.inteligenta,self.numerar) 

class Soldat(Erou):
    def __init__(self, viata, agilitate, noroc, magie, forta, inteligenta,numerar,diamand,scurtatura):
        super().__init__(viata, agilitate, noroc, forta, magie, inteligenta,numerar)
        self.diamand=diamand
        self.scurtatura=scurtatura

class Vrajitor(Erou):
    def __init__(self, viata, agilitate, noroc, magie, forta, inteligenta, numerar,prieten):
        super().__init__(viata, agilitate, noroc, magie, forta, inteligenta, numerar)
        self.prieten=prieten

class Savant(Erou):
    def __init__(self, viata, agilitate, noroc, magie, forta, inteligenta, numerar,prieten):
        super().__init__(viata, agilitate, noroc, magie, forta, inteligenta, numerar)
        self.prieten=prieten
    
class Asasin(Erou):
    def __init__(self, viata, agilitate, noroc, magie, forta, inteligenta, numerar,scurtatura):
        super().__init__(viata, agilitate, noroc, magie, forta, inteligenta, numerar)
        self.scurtatura=scurtatura

delay_print("Bine ai venit! Introdu numele pe care vrei sa il aiba eroul\n")
nume=input()
os.system('cls')
delay_print("Actiunea se petrece in vremuri demult apuse, pe taramuri din basme\nPovestea incepe cu eroul nostru {}, un tanar dintr-un sat indepatat care se hotaraste sa plece din casa parintilor lui ca sa-si gaseasca menirea. El se hotaraste sa mearga la hanul din sat prima data ca sa se gandeasca unde sa plece si ce sa faca. Acolo apare o clarvazatoare batrana care ii spune ca ii va ghici destinul, iar tanarul {} accepta.".format(nume,nume))
print("Apasa enter pentru a continua si enter")
enter=input()
os.system('cls')
tip=random.randrange(1,5)
if(tip==1):
    delay_print("Batrana crede ca vei fi soldat bun!\n")
elif(tip==2):
    delay_print("Batrana crede ca ai anumite puteri magice si ca vei deveni vrajitor!\n")
elif(tip==3):
    delay_print("Batrana crede ca vei fi un savant bun!\n")
else:
    delay_print("Batrana crede ca vei fi un asasin bun!\n")
delay_print("Accepti soarta pe care ti-a dat-o batrana(Decizia implica ca {} va devenii clasa data de batrana)?\nIntrodu 1 pentru da sau 2 pentru nu\n".format(nume))
while(1):
    acceptare=input()
    if(acceptare=='1' or acceptare=='2'):
        break
    print("optiune incorecta")
erou=nume
os.system('cls')
while(1):
    if(acceptare=='1'):
        if(tip==1):
            erou=Soldat(100,random.randrange(75,91),random.randrange(70,101),random.randrange(80,96),random.randrange(0,21),random.randrange(0,51),20,False,False)
            print("{} este soldat!".format(nume))
            break
        elif(tip==2):
            erou=Vrajitor(100,random.randrange(65,76),random.randrange(70,101),random.randrange(80,96),random.randrange(0,51),random.randrange(70,91),20,False)
            print("{} este vrajitor!".format(nume))
            break
        elif(tip==3):
            erou=Savant(100,random.randrange(65,76),random.randrange(70,101),random.randrange(75,86),random.randrange(0,51),random.randrange(80,96),20,False)
            print("{} este savant!".format(nume))
            break
        else:
            erou=Asasin(100,random.randrange(80,96),random.randrange(70,101),random.randrange(65,81),random.randrange(75,86),random.randrange(65,81),20,False)
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
            erou=Soldat(100,random.randrange(75,91),random.randrange(70,101),random.randrange(80,96),random.randrange(0,21),random.randrange(0,51),20,False,False)
            print("Ai ales clasa soldat!")
            break
        elif(tip=='2'):
            erou=Vrajitor(100,random.randrange(65,76),random.randrange(50,101),random.randrange(80,96),random.randrange(0,51),random.randrange(70,91),20,False)
            print("Ai ales clasa vrajitor!")
            break
        elif(tip=='3'):
            erou=Savant(100,random.randrange(65,76),random.randrange(70,101),random.randrange(75,86),random.randrange(0,51),random.randrange(80,96),20,False)
            print("Ai ales clasa savant!")
            break
        else:
            erou=Asasin(100,random.randrange(80,96),random.randrange(70,101),random.randrange(65,81),random.randrange(75,86),random.randrange(65,81),20,False)
            print("Ai ales clasa asasin!")
            break
delay_print("{} are anumite statistici cum ar fi sanatatea, norocul, agilitatea , abilitatile magice, forta si inteligenta.".format(nume))
print("De asemena, eroul are si o valuta cu care isi poate achizitiona anumite obiecte care il pot ajuta pe drum.\n")
print("Statisticile actuale are eroului sunt {}\n".format(erou.statistici()))    
print("Batrana ii mai da tanarului {} o harta a unui taram indepartat numit Eldoria, unde se spune ca s-ar afla elixirul nemuririi\nAstfel, {} pleaca spre Eldoria si ajunge intr-o padure fermecata unde vede o ciuperca atragatoare, {} fiind infometat.".format(nume,nume,nume))
print("Vrei sa mananci ciuperca ? Introdu 1 pentru da sau 2 pentru nu")
while(1):
    alegere=input()
    if(alegere=='1' or alegere=='2'):
        break
    print("optiune incorecta")
os.system('cls')
if(alegere=='1'):
    if(erou.noroc<70):
        gameover()
        sys.exit()
    else:
        if(type(erou)==Soldat):
            delay_print("Ciuperca ti-a crescut agilitatea cu 10\n")
            erou.cresteagilitatea(10)
            print("noile statistici sunt : {}".format(erou.statistici()))
        elif(type(erou)==Vrajitor):
            delay_print("Ciuperca ti-a crescut agilitatea cu 10\n")
            erou.cresteagilitatea(10)
            print("noile statistici sunt : {}".format(erou.statistici()))
        elif(type(erou)==Savant):
            delay_print("Ciuperca ti-a crescut agilitatea cu 10\n")
            erou.cresteagilitatea(10)
            print("noile statistici sunt : {}".format(erou.statistici()))
        else:
            delay_print("Ciuperca ti-a crescut inteligenta cu 10\n")
            erou.cresteinteligenta(10)
            print("noile statistici sunt : {}".format(erou.statistici()))
print("In padure dai de un urs cu un diamant in frunte care vine insistent catre tine. Ce faci?\n1.Il ataci si dezlantui o lupta intensa\n2.Faci o vraja asupra lui sa devina prietenul tau si sa vorbeasca limba oamenilor\n3.Vorbesti pe limba lui si il convingi ca esti pasnic\n4.Te feresti de urs si te urci intr-un copac")
while(1):
    alegere=input()
    if(alegere=='1' or alegere=='2' or alegere=='3' or alegere=='4'):
        break
    print("optiune incorecta")
os.system('cls')
if(type(erou)==Soldat):
    if(alegere=='1'):
        delay_print("Ai ales optiunea cea mai buna si ai infrant ursul. De asemenea i-ai luat si diamantul din frunte\n")
        erou.diamand=True
    elif(alegere=='2'):
        print("Incercarile tale de face vraji nu au functionat\nTotosi te ai luptat cu ursul si ai reusit sa fugi de el dar viata ti a scazut drastic")
        erou.scadehp(100-erou.magie)
        if(erou.viata<=0):
            gameover()
        print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
    elif(alegere=='3'):
        print("Ai incercat sa vorbesti pe limba ursului, dar pentru ca nu o sti acesta te-a inteles gresit si te atacat.\nTotusi, ai reusit sa fugi de el dar viata ti-a scazut drastic")
        erou.scadehp(100-erou.inteligenta)
        if(erou.viata<=0):
            gameover()
        print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
    else:
        print("Ai incercat sa fugi de urs si sa te urci in copac, dar tu nefiind prea agil te-ai impiedicat si ursul te-a atacat.\nTotusi, ai reusit sa fugi de el dar viata ti-a scazut drastic")
        erou.scadehp(100-erou.agilitate)
        if(erou.viata<=0):
            gameover()
        print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
elif(type(erou)==Vrajitor):
    if(alegere=='1'):
        print("Ai incercat sa te lupti cu ursul, dar tu nefiind prea puternic ai fost ranit grav si a trebuit sa fugi")
        erou.scadehp(100-erou.forta)
        if(erou.viata<=0):
            gameover()
        print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
    elif(alegere=='2'):
        print("Ai vrajit ursul cu succes, iar acesta se imprieteneste cu tine si decide sa te ajute si iti spune o scurtatura catre Eldoria")
        erou.prieten=True    
    elif(alegere=='3'):
        print("Ai incercat sa vorbesti pe limba ursului, dar pentru ca nu o sti acesta te-a inteles gresit si te atacat.\nTotusi, ai reusit sa fugi de el dar viata ti-a scazut drastic")
        erou.scadehp(100-erou.inteligenta)
        if(erou.viata<=0):
            gameover()
        print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
    else:
        print("Ai incercat sa fugi de urs si sa te urci in copac, dar tu nefiind prea agil te-ai impiedicat si ursul te-a atacat.\nTotusi, ai reusit sa fugi de el dar viata ti-a scazut drastic")
        erou.scadehp(100-erou.agilitate)
        if(erou.viata<=0):
            gameover()
        print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
elif(type(erou)==Savant):
    if(alegere=='1'):
        print("Ai incercat sa te lupti cu ursul, dar tu nefiind prea puternic ai fost ranit grav si a trebuit sa fugi")
        erou.scadehp(100-erou.forta)
        if(erou.viata<=0):
            gameover()
        print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
    elif(alegere=='2'):
        print("Incercarile tale de face vraji nu au functionat\nTotosi te ai luptat cu ursul si ai reusit sa fugi de el dar viata ti a scazut drastic")
        erou.scadehp(100-erou.magie)
        if(erou.viata<=0):
            gameover()
        print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
    elif(alegere=='3'):
        print("Tu fiind o persoana inteligenta, ai reusit sa vorbesti cu ursul si te-ai imprietenit cu el.\nAcesta a promis ca iti va arata o scurtatura catre Eldoria\n")
        erou.prieten=True
    else:
        erou.scadehp(100-erou.agilitate)
        print("Ai incercat sa fugi de urs si sa te urci in copac, dar tu nefiind prea agil te-ai impiedicat si ursul te-a atacat.\nTotusi, ai reusit sa fugi de el dar viata ti-a scazut drastic")
        if(erou.viata<=0):
            gameover()
        print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
else:
    if(alegere=='1'):
        print("Ai incercat sa te lupti cu ursul, dar tu nefiind prea puternic ai fost ranit grav si a trebuit sa fugi")
        erou.scadehp(100-erou.forta)
        if(erou.viata<=0):
            gameover()
        print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
    elif(alegere=='2'):
        print("Incercarile tale de face vraji nu au functionat\nTotosi te ai luptat cu ursul si ai reusit sa fugi de el dar viata ti a scazut drastic")
        erou.scadehp(100-erou.magie)
        if(erou.viata<=0):
            gameover()
        print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
    elif(alegere=='3'):
        print("Ai incercat sa vorbesti pe limba ursului, dar pentru ca nu o sti acesta te-a inteles gresit si te atacat.\nTotusi, ai reusit sa fugi de el dar viata ti-a scazut drastic")
        erou.scadehp(100-erou.inteligenta)
        if(erou.viata<=0):
            gameover()
        print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
    else:
        print("Fiind destul de agil, ai reusit sa fugi de urs si sa te urci intr-un copac inalt.\nDe acolo de sus vezi o scurtatura catre Eldoria")
        erou.scurtatura=True
delay_print("Iti continui drumul spre Eldoria si te intalnesti cu un negustor pe nume Brock\n")
print("De la acesta poti cumpara diverse lucruri, cum ar fi o licoare care sa-ti mareasca viata cu 20 de unitati, te poate ajuta in caz ca esti ranit, sau o amuleta pentru noroc")
print("Amuleta sau licoara costa fiecare 10 banuti\nDoresti sa achizitionezi una dintre ele?\nIntrodu 1 pt amuleta, 2 pentru licoare sau 3 daca nu doresti nimic")
while(1):
    alegere=input()
    if(alegere=='1' or alegere=='2' or alegere=='3'):
        break
    print("optiune incorecta")
if(type(erou)==Soldat and erou.diamand==True):
    delay_print("Sti ceva, Brock iti propune sa-i dai diamantul pe care vede ca il ai in ghiozdan, iar el iti va dezvalui o scurtatura catre Eldoria\n")
    print("Accepti asta: introdu 1 pentru da sau 2 pentru nu")
    while(1):
        alegere=input()
        if(alegere=='1' or alegere=='2'):
            break
        print("optiune incorecta")
    if(alegere=='1'):
        print("Ai ales sa ii dai diamantul lui Brock si astfel acesta ti-a spus o scurtatura si te-a ferit de un monstru ce era in drum")
        erou.scurtatura=True
    else:
        print("Treaba ta.")
else:
    if(alegere=='1'):
        erou.scadenumerar(10)
        erou.crestehp(10)
        delay_print("Ai ales sa achizitionezi amuleta si norocul ti-a crescut cu 10 procente\nNoile tale statistici sunt {}\n".format(erou.statistici()))
    elif(alegere=='2'):
        erou.scadenumerar(10)
        erou.crestenoroc(10)
        delay_print("Ai ales sa achizitionezi licoarea si astfel ti-a crescut viata cu 10 procente\nNoile tale statistici sunt {}\n".format(erou.statistici()))
    else:
        delay_print("Nu ai ales nimic si iti continui drumul, statisticile tale raman aceleasi {}\n".format(erou.statistici()))
if(erou.scurtatura==False or erou.prieten==False):
    delay_print("Nu ai gasit scurtatura catre Eldoria, asa ca te-ai intalnit pe drum")



