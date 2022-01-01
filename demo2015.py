# Annaliis Täheväli

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from algod import *

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def puhasta():
    tahvel.delete('all')

def color_picker(protsess):
    colors = ["green", "yellow", "orange", "red", "#8CD1F1", "#AFE88C", "#F8DAE3", "cyan", "#F1ED8C", "#C18FDE", "#B2A9F3", "#F955B3", "#EFEFEF"]
    color = ''
    
    if protsess == ' ':
        color = colors[-1]
    else:
        color = colors[alphabet.index(protsess)]

    return color


# joonistab tahvlile protsesse kujutavad ristkülikud numbrite ja protsesside nimedega
def joonista(jarjend):
    puhasta()
    eelmise_loppx = 110
    nr_x = 118
    y_koordinaat = 60
    y_koordinaat2 = 80
    kaugus = 0
    for i in range(len(jarjend)):
        for j in range(50):
            protsess = jarjend[i][j]
            kestus = 1
            kujund = tahvel.create_rectangle(eelmise_loppx, y_koordinaat, eelmise_loppx + kestus * 16,y_koordinaat2, fill=color_picker(protsess))
            keskpaik = eelmise_loppx+kestus * 8
            protsessi_id = tahvel.create_text(keskpaik, y_koordinaat+10, text=protsess)

            if i == 0:
                nr = tahvel.create_text(nr_x, 50, text=str(kaugus)) # 0-49
            kaugus += kestus
            eelmise_loppx += kestus*16
            nr_x += kestus*16

            # etapi nr ja lisatud protsessid
            etapp = tahvel.create_text(15, y_koordinaat+10, text=str(i + 1))
            try:
                protsess = tahvel.create_text(70, y_koordinaat+10, text=alphabet[i] + " : " + str(massiiviMeister()[i]))
            except:
                protsess = tahvel.create_text(70, y_koordinaat+10, text="-") 

        y_koordinaat += 20
        y_koordinaat2 += 20
        eelmise_loppx = 110
    etapi_silt = tahvel.create_text(20, 50, text="Etapp", font='Helvetica 9 bold')
    protsessi_silt = tahvel.create_text(70, 50, text="Protsess", font='Helvetica 9 bold')

# teeb järjendist kahetasemelise listi, mida on mugavam töödelda
def massiiviks(input_jarjend):
    valjund = []
    jupid = input_jarjend.split(";")
    for i in range(len(jupid)):
        hakkliha = jupid[i].split(",")
        saabumine = int(hakkliha[0])
        kestus = int(hakkliha[1])
        valjund.append([saabumine, kestus])
    return valjund

# otsustab, millist järjendit teha kahetasemeliseks massiiviks
def massiiviMeister():
    jarjend = []
    if var.get() == 1:
        return massiiviks(predef1)
    elif var.get() == 2:
        return massiiviks(predef2)
    elif var.get() == 3:
        return massiiviks(predef3)
    elif var.get() == 4:
        try:
            return massiiviks(kasutaja_jarjend.get())
        except:
            messagebox.showerror(title="Viga sisendis", message="Vigane kasutaja muster!")
            return massiiviks(predef1)
    else:
        return massiiviks(predef1)

def kasuvalija(jarjend, algoritm):
    if algoritm == "first_fit":
        return first_fit(jarjend)
    elif algoritm == "last_fit":
        return last_fit(jarjend)

def jooksuta_algoritmi(algoritm):
    jarjend = massiiviMeister()
    valjund = kasuvalija(jarjend, algoritm)
    joonista(valjund)
    keskm_oot = tahvel.create_text(80, 20, text="Algoritm: " + str(algoritm).replace("_", " ").upper(), font='Helvetica 9 bold')

predef1 = "4,5;2,7;9,2;4,6;7,1;6,4;8,8;3,6;1,10;9,2"
predef2 = "1,10;6,6;3,9;2,4;1,6;5,2;1,4;5,2;2,1;2,7"
predef3 = "5,10;6,6;3,9;8,4;3,6;5,12;1,4;15,3;3,4;9,7"


# GUI
raam = Tk()
raam.title("Planeerimisalgoritmid")
raam.resizable(False, False)
raam.geometry("930x500")

var = IntVar()
var.set(1)
Radiobutton(raam, text="Esimene", variable=var, value=1).place(x=10,y=40)
Radiobutton(raam, text="Teine", variable=var, value=2).place(x=10,y=70)
Radiobutton(raam, text="Kolmas", variable=var, value=3).place(x=10,y=100)
Radiobutton(raam, text="Enda oma", variable=var, value=4).place(x=10,y=130)

silt_vali = ttk.Label(raam, text="Vali või sisesta järjend (kujul 1,10;4,2;12,3;13,2)")
silt_vali.place(x=10, y=10)

silt1 = ttk.Label(raam, text=predef1)
silt1.place(x=120, y=40)

silt2 = ttk.Label(raam, text=predef2)
silt2.place(x=120, y=70)

silt3 = ttk.Label(raam, text=predef3)
silt3.place(x=120, y=100)

silt_run = ttk.Label(raam, text="Algoritmi käivitamiseks klõpsa nupule")
silt_run.place(x=10, y=160)

kasutaja_jarjend = ttk.Entry(raam)
kasutaja_jarjend.place(x=120, y=130, height=25, width=240)
kasutaja_jarjend.insert(END,"1,8;35,4;3,6;4,2;1,4;3,3;1,2;5,1;50,1")

tahvel = Canvas(raam, width=930, height=280, background="white")
tahvel.place(x=0, y=220)

first_fit_nupp = ttk.Button(raam, text="first-fit", command = lambda : jooksuta_algoritmi("first_fit"))
first_fit_nupp.place(x=10, y=190,height=25, width=80)

last_fit_nupp = ttk.Button(raam, text="last-fit", command = lambda : jooksuta_algoritmi("last_fit"))
last_fit_nupp.place(x=100, y=190,height=25, width=80)

raam.mainloop()
