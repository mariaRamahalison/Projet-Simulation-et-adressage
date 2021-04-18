class Ipv6:
    def __init__(self, ip):
        self.ip= ip
        self.abreviation=self.getAbreviation()
        self.adresseReseau=self.getAdresseReseau(ip)
        self.adresseDiffusion=self.getAdresseDiffusion(ip)
        self.complet=self.getAbrInv(ip)

            
    def getBin(self,ips):
        for i in range(len(ips)):
            if ips[i]!=":":
                ips[i]=str(int(ips[i],16))
                ips[i]=bin(int(ips[i]))[2:].zfill(4)
        return ips

    def getHexa(self,ips):
        for i in range(len(ips)):
            if ips[i]!=":":
                ips[i]=hex(int(ips[i], 2))[2:]
        return ips

    def getAdresseReseau(self,ip):
        ips=ip.split("/")
        if len(ips)>1:
            strbinaire=self.getBinaire(ips[0])
            nb=int(ips[1])
            ip=self.replace(nb,strbinaire,"0")
        return ip

    def getBinaire(self,ip):
        ip=self.getAbrInv(ip)
        ips=list(ip)
        hexa=self.getBin(ips)
        binn="".join(hexa)
        return binn

    def getAdresseDiffusion(self,ip):
        ips=ip.split("/")
        if len(ips)>1:
            strbinaire=self.getBinaire(ips[0])
            nb=int(ips[1])
            ip=self.replace(nb,strbinaire,"1")
        return ip

    def getInt(self,ips):
        for i in range(len(ips)):
            if ips[i]!=":":
                ips[i]=str(int(ips[i],2))
        return ips

    def replace(self,nb,ips,valeur):
        nbInt=int(nb)
        binaire=list(ips)
        for i in range(len(binaire)):
            if binaire[i]!=":":
                if nbInt<=0:
                    binaire[i]=valeur
                nbInt=nbInt-1
        strbinaire="".join(binaire)
        hexas=strbinaire.split(":")
        hexa=self.getHexa(hexas)
        strbinaire=":".join(hexa)
        return strbinaire

    def getAbreviation(self):
        ip=self.ip.split("/")[0]
        ip=self.abrZeros(ip)
        ip=self.abrZero(ip)
        return ip

    def replaceAbr(self,indice,nb,ips,valeur):
        indice=indice-nb+1
        ip=""
        sep=""
        for i in range(indice,nb+1):
            ips[i]=""
        for i in range(len(ips)):
            if i>0 and ips[i]!="":
                sep=":"
            if i==indice:
                sep=":"
            ip=ip+""+sep+""+ips[i]
            sep=""
        return ip

    def replaceNone(self,hexa):
        hexas=list(hexa)
        nb=0
        for i in range(len(hexas)-1):
            if hexas[i]=="0" and nb==0:
                hexas[i]=""
            else:
                nb=1
        return "".join(hexas)

    def abrZero(self,ip):
        ips=ip.split(":")
        for i in range(len(ips)):
            ips[i]=self.replaceNone(ips[i])
        return ":".join(ips)

    def abrZeros(self,ip):
        ips=ip.split(":")
        nb=0
        indice=0
        for i in range(len(ips)):
            if ips[i]=="0000" or ips[i]=="0":
                nb=nb+1
                indice=i
            else:
                if nb>1:
                    break
                nb=0
        if nb>1:
            ip=self.replaceAbr(indice,nb,ips,"")
        return ip



    def getZero(self,taille,sep):
        zeros=""
        for i in range(taille):
            zeros=zeros+""+sep
            zeros=zeros+"0"
        return zeros

    def getAbrInv(self,ip):
        ips=ip.split("/")
        ip=self.addZeros(ips[0])
        ip=self.addZero(ip)
        return ip 

    def addZeros(self,ip):
        ips=ip.split(":")
        taille=8-len(ips)
        zeros=ip.split("::")
        if len(zeros)>=0:
            taille=taille+1
            zero=self.getZero(taille,":")
            zeros[0]=zeros[0]+zero
            ip=":".join(zeros)
        return ip

    def addZero(self,ip):
        ips=ip.split(":")
        for i in range(len(ips)):
            ipHexa=list(ips[i])
            if len(ipHexa)<4:
                taille=4-len(ipHexa)
                zeros=self.getZero(taille,"")
                ips[i]=zeros+""+ips[i]
        ip=":".join(ips)
        return ip


ip="210F:0000:0000:0000:CCCC:0000:0000:000D"
ipv6=Ipv6(ip)
ip=ipv6.abreviation
print(ip)