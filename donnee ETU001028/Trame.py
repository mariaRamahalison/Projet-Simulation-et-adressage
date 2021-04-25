class Trame:
    def __init__(self,ipSource,ipDest,macSource,macDest,adresseReseauDest):
        self.ipSource=ipSource
        self.ipDest=ipDest
        self.macSource=macSource
        self.macDest=macDest
        self.routers=[]
        self.message="non"
        self.reseau=adresseReseauDest

    def setPortDest(self,port):
        self.portDest=port

        
