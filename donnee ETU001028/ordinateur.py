
from Trame import Trame
from Switch import Switch
from Router import Router
from Appelant import Appelant

class Ordinateur:
    def __init__(self, ip,mac,com,masque,passerelle,nom,reseau):
        self.ip= ip
        self.mac=mac
        self.masque=masque
        self.passerelle=passerelle
        self.commutateur=com
        self.tableArp=[]
        self.types="ordi"
        self.nom=nom
        self.adresseReseau=reseau
    
    def commutation(self,trame,appelant):
        if self.ip==trame.ipDest:
            trame.macDest=self.mac
            trame.message="envoyer"
            self.apprentissage(trame.ipSource,trame.macSource)
            self.affichageArp()

    def affichageArp(self):
        print(self.nom+":")
        print("table Arp:")
        print(self.tableArp)
        print("**************")

    def apprentissage(self,ip,mac):
        bools=self.verifyArp(ip)
        if bools==True:
            table=[ip,mac]
            self.tableArp.append(table)
            
    def verifyArp(self,ip):
        bools=True
        for i in range(len(self.tableArp)):
            if self.tableArp[i][0]==ip:
               bools=False
        return bools

    def communication(self,pc):
        trame=self.getTrameDonne(pc)
        print("TRAME:header src:"+trame.ipSource+"  dest:"+trame.ipDest)
        appelant=Appelant(self,self.ip,self.mac)
        self.commutateur.commutation(trame,appelant)
        if trame.macDest!=None:
            table=[trame.ipDest,trame.macDest]
            self.tableArp.append(table)
            self.affichageArp() 
            self.afficheHeader(trame)
        else:
            print("donne non envoyer")

    def afficheHeader(self,trame):
        routers=trame.routers
        print("TRAME:header:")
        print("src:"+trame.ipSource+"  dest:"+trame.ipDest)
        macSource=trame.macSource
        for i in range(len(trame.routers)):
            print("src:"+macSource+"  dest:"+routers[i])
            macSource=routers[i]
        print("src:"+macSource+"  dest:"+trame.macDest)
        print("message envoyer")
        print("**************")
        
    def getTrameDonne(self,pc):
        indice=self.getMacArp(pc.ip)
        if indice!=-1:
            macDest=self.tableArp[indice][1]
            trame=Trame(self.ip,pc.ipDest,self.mac,pc.macDest,pc.adresseReseau)
            return trame
        else:
            trame=Trame(self.ip,pc.ip,self.mac,None,pc.adresseReseau)
            return trame

    def getMacArp(self,ip):
        indice=-1
        for i in range(len(self.tableArp)):
            if self.tableArp[i][0]==ip:
                indice=i
        return indice


# PC1-S1-PC2
#     S1-R1-PC3
#     S1-R1-R2-PC4

S1=Switch(2,"s1")
S2=Switch(1,"s2")
pc1=Ordinateur("172.160.10","AA.AA.AA",S1,"255.0.0","172.160.01","pc1","172.160.00")
pc2=Ordinateur("172.160.11","BB.BB.BB",S1,"255.0.0","172.160.01","pc2","172.160.00")
pc3=Ordinateur("172.180.11","DD.DD.D",S2,"255.0.0","172.180.01","pc3","172.180.00")
pc4=Ordinateur("172.190.11","EE.EE.EE",S2,"255.0.0","172.180.01","pc4","172.190.00")


peripherieR2=[]
routageR2=[["eth/3",None,"172.190.00"],["eth/4",None,"172.190.00"]]
R2=Router("R2",routageR2,peripherieR2)

peripherieR1=[["eth/1",S1,"E1.E1.E1"],["eth/2",S2,"E2,E2.E2"],["eth/3",R2,"E3.E3.E3"]]
routageR1=[["eth/1",None,"172.160.00"],["eth/2",None,"172.180.00"],["eth/3",None,"172.190.00"]]
R1=Router("R1",routageR1,peripherieR1)
R2.peripheries=[["eth/3",R1,"E3.E3.E3"],["eth/4",pc4,"E4.E4.E4"]]


S1.setPeripheries([["F0/1",pc1],["F0/2",pc2],["F0/3",R1]])
S2.setPeripheries([["F0/4",pc3],["F0/5",R1]])


print("PC1 ping PC2")
pc1.communication(pc2)
print("")
print("")
print("")
print("PC1 ping PC3")
pc1.communication(pc3)
print("")
print("")
print("")
print("PC1 ping PC4")
pc1.communication(pc4)
