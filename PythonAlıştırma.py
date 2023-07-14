#Görev1:Verilen değerlerin veri yapılarını inceleyin
from typing import Set

x = 8
print(type(x))
y = 3.2
print(type(y))
z = 8j+18
print(type(z))
a ="Hello World"
print(type(a))
c = 23 < 22
print(type(c))
l = [1,2,3,4]
print(type(l))
d = {"Name":"Jake","Age":27,"Adress":"Downtown"}
print((type(d)))
t = ("Machine Learning","Data Science")
print(type(t))
s = {"Python","Machine Learning","Data Science"}
print(type(s))


#Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
text = "The goal is to turn data into information, and information into insight."
r1 = text.upper()
r2 = r1.replace(" ",",")
print(r2)

#Görev3: Verilen listeye aşağıdaki adımları uygulayınız.
lst = ["D","A","T","A","A","S","C","I","E","N","C","E"]
#Adım 1: Verilen listenin eleman sayısına bakınız.
print(len(lst))
#Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
print(lst[0::10])
#Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
lst2 = lst[0:4:1]
print(lst2)
#Adım 4: Sekizinci indeksteki elemanı siliniz.
del lst[8]
print(lst)
#Adım 5: Yeni bir eleman ekleyiniz.
lst.append("N")
print(lst)
#Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.
lst.insert(8,"N")
print(list)


#Görev4: Verilen sözlük yapısına aşağıdaki adımlarıu ygulayınız.
dict = {
    "Christian":["America",18],
    "Daisy":["England",12],
    "Antonio":["Spain",22],
    "Dante":["Italy",25]
}
#Adım1
print(dict.keys())
#adım2
print(dict.values())
#Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz
dict["Daisy"][1] = 13
print(dict)
#Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict2 = {"Ahmet":["Turkey",24]}
dict.update(dict2)
print(dict)
#Adım 5: Antonio'yu dictionary'den siliniz.
del dict["Antonio"]
print(dict)

#Görev 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.

l = [2,13,18,93,22]
def func(list):
    even_list = []
    add_list = []
    for i in list:
        if i % 2 == 0:
            even_list.append(i)

        else:
            add_list.append(i)
    return even_list,add_list

even,add = func(l)
print(func(l))

#Görev 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for i,ogrenci in enumerate(ogrenciler):
    if i<3:
        i +=1
        print("Mühendislik Fakültesi",i,".Öğrenci",ogrenci)
    else:
        i += 2
        print("Tıp Fakültesi",i,".Öğrenci",ogrenci)


#Görev 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
ders_kodu  = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontejan = [30,75,150,25]

for i,j,z in zip(kredi,ders_kodu,kontejan):
    if i<3:
        print("Kredisi",kredi[0],"olan",ders_kodu[0],"kodlu dersin kontejanı",kontejan[0],"kişidir.")
for i,j,z in zip(kredi,ders_kodu,kontejan):
    if i<4:
        print("Kredisi",kredi[1],"olan",ders_kodu[1],"kodlu dersin kontejanı",kontejan[1],"kişidir.")
        break
for i,j,z in zip(kredi,ders_kodu,kontejan):
    if i<5:
        print("Kredisi",kredi[2],"olan",ders_kodu[2],"kodlu dersin kontejanı",kontejan[2],"kişidir.")
        break
for i,j,z in zip(kredi,ders_kodu,kontejan):
    if i<6:
        print("Kredisi",kredi[3],"olan",ders_kodu[3],"kodlu dersin kontejanı",kontejan[3],"kişidir.")
        break
#Görev 8: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

kume1 = set(["data","python"])
kume2 =  set(["data","function","qcut","lambda","python","miuul"])

kume3 = kume2.difference(kume1)
print(kume3)