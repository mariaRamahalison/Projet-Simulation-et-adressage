from tkinter import *
from tkinter import ttk
import math


classe = [['A', '255.0.0.0',8], ['B', '255.255.0.0',16], ['C', '255.255.255.0',32]]
limite = [[1, 127], [128, 192], [192, 224]]
binaireMasque='11111111.11111111.11111111.11111111'

class Ipv4:
    def __init__(self, ip):
        self.ip= ip
        self.adresseReseau=self.getAdresseReseau(ip)
        self.adresseDiffusion=self.getAdresseDiffusion(ip)
        self.masque=self.getMasque(ip)
        self.classeIp=self.getClasse(ip)
        self.premier=self.getPremier()
        self.fin=self.getFin()
        self.nb=self.nbDispo()

    def nbDispo(self):
        ips=self.ip.split("/")
        nb=0
        if len(ips)>1:
            nb=32-int(ips[1])
        else:
            indice=self.getIndice(self.ip)
            nb=classe[indice][2]
        nb=(math.pow(2,nb))-2
        return str(nb)
            
    def getIndice(self,ip):
        ips = ip.split(".")
        debut=int(ips[0])
        indice=-1
        for i in range(3):
            if debut >= limite[i][0] and debut < limite[i][1]:
                indice=i
                break
        return indice

    def getClasse(self,ip):
        indice=self.getIndice(ip)
        return classe[indice][0]

    def replace(self,nb,ips,valeur):
        nbInt=int(nb)
        binaire=list(ips)
        print(ips)
        for i in range(len(binaire)):
            if binaire[i]!=".":
                if nbInt<=0:
                    binaire[i]=valeur
                nbInt=nbInt-1
        strbinaire="".join(binaire)
        binaire=strbinaire.split(".")
        binaire=self.getInt(binaire)
        strbinaire=".".join(binaire)
        return strbinaire


    def getBin(self,ips):
        for i in range(len(ips)):
            if ips[i]!=".":
                print(ips)
                ips[i]=bin(int(ips[i]))[2:].zfill(8)
        return ips

    def getInt(self,ips):
        for i in range(len(ips)):
            if ips[i]!=".":
                ips[i]=str(int(ips[i],2))
                print(ips[i])
        return ips

    def getMasque(self,ip):
        ips=ip.split("/")
        if len(ips)>1 :
            nb=int(ips[1])
            masque=self.replace(nb,binaireMasque,"0")
            return masque
        else:
            indice=(self.getIndice(ip))+1
            return classe[indice][1]

    def getAdresseReseau(self,ip):
        ips=ip.split("/")
        indice=self.getIndice(ip)+1
        adresseReseau=""
        if(len(ips)>1):
            binaire=self.getBin(ips[0].split("."))
            strbinaire=".".join(binaire)
            nb=int(ips[1])
            adresseReseau=self.replace(nb,strbinaire,"0")
        else:
            ips=ip.split(".")
            for i in range(len(ips)):
                if i>=indice:
                    ips[i]="0"
            adresseReseau=".".join(ips)
        return adresseReseau
            
    def getPremier(self):
        ip=self.adresseReseau
        ips=ip.split(".")
        ips[3]=str(int(ips[3])+1)
        return ".".join(ips)

    def getFin(self):
        ip=self.adresseDiffusion
        ips=ip.split(".")
        ips[3]=str(int(ips[3])-1)
        return ".".join(ips)
        

    def getAdresseDiffusion(self,ip):
        ips=ip.split("/")
        indice=self.getIndice(ip)+1
        adresseDiffusion=""
        if(len(ips)>1):
            binaire=self.getBin(ips[0].split("."))
            strbinaire=".".join(binaire)
            nb=int(ips[1])
            adresseDiffusion=self.replace(nb,strbinaire,"1")
        else:
            ips=ip.split(".")
            for i in range(len(ips)):
                if i>=indice:
                    ips[i]="255"
            adresseDiffusion=".".join(ips)
        return adresseDiffusion


ip="7.28.172.198/8"
ipv4=Ipv4(ip)
print("1 adresse:"+ipv4.nb+"classe: "+ipv4.classeIp+"   adresse reseau: "+ipv4.adresseReseau+"   adresse diffusion:"+ipv4.adresseDiffusion+"  masque:"+ipv4.masque)


