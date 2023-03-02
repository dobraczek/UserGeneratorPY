import json
import csv
import random
import unicodedata
import datetime
import glob

class VirtualUser:

    def __init__(self, sex = 1, minage = 18, maxage = 90) -> None:
        self.sex = sex
        self.minage = minage
        self.maxage = maxage
        self.username = ''

    def UserName(self):
        """Generovani jmena"""
        data2 = []
        file = open("name.json", "r", encoding="utf8")
        data = json.load(file)

        for i in data:
            if int(i['sex']) == self.sex:
                data2.append(i)

        count = len(data2)
        number = random.randint(0, (count-1))

        file.close()
        return data2[number]
    
    def UserSurname(self):
        """Generovani prijmeni"""
        data2 = []
        file = open("surname.json", "r", encoding="utf8")
        data = json.load(file)

        for i in data:
            if int(i['sex']) == self.sex:
                data2.append(i)

        count = len(data2)
        number = random.randint(0, (count-1))

        file.close()
        return data2[number]
    
    def UserNickname(self):
        """Generovani uživatelského jména"""
        file = open("nickname.json", "r", encoding="utf8")
        data = json.load(file)

        count = len(data)
        number = random.randint(0, (count-1))

        file.close()
        return data[number]
    
    def UserAddress(self):
        """Generování náhodné adresy"""
        files = glob.glob("./Ruian/*")
        count = len(files)
        number = random.randint(0, (count-1))
        filePath = files[number].replace("\\", "/")

        file = open(filePath, "r")
        data = list(csv.reader(file, delimiter=","))

        count = len(data)
        number = random.randint(1, (count-1))
        lineCsv = data[number][0]

        file.close()
        return lineCsv.split(";")

    
    def UserSex(self):
        """Vypsaní pohlaví v českém jazyce"""
        if self.sex == 1:
            return 'muž'
        else:
            return 'žena'
        
    def remove_accents(self, input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])
        
    def UserUsername(self, uname = ""):
        """Vypsání uživatelského jména"""
        name = self.remove_accents(input_str = uname)
        number = random.randint(0, 5)
        list = ["_", ".", "", "-"]

        if number == 4:
            return name.casefold()
        elif number == 5:
            return name.upper() + str(random.randint(10, 99))
        else:
            return  name + list[number] + str(random.randint(10, 99))
        
    def UserEmail(self, uname, sname):
        """Vypsání emailu"""
        domain = ['@zin.eu', '@czin.cz', '@czin.sk', '@tiscali.cz', '@wo.cz', '@worldonline.cz', '@atlas.cz', '@kamarad.cz', '@mujmejl.cz', '@mujweb.cz', '@podvodnik.cz',
                  '@senior.cz', '@centrum.cz', '@e-mail.cz', '@katedrala.cz', '@eposta.cz', '@e-posta.cz', '@bigboss.cz', '@dablik.cz', '@dobrafirma.cz', '@potvurka.cz', 
                  '@soukromy.cz', '@tajny.cz', '@uletak.cz', '@uletacka.cz', '@sexygirl.cz', '@studentka.cz', '@quick.cz', '@seznam.cz', '@post.cz', '@email.cz', 
                  '@volny.cz', '@vol.cz', '@klikni.cz', '@gmail.com', '@hotmail.cz']
        count = len(domain)
        ndomain = random.randint(0, (count-1))
        number = random.randint(1, 5)

        if number == 1:
            return (self.remove_accents(input_str = uname.casefold()) + domain[ndomain])
        elif number == 2:
            return (self.remove_accents(input_str = uname.casefold()) + str(random.randint(10, 99)) + domain[ndomain])
        elif number == 3:
            return (self.remove_accents(input_str = uname.casefold()) + "." + self.remove_accents(input_str = sname) + domain[ndomain])
        elif number == 4:
            return (self.remove_accents(input_str = sname.casefold()) + str(random.randint(10, 99)) + domain[ndomain])
        elif number == 5:
            return (self.remove_accents(input_str = sname[0].upper()) + self.remove_accents(input_str = sname) + domain[ndomain])
        else:
            return (self.remove_accents(input_str = uname.casefold()) + domain[ndomain])
        
    def UserPhone(self):
        """Vypsání telefonu"""
        phone = ['601', '602', '606', '607', '702', '720', '721', '722', '723', '724', '725', '726', '727', '728', '729',
	        '603', '604', '605', '730', '731', '732', '733', '734', '735', '736', '737', '738', '739',
	        '608', '770', '771', '772', '773', '774', '775', '776', '777', '778']
        count = len(phone)
        number = random.randint(0, (count-1))
        return phone[number] + str(random.randint(100000, 999999))

    def birthday(self):
        """Vypsání data narozeni a narozenin"""
        age = random.randint(int(self.minage), int(self.maxage))
        today = datetime.date.today()
        year = int(today.year)-age
        year = year
        day = random.randint(1, 28)
        moon = random.randint(1, 12)

        if (today.strftime("%m") == moon and today.strftime("%d") > day) and today.strftime("%m") > moon:
            age = age-1

        fulldate1 = str(day) + "." + str(moon) + "." + str(year)

        if day < 10:
            day = '0' + str(day)

        if moon < 10:
            moon = '0' + str(moon)

        fulldate2 = str(year) + "-" + str(moon) + "-" + str(day)

        birthday = {}
        birthday['age'] = str(age)
        birthday['date'] = fulldate1
        birthday['date2'] = fulldate2
    
        return birthday

    def UserPassword(self):
        char_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[\]^_`{|}~"
        passlength = random.randint(5, 18)
        password = ''

        for len in range(passlength):
            random_char = random.choice(char_seq)
            password += random_char
        
        list_pass = list(password)
        random.shuffle(list_pass)
        final_password = ''.join(list_pass)
        return final_password

    
    def DataPrint(self):
        """Výpis virtuálních uživatelských dat"""
        name = self.UserName()
        surname = self.UserSurname()
        nick = self.UserNickname()
        birthday = self.birthday()
        address = self.UserAddress()

        if address[10] == "":
            street = address[2]
        else:
            street = address[10]

        user = {}
        user['sex'] = self.UserSex()
        user['sex2'] = self.sex
        user['name'] = name['name']
        user['surname'] = surname['surname']
        user['nickname'] = nick['nick']
        user['username'] = self.UserUsername(uname = name['name'])
        user['password'] = self.UserPassword()
        user['email'] = self.UserEmail(uname = name['name'], sname = surname['surname'])
        user['phone'] = self.UserPhone()
        user['nameday'] = name['nameday']
        user['birthdate'] = birthday['date']
        user['birthdate2'] = birthday['date2']
        user['age'] = birthday['age']
        user['street'] = street
        user['street_num'] = address[12]
        user['city'] = address[2]
        user['zip'] = address[15]
        
        return user