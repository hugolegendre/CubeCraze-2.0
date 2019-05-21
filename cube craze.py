from tkinter import*
import time
from random import*

def replay():                           #Fonction replay qui relance le jeu avec un tableau de 2 lignes et 4 colonnes
    global tableau,zero,tableau1,d,e
    ligne1=len(tableau1)
    ligne=len(tableau)
    for j in range(ligne):
        for i in range(4):
            tableau[j][i]=0
    for j in range (3):
        for i in range(4):
            tableau[j][i]=1
        zero=randint(0,3)
        tableau[j][zero]=0

    for j in range(ligne1):
        for i in range(4):
            tableau1[j][i]=0
    for j in range (3):
        for i in range(4):
            tableau1[j][i]=1
        zero=randint(0,3)
        tableau1[j][zero]=0
    d=5
    e=0
    creer()
    temps()


def touche(evt):                        #Fonction touche qui permet d'effectuer des actions lorsqu'on appuie sur une certaine touche du clavier
    global tableau, tableau1,col,col1,lgn,lgn1
    keytableau=[65,90,69,82]            #keycode des touches de clavier qui sont respectivement: A,Z,E,R


    for i in range(4):
        if evt.keycode==keytableau[i]:      #Si la touche appuyée correspond aux touches A,Z,E ou R alors la fonction commance
            col=i                           #La touche du clavier correspond à la colonne 0,1,2,3
            n=9                             #On initialise la nième ligne à la dernière ligne du jeu
            while tableau[n][col]==0 and n>=0:   #Tant qu'il y n'y a pas de carrés noirs sr la nième ligne

                n=n-1                           #On vérifie maintenant la ligne du dessus
                if tableau[n][col]==1:     #Si cette ligne a déja un carré
                    tableau[n+1][col]=1             #Alors un carré est mis sur la ligne en dessous

                sommetableau=tableau[n+1][0]+tableau[n+1][1]+tableau[n+1][2]+tableau[n+1][3] #Somme des termes de la ligne du dessous
                if n==0 and tableau[n][col]==0:     #Si c'est la première ligne et qu'il n'y a pas de carrés noirs alors il faut en ajouter 1
                    tableau[n][col]=1
                    tableau.pop(n)


                if sommetableau==4:                 #S'il n'y a que carrés noir sur la ligne du dessous
                    tableau.pop(n+1)
                    tableau.append([0,0,0,0])        #Elle est supprimée et remplacée par des carrés blancs
                    lgn+=1
                    if lgn==4:
                        tableau1.insert(0,[1,1,1,1])
                        zero=randint(0,3)
                        tableau1[0][zero]=0
                        lgn=0
                                                         #Dans le mode multijoueur l'autre joueur se voit rajouter une ligne



            creer()

    keytableau1=[97,98,99,13]                       #keycode des touches du pavé numérique qui sont respectivement: 1,2,3,ENTREE
                                                    #Mode multijoueur donc répétition du même algorithme sur un autre tableau
    for i in range(4):
        if evt.keycode==keytableau1[i]:
            col1=i
            n1=9
            while tableau1[n1][col1]==0 and n1>=0:

                n1=n1-1
                if tableau1[n1][col1]==1:
                    tableau1[n1+1][col1]=1
                sommetableau1=tableau1[n1+1][0]+tableau1[n1+1][1]+tableau1[n1+1][2]+tableau1[n1+1][3]
                if tableau1[n1][col1]==1 and n1==0:
                    tableau1[n1+1][col1]=1
                    tableau.pop(n1)


                if sommetableau1==4:
                    tableau1.pop(n1+1)
                    tableau1.append([0,0,0,0])
                    lgn1+=1
                    if lgn1==4:
                        tableau.insert(0,[1,1,1,1])
                        zero=randint(0,3)
                        tableau[0][zero]=0
                        lgn1=0
            creer()



def temps():                                                #Fonction temps qui permet d'ajouter des carrés noirs toutes les ? secondes
    global tableau,MonCanevas,timer,tableau1

    timer+=d
    print (d)

    if timer>=10000:
        tableau.insert(0,[1,1,1,1])
        zero=randint(0,3)
        tableau[0][zero]=0
        tableau1.insert(0,[1,1,1,1])
        zero=randint(0,3)
        tableau1[0][zero]=0
        MonCanevas.destroy()
        creer()
        MonCanevas.after(1,temps)
        timer=0
    MonCanevas.after(1,temps)
    MonCanevas.after(100,diffictulte)



def creer():
    global xR,yR,c,Mafenentre1,joueurperdu
    Mafenetre.bind_all('<Key>',touche)
    MonCanevas = Canvas(Mafenetre,bg="white",width=1600,height=900)              #début creation de la fenetre
    MonCanevas.place(x=0,y=0)
    Ligne0=MonCanevas.create_line(400,0,400,1600,fill='black',width=1)
    Ligne1=MonCanevas.create_line(800,50,800,1600,fill='black',width=1)
    Ligne2=MonCanevas.create_line(1200,0,1200,1600,fill='black',width=1)
    A=MonCanevas.create_text(95,745,text="A",font=('Helvetica', '20'))
    Z=MonCanevas.create_text(160,745,text="Z",font=('Helvetica', '20'))
    E=MonCanevas.create_text(225,745,text="E",font=('Helvetica', '20'))
    R=MonCanevas.create_text(290,745,text="R",font=('Helvetica', '20'))
    Touche1=MonCanevas.create_text(1295,745,text="1",font=('Helvetica', '20'))
    Touche2=MonCanevas.create_text(1360,745,text="2",font=('Helvetica', '20'))
    Touche3=MonCanevas.create_text(1425,745,text="3",font=('Helvetica', '20'))
    ENTR=MonCanevas.create_text(1490,745,text="ENTR",font=('Helvetica', '14'))
    label=Label(Mafenetre,text="Cube Craze",font=('Helvetica', '16'))
    label.place(x=750,y=10)
    Boutondificulte1=Button(MonCanevas,text='Facile',width=20,command=diffictulte1)
    Boutondificulte1.place(x=500, y=260)
    Boutondificulte2=Button(MonCanevas,text='Normal',width=20,command=diffictulte2)
    Boutondificulte2.place(x=500, y=300)
    Boutondificulte3=Button(MonCanevas,text='Difficile',width=20,command=diffictulte3)
    Boutondificulte3.place(x=500, y=340)

    for j in range (10):
        for i in range (4):
            if tableau[j][i]==0:
                couleur='white'
            else :
                couleur='black'
            Rectangle=MonCanevas.create_rectangle(xR+65*i,yR+65*j,xR+60+65*i,yR+60+65*j,fill=couleur)
            sommetableau2=tableau[9][0]+tableau[9][1]+tableau[9][2]+tableau[9][3]
            sommetableau1=tableau[1][0]+tableau[1][1]

    if sommetableau1==0:
                tableau.insert(0,[1,1,1,1])
                zero=randint(0,3)
                tableau[0][zero]=0
    if sommetableau2>0:
        joueurperdu=1
        perdu()

    for j in range (10):
        for i in range (4):
            if tableau1[j][i]==0:
                couleur='white'
            else :
                couleur='black'
            Rectangle=MonCanevas.create_rectangle(xR1+65*i,yR1+65*j,xR1+60+65*i,yR1+60+65*j,fill=couleur)
            sommetableau2bis=tableau1[9][0]+tableau1[9][1]+tableau1[9][2]+tableau1[9][3]
            sommetableau1bis=tableau1[1][0]+tableau1[1][1]

    if sommetableau1bis==0:
                tableau1.insert(0,[1,1,1,1])
                zero=randint(0,3)
                tableau1[0][zero]=0

    if sommetableau2bis>0:
        joueurperdu=2
        perdu()


    anim=MonCanevas.create_rectangle(xT+65*col,yT,xT+60+65*col,775,fill="red")
    anim1=MonCanevas.create_rectangle(xT1+65*col1,yT,xT1+60+65*col1,775,fill="red")


def perdu():
##    global MonCanevas
    MonCanevas1 = Canvas(Mafenetre,bg="white",width=600,height=400)
    MonCanevas1.place(x=500,y=200)
    Bouton1=Button(MonCanevas1,text='Replay',width=20,command=replay)
    Bouton1.place(x=240, y=260)
    print(joueurperdu)
    if joueurperdu==1:
        Affichage = Label(MonCanevas1, text="Dommage! Joueur1 a perdu!",font=('Helvetica', '20'))
    else:
        Affichage = Label(MonCanevas1, text="Dommage! Joueur2 a perdu!",font=('Helvetica', '20'))
    Affichage.place(x=150,y=200)
##    photo = PhotoImage(file="tk_cible.gif")
##    item = MonCanevas1.create_image(0,0,anchor=NW, image=photo)
##    print("Image de fond (item",item,")")
##    Mafenetre.unbind_all('<Key>',touche)

def diffictulte1():
    global e
    e=0.0001

def diffictulte2():
    global e
    e=0.00025

def diffictulte3():
    global e
    e=0.001

def diffictulte():
    global MonCanevas,d

    d+=e

    MonCanevas.after(100,diffictulte)


tableau=[[0 for i in range(4)]for j in range(10)]
tableau1=[[0 for i in range(4)]for j in range(10)]
for j in range (3):
    for i in range(4):
        tableau[j][i]=1
    zero=randint(0,3)
    tableau[j][zero]=0

for j in range (3):
    for i in range(4):
        tableau1[j][i]=1
    zero=randint(0,3)
    tableau1[j][zero]=0

e=0             # rapidité daugmentation de la vitesse
d=5             # rapidité de dessente des carre
timer=0         # valeur incrementer pour augmente la pressision de la dessente des carré

Mafenetre= Tk()
Mafenetre.title("Cube Craze")
Mafenetre.geometry("1600x900")



MonCanevas = Canvas(Mafenetre,bg="white",width=1600,height=900)
MonCanevas.place(x=0,y=0)
xR=65; yR=65 ;xR1=1265 ;yR1=65 ; xT=65;yT=715;xT1=1265
couleur=''

label=Label(Mafenetre,text="Cube Craze")
label.pack()
col=200
col1=200

c=0
lgn=0
lgn1=0

creer()
temps()



mainloop()