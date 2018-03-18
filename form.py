#METE EKER
import os
bg=[]
Ad="Ad : "
Soyad="Soyad : "
Adresiniz="Adres : "
Telefon_Numaraniz="Telefon Numaranız : "
Ek_Bilgiler ="Ek Bilgiler : "
a=input("Adınız :")
bg.append(Ad+a)
sa=input("Soyadınız :")
bg.append(Soyad+sa)
ckt = a+sa+".txt"
dosya = open(ckt, "a")
adr=input("Adresiniz :")
bg.append(Adresiniz+adr)
tel=input("Telefon Numaranız :")
bg.append(Telefon_Numaraniz+tel)
eb=input("Ek Bilgiler : ")
bg.append(Ek_Bilgiler+eb)
i = 0
os.system("clear")
while i<=4:
    yz = bg[i] +"\n"
    ckt = a+sa+".txt"
    dosya = open(ckt, "a")
    dosya.write(yz)
    print(bg[i])
    i+=1
dosya.close()
dosya = open(ckt, "r")
a = str(dosya.read())
print(a,"\n DOSYALAR KAYDEDİLDİ")
