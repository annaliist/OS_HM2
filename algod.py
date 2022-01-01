from tkinter import messagebox
import random

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
valjund = []

def tuhjenda(): # täidame lõpp-järjendi tühjade väljadega
    global valjund

    for i in range(10):
        for j in range(50):
            valjund[i].append(" ")

def taida_auk(x,y,j,k,s): # alguskoordinaat (x,y), protsessi mõõdud (j x k), s - sümbol
    global valjund
    
    for rida in range(j):
        for veerg in range(k):
            valjund[rida+x][veerg+y] = alphabet[s]

def first_fit(jarjend):
    global valjund
    valjund = [[],[],[],[],[],[],[],[],[],[]]

    def kas_mahub(x,y,z): # paremale, vasakule, alguspunkt (jarjend[z])
        mahub = True
        alguspunkt = 0
        peata = False

        for i in range(50): # leiame alguspunkti
            if valjund[z][i] == " ":
                alguspunkt = i
                break

        for samm in range(50):
            try:
                for veerg in range(y):
                    peata = False

                    for rida in range(x):
                        print("VEERG " + str(veerg + alguspunkt))
                        print("RIDA: " + str(rida + z))
                        if valjund[rida + z][veerg + alguspunkt] == " ":
                            print("Tühi")    
                            mahub = True
                        else:
                            print("Antud alguspunktiga ei mahu, järgmine veerg")
                            peata = True
                            mahub = False  
                            break  
                    
                    if peata:
                        break         

                if mahub:
                    break
                else:
                    alguspunkt += 1
            except:
                mahub = False
                break

        if mahub:
            print("VIIMANE OTSUS: " + alphabet[z] + " mahub, alatest veerg " + str(alguspunkt) + ", rida " + str(z))
            return alguspunkt # top left koordinaadid valjund[z][alguspunkt]
        else:
            print("VIIMANE OTSUS: ei mahu")
            return 404                

    tuhjenda()

    for i in range(len(jarjend)):
        print(jarjend[i])
        koordinaat = kas_mahub(jarjend[i][1], jarjend[i][0], i)
        if koordinaat == 404: # kui ei mahu, lõpetab programmi
            messagebox.showerror(title="Mälu täis", message="Protsess " + alphabet[i] + " ei mahu mällu!\n Programm lõpetatud." )
            break
        else:
            print("Lisan protsessi " + alphabet[i])
            taida_auk(i, koordinaat, jarjend[i][1], jarjend[i][0], i)

            for k in range(10):
                print(valjund[k])

    return valjund

def last_fit(jarjend):
    global valjund
    valjund = [[],[],[],[],[],[],[],[],[],[]]

    def kas_mahub(x,y,z): # paremale, vasakule, alguspunkt (jarjend[z])
        mahub = True
        alguspunkt = 0
        peata = False

        for i in range(50): # leiame alguspunkti
            if valjund[z][i] != " ":
                alguspunkt = i + 1
                if alguspunkt > 49:
                    alguspunkt = 0
        
        print("ALGUSPUNKT: " + str(alguspunkt))

        for samm in range(50):
            try:
                for veerg in range(y):
                    peata = False

                    for rida in range(x):
                        print("VEERG " + str(veerg + alguspunkt))
                        print("RIDA: " + str(rida + z))
                        if valjund[rida + z][veerg + alguspunkt] == " ":
                            print("Tühi")    
                            mahub = True
                        else:
                            print("Antud alguspunktiga ei mahu, järgmine veerg")
                            peata = True
                            mahub = False  
                            break  
                    
                    if peata:
                        break         

                if mahub:
                    break
                else:
                    if alguspunkt == 49:
                        alguspunkt = 0
                    else:
                        alguspunkt += 1
            except:
                print("Otsime uut alguspunkti")
                if alguspunkt == 49:
                    alguspunkt = 0
                else:
                    alguspunkt += 1

        if mahub:
            print("VIIMANE OTSUS: " + alphabet[z] + " mahub, alatest veerg " + str(alguspunkt) + ", rida " + str(z))
            return alguspunkt # top left koordinaadid valjund[z][alguspunkt]
        else:
            print("VIIMANE OTSUS: ei mahu")
            return 404                

    tuhjenda()

    for i in range(len(jarjend)):
        print(jarjend[i])
        koordinaat = kas_mahub(jarjend[i][1], jarjend[i][0], i)
        if koordinaat == 404: # kui ei mahu, lõpetab programmi
            messagebox.showerror(title="Mälu täis", message="Protsess " + alphabet[i] + " ei mahu mällu!\n Programm lõpetatud." )
            break
        else:
            print("Lisan protsessi " + alphabet[i])
            taida_auk(i, koordinaat, jarjend[i][1], jarjend[i][0], i)

            for k in range(10):
                print(valjund[k])

    return valjund
