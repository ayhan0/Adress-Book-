class KISILER:
    def kisiler(self):
        #if form kisi_ekle is exist we add that person
        #when we came here user is approved there is no need for further check
        if self.form.get('kisi_ekle'):
            self.baglanti.execute(''' INSERT INTO kisiler(unvani,adi,soyad,calistigi_birim,telefonu)
            VALUES("%s","%s","%s","%s","%s")'''%(
                self.form.get('unvani'),
                self.form.get('adi'),
                self.form.get('soyadi'),
                self.form.get('calistigi_birim'),
                self.form.get('telefonu')))
        if self.form.get('kisi_sil'):
            self.baglanti.execute('DELETE FROM kisiler WHERE kisi_no = %s' %
                                  self.form.get('kisi_sil'))
            self.kisiGirisFormu()
            self.alt.append('<br><a = href ="%s/birimler">Birim eklemek için tıklayın</a'%
                            self.betik)
    def aramaformu(self):
        #searching form for all users from contacts
        self.alt.append('<br>fieldset><legend><b>Rehberde Arama</b></legend>')
        self.alt.append('<br> Aradığınız kişi: <input type = "text"name="kisi_adi">')
        self.alt.append('input type ="submit" name = "kisi_ara" value ="Ara>')
        self.alt.append('</fieldset><br>')
    def kisiara(self):
        self.aramaformu()
        if self.form.get('kisi_ara'):

            #if form values kisi ara exist we gonna find the values in database
            kisiadi= self.form.get('kisi_adi','')
            #lets remove the space front of the searching word
            kisiadi = kisiadi.strip()
            #we need to remove ; in sql query cause it might  trigger to run affect multiple queries
            kisiadi = kisiadi.replace(';','')
            silLink =''
            silBaslik =''
            if self.onayli :silBaslik='<th>Sil</th>'
            #we need restrict user for at least 3 words in the search section because we can get all the record by simply
            #searcing for a
            if len(kisiadi) <3:
                self.hata.append('Aranacak kelime 3 harften az olmalı')
            else:
                self.baglanti.row_factory = None
                #we search for the word that user searching
                sdb = self.baglanti.execute(
                    ''' SELECT k.*,b.birim_adi
                    FROM kisiler k, birimler b 
                    WHERE k.calistigi_birim = b.birim_no
                    AND (k.adi LIKE "%{0}%"
                    OR k.soyadi LIKE "%{0}%")'''.format(kisiadi)
                )
                kisiler=sdb.fetchall()
                if kisiler:
                    #lets list the contact as a table
                    rc = 1
                    self.alt.append('<fieldset><legend>Arama sonuçları </legend>')
                    self.alt.append('<table>')
                    self.alt.append('''<tr bgcolor = "669999"><th><Ünvanı </th>
                    <th>Adı</th><th>Soyadı</th><th>
                    Calıştığı Birim </th>
                    <th>Telefonu<th>%s</tr>'''%silBaslik)
            for k in kisiler:
                if self.onayli:
                    #searching user is approved lets provide the link that deleting for searching record:
                    silLink = '<td><a href = "%s?kisi_sil=%d>Sil</a></td>'%(
                        self.betik,k[0])
                    #lets write the record as a row
                    self.alt.append('''<tr bgcolor = {0}><td>{2}</td><td><td>{3}</td>
                    <td>{4}</td><td>{7}</td>
                    <td>{6}%s</td></tr>'''.format(self.renkler[rc],*k)%silLink)
                    rc = not rc
                    self.alt.append('</table>')
                    self.alt.append('</fieldset><br>')
    def kisiGirisFormu(self,bilgi= {}):
        #pre condition  query result is dictionary so lets make it list
        self.baglanti.row_factory= None
        #connect to database for sublist
        sdb = self.baglanti.execute('SELECT * FROM birimler')
        birimler = sdb.fetchall()
        gonderme = ('kisi_ekle','Kişi Ekle')
        self.alt.append('<fiedlset><legend><b>Rehbere Veri Girişi </b></legend>')
        self.alt.append('<br>Ünvanı: ')
        self.alt.append(('unvanı',
                        (('',''),
                         ('Arş.Gör','Arş.Gör'),
                         ('Dr.','Dr.'),
                         ('Yrd. Doç. Dr.,Yrd. Doç. Dr.'),
                         ('Doç. Dr.,Doç. Dr.'),
                         ('Prof. Dr.,Prof. Dr.'))
                        ).__str__())
        self.alt.append('<br>Adı:<input type = "text" name= "adi" value= "%s">'%
                        bilgi.get('adi',''))
        self.alt.append('<br>Soyadı:<input type = "text" name= "soyadi" value= "%s">' %
                        bilgi.get('soyadi', ''))
        self.alt.append('<br>Birimi:')
        #we get the data do database lets convert into checkbox
        self.alt.append('calistigi_birim',birimler).__str__()
        self.alt.append('<br>Telefonu:<input type ="text"name="telefonu" value="%s">'%
                        bilgi.get('soyadi',''))
        #lets create send button and value label values
        self.alt.append('''<br><center>
        <input type = "submit" name = "{0}"value ={1}">
        </center>'''.format(*gonderme))
        self.alt.append('</fieldset><br>')
    def kisiler(self):
        if self.form.get('kisi_ekle'):
            self.baglanti.execute('''INSERT INTO kisiler
            (unvani,adi,soyad,calistigi_birim,telefonu)
            VALUES("%s","%s","%s","%s","%s")'''%(
                self.form.get('unvani'),
                self.form.get('adi'),
                self.form.get('soyadi'),
                self.form.get('calistigi_birim'),
                self.form.get('telefonu')))
        if self.form.get('kisi_sil'):
            self.baglanti.execute('DELETE FROM kisiler WHERE kisi_no=%s'%
                                  self.form.get('kisi_sil'))
        self.kisiGirisFormu()
        #if user approved user will be do adding and deleting we need the show the form to user that he can do such operations
        self.alt.append('''<br><a href= "%s/birimler">
        Birim eklemek için tıklayın </a>'''%
                        self.betik)






                    



