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

class Gigant:
    def __init__(self,viata,agilitate,magie,forta,inteligenta):
        self.viata=viata
        self.agilitate=agilitate
        self.forta=forta
        self.inteligenta=inteligenta
        self.magie=magie
    def scadehp(self,nr):
        self.viata-=nr

class Elf:
    def __init__(self,viata,agilitate,magie,forta,inteligenta):
        self.viata=viata
        self.agilitate=agilitate
        self.forta=forta
        self.inteligenta=inteligenta
        self.magie=magie
    def scadehp(self,nr):
        self.viata-=nr

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
    def __init__(self, viata, agilitate, noroc, magie, forta, inteligenta,numerar,diamand,scurtatura,avantaj):
        super().__init__(viata, agilitate, noroc, forta, magie, inteligenta,numerar)
        self.diamand=diamand
        self.scurtatura=scurtatura
        self.avantaj=avantaj

class Vrajitor(Erou):
    def __init__(self, viata, agilitate, noroc, magie, forta, inteligenta, numerar,prieten,avantaj):
        super().__init__(viata, agilitate, noroc, magie, forta, inteligenta, numerar)
        self.prieten=prieten
        self.avantaj=avantaj

class Savant(Erou):
    def __init__(self, viata, agilitate, noroc, magie, forta, inteligenta, numerar,prieten,avantaj):
        super().__init__(viata, agilitate, noroc, magie, forta, inteligenta, numerar)
        self.prieten=prieten
        self.avantaj=avantaj
    
class Asasin(Erou):
    def __init__(self, viata, agilitate, noroc, magie, forta, inteligenta, numerar,scurtatura,avantaj):
        super().__init__(viata, agilitate, noroc, magie, forta, inteligenta, numerar)
        self.scurtatura=scurtatura
        self.avantaj=avantaj

delay_print("Bine ai venit! Introdu numele pe care vrei sa il aiba eroul\n")
nume=input()
os.system('cls')
delay_print("Actiunea se petrece in vremuri demult apuse, pe taramuri din basme\nPovestea incepe cu eroul nostru {}, un tanar dintr-un sat indepatat care se hotaraste sa plece din casa parintilor lui ca sa-si gaseasca menirea. El se hotaraste sa mearga la hanul din sat prima data ca sa se gandeasca unde sa plece si ce sa faca. Acolo apare o clarvazatoare batrana care ii spune ca ii va ghici destinul, iar tanarul {} accepta.".format(nume,nume))
print("Apasa enter pentru a continua")
enter=input()
os.system('cls')
tip=random.randrange(1,5)
match(tip):
    case 1:
        delay_print("Batrana crede ca vei fi soldat bun!\n")
    case 2:
        delay_print("Batrana crede ca ai anumite puteri magice si ca vei deveni vrajitor!\n")
    case 3:
        delay_print("Batrana crede ca vei fi un savant bun!\n")
    case 4:
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
    match(acceptare):
        case '1':
            match(tip):
                case 1:
                    erou=Soldat(100,random.randrange(75,91),random.randrange(70,101),random.randrange(80,96),random.randrange(0,21),random.randrange(0,51),20,False,False,False)
                    print("{} este soldat!".format(nume))
                    break
                case 2:
                    erou=Vrajitor(100,random.randrange(65,76),random.randrange(70,101),random.randrange(80,96),random.randrange(0,51),random.randrange(70,91),20,False,False)
                    print("{} este vrajitor!".format(nume))
                    break
                case 3:
                    erou=Savant(100,random.randrange(65,76),random.randrange(70,101),random.randrange(75,86),random.randrange(0,51),random.randrange(80,96),20,False,False)
                    print("{} este savant!".format(nume))
                    break
                case 4:
                    erou=Asasin(100,random.randrange(80,96),random.randrange(70,101),random.randrange(65,81),random.randrange(75,86),random.randrange(65,81),20,False,False)
                    print("{} este asasin!".format(nume))
                    break
        case '2':
            while(1):
                print("Introdu clasa pe care vrei sa o aiba eroul 1 pentru soldat, 2 pentru vrajitor, 3 pentru savant si 4 pentru asasin\nSoldatul are ca atribut principal fort, vrajitorul magia, savantul inteligenta si asasinul agilitatea")
                tip=input()
                if(tip=='1' or tip=='2' or tip=='3' or tip=='4'):
                    break
                else:
                    print("optiune incorecta")
            match(tip):
                case '1':
                    erou=Soldat(100,random.randrange(75,91),random.randrange(50,101),random.randrange(80,96),random.randrange(0,21),random.randrange(0,51),20,False,False,False)
                    print("Ai ales clasa soldat!")
                    break
                case '2':
                    erou=Vrajitor(100,random.randrange(65,76),random.randrange(50,101),random.randrange(80,96),random.randrange(0,51),random.randrange(70,91),20,False,False)
                    print("Ai ales clasa vrajitor!")
                    break
                case '3':
                    erou=Savant(100,random.randrange(65,76),random.randrange(50,101),random.randrange(75,86),random.randrange(0,51),random.randrange(80,96),20,False,False)
                    print("Ai ales clasa savant!")
                    break
                case '4':
                    erou=Asasin(100,random.randrange(80,96),random.randrange(50,101),random.randrange(65,81),random.randrange(75,86),random.randrange(65,81),20,False,False)
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
        delay_print("Ai facut toxinfectie alimentara si te ai intors acasa\nGAME OVER\n")
        sys.exit()
    else:
        if(type(erou)==Soldat):
            delay_print("Ciuperca ti-a crescut agilitatea cu 10\n")
            erou.cresteagilitatea(10)
            if(erou.agilitate>100):
                erou.agilitate=100
            print("noile statistici sunt : {}".format(erou.statistici()))
        elif(type(erou)==Vrajitor):
            delay_print("Ciuperca ti-a crescut agilitatea cu 10\n")
            erou.cresteagilitatea(10)
            if(erou.agilitate>100):
                erou.agilitate=100
            print("noile statistici sunt : {}".format(erou.statistici()))
        elif(type(erou)==Savant):
            delay_print("Ciuperca ti-a crescut agilitatea cu 10\n")
            erou.cresteagilitatea(10)
            if(erou.agilitate>100):
                erou.agilitate
            print("noile statistici sunt : {}".format(erou.statistici()))
        else:
            delay_print("Ciuperca ti-a crescut inteligenta cu 10\n")
            erou.cresteinteligenta(10)
            if(erou.inteligenta>100):
                erou.inteligenta=100
            print("noile statistici sunt : {}".format(erou.statistici()))
print("In padure dai de un urs cu un diamant in frunte care vine insistent catre tine. Ce faci?\n1.Il ataci si dezlantui o lupta intensa\n2.Faci o vraja asupra lui sa devina prietenul tau si sa vorbeasca limba oamenilor\n3.Vorbesti pe limba lui si il convingi ca esti pasnic\n4.Te feresti de urs si te urci intr-un copac")
while(1):
    alegere=input()
    if(alegere=='1' or alegere=='2' or alegere=='3' or alegere=='4'):
        break
    print("optiune incorecta")
os.system('cls')
if(type(erou)==Soldat):
    match(alegere):
        case '1':
            delay_print("Ai ales optiunea cea mai buna si ai infrant ursul. De asemenea i-ai luat si diamantul din frunte\n")
            erou.diamand=True
        case '2':
            print("Incercarile tale de face vraji nu au functionat\nTotosi te ai luptat cu ursul si ai reusit sa fugi de el dar viata ti a scazut drastic")
            erou.scadehp(100-erou.magie)
            if(erou.viata<=0):
                gameover()
            print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
        case '3':
            print("Ai incercat sa vorbesti pe limba ursului, dar pentru ca nu o sti acesta te-a inteles gresit si te atacat.\nTotusi, ai reusit sa fugi de el dar viata ti-a scazut drastic")
            erou.scadehp(100-erou.inteligenta)
            if(erou.viata<=0):
                gameover()
            print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
        case '4':
            print("Ai incercat sa fugi de urs si sa te urci in copac, dar tu nefiind prea agil te-ai impiedicat si ursul te-a atacat.\nTotusi, ai reusit sa fugi de el dar viata ti-a scazut drastic")
            erou.scadehp(100-erou.agilitate)
            if(erou.viata<=0):
                gameover()
            print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
elif(type(erou)==Vrajitor):
    match(alegere):
        case '1':
            print("Ai incercat sa te lupti cu ursul, dar tu nefiind prea puternic ai fost ranit grav si a trebuit sa fugi")
            erou.scadehp(100-erou.forta)
            if(erou.viata<=0):
                gameover()
            print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
        case '2':
            print("Ai vrajit ursul cu succes, iar acesta se imprieteneste cu tine si decide sa te ajute si iti spune o scurtatura catre Eldoria")
            erou.prieten=True    
        case '3':
            print("Ai incercat sa vorbesti pe limba ursului, dar pentru ca nu o sti acesta te-a inteles gresit si te atacat.\nTotusi, ai reusit sa fugi de el dar viata ti-a scazut drastic")
            erou.scadehp(100-erou.inteligenta)
            if(erou.viata<=0):
                gameover()
            print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
        case '4':
            print("Ai incercat sa fugi de urs si sa te urci in copac, dar tu nefiind prea agil te-ai impiedicat si ursul te-a atacat.\nTotusi, ai reusit sa fugi de el dar viata ti-a scazut drastic")
            erou.scadehp(100-erou.agilitate)
            if(erou.viata<=0):
                gameover()
            print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
elif(type(erou)==Savant):
    match(alegere):
        case '1':
            print("Ai incercat sa te lupti cu ursul, dar tu nefiind prea puternic ai fost ranit grav si a trebuit sa fugi")
            erou.scadehp(100-erou.forta)
            if(erou.viata<=0):
                gameover()
            print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
        case '2':
            print("Incercarile tale de face vraji nu au functionat\nTotosi te ai luptat cu ursul si ai reusit sa fugi de el dar viata ti a scazut drastic")
            erou.scadehp(100-erou.magie)
            if(erou.viata<=0):
                gameover()
            print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
        case '3':
            print("Tu fiind o persoana inteligenta, ai reusit sa vorbesti cu ursul si te-ai imprietenit cu el.\nAcesta a promis ca iti va arata o scurtatura catre Eldoria\n")
            erou.prieten=True
        case '4':
            erou.scadehp(100-erou.agilitate)
            print("Ai incercat sa fugi de urs si sa te urci in copac, dar tu nefiind prea agil te-ai impiedicat si ursul te-a atacat.\nTotusi, ai reusit sa fugi de el dar viata ti-a scazut drastic")
            if(erou.viata<=0):
                gameover()
            print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
else:
    match(alegere):
        case '1':
            print("Ai incercat sa te lupti cu ursul, dar tu nefiind prea puternic ai fost ranit grav si a trebuit sa fugi")
            erou.scadehp(100-erou.forta)
            if(erou.viata<=0):
                gameover()
            print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
        case '2':
            print("Incercarile tale de face vraji nu au functionat\nTotosi te ai luptat cu ursul si ai reusit sa fugi de el dar viata ti a scazut drastic")
            erou.scadehp(100-erou.magie)
            if(erou.viata<=0):
                gameover()
            print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
        case '3':
            print("Ai incercat sa vorbesti pe limba ursului, dar pentru ca nu o sti acesta te-a inteles gresit si te atacat.\nTotusi, ai reusit sa fugi de el dar viata ti-a scazut drastic")
            erou.scadehp(100-erou.inteligenta)
            if(erou.viata<=0):
                gameover()
            print("Noile tale statistici sunt: {}\n".format(erou.statistici()))
        case '4':
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
        delay_print("Ai ales sa ii dai diamantul lui Brock si astfel acesta ti-a spus o scurtatura care Eldoria\n")
        erou.scurtatura=True
    else:
        delay_print("Treaba ta.\n")
else:
    match(alegere):
        case '1':
            erou.scadenumerar(10)
            erou.crestenoroc(10)
            if(erou.noroc>100):
                erou.noroc=100
            delay_print("Ai ales sa achizitionezi amuleta si norocul ti-a crescut cu 10 procente\nNoile tale statistici sunt {}\n".format(erou.statistici()))
        case '2':
            erou.scadenumerar(10)
            erou.crestehp(10)
            if(erou.viata>100):
                erou.viata=100
            delay_print("Ai ales sa achizitionezi licoarea si astfel ti-a crescut viata cu 10 procente\nNoile tale statistici sunt {}\n".format(erou.statistici()))
        case '3':
            delay_print("Nu ai ales nimic si iti continui drumul, statisticile tale raman aceleasi {}\n".format(erou.statistici()))
print("Introdu enter pentru a continua")
alegere=input()
os.system('cls')
elf=Elf(200,100-erou.agilitate,100-erou.magie,100-erou.forta,100-erou.inteligenta)
if(type(erou)==Savant or type(erou)==Vrajitor):
    if(erou.prieten==False):
        delay_print("In continuare te intalnesti cu un elf ca cel din stapanul inelelor\n")
        while(1):
            delay_print("Acesta te ataca si iti provoaca daune\nTrebuia sa contraataci, ce abilitati iti vei folosi?\n1.Atac frontal folosindu-ti propria forta\n2.Magie negra asupra elfului\n3.Inteligenta(iti folosesti un dispozitiv ce il ai la indemana\n4.Te folosesti de agilitatea ta si te feresti de atacurile elfului si incerci sa-l iei prin surprindere\n")
            delay_print("Viata elfului este : {}\nStatisticile tale sunt {}\n".format(elf.viata,erou.statistici()))
            while(1):
                alegere=input()
                if(alegere=='1' or alegere=='2' or alegere=='3' or alegere=='4'):
                    break                
                print("optiune incorecta")
            os.system('cls')
            match(alegere):
                case '1':
                    delay_print("I-ai scazut viata elfului cu {} procente, dar si el ti-a scazut viata cu {} procente\n".format(erou.forta,elf.forta))
                    erou.scadehp(elf.forta)
                    elf.scadehp(erou.forta)
                    if(erou.viata<=0):
                        gameover()
                    if(elf.viata<=0):
                        print("Ai infrant elful cu succes")
                        break
                case '2':
                    delay_print("I-ai scazut viata elfului cu {} procente, dar si el ti-a scazut viata cu {} procente\n".format(erou.magie,elf.magie))
                    erou.scadehp(elf.magie)
                    elf.scadehp(erou.magie)
                    if(erou.viata<=0):
                        gameover()
                    if(elf.viata<=0):
                        print("Ai infrant elful cu succes")
                        break 
                case '3':
                    delay_print("I-ai scazut viata elfului cu {} procente, dar si el ti-a scazut viata cu {} procente\n".format(erou.inteligenta,elf.inteligenta))
                    erou.scadehp(elf.inteligenta)
                    elf.scadehp(erou.inteligenta)
                    if(erou.viata<=0):
                        gameover()
                    if(elf.viata<=0):
                        print("Ai infrant elful cu succes")
                        break
                case '4':
                    delay_print("I-ai scazut viata elfului cu {} procente, dar si el ti-a scazut viata cu {} procente\n".format(erou.agilitate,elf.agilitate))
                    erou.scadehp(elf.agilitate)
                    elf.scadehp(erou.agilitate)
                    if(erou.viata<=0):
                        gameover()
                    if(elf.viata<=0):
                        print("Ai infrant elful cu succes")
                        break
    delay_print("Apasa enter pentru a continua\n")
    alegere=input()
    os.system('cls')
else:
    if(erou.scurtatura==False):
        delay_print("In continuare te intalnesti cu un elf ca cel din stapanul inelelor\n")
        while(1):
            delay_print("Acesta te ataca si iti provoaca daune\nTrebuia sa contraataci, ce abilitati iti vei folosi?\n1.Atac frontal folosindu-ti propria forta\n2.Magie negra asupra elfului\n3.Inteligenta(iti folosesti un dispozitiv ce il ai la indemana\n4.Te folosesti de agilitatea ta si te feresti de atacurile elfului si incerci sa-l iei prin surprindere\n")
            delay_print("Viata elfului este : {}\nStatisticile tale sunt {}\n".format(elf.viata,erou.statistici()))
            while(1):
                alegere=input()
                if(alegere=='1' or alegere=='2' or alegere=='3' or alegere=='4'):
                    break                
                print("optiune incorecta")
            os.system('cls')
            match(alegere):
                case '1':
                    delay_print("I-ai scazut viata elfului cu {} procente, dar si el ti-a scazut viata cu {} procente\n".format(erou.forta,elf.forta))
                    erou.scadehp(elf.forta)
                    elf.scadehp(erou.forta)
                    if(erou.viata<=0):
                        gameover()
                    if(elf.viata<=0):
                        print("Ai infrant elful cu succes")
                        break
                case '2':
                    delay_print("I-ai scazut viata elfului cu {} procente, dar si el ti-a scazut viata cu {} procente\n".format(erou.magie,elf.magie))
                    erou.scadehp(elf.magie)
                    elf.scadehp(erou.magie)
                    if(erou.viata<=0):
                        gameover()
                    if(elf.viata<=0):
                        print("Ai infrant elful cu succes")
                        break 
                case '3':
                    delay_print("I-ai scazut viata elfului cu {} procente, dar si el ti-a scazut viata cu {} procente\n".format(erou.inteligenta,elf.inteligenta))
                    erou.scadehp(elf.inteligenta)
                    elf.scadehp(erou.inteligenta)
                    if(erou.viata<=0):
                        gameover()
                    if(elf.viata<=0):
                        print("Ai infrant elful cu succes")
                        break
                case '4':
                    delay_print("I-ai scazut viata elfului cu {} procente, dar si el ti-a scazut viata cu {} procente\n".format(erou.agilitate,elf.agilitate))
                    erou.scadehp(elf.agilitate)
                    elf.scadehp(erou.agilitate)
                    if(erou.viata<=0):
                        gameover()
                    if(elf.viata<=0):
                        print("Ai infrant elful cu succes")
                        break
    delay_print("Apasa enter pentru a continua\n")
    alegere=input()
    os.system('cls')
if(type(erou)==Savant or type(erou)==Vrajitor):
    if(erou.prieten==False):
        delay_print("Dupa ce ai infrant elful, iti continui drumul spre Eldoria ")
    else:
        delay_print("Iti continui drumul spre Eldoria ")
else:
    if(erou.scurtatura==False):
        delay_print("Dupa ce ai infrant elful, iti continui drumul spre Eldoria ")
    else:
        delay_print("Iti continui drumul spre Eldoria ")
delay_print("si te intalnesti cu o vrajitoare care te intreaba ce cauti pe aceste taramuri\nCe ii vei raspunde?\n1.Doar in trecere\n2.Caut sa ajung in Eldoria si sa gasesc elixirul tineretii\n")
while(1):
    alegere=input()
    if(alegere=='1' or alegere=='2'):
        break
    print("optiune incorecta")
os.system('cls')
match(alegere):
    case '1':
        delay_print("Vrajitoarea spune: Treaba ta\nDupa isi vede de drum\n")
    case '2':
        if(erou.noroc>=85):
            delay_print("Vrajitoarea spune: Multi au incercat, dar niciunul nu a reusit pana acum\nMa mir ca ai ajuns si pana aici\nLa portile templului din Eldoria unde se ascunde elixirul nemurii se afla un gigant de piatra daca pazeste acel elixir\nDupa ce infrangi acel gigant mai urmeaza si alte teste pana sa ajungi la elixir\nUite ia de aici aceasta amuleta iar cand o sa ai nevoie de mine eu voi sti unde te afli si voi veni sa te ajut\nMult noroc\n")
            erou.avantaj=True
        else:
            delay_print("Vrajitoarea spune: Nu stiu de nicio Eldoria\nDupa isi vede de drum\n")
print("Apasa enter pentru a continua")
alegere=input()
os.system('cls')
match(erou.avantaj):
    case True:
        delay_print("{} ajunge la portile templului din Eldoria si se intalneste cu gigantul de piatra\nAcesta constata ca pentru a deschide poarta are nevoie de inima gigantului\nAtunci apare vrajitoarea ce ai cunoscut-o mai devreme si iti spune ca te va ajuta ea sa treci de aceste porti\nAceasta te duce pe un teren subteran si intr un final ajungi intr-o camera din acel templu.\n".format(nume))
    case False:
        delay_print("{} ajunge in Eldoria si se ghideaza dupa propria harta si ajunge la un templu pazit de un gigant de piatra\nAcesta constata ca pentru a deschide poarta are nevoie de inima gigantului si isi da seama ca singura metoda de a obine este sa se lupte cu gigantul si sa o ia de la el\n".format(nume))
        gigant=Gigant(200,100-erou.agilitate,100-erou.magie,100-erou.forta,100-erou.inteligenta)
        while(1):
            delay_print("Acesta te ataca si iti provoaca daune\nTrebuia sa contraataci, ce abilitati iti vei folosi?\n1.Atac frontal\n2.Magie negra\n3.Inteligenta(iti folosesti un dispozitiv ce il ai la indemana\n4.Atac prin invaluire(Agilitate)\n")
            delay_print("Viata gigantului este : {}\nStatisticile tale sunt {}\n".format(gigant.viata,erou.statistici()))
            while(1):
                alegere=input()
                if(alegere=='1' or alegere=='2' or alegere=='3' or alegere=='4'):
                    break                
                print("optiune incorecta")
            os.system('cls')
            match(alegere):
                case '1':
                    delay_print("I-ai scazut viata gigantului cu {} procente, dar si el ti-a scazut viata cu {} procente\n".format(erou.forta,gigant.forta))
                    erou.scadehp(gigant.forta)
                    gigant.scadehp(erou.forta)
                    if(erou.viata<=0):
                        gameover()
                    if(gigant.viata<=0):
                        print("Ai infrant gigantul cu succes")
                        break
                case '2':
                    delay_print("I-ai scazut viata gigantului cu {} procente, dar si el ti-a scazut viata cu {} procente\n".format(erou.magie,gigant.magie))
                    erou.scadehp(gigant.magie)
                    gigant.scadehp(erou.magie)
                    if(erou.viata<=0):
                        gameover()
                    if(gigant.viata<=0):
                        print("Ai infrant gigantul cu succes")
                        break 
                case '3':
                    delay_print("I-ai scazut viata gigantului cu {} procente, dar si el ti-a scazut viata cu {} procente\n".format(erou.inteligenta,gigant.inteligenta))
                    erou.scadehp(gigant.inteligenta)
                    gigant.scadehp(erou.inteligenta)
                    if(erou.viata<=0):
                        gameover()
                    if(gigant.viata<=0):
                        print("Ai infrant gigantul cu succes")
                        break
                case '4':
                    delay_print("I-ai scazut viata gigantului cu {} procente, dar si el ti-a scazut viata cu {} procente\n".format(erou.agilitate,gigant.agilitate))
                    erou.scadehp(gigant.agilitate)
                    gigant.scadehp(erou.agilitate)
                    if(erou.viata<=0):
                        gameover()
                    if(gigant.viata<=0):
                        print("Ai infrant gigantul cu succes")
                        break
print("Apasa enter pentru a continua")
alegere=input()
os.system('cls')
if(erou.viata<100):
    delay_print("Viata ti-a revenit la 100 de procente\n")
delay_print("Ajungi intr-o camera plina de hieroglife si te aproprii de un stativ pe care se afla o scrisoare. Scrisoarea spune asa:\nCel care decide sa-si incerce norocul si treaca de aceasta usa va trebui sa rezolve cateva ghicitori intr-un timp limitat\n")
print("Apasa enter pentru a continua")
alegere=input()
os.system('cls')
delay_print("Ajuns in eroul este prins in anumite nisipuri miscatoare care il trag tot mai jos. Se pare ca va trebui sa raspunda rapid la intrebari\n")
while(1):
    delay_print("Prima intrebare este: Unele luni ale anului au 31 de zile, altele au numai 30. Câte luni au 28 de zile?\n1.6\n2.12\n3.una\n4.10\n")
    while(1):
        alegere=input()
        if(alegere=='1' or alegere=='2' or alegere=='3' or alegere=='4'):
            break
        print("optiune incorecta")
    os.system('cls')
    if(alegere=='1' or alegere=='3' or alegere=='4'):
        erou.scadehp(25)
        if(erou.viata<=0):
            gameover()
        delay_print("Ai raspuns gresit la intrebare si viata ti-a scazut cu 10 procente. Noua ta viata este : {}\n".format(erou.viata))
    else:
        delay_print("Raspuns corect\n")
        break
while(1):
    delay_print("A 2-a intrebare este: Tatăl Adrianei are cinci fete: Ana, Alina, Anemona și Ariana. Cum o cheamă pe a cincea?\n1.Ana\n2.Alina\n3.Anemona\n4.Adriana\n")
    while(1):
        alegere=input()
        if(alegere=='1' or alegere=='2' or alegere=='3' or alegere=='4'):
            break
        print("optiune incorecta")
    os.system('cls')
    if(alegere=='1' or alegere=='3' or alegere=='2'):
        erou.scadehp(25)
        if(erou.viata<=0):
            gameover()
        delay_print("Ai raspuns gresit la intrebare si viata ti-a scazut cu 10 procente. Noua ta viata este : {}\n".format(erou.viata))
    else:
        delay_print("Raspuns corect\n")
        break
while(1):
    delay_print("A 3-a intrebare este: Doctorul îţi prescrie să iei trei pastile în fiecare seară, câte una la fiecare jumătate de oră. În câte minute ai terminat sa iei pastilele?\n1.30\n2.90\n3.60\n4.120\n")
    while(1):
        alegere=input()
        if(alegere=='1' or alegere=='2' or alegere=='3' or alegere=='4'):
            break
        print("optiune incorecta")
    os.system('cls')
    if(alegere=='1' or alegere=='2' or alegere=='4'):
        erou.scadehp(25)
        if(erou.viata<=0):
            gameover()
        delay_print("Ai raspuns gresit la intrebare si viata ti-a scazut cu 10 procente. Noua ta viata este : {}\n".format(erou.viata))
    else:
        delay_print("Raspuns corect\n")
        break
delay_print("Esti eliberat si vezi cum din pamant apare un stativ pe care se afla faimosul elixir al tineretii\n")
print("Jocul a ajuns la sfarsit! Joc realizat de Rares Catana, student in anul 1 la facultatea de Automatica si Calculatoare UPT, specializarea CTI-RO")
