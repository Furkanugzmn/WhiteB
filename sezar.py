import time
 
soylenen = str(input("Kelime: "))
n = int(input("Değişim Miktarı: "))
time.sleep(1)
y = list(soylenen)
print("Kelime Uzunluğu ",len(y))
print("---------------------------------------------------------")

Number_List = ["a","b","c","d","e","f","g","h","ı","i","j","k","l","m","n","o","p","r","s","ş","t","u","ü","v","w","x","y","z"]
New_List = []

def harf_donumu(harf_konumu,kaydırma_miktarı):

    time.sleep(0.7) 
    fark = int(len(Number_List)) - int(harf_konumu) #Fark Bulunur Ve Liste Sonuna Eşitlenir
    basa_sar = int(kaydırma_miktarı) - fark #Burada En Sona Kadar Getirilen Sayının En bastan Ne Kadar Gideceği Belirlenir
    bastan_gelen_harf = Number_List[basa_sar] #Yeni Harf 
    print("Yeni Harf : ",bastan_gelen_harf)
    add_list(bastan_gelen_harf,New_List)

def add_list(harf,liste):
    liste.append(harf)
    print("---------------------------------")
    print("Harf Listeye Eklendi..")
    print("Liste(Güncel) : ",liste)
    print("---------------------------------")
    time.sleep(1.2)

def bosluk_cozucu(bosluk_konumu):
    print("Boşluk Bulundu")
    time.sleep(0.5)
    if str(bosluk_konumu) == " ":
        print("Değişim Olmayacak")
        New_List.append(" ")
        print("Liste(Güncel) : ",New_List)
        print("---------------------------------------------------------")


m = 0
while m < int(len(soylenen)):

    t =(int(len(y))+m-int(len(y)))
    time.sleep(0.5)
    print("Kelime: ",y[t])

    if str(y[t]) == " ":
        bosluk_cozucu(y[t])
        m = m+1
        continue

    print("Sözlük Numarası: ",Number_List.index(y[t]))
    time.sleep(1.5)
    
    if int(Number_List.index(y[t]))+ n >= int(len(Number_List)):
        harf_donumu(Number_List.index(y[t]),n)
        m = m+1
        print("---------------------------------------------------------")


    else:

        print("Yeni Harf : ",Number_List[int(Number_List.index(y[t]))+n])
        time.sleep(0.4)
        add_list(Number_List[int(Number_List.index(y[t]))+n],New_List)
        m = m+1
        print("---------------------------------------------------------")

silinenler = "[],', "
str_hal = str(New_List)
cıktı = str.maketrans("","",silinenler)

print("Şifrelenmiş Hal: ",str_hal.translate(cıktı))
print("Orjinal: ",soylenen)

print("----------------------------------------------------------------------------------------------------------")
