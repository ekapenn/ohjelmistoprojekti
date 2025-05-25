#Sallitut arvot
sallit_tavoite= ["laihtua", "kasvattaa massaa", "pitää kunto kunnossa"]
sallit_taso= ["aloittelija", "keskitaso", "edistynyt"]
sallit_mieltymys= ["kardio", "voimaharjoittelu", "venyttely"]

#Kysytään käyttäjän nimen
nimi = input("Mikä sinun nimesi?: ")
#alkutervehdys
print(f"Hei,{nimi}!\nValitse mikä treeniohjelma sinulle sopii\nsekä kuinka paljon vettä täytyy juoda.")

#ekakysymys ja tavoite, ja muuntaa vastauksen pieniksi kirjaimiksi 
while True:
    tavoite = input("\nMikä sinun tavoite?\nlaihtua / kasvattaa massaa  / pitää kunto kunnossa: ").lower()
    if tavoite in sallit_tavoite: #syötteen tarkistaminen
        break
    print("Tarkista syöttö: vain annetuista vaihtoehdoista") #virheilmoitus

#tokakysymys-taso
while True:
    taso = input("Mikä taso sinulla juuri nyt?\naloittelija / keskitaso / edistynyt: ").lower()
    if taso in sallit_taso: #syötteen tarkistaminen
        break
    print("Tarkista syöttö: vain annetuista vaihtoehdoista") #virheilmoitus
#kolmaskysymys-mieltymys
while True:
    mieltymys= input("Mitä eniten tykkäät?\nkardio / voimaharjoittelu / venyttely: ").lower()
    if mieltymys in sallit_mieltymys: #syötteen tarkistaminen
        break
    print("Tarkista syöttö: vain annetuista vaihtoehdoista") #virheilmoitus

#neljäskysymys-paino
while True:
    try:
        paino = float(input("Mikä on painosi?: "))
        if paino <= 0: #tarkastetaan, että paino on suurempi kuin nolla
            print("Painon pitäisi olla myönteinen luku. Syötä uudelleen.")
            continue
        elif paino > 200: #luku ei voi olla isompi kuin 200 muuten on se virhellinen 
            continue
        break
    except ValueError:
        print("Syötä luku. Esim, 70.")# jos vastaus on väärä, näytetään tämä viesti

#treenin suositus
suositus= ""
#treenin suositus jos halutaan laihtua 
if tavoite == "laihtua" and  taso== "aloittelija" and mieltymys in["kardio", "voimaharjoittelu", "venyttely"]:
    suositus = "Treenit + 15min kardio, 2-5 kertaa viikossa"
elif tavoite == "laihtua" and  taso== "keskitaso" and mieltymys in["kardio", "voimaharjoittelu", "venyttely"]:
    suositus = "Treenit + 20min kardio, 2-5 kertaa viikossa"
elif tavoite == "laihtua" and  taso== "edistynyt" and mieltymys in["kardio", "voimaharjoittelu", "venyttely"]:
    suositus = "Treenit + 30min kardio, 2-4 kertaa viikossa"
#treenit suositus jos halutaan lisätä massaa   
if tavoite == "kasvattaa massaa" and  taso== "aloittelija" and mieltymys in["voimaharjoittelu", "venyttely"]:
    suositus = "Voimaharjoittelu, 2-4 kertaa viikossa"
elif tavoite == "kasvattaa massaa" and  taso== "keskitaso" and mieltymys in["voimaharjoittelu", "venyttely"]:
    suositus = "Voimaharjoittelu, 3-4 kertaa viikossa"
elif tavoite == "kasvattaa massaa" and  taso== "edistynyt" and mieltymys in["kardio", "voimaharjoittelu", "venyttely"]:
    suositus = "Voimaharjoittelu, 2-4 kertaa viikossa"
#treenit suositus jos on edistynyt
if tavoite == "pitää kunto kunnossa" and  taso== "aloittelija" and mieltymys in["kardio", "voimaharjoittelu", "venyttely"]:
    suositus = "Kevyttä voimaharjoittelua 2-3 kertaa viikossa + kävelylenkkejä."
elif tavoite == "pitää kunto kunnossa" and  taso== "keskitaso" and mieltymys in["kardio", "voimaharjoittelu", "venyttely"]:
    suositus = "Treenit + 30min kardio, 2-4 kertaa viikossa"
elif tavoite == "pitää kunto kunnossa" and  taso== "edistynyt" and mieltymys in["kardio", "voimaharjoittelu", "venyttely"]:
    suositus = "Treenit, 3-4 kertaa viikossa"

#Lasketaan, kuinka paljon vettä tarvitaan
vesi= paino * 0.03 #kaava 30 ml 1kg painoa kohti = 0,03 litraa/kg.
trenivesi= 0.5 if tavoite in ["laihtua", "kasvattaa massaa" ] else 0.0 #jos tavoite on aktiivinen lisätään vielä 0,5 litraa liikuntaa varten.
yleisvesi = vesi + trenivesi #vesimäärä yhteensä

#tulos
print("\n" + "=" * 57) #kehyksen yläreuna
print("{:^57}".format ("TULOS")) #Tämä tulostaa keskelle sanan
print(f"Nimi: {nimi}")
print(f"Tavoite: {tavoite}")
print(f"Taso: {taso}")
print(f"Treeniohjelma: {suositus}") #lopullinen suositus
print(f"Juomaveden suositus: {yleisvesi:.2f}l/päivä")
print("\n" + "=" * 57) #kehyksen alareuna