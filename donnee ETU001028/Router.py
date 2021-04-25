from Appelant import Appelant
from Trame import Trame

class Router:
    def __init__(self,nom,routing,per):
        self.tableArp= []
        self.routage=routing
        self.nom=nom
        self.types="router"
        self.peripheries=per
    
    def setIp(self,ip):
        self.ip=ip
    def setMac(self,mac):
        self.mac=mac
    def setPeripheries(self,per):
        self.peripheries=per

    def verifyReseau(self,trame):
        intf=0
        adresseReseau=trame.reseau
        for i in range(len(self.routage)):
            if self.routage[i][2]==adresseReseau:
                intf=self.routage[i][0]
                macRouter=self.getMacRouter(intf)
                self.mac=macRouter
                trame.routers.append(macRouter)
        return intf
    
    def getMacRouter(self,intf):
        for i in range(len(self.peripheries)):
            if self.peripheries[i][0]==intf:
                return self.peripheries[i][2]

    def affichageRoutage(self):
        print(self.nom+":")
        print("table de routage")
        print(self.routage)
        print("table de arp")
        print(self.tableArp)
        print("************")

    def commutation(self,trame,appelant):
        # appelant routage
        intf=self.verifyReseau(trame)
        if intf!=0:
            self.apprentissage(appelant.ip,appelant.mac)
            mac=self.verifyArp(trame.ipDest)
            if mac!=None:
                trame.macDest=mac
            self.diffusion(trame,intf,appelant)
            if trame.message!="non":
                self.affichageRoutage()
       
    def apprentissage(self,ip,mac):
        macA=self.verifyArp(ip)
        if macA==None:
            table=[ip,mac]
            self.tableArp.append(table)

    def diffusion(self,trame,intf,appelant):
        for i in range(len(self.peripheries)):
            if self.peripheries[i][1]!=appelant.appelant:
                if self.peripheries[i][0]==intf:
                    appelantN=Appelant(self,appelant.ip,appelant.mac)
                    self.peripheries[i][1].commutation(trame,appelantN)
                if trame.message!="non":
                    self.apprentissage(trame.ipDest,trame.macDest)
    def verifyArp(self,ip):
        mac=None
        for i in range(len(self.tableArp)):
            if self.tableArp[i][0]==ip:
                mac=self.tableArp[i][1]
        return mac
