import numpy as np


#NUMPY ARRAY

#matrix yapar

benimlist=[20,30,40]
matrixlist=[[10,20,30],[20,30,40],[30,40,50]]
asd=np.array(matrixlist)


#ARANGE

#np.arange(0,10,2) 0 dan 10 a kadar 2şerli array oluşturur

#range 0 dan başlayarak sayıları o sayıya kadar sıralatır

a=list(range(0,10))#===[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b=np.arange(0,10,2)#===([0,2,4,6,8])



#ZEROS,ONES

#np.zeros(1) 1 tane 0 lı array oluşturur

#np.zeros(2,2) 2 ye 2 lik  0lı  array oluşturur

#BU İŞLEMLERİ ZEROS YERİNE ONES YAZARAKTA YAPABİLİRSİNİZ

a=np.zeros((2,2))#==([0. 0.]
#                    [0. 0.])


#LİNSPACE

#np.linspace(0,15,3) sıfır ile 15 arasında 3 sayı verir

a=np.linspace(10,30,3)#===[10. 20. 30.]


#RANDOM

#np.random.randn(2,2) 2ye 2 lik rastgele float değer verir
a=np.random.randn(2,2)#===[-1.20067082  0.60464572]
                        # [-0.82746699 -0.63959128]

#np.random.randint(10,100,3) 10 ile 100 arası 3 tane int verir

a=np.random.randint(10,100,9)#===(11,33,44)

#RESHAPE

#reshape(3,3) eğer 9 karakter varsa 3 e elük bir array verir

a=a.reshape(3,3)#==[[81 82 57]
#                   [74 29 93]
#                   [23 12 50]]



#SHAPE


#.shape dizinin index ve kolon sayısını veriri


a.shape#===(3,3)


#.MAX()


#dizedeki en büyük sayıyı verir


#.MİN()


#dizideki en küçük sayıyı veriri


#.ARGMAX()


#dizedeki en büyük sayının index ve kolonunu gösterir



#.ARGMin()


#dizedeki en küçük sayının index ve kolonunu gösterir



#[3:8]


#a[3:8] a daki 3 ile 8 arasındaki indexleri sıralatır ve değiştirmemizde büyük kolaylık sağlar


#[:]

#a[:] tüm dize ile işlem yapmamızı sağlar


#COPY


#.copy() diziyi kopyalamamızı ve diğer dizeye etki etttirtmeden çalışabilmemizi sağlar





a=np.array([[4, 7, 4, 5, 9],
            [2, 5, 0, 7, 7],
            [1, 9, 0, 8, 2]])



print(np.subtract(a, 2))
# 2 index e kadar . index dahil değil, indexlerdeki 3 colum una kadar 3 dahil değil

#BİR DİZENİN N.Cİ KUVVETİNİ ALDIRTMA 
#np.power(v, 3) 3.KUVVETİNİ ALDIRTIR
np.random.randint(10, size = (3,3,2))#3 elemanı 3 er listeden oluşan listelerinde 2 şer eleman bulunana liste oluşturtturur
