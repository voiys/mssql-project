import random, datetime

#randomiseam igraca: ime, prezime, teamId, jerseyNumber, dateOfBirth, bestScorer

def getRandomDate(random_year_min, random_year_max):
    random_year = random.randint(random_year_min, random_year_max)
    random_month = random.randint(1, 12)
    random_day = 0
    
    if random_year % 4 == 0: #ako je godina prijestupna
        if random_month == 2:
            random_day = random.randint(1, 29)
        elif random_month in [4, 6, 9, 11]:
            random_day = random.randint(1, 30)
        else:
            random_day = random.randint(1,31)
    else: #ako nije prijestupna
        if random_month == 2:
            random_day = random.randint(1, 28)
        elif random_month in [4, 6, 9, 11]:
            random_day = random.randint(1, 30)
        else:
            random_day = random.randint(1,31)
    
    datum = datetime.datetime(random_year, random_month, random_day) #stvaranje datuma
    
    return datum.date()

def getRandomDateOfBirth():
    random_year = random.randint(1975, 2000)
    random_month = random.randint(1, 12)
    random_day = 0
    
    if random_year % 4 == 0: #ako je godina prijestupna
        if random_month == 2:
            random_day = random.randint(1, 29)
        elif random_month in [4, 6, 9, 11]:
            random_day = random.randint(1, 30)
        else:
            random_day = random.randint(1,31)
    else: #ako nije prijestupna
        if random_month == 2:
            random_day = random.randint(1, 28)
        elif random_month in [4, 6, 9, 11]:
            random_day = random.randint(1, 30)
        else:
            random_day = random.randint(1,31)
    
    datum = datetime.datetime(random_year, random_month, random_day) #stvaranje datuma
    
    return datum.date()

def getRandomPlayer(numberOfPlayers):
    #otvoreni fileovi
    ime = open('ime.txt', mode='r', encoding='utf-8')
    prezime = open('prezime.txt', mode='r', encoding='utf-8')

    #procitani fileovi i podjeljeni u liste
    ime_lista = ime.read().split('\n')
    prezime_lista = prezime.read().split('\n')

    #mice brojeve, razmake i prazne linije
    for item in ime_lista:
        if item == '' or item.isdecimal() == True or item == ' ':
            ime_lista.remove(item)
            
    for item in prezime_lista:
        if item == '' or item.isdecimal() == True or item == ' ':
            prezime_lista.remove(item)

    # counter
    i = 0
    
    while i < numberOfPlayers:
        #generiranje random brojeva
        random_number_ime = random.randrange(0, len(ime_lista))
        random_number_prezime = random.randrange(0, len(prezime_lista))
        random_number_team_id = random.randint(1, 30)
        random_number_broj_dresa = random.randint(0, 99)
        random_number_datum_rodenja = str(getRandomDateOfBirth())
        

        yield str(ime_lista[random_number_ime] + ' ' + prezime_lista[random_number_prezime]), random_number_team_id, random_number_broj_dresa, random_number_datum_rodenja
        
        #za kraj povecava se counter za 1
        i += 1

def getRandomRetiredPlayer(numberOfPlayers):
    #otvoreni fileovi
    ime = open('ime.txt', mode='r', encoding='utf-8')
    prezime = open('prezime.txt', mode='r', encoding='utf-8')

    #procitani fileovi i podjeljeni u liste
    ime_lista = ime.read().split('\n')
    prezime_lista = prezime.read().split('\n')

    #mice brojeve, razmake i prazne linije
    for item in ime_lista:
        if item == '' or item.isdecimal() == True or item == ' ':
            ime_lista.remove(item)
            
    for item in prezime_lista:
        if item == '' or item.isdecimal() == True or item == ' ':
            prezime_lista.remove(item)

    # counter
    i = 0
    
    while i < numberOfPlayers:
        #generiranje random brojeva
        random_number_ime = random.randrange(0, len(ime_lista))
        random_number_prezime = random.randrange(0, len(prezime_lista))
        random_number_team_id = random.randint(1, 30)
        random_number_broj_dresa = random.randint(0, 99)
        random_number_datum_rodenja = str(getRandomDate(1965, 1975))
        

        yield str(ime_lista[random_number_ime] + ' ' + prezime_lista[random_number_prezime]), random_number_team_id, random_number_broj_dresa, random_number_datum_rodenja
        
        #za kraj povecava se counter za 1
        i += 1


def getRandomMatch(numberOfMatches):
    """
    Stvara random Match i scoreve i yielda njihove vrijednosti kako bi ih mogao insertat
    """

    #counter
    i = 0

    while i < numberOfMatches:
        random_number_team_home = random.randint(1, 30)
        random_number_team_away = random.randint(1, 30)

        yield random_number_team_home, random_number_team_away,random.randint(0, 1), str(getRandomDate(1975, 2019))

        #za kraj povecava se counter za 1
        i += 1
