from tkinter import *
from tkinter import ttk
from Ipv4 import Ipv4
from Ipv6 import Ipv6


    
def drawTable(fenetre, titre, donnees,taille):
    for i in tree.get_children():
        tree.delete(i)
    tree['columns'] = titre
    tree['show'] = 'headings'
    for i in range(len(titre)):
        tree.column(""+titre[i], width=taille, anchor=CENTER)
        tree.heading(""+titre[i], text=""+titre[i], anchor=CENTER)
    for j in range(len(donnees)):
        tree.insert('', 'end', text="", values=donnees[j])
    tree.place(x=10, y=70)

def ipv4():
    ip = ipv4Input.get()
    titre = ("ip", "classe", "masque de sous reseau", "adresse reseau", "adresse diffusion","premiere adresse","derniere adresse","Nb adresses disponibles")
    ipv4=Ipv4(ip)
    donnees = [[ipv4.ip,ipv4.classeIp,ipv4.masque,ipv4.adresseReseau,ipv4.adresseDiffusion,ipv4.premier,ipv4.fin,ipv4.nb]]
    drawTable(mainapp, titre, donnees,150)

def ipv6():
    ip = ipv6Input.get()
    ips=ip.split("/")
    if len(ips)>1:
        titre = ("ip","abreviation","complet","adresse reseau", "adresse diffusion")
        ipv6=Ipv6(ip)
        donnees = [[ipv6.ip,ipv6.abreviation,ipv6.complet,ipv6.adresseReseau,ipv6.adresseDiffusion]]
        drawTable(mainapp, titre, donnees,230)
    else:
        titre = ("ip","abreviation","complet")
        ipv6=Ipv6(ip)
        donnees = [[ipv6.ip,ipv6.abreviation,ipv6.complet]]
        drawTable(mainapp, titre, donnees,230)

mainapp = Tk()
mainapp.title("IPV4")
mainapp.geometry("1500x200")

tree = ttk.Treeview(mainapp,height=3)
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

