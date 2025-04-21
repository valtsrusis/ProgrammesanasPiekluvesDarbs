#importē sq_lite3 bibliotēku, kas nodrošina vieglu diska datubāzi, kurai nav nepieciešams atsevišķs servera process.
import sqlite3


#Definēta funkcija, kas pieprasa datubāzes failu un atgriež visus ierakstītus datus.
def show_all():
    connection = sqlite3.connect('login.db')

    c = connection.cursor()

    c.execute("SELECT * FROM login_information")
    items = c.fetchall()

    for item in items:
        print(item[0], item[1], item[2])
    
    connection.commit()

    connection.close()

#Definēta funkcija, kas pieprasa datubāzes failu un pievieno vienu jaunu ierakstu failā.
def add_one(id,username,password):
    connection = sqlite3.connect('login.db')
    c = connection.cursor()
    c.execute("INSERT INTO login_information VALUES (?,?)", (id,username,password))
    connection.commit()
    connection.close()

#Definēta funkcija, kas pieprasa datubāzes failu un izdzēš vienu ierakstu failā.
def delet_one(id):
    connection = sqlite3.connect('login.db')
    c = connection.cursor()
    c.execute("DELETE from login_information WHERE id = (?)", id)
    connection.commit()
    connection.close()


#Lai izveidotu stacionāru datubāzi, uz kuras var funkcionāli strādāt un parādīt tkinter tabulā,
#sākumā jāsavieno un jāizveido datubāzes fails un saraksts ar saviem datiem.
'''
connection = sqlite3.connect('products.db')
c = connection.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS electronic_products  (
            product_name TEXT,
            price REAL,
            currency TEXT
    )""")

data = [['Datoru pele', '50.99', '€'], ['Monitors', '100', '€'], ['Tastatūra', '59.99', '€'], ['Video karte', '340.99', '€'], ['Personālais dators', '1240.99', '€']]
'''
#Tad pievieno sarakstu ciklā un sarakstu pievieno datubāzes failā pa katram (VALUES).
'''
for record in data:
    c.execute("INSERT INTO electronic_products VALUES (:product_name, :price, :currency)", 
        {
        'product_name': record[0],
        'price': record[1],
        'currency': record[2]
        }      
              
        )

#apstiprina datubāzes visus neapstiprinātos darījumus.
connection.commit()
#aizver datubāzes savienojumu.
connection.close()
'''
#Tad izveido vaicājuma funkciju, ko datubāzes fails atgriež visus pieejami pievienotus datus, lai pārbaudītu datubāzes pārstāvēšanu.
'''
def query_database():
    connection = sqlite3.connect('products.db')
    c = connection.cursor()
    c.execute("SELECT * FROM electronic_products")
    # c.execute("SELECT rowid, * FROM electronic_products where product_name LIKE '%dato%'")
    records = c.fetchall()
    print(records)
    #apstiprina datubāzes visus neapstiprinātos darījumus.
    connection.commit()
    #aizver datubāzes savienojumu.
    connection.close()

#query_database()
'''

#Tiek izmantots 'with open' funkcija, kas atvēr failas bildi, izlasa (.read() funkcija) un atgriež (return) izlasīto bildi programmai.
def convert_image():
    filename = "pele_1.png"
    with open(filename, 'rb') as file:
        photo = file.read()
    return photo
