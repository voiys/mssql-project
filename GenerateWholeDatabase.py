import pyodbc, Generator


#spajanje se na bazu preko connectionString-a
server = 'localhost'
database = 'dbKosarka1'
username = 'sa' #korisnicko ime promjeniti na admina vlastitog servera
password = '41ALgrHM' #lozinka
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password) #ODBC Driver 17 for SQL Server ovo je krucijalan dio, bez drivera ne radi (ako nemate verziju sql server 2017 pronađite odgovarajući driver)

#postavljanje svog encoding/decoding-a u utf-8
cnxn.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
cnxn.setencoding(encoding='utf-8')

#stvaranje cursora
cursor = cnxn.cursor()

#n = broj ponavljanja unosa itema
n = 100 # <---- za mijenjanje broja unosa promijenite n, ili na mjestima gdje se nalazi n unesite vrijednost

#query
#retired igraci
for item in Generator.getRandomRetiredPlayer(n):
    cursor.execute("EXEC RetiredPlayer_Insert ?, ?, ?, ?", item[0], item[1], item[2], item[3])
    cnxn.commit()

#igraci
for item in Generator.getRandomPlayer(n):
    cursor.execute("EXEC Player_Insert ?, ?, ?, ?", item[0], item[1], item[2], item[3])
    cnxn.commit()

#matchevi i scorevi
for item in Generator.getRandomMatch(n):
    cursor.execute("EXEC Match_Insert ?, ?, ?, ?", item[0], item[1], item[2], item[3])
    cnxn.commit()