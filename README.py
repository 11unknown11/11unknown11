# 1
def sahetap(a,h):
    return 0.5 * a * h
# 2
def tekrarsil(a):
    soz,t = "",""
    for c in a: # sozdeki herfleri gezirik
        if c != t: # herfin evvelki herfle eyni olmadigini yoxlayiriq
            soz+=c # eyni deyilse soze elave edirik
        t = c # indiki herfi evvelki herf kimi yadda saxlayiriq
    return soz
# 3
def butunreqemler(eded):
    return list(filter(lambda x: str(x) not in str(eded) ,range(1,10))) # [1,9] araligini filter edirik    
print(butunreqemler(98305614820698024492))
# 4
def nomre(a):
    emsal = 1
    if(a.startswith("10")): # startswith funksiyasi stringin ona verilen argumentle baslayib baslamadigina gor True ve ya False return edir 
        emsal = emsal + 2 # eger 10 la baslayirsa demeli Baki nomresidir emsala 2 elave edirik
    hisseler = a.split("-") # nomreni ni - ayiririq

    if(hisseler[1][0] == hisseler[1][1]): # nomrenin ikinci hissesi eyni herlerden ibaretdirse onda emsala 3 artiririq
        emsal = emsal + 3
    
    if(hisseler[2][0] == hisseler[2][1] == hisseler[2][2]): # nomrenin ucuncu hissesi hamsi eynidirse onda emsala 6 artiririq
        emsal = emsal + 6
    
    print(emsal*50)

nomre("10-UU-556")
# 5
def bolunen(eded):
    return eded % sum([int(i) for i in str(eded)])
print(bolunen(131))
# 6
def multN(n,a=1):
    while(n//10 != 0):
        a,n=a*(n%10),n//10
    return a*(n%10)
def addim(num,counter = 0):
    if(num in range(10)): return counter
    return addim(multN(num),counter+1)
print(addim(77))
# 7
def tambolunen35():
    return list(filter(lambda x: x%3==0 and x%5==0 ,range(1,100)))
print(tambolunen35())
# 8 
print(len(list(range(0,int(input("Eded daxil edin: ")),2)))) 
# 9
m = [2,2,4,3,6,9,6,1,5,1] # siyahi verilib
for a in range(len(m)-1,-1,-1):
    if(m[a]>3):
        m.pop(a)
print(m)

# 10
ayliqqiymetler = [136,151,125,119,146,133,118,106,138,136,127,101]
print(str(ayliqqiymetler.index(min(ayliqqiymetler))+1)+" ayda mali alib "+str(ayliqqiymetler.index(max(ayliqqiymetler))+1)+" ayda satmaq lazimdir")
# 11
for i in range(1,6):
    print((i*str(i)).center(5))
# 12
# fibonacci seriyasi: 0,1,1,2,3,5,8 
def fibonacci(eded,evvelkieded):
    if eded > 100:
        return
    print(eded)
    return fibonacci(eded+evvelkieded,eded)
fibonacci(1,0)
# 13
print(sum([int(a) for a in input("Ededler: ").split(",")]))
# 14
print(input("Cumle: ").split(" ")[-1])
# 15
print([int(a)**2 for a in input("Ededler: ").split(",")])
# 16
print(len(list(filter(lambda x: x%3==0 and x%5!=0 ,range(100,200)))))
# 17
saitler = ["a","ı","o","u","e","ə","i","ö","ü"]
print(len(list(filter(lambda x: x in saitler,input("Cumle : ")))))
# 18
eded = input("Eded: ")
print(list(filter(lambda x: str(x) not in eded ,range(0,10))))
# 19
print(input("Cumle: ").split()[::-1])
# 20
l = {len(a):a for a in input("Cumle: ").split(" ")}
print(l[min(l.keys())])
# 21
l = {len(a):a for a in input("Cumle: ").split(" ")}
print(l[max(l.keys())])
# 22
print(len(input("Cumle: ").split(" ")))
# 23
l = {a:len(a) for a in input("Cumle: ").split(" ")}
print(len(list(filter(lambda x: x==4,l.values()))))
# 24
print(list(filter(lambda x: x.startswith("a") and x.endswith("m"),input("Cumle : ").split(" "))))
# 25 
print(len(list(filter(lambda x: x.endswith("lar"),input("Cumle : ").split(" ")))))
# 26 : 22 ile eyni
# 27
setr = input("Setr: ")
print(list(filter(lambda x: setr[x].isupper(),range(0,len(setr)))))
# 28
def isogram(soz):
    l = {a:soz.count(a) for a in soz}
    return len(list(filter(lambda x: x != 1,l.values()))) == 0
print(isogram(input("Soz: ")))
# 29
def convert(soz):
    boyukHerfSayi = len(list(filter(lambda x: x.isupper(),[a for a in soz])))
    kicikHerfSayi = len(list(filter(lambda x: x.islower(),[a for a in soz])))
    return boyukHerfSayi if boyukHerfSayi < kicikHerfSayi else kicikHerfSayi
print(convert(input("Soz: ")))
# 30
def armstrongnumber(eded):
    reqemler =  [int(a) for a in str(eded)]
    return eded == sum([a**3 for a in reqemler])
print(armstrongnumber(153))
# 31
def polindromecheck(eded):
    return str(eded) == str(eded)[::-1] 
print(polindromecheck(2872))
# 32
def artmasirasi(eded):
    reqemler = [int(a) for a in eded] # eded reqemlerine bolunur, int-e cevirib listde saxlayiriq
    return reqemler == sorted(reqemler)
print(artmasirasi((input("Eded: "))))
# 33
def ozreqemlerinebolunur(eded):
    reqemler = [int(a) for a in eded]
    return len(list(filter(lambda x: int(eded)%x==0,reqemler))) == len(eded)
print(ozreqemlerinebolunur(input("Eded: ")))
# 34
def cutsil(eded):
    return "".join(list(filter(lambda x: int(x)%2!=0,[a for a in eded])))
print(cutsil(input("Eded: ")))
# 35
def NOYES(eded):
    l = {a:eded.count(a) for a in eded}
    return "YES" if len(list(filter(lambda x: x!=1,l.values()))) == 0 else "NO"
print(NOYES(input("Eded: ")))
# 36
def dayaqNoqtesi(list):
    for a in range(1,len(list)):
        if sum(list[:a]) == sum(list[a+1:]):
            return list[a]
print(dayaqNoqtesi([9,1,9]))
# 37
def fibonacci(vereded,eded=1,evvelkieded=0):
    if eded > vereded:
        return
    print(eded)
    return fibonacci(vereded,eded+evvelkieded,eded)
fibonacci(10)
# 38
def myFunction(soz,herfler):
    for a in soz:
        if a not in herfler:
            soz = soz.replace(a,"-")
    return soz
print(myFunction("helicopter",["o","e","s"]))
# 39 
ededler = list(filter(lambda x: x%7==0,range(1,int(input("Eded: ")))))
hasil = 1
for i in ededler:
    hasil*=i
print(hasil)
# 40
siyahi = list(filter(lambda x: str(x).endswith("3"),range(1,int(input("Eded: ")))))
print(siyahi)
# 41
x,y = input("X,Y : ").split(",")
siyahi = list(filter(lambda x: x%6!=0,range(int(x),int(y))))
print(siyahi)








#ELAVELER
#40 Yeni siyahı(list) yaradın və daxil edilmiş (input funlsiyasi ilə) ədədə qədər olan və 3 rəqəmi ilə bitən
#ədədləri həmin siyahiya əlavə edin
new = []
daxileded = int(input())

for eded in range(1, daxileded):
    if str(eded).endswith("3"):
        new.append(eded)

for eded in new:
    print(eded, end=' ')
#3. Verilmiş ədədin içində bütün rəqəmlərin olub olmamasını yoxlayan funksiya yazın.
reqemler = [str(i) for i in range(0, 10)]
reqemler_ = [0 for i in range(0, 10)]
text = input()
for i in text:
    reqemler_[reqemler.index(i)] = 1

for i in range(0, 10):
    if reqemler_[i] == 0:
        print(reqemler[i], end=' ')

#5. Ədədin onu təşkil edən rəqəmlərin cəminə qalıqsız bölündüyünü müəyyən edən funksiya yazın.
a = input()
cem = 0
for i in a:
    cem += int(i)
if int(a) % cem == 0:
    print("qaliqsiz bolunur")
else:
    print("qaliqli bolunur")


#6 Ədədin rəqəmlərinin hasilinin rəqəm olması üçün neçə dövr getməli olduğunu bildirən funksiya yazın.
eded = input()
hasil = 1
addimlarin_sayi = 0
while True:
    for i in eded:
        hasil *= int(i)
    addimlarin_sayi += 1
    eded = str(hasil)
    hasil = 1
    if len(eded) == 1:
        break
print(addimlarin_sayi)

#12. Çıxışda 100-ə qədər olan Fibonaçi ədədlərini göstərən proqram yazın.
a = 0
a1 = 1

for i in range(100):
    a, a1 = a1, a + a1
    if a > 100:
        break
    print(a, end=" ")

# 27. Arqument kimi tək bir sətri götürən və sətirdəki bütün böyük hərflərin indekslərin olduğu sıralanmış
# siyahı(list) qaytaran funksiya yaradın. myFunction(“HeLlo WorD”) → [0,2,6,9]

text = input() #Hello world
               #0123456789 10
new = []

for i in range(len(text)): # HellO WorlD (0, 1, 3 ..... 10)
    if text[i].isupper(): # text[4] => o  'o'.isupper()
        new.append(i)

print(new)

#28 isogram dublikat hərfləri olmayan sözdür. Sətir götürən və "isogram" olub-olmamasından asılı olaraq True və
#ya False qaytaran funksiya yaradın.

text = input() # isogram

eded_isogramdir = True

for i in text:
    if text.count(i) != 1: #2
        eded_isogramdir = False
        break

if eded_isogramdir == True:
    print('eded isogrisogramdir')
else:
    print('eded isogram deyil')
    
  
#tapsiriq 2
def tekrar(soz):
    a=""
    b=""
    for i in soz:
        if i!=a:
            b=b+i
        a=i
    return b
soz=list(input())
print(tekrar(soz))
   
    
