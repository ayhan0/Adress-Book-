import cgi,cgitb,os,time,sqlite3
from http import cookies
cgitb.enable()

from onayla import ONAYLA
from birimler import BIRIMLER
from kisiler import KISILER

class REHBER(ONAYLA,BIRIMLER,KISILER):
    def __init__(self):
        self.form = cgi.FieldStorage(encoding='cp1254')
        self.form.get = self.form.getvalue()
        self.betik.os.environ['SCRİPT_NAME']
        self.ust = []
        self.alt = []
        self.hata = []
        self.formAction = ''
        self.renkler = ['#DCDCDC', '#FFFFFF']
        # first all users is unapproved
        self.onayli = False
        # checking the cookies
        self.cerezler = cookies.SimpleCookie()
        try:self.cerezler.load(os.environ["HTTP_COOKIE"])
        except: pass

        # all the info we got from the user should transferring with form
        # and use path for it
        self.path = os.environ['PATH_INFO'].split('/')

        #connection for database
        self.baglanti = sqlite3.connect('d:/programlarım/adresdefteri.db')
        self.baglanti.row_factory=sqlite3.Row
        #check if user approved or not
        self.onayla()
        # if path is smaller than 4 lets search for the person
        if len(self.path)<4:self.kisiara()
        if self.onayli:
            if len(self.path)>3:
                # path is bigger than third and third object equals birimler we should go to that object
                if self.path[3] == 'birimler':
                    self.birimler()
                else:
                    self.kisiler()
        #now we gonna make html
        # lets print our cookies first
        if self.cerezler:print(self.cerezler)
        #now header
        print('Content-Type: text/html; charset= windows-1254\n')
        #lets make html content
        print(''' <html><head>
              <title>Telefon Rehberi</title>
              <link rel = stylesheet href = "/rehber.css" type = "text/css">
              </head>
              <body> <form METHOD ="POST" ACTION = "%s%s">
              ''' % (os.environ['SCRİPT_NAME'],self.formAction))
        # if an error occured lets print on  red color
        if self.hata:
            print('<br><font_color = "red"<b> İşleminiz yapılırken hata oluştu":</b><br>'),
            #now print the datas
        print('''<table><tr><td bgcolor = "669999" class = "nobrtd">%s</td></tr><tr><td> class = "nobrtd">%s</td></tr> '''%(
            '/n'.join(self.ust),'/n'.join(self.alt)))
        print('<form></body></html>')
        #extract infos to database and close
        self.baglanti.commit()
        self.baglanti.close()

        self.kisiGirisFormu()
        self.alt.append(''' <br><a href = "%s/birimler">)
        Birim eklemek için tıklayın</a> ''' %
                        os.environ['SCRIPT_NAME'])

        REHBER()
