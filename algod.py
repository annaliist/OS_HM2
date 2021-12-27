def massiiviks(input_jarjend):
    valjund = []
    jupid = input_jarjend.split(";")
    for i in range(len(jupid)):
        hakkliha = jupid[i].split(",")
        saabumine = int(hakkliha[0])
        kestus = int(hakkliha[1])
        valjund.append([saabumine, kestus])
    return valjund

järjend = [['A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
['A', 'B', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', 'H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
['A', 'B', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', 'H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
['A', 'B', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', 'H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
['A', 'B', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
['A', 'F', 'F', ' ', ' ', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
['A', 'F', 'F', ' ', ' ', 'G', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
['A', 'F', 'F', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
['I', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
valjund = []

# [[1, 8], [35, 4], [3, 6], [4, 2], [1, 4], [3, 3], [1, 2], [5, 1], [50, 1]]
def first_fit(jarjend):
    global valjund
    valjund.clear
    valjund = [[],[],[],[],[],[],[],[],[],[]]

    def kas_mahub(x,y,z): # paremale, vasakule, alguspunkt (jarjend[z])
        global valjund
        mahub = True
        alguspunkt = 0

        for i in range(50):

            try:
                for veerg in range(y):
                    for rida in range(x):
                        print("VEERG " + str(veerg))
                        print("RIDA: " + str(rida + z))
                        if valjund[rida + z][veerg] == " ":
                            print("Tühi")    
                            mahub = True                    
                        else:
                            print("Pole tühi, järgmine veerg")
                            alguspunkt += 1
                            mahub = False
                            break
                
                if mahub:
                    print("ALGUSPUNKT: " + str(alguspunkt))
                    break

            except:
                print("Ei mahu")
                mahub = False
                break

        if mahub:
            print("VIIMANE OTSUS: " + alphabet[z] + " mahub, alatest veerg " + str(alguspunkt) + ", rida " + str(z))
            return alguspunkt # top left koordinaadid valjund[z][alguspunkt]
        else:
            print("VIIMANE OTSUS: ei mahu")
            return 404

    def taida_auk(x,y,j,k,s): # alguskoordinaat (x,y), protsessi mõõdud (j x k), s - sümbol
        global valjund
        
        for rida in range(j):
            for veerg in range(k):
                valjund[rida+x][veerg+y] = alphabet[s]
                

    # täidame lõpp-järjendi tühjade väljadega
    for i in range(10):
        for j in range(50):
            valjund[i].append(" ")


    for i in range(len(jarjend)):
        print(jarjend[i])
        koordinaat = kas_mahub(jarjend[i][1], jarjend[i][0], i)
        if koordinaat == 404: # otsib esimest vaba auku enda reas
            print("Protsess " + alphabet[i] + " ei mahu!") # kui ei mahu, lõpetab programmi
            print("Programm lõpetatud.")
            break
        else:
            print("Lisan protsessi " + alphabet[i])
            taida_auk(i, koordinaat, jarjend[i][1], jarjend[i][0], i)

            for k in range(10):
                print(valjund[k])

    for i in valjund:
        print(valjund[i])

    return valjund

first_fit(massiiviks("1,8;35,4;3,6;4,2;1,4;3,3;1,2;5,1;50,1"))
#first_fit(massiiviks("1,8;35,4"))


















def last_fit(jarjend):
    valjund = []

    return valjund

def best_fit(jarjend):
    valjund = []

    return valjund

def worst_fit(jarjend):
    valjund = []

    return valjund

def random_fit(jarjend):
    valjund = []

    return valjund