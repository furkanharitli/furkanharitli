import numpy as np
import pandas as pd

#SERİLER

#seriler verileri çok daha iyi bir şekilde gösterir

benimsoz={"at":2,"mat":3,"fat":4}
a=pd.Series(benimsoz)



#DİZE BÖYLEDE OLUŞTURULA BİLİR


ben=[2,3,4]
son=["at","mat","fat"]
        #   data  /  indek
a=pd.Series(ben,son)

b=pd.Series(ben,son)


#a İLE b TOPLANIP BAŞKA BİR DİZEYE EŞİTLENEBİLİR


c=a+b#==at     2
       #mat    3
       #fat    4



#VERİ ÇERÇEVESİ

t=np.random.randn(4,3)

dataf=pd.DataFrame(t)
#dataframe serilerin 2 boyutlu halidir

#pd.Dataframe(s,index=[a,b,c,d],columns=fgh) index ve kolonu vererekten verileri güzelce gruplandırırsınız
K=pd.DataFrame(t,index=["a","b","c","d"],columns=["k","g","h"])#==    k         g         ha  
#                                                                a  0.292813 -0.640684  0.050652
#                                                                b -0.014675  0.122077  1.478138
#                                                                c -0.150563 -0.840513 -3.512761
#                                                                d  0.111510 -0.784703 -0.717240

#.LOC[b] ile indexi getirttiririz

#AXİS İLE İNDEX Mİ KOLON MU OLDUĞUNU BELİRTEBİLİRİZ
fa=K.drop("h",axis=1)#=h DÜŞÜRÜLDÜ

#İNPLACE == K.drop("h",axis=1,inplace),,,,,,yapılan işlem kalıcı hale gelir


#dataframe <0 SIFIRDAN KÜÇÜK OLUP OLMAMASINA GÖRE TRUE FALSE KOYULUR EĞER DF NİN İÇİNE KOYULURSA FALSELER DEĞER ALMAZ
S=K<0          #k         g
K[S]#==  a -0.131397 -1.333918
#        b       NaN       NaN
#        c       NaN -1.752423
#        d       NaN -0.379691


#İNDEX RESETLEME 

K.reset_index()#===                  index    k         g         h
#                                0     a  0.755004 -2.139376 -0.436215
#                                1     b  0.484921 -0.578394  0.247825
#                                2     c  0.799071  1.621482  1.465481
#                                3     d  0.980489  2.033719  0.126255
#index resetlendiğinde python yeni index olarak 0 dan başlar ve eski indexi colon adı index olan bir kolona verir
asd=["as","sa","ma","ka"]
K["yen"]=asd




#İNDEX DEĞİŞTİRME

#.set_index("yen") ile index değişebilir


K.set_index("yen")#                          k         g         h
#                                    yen
#                                    as   0.615576  0.242425 -1.605756
#                                    sa   1.278064  0.905630  0.135331
#                                    ma  -0.581830 -0.322832  1.498133
#                                    ka   1.521226 -0.784092  0.578950



#MULTİ İNDEX
ilkindexler=["kırık","kırık","kırık","harıt","harıt","harıt"]
icindex=["furo","ela","eda","seda","ali","efe"]

#iki liste oluşturuyoruz

birlesikind=list(zip(ilkindexler,icindex))

#listeleri birleştiriyoruz

birlesikindex=pd.MultiIndex.from_tuples(birlesikind)

#multi index yapıyoruz

yasnot=[[13,"A"],[10,"B"],[11,"C"],[12,"D"],[13,"E"],[9,"B"]]
yn=np.array(yasnot)

#veriyi dizi haline getiriyoruz

cizdat=pd.DataFrame(yn,index=birlesikindex,columns=("yas","mes"))

#hazır


#EKSİK VERİLERLE ÇALIŞMAK

das={"ist":[30,29,np.nan],"ank":[20,np.nan,25],"izm":[40,39,38]}
havd=pd.DataFrame(das)



#.DROPNA(axis=0 or 1)

        #boş verisi olan satırları yok eder

        #     .dropna(axis=1,thresh=2)
        
#.FİLLNA(10)
        
        #boş olanları 10 ile doldurur
        

#SINIFLANDIRMA

#.groupby() ile verileri kategorize ederek verideki bilgileri daha kolay analiz etmemize olanak sağlar

miii={"departman":["yaz","yaz","paz","paz","huk","huk"],
      "calisan ad":["eda","seda","ela","muv","wuj","fur"],
      "maas":[100,300,400,500,600,700]}
maasdata=pd.DataFrame(miii)
dasd=maasdata.groupby("departman")  
dasd.mean()#ortalama verir
dasd.count()#hangi departmanda kaç kişi çalışıyor
dasd.min()#kategoride en küçük sayıyı veriri
dasd.max()#kategoride en büyük sayıyı veriri
dasd.describe()#analiz edip önümüze koyar



#BİRLEŞTİRME
#KOLONLARI AYNI FAKAT  VERİLERİ FARKLI OLAN DİZİLERİ BİRLEŞTİRİR
sozluk={"isim":["sam","rem","ram","mem"],
        "spor":["koş","yüz","koş","basket"]
   ,    "kalori":[100,200,300,400]}
dataf1=pd.DataFrame(sozluk,index=[1,2,3,4])
sozluk1={"isim":["rat","roz","rex","mex"],
        "spor":["koş","yüz","koş","basket"]
   ,    "kalori":[200,200,20,100]}
dataf2=pd.DataFrame(sozluk1,index=[5,6,7,8])
sozluk2={"isim":["rat","roz","rex","mex"],
        "spor":["koş","yüz","koş","basket"]
   ,    "kalori":[200,200,20,100]}
dataf3=pd.DataFrame(sozluk2,index=[9,10,11,12])
asea=pd.concat([dataf1,dataf2,dataf3])
#PD.CONCAT()BİRLEŞTİRİR

#MERGE

#İKİ DATAFRAME Yİ ORTAK KOLONLAR SAYESİNDE BİRLEŞTİRME

#istanbul=pd.merge(merg,merge,on="isim")


sozluk4={"isim":["rat","roz","rex","mex"],
         "spor":["koş","yüz","koş","basket"]}
merg=pd.DataFrame(sozluk4)
sozluk5={"isim":["rat","roz","rex","mex"],
        "kalori":[10,20,30,40]}
merge=pd.DataFrame(sozluk5)
istanbul=pd.merge(merg,merge,on="isim")     #burda birleştiriliyor


istanbul["spor"].unique()#kolonda kullanılan değişkenleri getirir

istanbul["spor"].nunique()#kolonda kullanılan değişkenlerin sayısını verir

istanbul["spor"].value_counts()#değişkenlerin bulunma sayısı

#istanbul["spor"].apply()#def fonksiyonları uygulatır

istanbul.isnull()#bölmede veriolup olmadığını kontrol eder


#EXLELE VERİ YAZMAK ÇEKMEK


#pd.read_excel()ile  veri alınır
#.to_excel()ile veri yazılır
data=pd.read_excel("bisiklet_fiyatlari.xlsx")