import random
import time
def poczatek():
    punkty = 0
    tryb = 0        
    ocena = 0
    ocena2 = 0
    tryb_2 = 0
    jeden = 0
    dwa = 0
    tryb_3 = 0
    x = 0
    koniec = 0
    tryb_konwersja = 0




    
    def pyt_koniec ():
            
        koniec = input()
                

        if koniec == "Nie":
            exit()

        elif koniec == "Tak":
            time.sleep(0.5)
            print ()
            time.sleep(0.5)
            print ()
            time.sleep(0.5)
            print ()
            poczatek()
                

        else:
            
            print ("Napisz Tak lub Nie!")
            time.sleep(0.3)
            pyt_koniec()




    print ("================NAUKA TABLICZKI MNOŻENIA BETA v. 1.5================")

    time.sleep(1.5)

    print ()

    time.sleep(1.5)

    print ("Wybierz tryb:")

    time.sleep(1.5)
    
    print ("1 = 10 pytań (z oceną)")

    time.sleep(1.5)

    print ("2 = ? pytań (bez oceny)")

    time.sleep(1.5)

    print ("3 = nieskończoność pytań (bez oceny)")


    tryb = int(input())

    




    time.sleep(1.5)
    print ()
    time.sleep(0.5)
    print ()
    time.sleep(1.5)


        
    if tryb == 1:

    
    
        for x in range (0, 10):

            jeden = random.randint(1,10)
            dwa = random.randint(1,10)

            praw_wyn = jeden * dwa

            time.sleep(1.5)
        
            print ("Pytanie nr. ", x+1)

            time.sleep(1.5)
    
            print (jeden, " * ", dwa, " = ", end=" ")
        
            wynik = int(input())

            time.sleep(1)

            if wynik == praw_wyn:
                print ("Brawo, podałeś/aś dobry wynik!")
                time.sleep(0.5)
                print ()
            
                punkty = punkty + 1
        
    
            else:
                print ("Musisz jeszcze poćwiczyć,")
        
                time.sleep(1)
        
                print ("bo prawidłowy wynik to %s." %praw_wyn)
                time.sleep(0.5)
                print ()



        if punkty < 4:
            ocena = niedostateczny

        elif punkty == 4:
            ocena = dopuszczajączy
    
        elif punkty == 5 or punkty ==6:
            ocena = dostateczny

        elif punkty == 7 or punkty == 8:
            ocena = dobry

        elif punkty == 9:
            ocena = bardzo
            ocena2 = dobry

        else:
            ocena = celujący


        time.sleep(2)

        if punkty == 9:
        
            print("Twoja ocena to: %s %s" %(ocena, ocena2))

        else:
            print("Twoja ocena to: %s" %ocena)

            time.sleep(1)

            print ("Twoje punkty to: %s" %punkty)

        time.sleep(0.5)
        print ()
        time.sleep(0.5)
        print ()
        time.sleep(0.5)
        print ("Zakończono! Czy chcesz kontynuować? Napisz Tak lub Nie.")


        pyt_koniec()
        



    elif tryb == 2:

        time.sleep(1)
    
        tryb_2 = int(input("Podaj ilość pytań to wykonania: "))

        print ()
        time.sleep(0.5)
        print ()
        time.sleep(0.5)
    
        for x in range (0, tryb_2):

            
            jeden = random.randint(1,10)
            dwa = random.randint(1,10)
    
            praw_wyn = jeden * dwa
    
            time.sleep(1.5)
        
            print ("Pytanie nr. ", x+1)
    
            time.sleep(1.5)
    
            print (jeden, " * ", dwa, " = ", end=" ")
    
            wynik = int(input())

            time.sleep(1)

            if wynik == praw_wyn:
                print ("Brawo, podałeś/aś dobry wynik!")
                time.sleep(0.5)
                print ()

        
            else:
                print ("Musisz jeszcze poćwiczyć,")
        
                time.sleep(1)
            
                print ("bo prawidłowy wynik to %s." %praw_wyn)
                time.sleep(0.5)
                print ()



        time.sleep(0.5)
        print ()
        time.sleep(0.5)
        print ()
        time.sleep(0.5)
        print ("Zakończono! Czy chcesz kontynuować? Napisz Tak lub Nie.")


        pyt_koniec()
        

    

    elif tryb == 3:
        
                while tryb_3 == 0:
        

            
                    jeden = random.randint(1,10)
                    dwa = random.randint(1,10)
    
                    praw_wyn = jeden * dwa

                    time.sleep(1.5)
    
                    print ("Pytanie nr. ", x+1)

                    x = x+1

                    time.sleep(1.5)
        
                    print (jeden, " * ", dwa, " = ", end=" ")
        
                    wynik = int(input())
    
                    time.sleep(1)

                    if wynik == praw_wyn:
                        print ("Brawo, podałeś/aś dobry wynik!")
                        time.sleep(0.5)
                        print ()

        
                    else:
                        print ("Musisz jeszcze poćwiczyć,")
        
                        time.sleep(1)
            
                        print ("bo prawidłowy wynik to %s." %praw_wyn)
                        time.sleep(0.5)
                        print ()
    
    

   
    




poczatek() 
