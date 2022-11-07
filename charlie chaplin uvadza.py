#vlozenie modulu
import tkinter

#otvorenie potrebneho suboru
subor = open("kompresia_obrazka_2.txt","r")
 
#precitanie prveho riadku a zistenie rozmerov
prvy_riadok = subor.readline()
riadocek = prvy_riadok.split()
sirka = int(riadocek[0])
vyska = int(riadocek[1])

#nastavenie platna a jeho rozmerov
canvas = tkinter.Canvas(width=sirka, height=vyska) 
canvas.pack()

#premenne
x = 0
y = 0
kolky_riadok = 0
predosly = 0

#precitanie riadkov a ulozenie
riadky = subor.readlines()

def ciernobiely_svet(): #funkcia na vykreslenie povodneho obrazku z udajov v subore
    #globalne premenne
    global x,y
    global kolky_riadok, predosly

    #vykreslenie momentalneho riadku ak nepresiahol vysku
    if kolky_riadok < vyska:
        for pismeno in riadky[kolky_riadok]:
            if pismeno == '0':
                canvas.create_rectangle(x,y,x+1,y+1,fill='black',outline='')
            else:
                canvas.create_rectangle(x,y,x+1,y+1,fill='white',outline='')

            #zmena suradnice x    
            x += 1

        #zmeny suradnic x a y    
        x = 0    
        y += 1

        #zmena riadku
        kolky_riadok += 1

        #pokracovanie vo funkcii
        canvas.after(1,ciernobiely_svet)

    #zresetovanie hodnot ak riadok presiahol vysku
    else:
        x = 0
        y = 0
        kolky_riadok = 0
        predosly = 0

        #ukoncenie funkcie
        return None  

def bielocierny_svet(): #funkcia na vykreslenie negativu obrazka
    #globalne premenne
    global x,y
    global kolky_riadok, predosly

    #vykreslenie momentalneho riadku ak nepresiahol vysku
    if kolky_riadok < vyska:
        for pismeno in riadky[kolky_riadok]:
            if pismeno == '0':
                canvas.create_rectangle(x,y,x+1,y+1,fill='white',outline='')
            else:
                canvas.create_rectangle(x,y,x+1,y+1,fill='black',outline='')

            #zmena suradnice x    
            x += 1

        #zmeny suradnic x a y    
        x = 0    
        y += 1

        #zmena riadku
        kolky_riadok += 1

        #pokracovanie vo funkcii
        canvas.after(1,bielocierny_svet)

    #zresetovanie hodnot ak riadok presiahol vysku
    else:
        x = 0
        y = 0
        kolky_riadok = 0
        predosly = 1

        #ukoncenie funkcie
        return None

def vypocet(): #funkcia na zistenie ktory obrazok treba "znegativizovat"
    #globalna premenna
    global predosly

    #zistenie predosleho obrazku podla vopred zadanych hodnot
    if predosly == 1:
        ciernobiely_svet()
    else:
        bielocierny_svet()

#privolanie funkcie
ciernobiely_svet()

#vytvorenie tlacidla
carovne_tlacitko = tkinter.Button(text='Negatív',command=vypocet)
carovne_tlacitko.pack()

#zatvorenie suboru
subor.close()

