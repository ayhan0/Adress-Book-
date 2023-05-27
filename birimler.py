class BIRIMLER:
    def birimGirisFormu(self,bilgi={}):
        self.alt.append('<br><fieldset><legend><b>Birim Girişi </b></legend>')
        gonderme = ('birim_ekle','Birimi Guncelle')
        self.alt.append('input_type="text,name ="birim_adi" value ="%s" size="40">'%
                        bilgi.get('birim_adi',''))
        self.alt.append('<input type ="submit" name ="{0}"value="{1}">'.format(*gonderme))
        self.alt.append('</fieldset><br>')
    def birimler(self):
        self.formAction = '/birimler'
        birim = {}
        if self.form.get('birim_ekle'):
            if self.form.get('birim_adi'):
                self.baglanti.execute(
                    'INSERT INTO birimler (birim_adi) VALUES("%s")'%
                    self.form.get('birim_adi')
                )
            else:
                self.hata.append('Birim adı yazmadınız')
        if self.form.get('birim_guncelle'):
            self.baglanti.execute(
                'UPDATE birimler SET birim_adi = "%s" WHERE birim_no=%s'%
                self.form.get('birim_sil')
            )
        sdb= self.baglanti.execute('SELECT *FROM birimler')
        birimListesi=sdb.fetchall()
        if birimListesi:
            rc=1
            self.alt.append('<fieldset><legend>Birimler</legend>')
            self.alt.append('<table>')
            self.alt.append('<tr bgcolor ="#669999"><th>Birim</th><th>Sil</th></tr>')
            for b in birimListesi:
                self.alt.append(''' <tr bg color ="{0}">
                <td>a=href ="?birim_duzenle="{1}">{2}</td><td>
                <a href =?"birim_sil = {1}">Sil</a>'''.format(self.renkler[rc],*b))
                rc =not rc
            self.alt.append('</table>')
            self.alt.append('</fieldset>')
        self.birimGirisFormu(birim)
        self.alt.append('<br><a href = "%s">Ana Pencere </a>'%self.betik)