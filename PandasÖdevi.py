import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib as plt
#Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
df=sns.load_dataset("titanic")
df.head()
#Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
df["sex"].value_counts()
#Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
df.nunique()
#Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.
df["pclass"].nunique()
df.pclass.unique()
#Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
df[["pclass","parch"]].nunique()
#Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz
df["embarked"].dtype
df.info()
df["embarked"].astype("category")
#Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
df[df["embarked"]=="C"].head()
#Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
df[df["embarked"] !="S"].head()
#Görev9: Yaşı 30dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
df[(df["age"]<30) & (df["sex"]== "male") ].head()
#Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
df[(df["fare"]>500) | (df["age"] > 70)].head()


#Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
df.isnull().sum()
#Görev 12: who değişkenini dataframe’den çıkarınız.
df.drop("who",axis=1,inplace=True)
#Görev 13: deck değişkenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
df["deck"].fiilna(df["deck"].mode()[0],inplace=True)
#Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
df["age"] = df["age"].fillna(df["age"].median())
#Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
df.groupby(["pclass","sex"]).agg({"survived":["sum","count","mean"]})
#Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
df["age_flag"]=df["age"].apply(lambda x: 1 if x < 30 else 0)
#Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
dff=sns.load_dataset("tips")
#Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz
dff.groupby("time").agg({"total_bill":["sum","min","max","mean"]})
#Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
dff.groupby(["day","time"]).agg({"total_bill":["sum","min","max","mean"]})
#Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
dff.loc[(dff["size"] < 3) & (dff["total_bill"] > 10), "total_bill"].mean()
#Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
dff["total_bill_tip_sum"] =dff["tip"] + dff["total_bill"]