from tkinter import *
from tkinter import ttk
from Ipv4 import Ipv4
from Ipv6 import Ipv6
from tkinter.messagebox import showerror

    
def drawTable(fenetre, titre, donnees,taille,y):
    tree = ttk.Treeview(mainapp,height=2)
    tree['columns'] = titre
    tree['show'] = 'headings'



    for i in range(len(titre)):
        tree.column(""+titre[i], width=taille, anchor=CENTER)
        tree.heading(""+titre[i], text=""+titre[i], anchor=CENTER)
    for j in range(len(donnees)):
        tree.insert('', 'end', text="", values=donnees[j])
    tree.place(x=10, y=y)

def ipv4():
    ip = ipv4Input.get()



    titre = ("ip", "classe","masque de sous reseau","adresse reseau", "adresse diffusion","premiere adresse","derniere adresse","Nb adresses disponibles")
    try:
        ipv4=Ipv4(ip)
        donnees = [[ipv4.ip,ipv4.classeIp,ipv4.masque,ipv4.adresseReseau,ipv4.adresseDiffusion,ipv4.premier,ipv4.fin,ipv4.nb]]
        drawTable(mainapp, titre, donnees,150,50)
    except:
        showerror("Erreur", "ip invalide")
    

def ipv6():
    ip = ipv6Input.get()
    ips=ip.split("/")



    try:
        ipv6=Ipv6(ip)
        if len(ips)>1:
            titre = ("ip","abreviation","complet","adresse reseau","adresse diffusion")
            donnees = [[ipv6.ip,ipv6.abreviation,ipv6.complet,ipv6.adresseReseau,ipv6.adresseDiffusion]]
            drawTable(mainapp, titre, donnees,250,150)
        else:
            titre = ("ip","abreviation","complet","adresse reseau","adresse diffusion")
            donnees = [[ipv6.ip,ipv6.abreviation,ipv6.complet,"",""]]
            drawTable(mainapp, titre, donnees,250,150)
    except:
        showerror("Erreur", "ip invalide")

mainapp = Tk()
mainapp.title("IPV4")
mainapp.geometry("1550x600")


label = Label(mainapp, text="IPV4 ", font=("Arial", 12))
label.place(x=10, y=10, anchor=NW)


ipv4Input = Entry(mainapp, font=("Arial", 12))
ipv4Input.place(x=50, y=10)
bouton = Button(mainapp, text="Valider", font=("Arial", 12), command=ipv4)
bouton.place(x=250, y=10)


label = Label(mainapp, text="IPV6 ", font=("Arial", 12))
label.place(x=450, y=10, anchor=NW)
ipv6Input = Entry(mainapp, font=("Arial", 12))
ipv6Input.place(x=500, y=10)
boutonV6 = Button(mainapp, text="Valider", font=("Arial", 12), command=ipv6)
boutonV6.place(x=700, y=10)

mainapp.mainloop()

