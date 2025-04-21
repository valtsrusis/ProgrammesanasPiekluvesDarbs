#importē tkinter bibliotēku, kas ir python grafiskais lietotāja saskarne.
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
#importē sq_lite3 bibliotēku, kas nodrošina vieglu diska datubāzi, kurai nav nepieciešams atsevišķs servera process.
import sqlite3
#importē citus python failus, lai globāli izmanto citas funkcijas no atsevišķiem failiem.
import test_map
#importē ctypes bibliotēku, kas nodrošina ar saderīgus datu tipus.
import ctypes

#metodes funckija ar ko izsauc pogā Meklēt - atgriež lietotāja ievadīto informāciju.
def search_records():
    lookup_records = search_entry.get()

    #izveido funkcijas ciklu, kas izdzēš datus no tabula, lai nepārklājas ar jau pievienotiem datiem.
    for record in table.get_children():
        table.delete(record)

    #savieno datubāzes failu un atgriež pieejamos datus ar ko lietotājs ievadījis meklēšanas rīkā.
    connection = sqlite3.connect('products.db')
    c = connection.cursor()
    c.execute("SELECT * FROM electronic_products WHERE product_name LIKE ?", ('%' + lookup_records + '%',))
    records = c.fetchall()

    #kad funkcija atgriežas, python atbrīvo atmiņu, ko izmanto visi funkcijas mainīgie.
    global count

    #izveido mainīgo skaitli
    count = 0

    #izveido funkcijas ciklu, kas pievieno visus pieejamos datubāzes datus tabulā.
    for record in records:
        if count % 2 == 0:
            table.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
        else:
            table.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('oddrow',))
        count += 1
    
    #apstiprina datubāzes visus neapstiprinātos darījumus.
    connection.commit()
    #aizver datubāzes savienojumu.
    connection.close()

#izsaukta funkcija no iepriekšēja python faila.
def new_tab():
    #kad funkcija atgriežas, python atbrīvo atmiņu, ko izmanto visi funkcijas mainīgie.
    global search_entry, root, table
    #izveido grafisko saskarni jeb logu no tkinter bibliotēka un to nosaukumu.
    root = Tk()
    root.title("Ventspils Starptautiska elektronika")

    #gara līnīju komanda, lai samainītu uzdevumjoslas ikonu uz izvēlēto ikonas bildi izmantojot ctypes importētu bibliotēku.
    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    root.iconbitmap('Designer.ico')

    #maina logas izmēru
    root.geometry("900x700")

    #ievada maināmo izmēra funkciju uz 'False', lai lietotājs nespēj mainīt programmatūras izmēru.
    root.resizable(False, False)

    #logas virsraksts
    greeting_veikals = tk.Label(root, text="Lūdzu, ievadiet savu izvēlēto elektronisko ierīci!", fg='blue', font=('Aerial', 20, 'bold'))
    greeting_veikals.pack()

    #ievieto teksta logrīku LabelFrame
    search_frame = LabelFrame(root, text="Ievades rīks")
    search_frame.pack(padx=10, pady=10)

    #ievieto ievades logrīku Entry.
    search_entry = Entry(search_frame, font=("Helvetica", 18))
    search_entry.pack(pady=20, padx=20)

    #ievieto poga logrīku Button ar pievienotu funkciju vai metodi, kas jāizsauc, noklikšķinot uz pogas.
    search_button = Button(root, text="Meklēt", command=search_records)
    search_button.pack(padx=20, pady=20)

    #Treeview ir lietotāja saskarnes logrīks, kas parāda datus tabula formā.
    table = ttk.Treeview(root, columns=('Prece', 'Cena', '€'), show='headings')
    #ievada tabulas virsrakstus
    table.heading('Prece', text='Pieejamās preces')
    table.heading('Cena', text='Cena')
    table.heading('€', text='Valūta')
    table.pack(padx=50, pady=50, fill='both', expand=True)

    #izsauc funkciju
    query_database()

    #ievieto poga logrīku Button ar pievienotu funkciju vai metodi, kas jāizsauc, noklikšķinot uz pogas.
    contact_button = Button(text="Kontakti", height=2, width=20, bd=3, relief="groove", command=lambda:contactProcess())
    contact_button.place(x=700, y=630)

#izsauc funkciju no citas izsauktās funkcijas logā
def query_database():
    #savieno datubāzes failu un atgriež visus pieejamos datus.
    connection = sqlite3.connect('products.db')
    c = connection.cursor()
    c.execute("SELECT * FROM electronic_products")
    records = c.fetchall()

    #izveido mainīgo skaitli
    count = 0

    #izveido funkcijas ciklu, kas pievieno visus pieejamos datubāzes datus tabulā.
    for record in records:
        if count % 2 == 0:
            table.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
        else:
            table.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('oddrow',))
        #palielina katru skaitu par 1 ciklā.
        count += 1
    
    #apstiprina datubāzes visus neapstiprinātos darījumus.
    connection.commit()
    #aizver datubāzes savienojumu.
    connection.close()

#izsaukta funkcija, ja ar dubultklikšķi nospiests ir lietotāja izvēlētā tabulu datu vērtība.
def on_row_double_click(event):
    #funkcija, ja lietotājs uzspiež uz tabulu vērtības.
    selected_item = table.focus()
    if not selected_item:
        return

    values = table.item(selected_item, 'values')
    if not values:
        return

    #kad funkcija atgriežas, python atbrīvo atmiņu, ko izmanto visi funkcijas mainīgie.
    global product_window

    #izveido grafisko saskarni jeb logu no tkinter bibliotēka un to nosaukumu.
    product_window = tk.Toplevel()
    product_window.title("Produkta informācija")

    #maina logas izmēru
    product_window.geometry("600x600")

    #gara līnīju komanda, lai samainītu uzdevumjoslas ikonu uz izvēlēto ikonas bildi izmantojot ctypes importētu bibliotēku.
    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    product_window.iconbitmap('Designer.ico')

    #ievada maināmo izmēra funkciju uz 'False', lai lietotājs nespēj mainīt programmatūras izmēru.
    product_window.resizable(False, False)

    #logas virsraksts
    tk.Label(product_window, text="Produkta informācija", font=('Helvetica', 16, 'bold')).pack(pady=10)

    #ievieto teksta logrīku Label, kas no teksta rāda piešķirtu vērtības nosaukumu no izvēlētā datubāzes vērtības.
    product_name = tk.Label(product_window, text=f"Nosaukums: {values[0]}", font=('Helvetica', 12))
    product_name.pack(pady=5)
    product_price = tk.Label(product_window, text=f"Cena: {values[1]}", font=('Helvetica', 12))
    product_price.pack(pady=5)
    product_currency = tk.Label(product_window, text=f"Valūta: {values[2]}", font=('Helvetica', 12))
    product_currency.pack(pady=5)

    #ievieto poga logrīku Button ar pievienotu funkciju vai metodi, kas jāizsauc, noklikšķinot uz pogas. Kad funkcija ir izsaukta (.destroy), tad aizvēr product_window ciet.
    goback_button = Button(product_window, text="Aizvērt", width=10, height=2, command=product_window.destroy)
    goback_button.place(x=50, y=530)

    #ievieto poga logrīku Button ar pievienotu funkciju vai metodi, kas jāizsauc, noklikšķinot uz pogas.
    purchase_button = Button(product_window, text="Pirkt", width=15, height=3, command=lambda:purchaseProcess(product_name, price=None))
    purchase_button.place(x=430, y=512)

#definēta funkcija ar ko izsauc poga Pirkt - iemet ziņojuma kastīti ar kuru piešķir atsevišķas vērtības no izvēlētā datubāzes vērtības.
def purchaseProcess(product_name, price):
    messagebox.showinfo("Pirkums apstiprināts", f"Jūs iegādājāties: {product_name} par {price} EUR!\nPaldies par pirkumu.")

    #funkcija, kas aizver logu ciet.
    product_window.destroy()

#definē funckiju ar ko izsauc poga Kontakti - iemet lietotāju jaunā logā, kas attēlo īpašnieka telefona numurs (Label).
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

#izsaukta funkcija no iepriekšēja python faila konkrēti no logošanas pogas nosacījuma. Šī funkcija ir izsaukta tikai, ja lietotājs ir ielogots ar savu kontu.
def logoff_tab():
    logoff = tk.Label(root, text="Iziet no konta", fg="blue", cursor='hand2', font=('underline'))
    logoff.place(x=400, y=220)

    #ievietota saistīšanas funkcija, kas tiek izmantota notikumu risināšanai, piemēram, šī funkcija tiks izsaukta, ja teksts ir nospiests ar peles kursoru kreisā pogā.
    logoff.bind('<Button-1>', previous_window)

    #ievietota saistīšanas funkcija, kas tiek izmantota notikumu risināšanai, piemēram, šī funkcija tiks izsaukta, ja teksts ir dubultklikšķināts ar peles kursoru kreisā pogā.
    table.bind("<Double-1>", on_row_double_click)

#izsaukta funkcija tekstā "Iziet no konta".
def previous_window(event):
    #tiek pievienots parametrs, lai funkcija strādātu.
    event.char
    #funkcija, kas aizver logu ciet.
    root.destroy()