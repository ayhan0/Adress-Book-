import hashlib
import time
class ONAYLA:
    def onayla(self):
        # lets check user name and password are correct or not:
        if self.form.get('parola'):
            kullanici=self.form['kullanici'].value
            parola = self.form['parola'].value
            sdb =self.baglanti.execute = (''' SELECT kullanici_parolasi from kullanicilar 
            where  kullanici_adi = "%s"'''% kullanici)
            dbBilgi = sdb.fetchone()
            hash_parola =hashlib.md5(parola.encode()).hexdigest()
            if dbBilgi:
                if dbBilgi['kullanici_parolasi'] == hash_parola:
                       self.onayli = True
                       self.kullanici = kullanici
                       oturum = hashlib.md5(str(time.time()).encode().hexdigest())
                       self.baglanti.execute(''' UPDATE kullanicilar SET kullanici_oturumu = "%s" where kullanici_adi = "%s"'''%
                                  (oturum,kullanici))
                       self.cerezler['rehber_kullanici'] = self.kullanici
                       self.cerezler['rehber_oturum']= oturum

        elif self.cerezler.get('rehber_kullanici') and self.cerezler.get('rehber_oturumu'):
            kullanici = self.cerezler['rehber_kullanici'].value
            oturum = self.cerezler['rehber_oturumu'].value
            sdb = self.baglanti.execute('''SELECT kullanici_oturumu FROM kullanicilar WHERE kullanici_adi = "%s"''' % kullanici)
            dbBilgi = sdb.fetchone()
        if dbBilgi:
            if dbBilgi['kullanici_oturumu'] == oturum :
                #cookies are correct so lets make the user approve and self.onayli object true
                self.onayli= True
                self.kullanici = kullanici
            if self.onayli:
                self.ust.append('<b>%s</b> kullanici adi ile oturum açılmıştır'%self.kullanici)
                # if the use is approved in head we display user approved and write his name instead of entrance form
            else:
                self.ust.append('''<fieldset><legend><b>Lütfen giriş yapınız</b></legend>
                Kullanıcı Adı :<input type = "text" name _ "kullanici">
                Parola: <input type = "password" name = "parola">
                <input type ="submit" value ="Gönder"></field>''')

