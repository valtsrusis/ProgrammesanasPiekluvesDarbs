#importē tkinter bibliotēku, kas ir python grafiskais lietotāja saskarne.
import tkinter as tk
from tkinter import messagebox
from tkinter import *
#importē citus python failus, lai globāli izmanto citas funkcijas no atsevišķiem failiem.
import test_datubaze
import test_map
import test_veikals
#importē sq_lite3 bibliotēku, kas nodrošina vieglu diska datubāzi, kurai nav nepieciešams atsevišķs servera process.
import sqlite3
#importē hashlib bibliotēku, kas ģenerē jaucējkodas, ziņojumu īssavilkums un aizsargā lietotāja datus.
import hashlib
#importē ctypes bibliotēku, kas nodrošina ar saderīgus datu tipus.
import ctypes

#savienota un izveidota datubāzes fails ar sastītu tabulu
connection = sqlite3.connect('login.db')
c = connection.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS login_information  (
            id integer PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
    )""")

#apstiprina datubāzes visus neapstiprinātos darījumus.
connection.commit()    

#izveido grafisko saskarni jeb logu no tkinter bibliotēka un to nosaukumu.
root = tk.Tk()
root.title("Ventspils Starptautiska elektronika")

#gara līnīju komanda, lai samainītu uzdevumjoslas ikonu uz izvēlēto ikonas bildi izmantojot ctypes importētu bibliotēku.
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
root.iconbitmap('Designer.ico')

#maina logas izmēru
root.geometry("900x400")

#ievada maināmo izmēra funkciju uz 'False', lai lietotājs nespēj mainīt programmatūras izmēru.
root.resizable(False, False)

#logas virsraksts
greeting = tk.Label(root, text="Laipni lūdzam Ventspils Starptautiskajā elektronikas veikalā!",
                    fg='blue', font=('Aerial', 20, 'bold'))
greeting.pack()

#ievieto teksta logrīku Label
username = tk.Label(root, text="Lietotājvārds: ", font=('Times New Roman', 13))
username.place(x=310, y=100)
password = tk.Label(root, text="Parole: ", font=('Times New Roman', 13))
password.place(x=330, y=150)

#ievieto ievades logrīku Entry.
username_entry = Entry(root, bd=2, relief="ridge")
username_entry.place(x=410, y=100)
password_entry = Entry(root, bd=2, relief="ridge", show='*')
password_entry.place(x=410, y=150)

#ievieto poga logrīku Button ar pievienotu funkciju vai metodi, kas jāizsauc, noklikšķinot uz pogas.
contact_button = Button(text="Kontakti", height=2, width=20, bd=3, relief="groove",
                        command=lambda:contactProcess())
contact_button.place(x=700, y=330)

#ievieto poga logrīku Button ar pievienotu funkciju vai metodi, kas jāizsauc, noklikšķinot uz pogas.
registration_button = Button(text="Piereģistrēties", height=3, width=20, bd=6, relief="raised",
                            command=lambda:registrationProcess())
registration_button.place(x=280, y=200)

#ievieto poga logrīku Button ar pievienotu funkciju vai metodi, kas jāizsauc, noklikšķinot uz pogas.
login_button = Button(text="Ielogoties", height=3, width=20, bd=6, relief="raised",
                    command=lambda:loginProcess())
login_button.place(x=460, y=200)

#ievieto poga logrīku Button ar pievienotu funkciju vai metodi, kas jāizsauc, noklikšķinot uz pogas.
guest_button = Button(text="Viesu režīms", height=3, width=20,
                    command=lambda:guestProcess())
guest_button.place(x=375, y=280)

#metodes funckija ar ko izsauc pogā Viesu režīms - iemet lietotāju jaunā programmatūras logā pēc ziņojuma kastes.
def guestProcess():
    messagebox.showinfo("Laipni lūdzam", "Vari tagad apskatīt preces!")
    #funkcija, kas aizver logu ciet.
    root.destroy()
    #izsauc funkciju no cita python faila.
    test_veikals.new_tab()

#metodes funckija ar ko izsauc pogā Piereģistrēties - atgriež lietotāja ievadīto lietotājvārdu un paroli kā arī izsauc iekšējo funkciju.
def registrationProcess():
    username = username_entry.get()
    password = password_entry.get()
    register_user(username, password)

#metodes funckija ar ko izsauc pogā Ielogoties - atgriež lietotāja ievadīto lietotājvārdu un paroli kā arī izsauc iekšējo funkciju.
def loginProcess():
    username = username_entry.get()
    password = password_entry.get()
    login_user(username, password)

#definē jaucējkodu no lietotāja ievadīto paroli un atgriež ģenerēto jaucējkoda rindu ar ko aizsargā lietotāja datus no datubāzes saglabāšanā.
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#izsaucāma funkcija logošanās, kas pārbauda lietotāja ievadīto lietotājvārdu un paroli datubāzē.
def login_user(username, password):
    hashed_password = hash_password(password)
    c.execute("SELECT * FROM login_information WHERE username = ? AND password = ?",
              (username, hashed_password))
    user = c.fetchone()
    #uzbūvēta 'if-else' paziņojums, lai izpildītu gan konkrētā nosacījuma patieso, gan nepatieso daļu. 
    #ja lietotāja ievadītie dati sakrīt no datubāze saglabātā, tad lietotājs tiek iemests internetveikala logu no izsauktā funkcijas no cita python faila.
    if user:
        test_datubaze.show_all()
        messagebox.showinfo("Veiksme", "Veiksmīga logošana!")
        #funkcija, kas aizver logu ciet.
        root.destroy()
        test_veikals.new_tab()

        #izsauc funkciju no cita python faila konkrēti pēc logošanas pogas nosacījuma.
        test_veikals.logoff_tab()
    #ja lietotāja ievadītie dati nesakrīt no datubāze saglabātā, tad parādās kļudu paziņojuma kaste, lai pārbauda ievadīto lietotājvārdu vai paroli.
    else:
        messagebox.showerror("Kļūda", "Nepareizi ievadīta lietotājvārds vai parole!")

#izsaucāma funkcija reģistrēšanā, kas saglabā lietotāja lietotājvārdu un jaucējkoda ģenerētu rindas paroli datubāzē.
def register_user(username, password):
    try:
        hashed_password = hash_password(password)
        c.execute("INSERT INTO login_information (username, password) VALUES (?,?)",
              (username, hashed_password))
        connection.commit()
        messagebox.showinfo("Veiksme", "Veiksmīga reģistrācija!")
    #ja lietotāja ievadītie dati jau sakrīt no datubāzes saglabātā, tad nevis pārraksta lietotāja ievadīto datubāzē, bet parādās kļudu paziņojuma kaste, ka šis lietotājvārds ir jau izmantots.
    except sqlite3.IntegrityError:
        messagebox.showerror("Kļūda", "Šis lietotājvārds ir jau izmantots!") 

#definē funckiju ar ko izsauc pogā Kontakti - iemet lietotāju jaunā logā, kas attēlo īpašnieka telefona numurs (Label).
def contactProcess():
    #izveido grafisko saskarni jeb logu no tkinter bibliotēka un to nosaukumu.
    top = tk.Toplevel()

    #maina logas izmēru.
    top.geometry("900x600")

    #ievada maināmo izmēra funkciju uz 'False', lai lietotājs nespēj mainīt programmatūras izmēru.
    top.resizable(False, False)
    top.title("Ventspils Starptautiska elektronika")

    #gara līnīju komanda, lai samainītu uzdevumjoslas ikonu uz izvēlēto ikonas bildi izmantojot ctypes importētu bibliotēku.
    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    top.iconbitmap('Designer.ico')

    #ievieto poga logrīku Button ar ko funkcija aizver logu ciet.
    topButton = Button(top, text="CLOSE", command = top.destroy)
    topButton.pack()
    author = tk.Label(top, text="Telefona numurs 📞: +371 20093842")
    author.pack()
    
    #izsauc funkciju no cita python faila.
    test_map.maps_function()

#funkcija, kas ir bezgalīga cilpa, ko izmanto, lai palaistu programmu, gaidītu, līdz notiks notikums, un apstrādātu notikumu, kamēr logs nav aizvērts.
tk.mainloop()