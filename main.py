import sqlite3

connection = sqlite3.connect('d:/programlarım/adresdefteri.db')
"""""
connection.execute(''' CREATE TABLE birimler (birim_no integer primary key, birim_adi varchar(50))''')
connection.execute(''' CREATE TABLE kisiler ( kisi_no integer primary key,unvanı varchar(20),adi varchar(50),soyadi varchar(50),
calistigi_birim integer, telefonu varchar(20) , foreign key (calistigi_birim) references birimler(birim_no))''')
connection.execute('''CREATE TABLE kullanicilar(kullanici_no integer primary key, kullanici_adi varchar(20), 
kullanici_parolasi varchar(32),kullanici_oturumu varchar(32) default null )''')
connection.commit()
"""""
import hashlib
password = hashlib.md5('adana01'.encode()).hexdigest()
#print(password)

connection.execute(''' INSERT INTO kullanicilar (kullanici_adi , kullanici_parolasi ) VALUES ("%s" ,  "%s")''' %('*****',*****))
connection.commit()

