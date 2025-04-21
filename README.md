# Piekluves_Darbs
**p2-exam-darbs**

**Problēma** - Viens pusaudzis grib nopirkt jaunu spēles konsoli un piemērotu elektronikas sīkrīku. Pusaudzis atrod pieejamu jaunu spēles konsoli plauktā, bet RD Electronics un citu elektronikas veikalos Ventspilī nav piemērotāka elektronikas sīkrīku. Pusaudzis apmeklē internetveikalā un uzzināja, ka ir pieejams sīkrīks Rīgā, nevis Ventspilī. Ventspilī nav plašāki piemērotāki elektronikas veikali. Cilvēki ceļo uz galvaspilsētu Rīga un citās pilsētās tikai fiziskos elektronikas veikalos dēļ. Cilvēki tērē piegādes cenas un gaida pāris dienas, lai dabūtu savu produktu rokās.

**Risinājums** 
- _Reklamēšu jaunu elektronikas veikalu nosaukumā "Ventspils Starptautiska elektronika" jeb "VSE", izmantojot aplikāciju_
- _lietotājs var piereģistrēties, sameklēt pieejamu elektronisko sīkrīku_
- _noklikšķinot uz programmas ieejamo saiti, lietotājs tiek ielikts uz oriģinālo veikala mājaslapu_

**Mērķauditorija** - Cilvēki, biežāk pusaudži, kuri grib aiziet un nopirkt savu preci netālu (5min) no savas mājas.
## Programmas Prasību Specifikācijas

**Funkcionālās prasības** - izmantošu pieejamās GUI bibliotēkas (Tkinter), programmu kodus (Python), API funkciju (atrašanas vieta veikalā) un Datubāzi, kas saglabā starptautiskās elektronikas preces. Kā arī izmantošu datubāzi, lai saglabā lietotāja informāciju un vēsturi ar sameklētām precēm. Reģistrācijas cilnē būs "reCAPTCHA" poga, kas pārbauda lietotāju un novērs eksplotāciju programmā.
1. _preces meklēšana poga, lai lietotājs var brīvi ievadīt un sameklēt savu ievēloto preci_
2. _rekomendācijas poga ar ko izmantos lietotāja nesen meklētās preces datus un izmantos tos datus, lai ar vizualizāciju parāda šo preces attēlu, kad iespied pogu "rekomendācija" (PS: ši poga tikai parādīsies, kad lietotājs ievada savu ievēloto preci uz "preces meklēšana" pogā, kad datubāze saglabā lietotāja darbību)_
3. _saites kontaktinformācija poga, kur ir pievienots veikalas atrašanas vieta un telefona numurs, lai lietotājs var sazināties ar veikala vadītāja_
4. _reģistrācijas poga, ko lietotājs var ierakstīties savā kontā un apskatīt aplikācijas internetveikalu_

***Funkcionālās prasības 1 - (Poga "Reģistrēties"):***

- Datu ievada nepieciešamība 

  Nepieciešams ievadīt - Vārds, Uzvārds, E-pasts, Parole

- Datu ievades saturs

  Vārds - Jānis, Uzvārds - Bulgerts, E-pasts - janis.bulgerts@gmail.com, Parole - 1234

- Datu apstrāde 

  Lietotājam būs saglabāta kontu informācija datubāzē

- Datu izvade 

  Iemetīs lietotāju uz jauno cilni.

***Funkcionālā prasība 2 - (Teksta slīpsvītra "iziet no konta")***

- Datu ievada nepieciešamība 

  Nospiedot uz "iziet no konta" slīpsvītru ar kursoru 

- Datu ievades saturs 

  Lietotājs grib iziet ārā no viņa konta, lai nesaglabā meklētas preces

- Datu apstrāde 

  Lietotāja konta informācija vēl ir saglabāta datubāzē, tikai jāievada atkal reģistrācijas cilnē

- Datu izvade 

  Iemetīs lietotāju uz iepriekšējo cilnu, kur lietotājai ir izvēle atkal reģistrēties vai ieiet viesu režīmā

***Funkcionālā prasība 3 - (Poga "Meklēt")***

- Datu ievada nepieciešamība

  Ievadīt savu nepieciešamo elektronikas sīkrīka preci

- Datu ievades saturs 

  Elektronikas sīkrīku prece - Pele

- Datu apstrāde  

  Datubāze sameklēs ievadīto lietotāju preci (peli) 

- Datu izvade 

  Funkcija rekomendēs lietotāja ievadīto preci (peles rekomendācijas no populāras firmas)

***Funkcionālā prasība 4 - (Preces priekšstaktījums)*** 

- Datu ievada nepieciešamība 

  Nospiedot uz lietotāja izvēlēto preci ar kursoru.

- Datu ievades saturs 

  Nospiestā prece - Pele

- Datu apstrāde 

  Datubāze sameklēs nospiesto lietotāju preci (peli) 

- Datu izvade 

  Iemetīs lietotāju uz jauno cilnu lietotāja izvēlētā precē.

***Funkcionālā prasība 5 - (Poga "Nopirkt")***

- Datu ievada nepieciešamība 

  Nospiedot uz pogu "Nopirkt" ar kursoru.

- Datu ievades saturs:

  Nav.

- Datu apstrāde

  Programma izveidos papildcilnu ar kuru izģenerēs rēķinu, datu bāzē sameklēs lietotāja informāciju E-pastu, sameklēto E-pastu atsūtīs pircējam pastu ar pieprasījumu un 

- Datu izvade

  Izvada papildcilni ar datu apstrādes teikto un 

***Funkcionālā prasība 6 - (Viesa režīms)***

- Datu ievada nepieciešamība 

  Nospiedot uz pogu "Viesa režīms" ar kursoru. 

- Datu ievades saturs 

  Nav. 

- Datu apstrāde 

  Lietotāja dati netiks saglabāti, kad apmeklē veikalas saiti.

- Datu izvade 

  Iemetīs lietotāju uz jauno cilni bez konta.

***Funkcionālā prasība 7 - (Veikalu kontaktinformācija)***

- Datu ievada nepieciešamība 

  Nospiedot uz pogu "kontaktinformācija" ar kursoru. 

- Datu ievades saturs 

  Lietotājs grib sazināties ar vietnes īpašnieku. 

- Datu apstrāde 

  Iespiežot uz kontaktinformācijas pogu, lietos API Google Maps, lai rādītu lietotājam veikalas atrašanas vietu.

- Datu izvade 

  Iemetīs lietotāju uz jauno cilni ar redzamu vietnes īpašnieka telefona numuru un veikalas atrašanas vietu.

**Lietotāja saskarnes dizains** - Lietotāja pirmā cilnes vizualizācija būs ielogoties (lietotāja vārds un parole, kas saglabās to datus), opcija - poga piereģistrēties, lai lietotājs ievada savu nepieciešamo informāciju (Vārds, Uzvārds, E-pasts, Parole un "reCAPTCHA" poga). Lietotājam ir arī iespēja ieiet uz viesa režīmu, kas nesaglabā lietotāja sameklētās preces vēsturi. Pēc šis cilnes, lietotājam būs izvēle noklikšķināt uz trim pogām:
1) preces meklēšana poga
2) pirkšana poga
3) saites kontaktinformācija poga

Papildināts ar vizualizācijas plakātu, kas reklamē mērķauditoriju par unikāli importētam elektronikas preču sīkrīkus.

**Tehniskās prasības** - programmatūra ir izveidots Windows operatīva sistēma. Programmatūrā būs jaizmanto funkcionālā datoru pele un klaviatūra. Programmā nav pieprasījumi datoru specifikācijām(aptuveni ļoti maz operatīva atmiņa izmantojums).
