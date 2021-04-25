from Appelant import Appelant
class Switch:
    def __init__(self, nbPort,nom):
        self.nbPort=nbPort
        self.tableMac=[]
        self.nom=nom
        self.types="switch"

    def setPeripheries(self,per):
        self.peripheries=per

    def getPort(self,appelant):
        for i in range(len(self.peripheries)):
            if self.peripheries[i][1]==appelant.appelant:
                return self.peripheries[i][0]

    def commutation(self,trame,appelant):
        port=self.getPort(appelant)
        self.apprentissage(port,appelant.mac)
        self.envoyer(trame,appelant)
        if trame.message=="non":
            self.diffusion(trame,appelant)
        if trame.message!="non":
            self.AffichageMac()

    def AffichageMac(self):
        print(self.nom)
        print("table Mac")
        print(self.tableMac)
        print("**************")
    
    def getPeripheries(self,port):
        for i in range(len(self.peripheries)):
            if self.peripheries[i][0]==port:
                return i

    def envoyer(self,trame,appelant):
        port=self.verifyTableMac(trame.macDest)
        if port!=None:
            i=self.getPeripheries(port)
            appelantN=Appelant(self,appelant.ip,appelant.mac)
            self.peripheries[i][1].commutation(trame,appelant)
            if trame.macDest!=None :
                self.apprentissage(self.peripheries[i][0],trame.macDest)

    def apprentissage(self,portS,mac):
        port=self.verifyTableMac(mac)
        if port==None:
            table=[portS,mac]
            self.tableMac.append(table)

    def verifyTableMac(self,mac):
        port=None
        for i in range(len(self.tableMac)):
            if self.tableMac[i][1]==mac :
                port=self.tableMac[i][0]
        return port

    def diffusion(self,trame,appelant):
        for i in range(len(self.peripheries)):
            if self.peripheries[i][1]!=appelant.appelant:
                appelantN=Appelant(self,appelant.ip,appelant.mac)
                self.peripheries[i][1].commutation(trame,appelantN)
                if trame.message!="non":
                    self.apprentissage(self.peripheries[i][0],trame.macDest)

    

