import random
import time

        
#Pelit

#Ventti
#Tekijä: Niklas
def Ventti(raha):
    print('Ladataan peliä...')
    time.sleep(1)
    print()
    
    #ohjeet
    ohje=input('Haluatko lukea ohjeet? (k/e) ')
    ohje=ohje.lower()
    if ohje == 'k':
        print('Pelin tavoite on saada korttien lukujen summaksi 21, tai enemmän kuin vastustaja.')
        print('Jos saat tasan 21, voittosi kerrotaan 1.5:llä.')
    print()

    while True:
        #saldon tarkistus
        if raha<=0:
            print('Sinulla ei ole tarpeeksi rahaa.')
            input('Paina Enter.')
            print()
            print('Ladataan valikkoa...')
            time.sleep(1)
            print()
            return raha



        #Pakan luonti
        maat=['Hertta','Ruutu','Pata','Risti']
        numerot=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        pakka=[]
        arvot=[]
        for maa in maat:
            for numero in numerot:
                pakka.append(maa+' '+numero)
        for maa in range(4):
            for numero in range(13):
                arvot.append(numero+1)



        #Pelaajan vuoro
        #panos
        panos=0
        summa=0
        vastaus='k'
        panos_annettu=0
        while panos_annettu==0:
            print('Sinulla on rahaa:',raha)
            panos=input('Anna panos: ')
            if panos.isnumeric():
                panos = int(panos)
                if panos>raha:
                    print('Sinulla ei ole näin paljon rahaa.')
                    print ()
                elif panos<=0:
                    print('Sinun on pakko asettaa panos.')
                    print ()
                else:
                    panos_annettu = 1
            elif panos.isnumeric()==False:
                print('Antamasi panos ei ole kelvollinen')
                print()
                
        print()

        #peli
        while vastaus=='k':
            for i in range(1):
                kortti=random.randint(0,len(pakka)-1)
                print(pakka[kortti])
                summa=summa+arvot[kortti]
                pakka.pop(kortti)
                arvot.pop(kortti)
                if summa>21:
                    vastaus='e'
                    break
                print('Yhteensä nyt: ', summa)
                vastaus=input('Jatketaanko? (k/e) ')
                vastaus=vastaus.lower()
        print('Yhteensä: ', summa)



        #Tietokoneen vuoro
        print()
        print('Tietokoneen vuoro')
        tksumma=0
        vastaus='k'
        while vastaus=='k':
            kortti=random.randint(0,len(pakka)-1)
            print(pakka[kortti])
            tksumma=tksumma+arvot[kortti]
            pakka.pop(kortti)
            arvot.pop(kortti)
            if summa>21:
                vastaus='e'
            elif tksumma>summa:
                vastaus='e'
        print('Yhteensä: ', tksumma)
        print()



        #Lopputulos
        if summa>21:
            print('Hävisit!')
            raha=raha-panos
            print('Hävisit', panos, 'rahaa.')
            
        elif summa==21:
            print('Voitit!')
            voitto=panos*1.5
            voitto=int(voitto)
            raha=raha+voitto
            print('Voitit', panos, 'rahaa.')
            
        elif tksumma>21:
            print('Voitit!')
            raha=raha+panos
            print('Voitit', panos, 'rahaa.')
            
        else:
            print('Hävisit!')
            raha=raha-panos
            print('Hävisit', panos, 'rahaa.')
            
        print('Sinulla on nyt', raha, 'rahaa.')
        print()

        #uusi peli?
        uusiPeli=input('Haluatko pelata uudelleen? (k/e) ')
        uusiPeli=uusiPeli.lower()
        if uusiPeli!='k':
            print()
            print('Ladataan valikkoa...')
            time.sleep(1)
            print()
            return raha
        print()
        continue



#Numeron arvaus
#Tekijä: Niklas
def Numeron_arvaus(raha):
    print('Ladataan peliä...')
    time.sleep(1)
    print()
    
    #ohjeet
    ohje=input('Haluatko lukea ohjeet? (k/e) ')
    ohje=ohje.lower()
    if ohje == 'k':
        print('Peli arpoo numeron 1 ja 100 väliltä.')
        print('Tehtäväsi on arvat numero.')
        print('Mitä lähemmäs arvauksesi osuu, sitä enemmän rahaa voitat.')
        print('Jos arvauksesi on enemmän kuin 25 ohi, et voita mitään.')
    print()

    while True:
        #saldon tarkistus
        if raha<=0:
            print('Sinulla ei ole tarpeeksi rahaa.')
            menu=input('Paina Enter.')
            print()
            print('Ladataan valikkoa...')
            time.sleep(1)
            print()
            return raha

        #numeron arpominen
        numero=random.randint(1,100)
        #print(numero)

        #panos
        panos=0
        panos_annettu=0
        while panos_annettu==0:
            print('Sinulla on rahaa:',raha)
            panos=input('Anna panos: ')
            if panos.isnumeric():
                panos = int(panos)
                if panos>raha:
                    print('Sinulla ei ole näin paljon rahaa.')
                    print ()
                elif panos<=0:
                    print('Sinun on pakko asettaa panos.')
                    print ()
                else:
                    panos_annettu = 1
            elif panos.isnumeric()==False:
                print('Antamasi panos ei ole kelvollinen')
                print()
        raha=raha-panos

        print()

        #arvaus
        kelvollinenArvaus=0
        while kelvollinenArvaus==0:
            arvaus=input('Arvauksesi: ')
            if arvaus.isnumeric()==False:
                print('Arvauksesi ei ole kelvollinen.')
                print()
            else:
                arvaus=int(arvaus)
                if arvaus>=0 and arvaus<=100: 
                    kelvollinenArvaus=1
                else:
                    print('Arvauksesi ei ole kelvollinen.')
                    print()
                
        #tulos
        häviö=0
        erotus=numero-arvaus
        erotusABS=abs(erotus)
        #tasan
        if erotusABS==0:
            print('Arvasit oikein!')
            raha=raha+panos*20
            print('Voitit', panos*20, 'rahaa!')

        #1
        elif erotusABS==1:
            print('Arvausesi on', erotusABS, 'ohi.')
            raha=raha+panos*10
            print('Voitit', panos*10, 'rahaa!')

        #2-3
        elif erotusABS>=2 and erotusABS<=3:
            print('Arvausesi on', erotusABS, 'ohi.')
            raha=raha+panos*5
            print('Voitit', panos*5, 'rahaa!')

        #4-10
        elif erotusABS>=4 and erotusABS<=10:
            print('Arvausesi on', erotusABS, 'ohi.')
            raha=raha+panos*3
            print('Voitit', panos*3, 'rahaa!')

        #11-15
        elif erotusABS>=11 and erotusABS<=15:
            print('Arvausesi on', erotusABS, 'ohi.')
            raha=raha+panos*2
            print('Voitit', panos*2, 'rahaa!')

        #16-25
        elif erotusABS>=16 and erotusABS<=25:
            print('Arvausesi on', erotusABS, 'ohi.')
            raha=raha+panos
            print('Voitit', panos, 'rahaa!')

        #enemmän kuin 25
        else:
            print('Arvauksesi on enemmän kuin 25 ohi.')
            if raha < 0:
                raha=0
            print('Et voita mitään.')
            häviö=1

        print('Sinulla on nyt', raha, 'rahaa.')

        #uusi peli?
        print()
        uusiPeli=input('Haluatko pelata uudelleen? (k/e) ')
        uusiPeli=uusiPeli.lower()
        if uusiPeli!='k':
            print()
            print('Ladataan valikkoa...')
            time.sleep(1)
            print()
            return raha
        print()
        continue



#Ruletti
#Tekijä: Väinö
def Ruletti(raha):
    print('Ladataan peliä...')
    time.sleep(1)
    print()

    #ohjeet
    ohje=input('Haluatko lukea ohjeet? (k/e) ')
    ohje=ohje.lower()
    if ohje == 'k':
        print('Voit asettaa panoksen värille (punainen tai musta); numerolle (0-36); onko numero parillinen tai pariton;')
        print('ensimmäiselle, toiselle tai kolmannelle kahdentoista sarjalle (1-12, 13-24 tai 25-36);')
        print('ensimmäiselle tai toiselle kahdeksantoista sarjalle (1-18 tai 19-36); tai jollekkin yksittäiselle numerolle.')
    print()
    
    '''general.py

    PURPOSE:    To provide the basic betting options and random spin generation for
                American-style roulette.

                This is a fairly primitive roulette betting version, as the betting
                styles 8--11 aren't completely accurate: in standard roulette,
                betting on two numbers (split) must be adjacent on the roulette
                board. Similar for the other betting styles. This version allows
                splitting over any numbers.

    FURTHER
    READING:    Additional documentation on the basic rules of roulette can be
                found here:
                => http://www.ildado.com/roulette_rules.html
                => http://www.rouletteonline.net/odds/
                => https://en.wikipedia.org/wiki/Roulette

    AUTHOR:     Nicholas P. Taliceo
                ntaliceo@gmail.com  |  www.NicholasTaliceo.com

    DATE:       August 06, 2017
    '''

    bankroll = raha


    def spins():
        global slots
        slots = {'00': 'green', '0': 'green', '1': 'black', '2': 'red',
                 '3': 'black', '4': 'black', '5': 'red', '6': 'black', '7': 'red',
                 '8': 'black', '9': 'red', '10': 'black', '11': 'red',
                 '12': 'red', '13': 'black', '14': 'red', '15': 'black',
                 '16': 'black', '17': 'red', '18': 'black', '19': 'red',
                 '20': 'red', '21': 'black', '22': 'red', '23': 'black',
                 '24': 'black', '25': 'red', '26': 'black', '27': 'red',
                 '28': 'red', '29': 'black', '30': 'red', '31': 'black',
                 '32': 'black', '33': 'red', '34': 'black', '35': 'red',
                 '36': 'red'}

        result = random.choice(list(slots.keys()))
        return result


    def bet_value(bet_type):
        kelvollinen_veto=0
        
        if bet_type == 1:
            while kelvollinen_veto==0:
                bet_val = input("Onko vetosi Parilline (1) vai Pariton (2)?: ")
                if bet_val.isnumeric():
                    bet_val=int(bet_val)
                    if bet_val < 1 or bet_val > 2:
                        print('Valintasi ei ole kelvollinen')
                        print()
                    elif bet_val == 1 or bet_val == 2:
                        kelvollinen_veto=1
                elif bet_val.isnumeric()==False:
                    print('Valintasi ei ole kelvollinen')
                    print()
            return bet_val
        
        if bet_type == 2:
            while kelvollinen_veto==0:
                bet_val = input("Onko vetosi Punainen (1) vai Musta (2)?: ")
                if bet_val.isnumeric():
                    bet_val=int(bet_val)
                    if bet_val < 1 or bet_val > 2:
                        print('Valintasi ei ole kelvollinen')
                        print()
                    elif bet_val == 1 or bet_val == 2:
                        kelvollinen_veto=1
                elif bet_val.isnumeric()==False:
                    print('Valintasi ei ole kelvollinen')
                    print()
            return bet_val
        if bet_type == 8:
            
            while kelvollinen_veto==0:
                bet_list = []
                num1 = input("Ensimmäinen numero: ")
                if num1.isnumeric():
                    num1=int(num1)
                    if num1 < 0 or num1 > 36:
                        print('Valintasi ei ole kelvollinen')
                        print()
                    elif num1 >=0 or num1 <=36:
                        bet_list.append(num1)
                elif num1.isnumeric()==False:
                    print('Valintasi ei ole kelvollinen')
                    print()
                
                num2 = input("Toinen numero: ")
                if num2.isnumeric():
                    num2=int(num2)
                    if num2 < 0 or num2 > 36:
                        print('Valintasi ei ole kelvollinen')
                    elif num2 >=0 or num2 <=36:
                        bet_list.append(num2)
                        kelvollinen_veto = 1
                elif num2.isnumeric()==False:
                    print('Valintasi ei ole kelvollinen')
            return bet_list
        if bet_type == 9:
            
            while kelvollinen_veto==0:
                bet_list = []
                num1 = input("Ensimmäinen numero: ")
                if num1.isnumeric():
                    num1=int(num1)
                    if num1 < 0 or num1 > 36:
                        print('Valintasi ei ole kelvollinen')
                        print()
                    elif num1 >=0 or num1 <=36:
                        bet_list.append(num1)
                elif num1.isnumeric()==False:
                    print('Valintasi ei ole kelvollinen')
                    print()
                    
                num2 = int(input("Toinen numero: "))
                if num2.isnumeric():
                    num2=int(num2)
                    if num2 < 0 or num2 > 36:
                        print('Valintasi ei ole kelvollinen')
                    elif num2 >=0 or num2 <=36:
                        bet_list.append(num2)
                elif num2.isnumeric()==False:
                    print('Valintasi ei ole kelvollinen')
                    
                num3 = int(input("Kolmas numero: "))
                if num3.isnumeric():
                    num3=int(num3)
                    if num3 < 0 or num3 > 36:
                        print('Valintasi ei ole kelvollinen')
                    elif num3 >=0 or num3 <=36:
                        bet_list.append(num3)
                        kelvollinen_veto = 1
                elif num3.isnumeric()==False:
                    print('Valintasi ei ole kelvollinen')
            return bet_list
        if bet_type == 10:
            
            while kelvollinen_veto==0:
                bet_list = []
                num1 = int(input("Ensimmäinen numero: "))
                if num1.isnumeric():
                    num1=int(num1)
                    if num1 < 0 or num1 > 36:
                        print('Valintasi ei ole kelvollinen')
                        print()
                    elif num1 >=0 or num1 <=36:
                        bet_list.append(num1)
                elif num1.isnumeric()==False:
                    print('Valintasi ei ole kelvollinen')
                    print()
                    
                num2 = int(input("Toinen numero: "))
                if num2.isnumeric():
                    num2=int(num2)
                    if num2 < 0 or num2 > 36:
                        print('Valintasi ei ole kelvollinen')
                    elif num2 >=0 or num2 <=36:
                        bet_list.append(num2)
                elif num2.isnumeric()==False:
                    print('Valintasi ei ole kelvollinen')
                
                num3 = int(input("Kolmas numero: "))
                if num3.isnumeric():
                    num3=int(num3)
                    if num3 < 0 or num3 > 36:
                        print('Valintasi ei ole kelvollinen')
                    elif num3 >=0 or num3 <=36:
                        bet_list.append(num3)
                elif num3.isnumeric()==False:
                    print('Valintasi ei ole kelvollinen')
                
                num4 = int(input("Neljäs numero: "))
                if num4.isnumeric():
                    num4=int(num4)
                    if num4 < 0 or num4 > 36:
                        print('Valintasi ei ole kelvollinen')
                    elif num4 >=0 or num4 <=36:
                        bet_list.append(num4)
                        kelvollinen_veto = 1
                elif num4.isnumeric()==False:
                    print('Valintasi ei ole kelvollinen')
                
            return bet_list
        
        if bet_type == 11:
            while kelvollinen_veto==0:
                bet_list = []
                num1 = int(input("Ensimmäinen numero: "))
                if num1.isnumeric():
                    num1=int(num1)
                    if num1 < 0 or num1 > 36:
                        print('Valintasi ei ole kelvollinen')
                        print()
                    elif num1 >=0 or num1 <=36:
                        bet_list.append(num1)
                elif num1.isnumeric()==False:
                    print('Valintasi ei ole kelvollinen')
                    print()
                    
                num2 = int(input("Toinen numero: "))
                if num2.isnumeric():
                    num2=int(num2)
                    if num2 < 0 or num2 > 36:
                        print('Valintasi ei ole kelvollinen')
                    elif num2 >=0 or num2 <=36:
                        bet_list.append(num2)
                elif num2.isnumeric()==False:
                    print('Valintasi ei ole kelvollinen')
                
                num3 = int(input("Kolmas numero: "))
                if num3.isnumeric():
                    num3=int(num3)
                    if num3 < 0 or num3 > 36:
                        print('Valintasi ei ole kelvollinen')
                    elif num3 >=0 or num3 <=36:
                        bet_list.append(num3)
                elif num3.isnumeric()==False:
                    print('Valintasi ei ole kelvollinen')
                
                num4 = int(input("Neljäs numero: "))
                if num4.isnumeric():
                    num4=int(num4)
                    if num4 < 0 or num4 > 36:
                        print('Valintasi ei ole kelvollinen')
                    elif num4 >=0 or num4 <=36:
                        bet_list.append(num4)
                elif num4.isnumeric()==False:
                    print('Valintasi ei ole kelvollinen')
                    
                num5 = int(input("Viides numero: "))
                if num5.isnumeric():
                    num5=int(num5)
                    if num5 < 0 or num5 > 36:
                        print('Valintasi ei ole kelvollinen')
                    elif num5 >=0 or num5 <=36:
                        bet_list.append(num5)
                elif num5.isnumeric()==False:
                    print('Valintasi ei ole kelvollinen')
                
                num6 = int(input("Kuudes numero: "))
                if num6.isnumeric():
                    num6=int(num6)
                    if num6 < 0 or num6 > 36:
                        print('Valintasi ei ole kelvollinen')
                    elif num6 >=0 or num6 <=36:
                        bet_list.append(num6)
                        kelvollinen_veto = 1
                elif num6.isnumeric()==False:
                    print('Valintasi ei ole kelvollinen')

            return bet_list
        
        if bet_type == 12:
            while kelvollinen_veto==0:
                bet_list = ['00', '0', '1', '2', '3']
                kelvollinen_veto=1
            return bet_list
        
        if bet_type == 13:
            while kelvollinen_veto==0:
                bet_val = input("Minkä numeron valitset: 00, 0, 1-36?: ")
                if bet_val.isnumeric():
                    bet_val=int(bet_val)
                    if bet_val < 0 or bet_val > 36:
                        print('Valintasi ei ole kelvollinen')
                        print()
                    elif bet_val >= 0 or bet_val <= 36:
                        kelvollinen_veto=1
                elif bet_val.isnumeric()==False:
                    print('Valintasi ei ole kelvollinen')
                    print()
            return bet_val


    def adjusted_bankroll(result, balance, bet_val):
        balance -= bet
        print()
        print('.')
        time.sleep(1)
        print('..')
        time.sleep(1)
        print('...')
        time.sleep(1)
        # Adjust player balance for even/odd bets.
        if (bet_type == 1) and (bet_val == 1):  # Even
            if (int(result) % 2 == 0) and (int(result) != 0):
                payout = bet
                balance += bet + payout
                prompt = ("Voitit!\n"
                "Sinulla on nyt %s rahaa!") % balance
            else:
                prompt = ("Hävisit!\n"
                "Sinulla on nyt %s rahaa!") % balance
        if (bet_type == 1) and (bet_val == 2):  # Odd
            if int(result) % 2 == 1:
                payout = bet
                balance += bet + payout
                prompt = ("Voitit!\n"
                "Sinulla on nyt %s rahaa!") % balance
            else:
                prompt = ("Hävisit!\n"
                "Sinulla on nyt %s rahaa!") % balance
        # Adjust player balance for red/black bets.
        if (bet_type == 2) and (bet_val == 1):  # Red
            if slots[result] == 'red':
                balance += 2 * bet
                prompt = ("Voitit!\n"
                "Sinulla on nyt %s rahaa!") % balance
            else:
                prompt = ("Hävisit!\n"
                "Sinulla on nyt %s rahaa!") % balance
        if (bet_type == 2) and (bet_val == 2):  # Black
            if slots[result] == 'black':
                balance += 2 * bet
                prompt = ("Voitit!\n"
                "Sinulla on nyt %s rahaa!") % balance
            else:
                prompt = ("Hävisit!\n"
                "Sinulla on nyt %s rahaa!") % balance
        # Adjust player balance for the set of twelves.k
        if bet_type == 3:  # First Twelve
            if (int(result) >= 1) and (int(result) <= 12):
                balance += 3 * bet
                prompt = ("Voitit!\n"
                "Sinulla on nyt %s rahaa!") % balance
            else:
                prompt = ("Hävisit!\n"
                "Sinulla on nyt %s rahaa!") % balance
        if bet_type == 4:  # Second Twelve
            if (int(result) >= 13) and (int(result) <= 24):
                balance += 3 * bet
                prompt = ("Voitit!\n"
                "Sinulla on nyt %s rahaa!") % balance
            else:
                prompt = ("Hävisit!\n"
                "Sinulla on nyt %s rahaa!") % balance
        if bet_type == 5:  # Third Twelve
            if (int(result) >= 25) and (int(result) <= 36):
                balance += 3 * bet
                prompt = ("Voitit!\n"
                "Sinulla on nyt %s rahaa!") % balance
            else:
                prompt = ("Hävisit!\n"
                "Sinulla on nyt %s rahaa!") % balance
        # Adjust the player balance for the first and second set of eighteen.
        if bet_type == 6:  # First Eighteen
            if (int(result) >= 1) and (int(result) <= 18):
                balance += 2 * bet
                prompt = ("Voitit!\n"
                "Sinulla on nyt %s rahaa!") % balance
            else:
                prompt = ("Hävisit!\n"
                "Sinulla on nyt %s rahaa!") % balance
        if bet_type == 7:  # Second Eighteen
            if (int(result) >= 19) and (int(result) <= 36):
                balance += 2 * bet
                prompt = ("Voitit!\n"
                "Sinulla on nyt %s rahaa!") % balance
            else:
                prompt = ("Hävisit!\n"
                "Sinulla on nyt %s rahaa!") % balance
        # Adjust for betting multiple numbers at the same time.
        if bet_type == 8:  # Combination of two numbers
            if int(result) in bet_val:
                balance += 18 * bet
                prompt = ("Voitit!\n"
                "Sinulla on nyt %s rahaa!") % balance
            else:
                prompt = ("Hävisit!\n"
                "Sinulla on nyt %s rahaa!") % balance
        if bet_type == 9:  # Combination of three numbers
            if int(result) in bet_val:
                balance += 12 * bet
                prompt = ("Voitit!\n"
                "Sinulla on nyt %s rahaa!") % balance
            else:
                prompt = ("Hävisit!\n"
                "Sinulla on nyt %s rahaa!") % balance
        if bet_type == 10:  # Combination of four numbers
            if int(result-1) in bet_val:
                balance += 9 * bet
                prompt = ("Voitit!\n"
                "Sinulla on nyt %s rahaa!") % balance
            else:
                prompt = ("Hävisit!\n"
                "Sinulla on nyt %s rahaa!") % balance
        if bet_type == 11:  # Combination of six numbers
            if int(result) in bet_val:
                balance += 6 * bet
                prompt = ("Voitit!\n"
                "Sinulla on nyt %s rahaa!") % balance
            else:
                prompt = ("Hävisit!\n"
                "Sinulla on nyt %s rahaa!") % balance
        if bet_type == 12:  # Combination of 00-0-1-2-3
            if result in bet_val:
                balance += 7 * bet
                prompt = ("Voitit!\n"
                "Sinulla on nyt %s rahaa!") % balance
            else:
                prompt = ("Hävisit!\n"
                "Sinulla on nyt %s rahaa!") % balance
        # Adjust player balance if bet a single number.
        if bet_type == 13:
            if result == bet_val:
                payout = 36 * bet
                balance += payout
                prompt = ("Voitit!\n"
                "Sinulla on nyt %s rahaa!") % balance
            else:
                prompt = ("Hävisit!\n"
                "Sinulla on nyt %s rahaa!") % balance

        global bankroll
        bankroll = balance

        return (prompt, bankroll)

    keep_playing = 'yes'
    while (keep_playing.lower() == 'yes') or (keep_playing.lower() == 'y'):
        #saldon tarkistus
        if raha<=0:
            print('Sinulla ei ole tarpeeksi rahaa.')
            input('Paina Enter.')
            print()
            print('Ladataan valikkoa...')
            time.sleep(1)
            print()
            return raha

        bet = 0
        panos_annettu=0
        while panos_annettu==0:
            print('Sinulla on rahaa:',raha)
            bet=input('Anna panos: ')
            if bet.isnumeric():
                bet= int(bet)
                if bet>raha:
                    print('Sinulla ei ole näin paljon rahaa.')
                    print ()
                elif bet<=0:
                    print('Sinun on pakko asettaa panos.')
                    print ()
                else:
                    panos_annettu = 1
            elif bet.isnumeric()==False:
                print('Antamasi panos ei ole kelvollinen')
                print()
        print()

        valinta=0
        while valinta==0: 
            print("(1) Parillinen/Pariton\n"
                                 "(2) Punainen/Musta\n"
                                 "(3) Ensimmäinen kaksitoista (1-12)\n"
                                 "(4) Toinen kaksitoista (13-24)\n"
                                 "(5) Kolmas kaksitoista (25-36)\n"
                                 "(6) Ensimmäinen kahdeksantoista (1-18)\n"
                                 "(7) Toinen kahdeksantoista (19-36)\n"
                                 "(8) Kahden numeron yhdistelmä\n"
                                 "(9) Kolmen numeron yhdistelmä\n"
                                 "(10) Neljän numeron yhdistelmä\n"
                                 "(11) Kuuden numeron yhdistelmä\n"
                                 "(12) 1-2-3-0-00 yhdistelmä\n"
                                 "(13) Valitse yksi numero)")
            print()
            bet_type = input("Minkälainen veto? Valitse yksi yllä annettu numero: ")
            if bet_type.isnumeric():
                bet_type=int(bet_type)
                if bet_type < 1 or bet_type > 13:
                    print('Valintasi ei ole kelvollinen.')
                    print()
                else:
                    valinta=1
            elif bet_type.isnumeric() == False:
                print('Valintasi ei ole kelvollinen.')
                print()

        spins2 = spins()

        slots2 = {'00': 'Vihreä', '0': 'Vihreä', '1': 'Musta', '2': 'Punainen',
                 '3': 'Musta', '4': 'Musta', '5': 'Punainen', '6': 'Musta', '7': 'Punainen',
                 '8': 'Musta', '9': 'Punainen', '10': 'Musta', '11': 'Punainen',
                 '12': 'Punainen', '13': 'Musta', '14': 'Punainen', '15': 'Musta',
                 '16': 'Musta', '17': 'Punainen', '18': 'Musta', '19': 'Punainen',
                 '20': 'Punainen', '21': 'Musta', '22': 'Punainen', '23': 'Musta',
                 '24': 'Musta', '25': 'Punainen', '26': 'Musta', '27': 'Punainen',
                 '28': 'Punainen', '29': 'Musta', '30': 'Punainen', '31': 'Musta',
                 '32': 'Musta', '33': 'Punainen', '34': 'Musta', '35': 'Punainen',
                 '36': 'Punainen'}
        color=slots2[spins2]
        
        (prmpt, balance) = adjusted_bankroll(spins2, bankroll, bet_value(bet_type))
        print("\nVoittava numero on:", color, "%s!" % spins2)
        print(prmpt)
        bankroll = balance
        raha=balance

        #uusi peli?
        uusiPeli=input('Haluatko pelata uudelleen? (k/e) ')
        uusiPeli=uusiPeli.lower()
        if uusiPeli!='k':
            print()
            print('Ladataan valikkoa...')
            time.sleep(1)
            print()
            return raha
        print()
        continue


#Pelikone
#Tekijä: Tommi
def Pelikone(raha):
    print('Ladataan peliä...')
    time.sleep(1)
    print()

    ohje=input('Haluatko lukea ohjeet? (k/e) ')
    ohje=ohje.lower()
    if ohje == 'k':
        print("Peliautomaattiin annetaan panos.")
        print("Peliautomaatista pitää tulla kolme samaa sanaa, jotta pelaaja voittaa.")
        print("Pelaajan antama panos toimii kertoimena, joka kertoo voitto määrän.")
    print()
    print()

    #Voitto pöytä
    print("Voittojen perusarvot (Panos: 1 raha)")
    print("Puu = 2 rahaa.")
    print("Sydän = 5 rahaa.")
    print("Mansikka = 15 rahaa.")
    print("Kello = 25 rahaa.")
    print("Appelsiini = 50 rahaa.")
    print("Kolikko = 250 rahaa.")
    print("Apila = 500 rahaa")
    print("Seitsemän kertaa pelaajan antaman panoksen kahdella(perusarvo).")
    print(" ")
    print(" ")

    int1 = 0
    int2 = 0
    int3 = 0

    roll = " "
    roll2 = " "
    roll3 = " "

    #Kysyy pelaako pelaaja.
    #Tarkistaa pelaajan raha määrän.
    #Kysyy pelaajaa antamaan panoksen rahasta ja tarkistaa, että panos on suurempin kuin nolla.
    #Tarkistaa, että pelaaja ei voi antaa suurempaa panosta kuin pelaajalla on rahaa.
    while True:
        voitto_og=False
        #saldon tarkistus
        if raha<=0:
            print('Sinulla ei ole tarpeeksi rahaa.')
            input('Paina Enter.')
            print()
            print('Ladataan valikkoa...')
            time.sleep(1)
            print()
            return raha
        
        #panos
        panos=0
        vastaus='k'
        panos_annettu=0
        while panos_annettu==0:
            print('Sinulla on rahaa:',raha)
            panos=input('Anna panos: ')
            if panos.isnumeric():
                panos = int(panos)
                if panos>raha:
                    print('Sinulla ei ole näin paljon rahaa.')
                    print ()
                elif panos<=0:
                    print('Sinun on pakko asettaa panos.')
                    print ()
                else:
                    panos_annettu = 1
            elif panos.isnumeric()==False:
                print('Antamasi panos ei ole kelvollinen')
                print()        
        raha = raha - panos

        print ()
        print("Vedätään peliautomaattia.")
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)

    #Arpoo int arvoille arvon yhdestä kahdeksaan.
        int1 = random.randrange(1, 9, 1)
        int2 = random.randrange(1, 9, 1)
        int3 = random.randrange(1, 9, 1)

        
    #Antavat roll arvoille arvon int arvon perusteella.
        match int1:
            case 1:
                roll = "Puu"
            case 2:
                roll = "Sydän"
            case 3:
                roll = "Seitsemän"
            case 4:
                roll = "Appelsiini"
            case 5:
                roll = "Kolikko"
            case 6:
                roll = "Kello"
            case 7:
                roll = "Mansikka"
            case 8:
                roll = "Apila"

        match int2:
            case 1:
                roll2 = "Puu"

            case 2:
                roll2 = "Sydän"
                
            case 3:
                roll2 = "Seitsemän"
                
            case 4:
                roll2 = "Appelsiini"
                
            case 5:
                roll2 = "Kolikko"
                
            case 6:
                roll2 = "Kello"
                
            case 7:
                roll2 = "Mansikka"
                
            case 8:
                roll2 = "Apila"
                

        match int3:
            case 1:
                roll3 = "Puu"
                
            case 2:
                roll3 = "Sydän"
                
            case 3:
                roll3 = "Seitsemän"
                
            case 4:
                roll3 = "Appelsiini"
              
            case 5:
                roll3 = "Kolikko"
                
            case 6:
                roll3 = "Kello"
                
            case 7:
                roll3 = "Mansikka"
                
            case 8:
                roll3 = "Apila"

        print(roll, roll2, roll3)
        print('')

    #Tarkistaa, onko roll arvot samat.
        if roll == roll2 and roll == roll3:
            print ("Voitit!")
            voitto_og = True
        else:
            print('Hävisit!')
            print ("Hävisit", panos, 'rahaa.')
            print("------")

    #Jakaa raha palkinnon roll arvon perusteella.
        voitto=0
        if voitto_og == True:
            match roll:
                case "Puu":
                    voitto = 2 * panos
                    raha = raha + voitto
                    print('Voitit', voitto, 'rahaa!')
                    print ("Sinulla on nyt ", raha, " rahaa!")
                    print ("------")
                    print(" ")

                case "Sydän":
                    voitto = 5 * panos
                    raha = raha + voitto
                    print('Voitit', voitto, 'rahaa!')
                    print ("Sinulla on nyt ", raha, " rahaa!")
                    print ("------")
                    print(" ")

                case "Seitsemän":
                    voitto = panos * 2 * panos
                    raha = raha + voitto
                    print('Voitit', voitto, 'rahaa!')
                    print ("Sinulla on nyt ", raha, " rahaa!")
                    print ("------")
                    print(" ")

                case "Appelsiini":
                    voitto = 50 * panos
                    raha = raha + voitto
                    print('Voitit', voitto, 'rahaa!')
                    print ("Sinulla on nyt ", raha, " rahaa!")
                    print ("------")
                    print(" ")

                case "Kolikko":
                    voitto = 250 * panos
                    raha = raha + voitto
                    print('Voitit', voitto, 'rahaa!')
                    print ("Sinulla on nyt ", raha, " rahaa!")
                    print ("------")
                    print(" ")
                    
                case "Kello":
                    voitto = 25 * panos
                    raha = raha + voitto
                    print('Voitit', voitto, 'rahaa!')
                    print ("Sinulla on nyt ", raha, " rahaa!")
                    print(" ")
                    
                case "Mansikka":
                    voitto = 15 * panos
                    raha = raha + voitto
                    print('Voitit', voitto, 'rahaa!')
                    print ("Sinulla on nyt ", raha, " rahaa!")
                    print ("------")
                    print(" ")

                case "Apila":
                    voitto = 500 * panos
                    raha = raha + voitto
                    print('Voitit', voitto, 'rahaa!')
                    print ("Sinulla on nyt ", raha, " rahaa!")
                    print ("------")
                    print(" ")

        print('Sinulla on nyt', raha, 'rahaa.')
        print()

        #uusi peli?
        uusiPeli=input('Haluatko pelata uudelleen? (k/e) ')
        uusiPeli=uusiPeli.lower()
        if uusiPeli!='k':
            print()
            print('Ladataan valikkoa...')
            time.sleep(1)
            print()
            return raha
        print()
        continue




#Venäläinen ruletti
#Tekijä: Niklas
def Venäläinen_ruletti(raha):
    print('Ladataan peliä...')
    time.sleep(1)
    print()

    #saldon tarkistus
    if raha < 5000:
        print('Sinulla pitää olla vähintään 2500 rahaa pelataksesi tätä peliä.')
        print('Sinulta puuttuu', 2500-raha, 'rahaa.')
        input('Paina Enter.')
        print()
        print('Ladataan valikkoa...')
        time.sleep(1)
        print()
        return raha

    #peli
    elif raha >= 5000:
        vastaus=input('Oletko varma? (k/e) ')
        vastaus=vastaus.lower()
        if vastaus=='k':
            chamber=random.randint(1,7)
            print('.')
            time.sleep(1)
            print('..')
            time.sleep(1)
            print('...')
            time.sleep(1)
            print('....')
            time.sleep(1)
            print('.....')
            time.sleep(1)
            #voitto
            if chamber==1:
                print('Voitit', raha, 'rahaa!')
                raha=raha*2
                print()
                print('Ladataan valikkoa...')
                time.sleep(1)
                print()
                return raha
            #häviö
            else:
                print('Hävisit', raha, 'rahaa!')
                raha=raha*0
                print()
                print('Ladataan valikkoa...')
                time.sleep(1)
                print()
                return raha
        else:
            print()
            print('Ladataan valikkoa...')
            time.sleep(1)
            print()
            return raha
        
    



raha=10

#Valikko
while True:
    kelvollinenVastaus=0
    while kelvollinenVastaus != 1:
        print()
        print('Tervetuloa CMD Casinoon!')
        print()

        #saldon tarkistus
        if raha <= 0:
            print('Sinulla ei ole yhtään rahaa.')
            sulku=input('Paina Enter. ')
            if sulku == "res":
                raha=raha+20
                print()
                print('Ladataan...')
                time.sleep(1)
                print()
                continue
            print()
            print('Suljetaan peliä...')
            kelvollinenVastaus=1
            time.sleep(1)
            break
        print('Sinulla on', raha, 'rahaa.')
        print()

        #pelit ja valinta
        print('Pelit:')
        print('(1) Ventti')
        print('(2) Numeron Arvaus')
        print('(3) Ruletti')
        print('(4) Pelikone')
        print('(5) Venäläinen Ruletti')
        print()
        print('(0) Sulje peli')
        print()

        peliValinta=input('Valitse peli: ')
        peliValinta=peliValinta.lower()
        print()
        
        #valinnan tarkistus
        if peliValinta == '1':
            raha=Ventti(raha)
        elif peliValinta == '2':
            raha=Numeron_arvaus(raha)
        elif peliValinta == '3':
            raha=Ruletti(raha)
        elif peliValinta == '4':
            raha=Pelikone(raha)
        elif peliValinta == '5':
            raha=Venäläinen_ruletti(raha)
        elif peliValinta == '0':
            print('Suljetaan peliä...')
            time.sleep(1)
            break
        else:
            print('Valitsemaasi peliä ei löytynyt.')
            print()
            print()
            continue
    break
