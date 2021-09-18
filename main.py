
from random import randint as rand
from time import sleep

MAX_VAULE_TO_RANDRANGE = 100
MIN_VAULE_TO_RANDRANGE = 1
GAMER_SCORE = 0
GAMER_FAIL = 0
IS_PROGRAM_RUN = True
IS_PLAY_GAME = False


IS_BONUS_SEEING = False
IS_BONUS_BUGGER = False

RandVal = 0

def printNewLine():
    print(" ")

def printRules():

    print("Zasady:")
    print("Komputer losuje liczbę z przedziału:" ,str(MIN_VAULE_TO_RANDRANGE) +", " + str(MAX_VAULE_TO_RANDRANGE))
    print("Twoim zadaniem jest odgadnąć tą liczbę z jak najmniejszą liczbą pomyłek")
    print("Za każda wygraną dostajesz punkty im mniejsza")
    print("Im mniejsza liczba błędów tym wiecej punktów otrzymujesz")

def printMenu():
    print("Menu")
    print("G - Graj")
    print("S - Sklep")
    print("Z - Sprawdź zasady")
    print("P - Sprawdź punkty")
    print("E - Exit")





def showShop():
    if IS_BONUS_SEEING == False:
        print("W - (Widzący) Koszt 100 punktów")
    else:
        print("Widzący - Wykupione")
    if IS_BONUS_BUGGER == False:
        print("B - (Bugger) Koszt 50 punktów")
    else:
        print("Bugger - Wykupione")
    print("E - Exit")


def zapisz():
    plik = open("Zapis.txt", "w")
    if plik.writable():
        plik.write("Score=" + str(getScore()) + "\n")
        plik.write("Seeing=" + str(IS_BONUS_SEEING) + "\n")
        plik.write("Bugger=" + str(IS_BONUS_BUGGER) + "\n")
    plik.close()

def wczytajZapisz():
    try:
        plik = open("Zapis.txt", "r")
    except FileNotFoundError:
        plik = open("Zapis.txt", "w")
        if plik.writable():
            plik.write("Score=0\n")
            plik.write("Seeing=False\n")
            plik.write("Bugger=False\n")
        plik.close()
        plik = open("Zapis.txt", "r")



    if plik.readline():
        for i in plik:


            Scrstr = ""
            pierw = ""
            for x in i:

                if pierw != "Score" and pierw != "Seeing" and pierw != "Bugger":
                    pierw += x

                else:
                    if x == "=":
                        continue

                    if pierw == "Score":

                        if i.index("\n") == i.index(x):

                            Scr = int(Scrstr)

                        else:

                            Scrstr += str(x)

                            continue
                        try:
                            global GAMER_SCORE
                            GAMER_SCORE = Scr
                        except TypeError:
                            GAMER_SCORE = 0
                            print("Błąd odczytu punktów")
                        break
                    if pierw == "Seeing":
                        global IS_BONUS_SEEING
                        Scr = x
                        if Scr == "T":
                            IS_BONUS_SEEING = True
                        else:
                            IS_BONUS_SEEING = False

                        break
                    if pierw == "Bugger":
                        global IS_BONUS_BUGGER
                        Scr = x
                        if Scr == "T":
                            IS_BONUS_BUGGER = True
                        else:
                            IS_BONUS_BUGGER = False

                        break


    plik.close()

def getScore():
    return GAMER_SCORE

def getFail():
    return GAMER_FAIL





while IS_PROGRAM_RUN:
    if IS_PLAY_GAME:

        if RandVal == 0:
            print("Komputer losuje liczbę...")
            RandVal = rand(MIN_VAULE_TO_RANDRANGE, MAX_VAULE_TO_RANDRANGE)
            sleep(2)
            print("Liczba została wylosowana")

        if RandVal > 0:
            printNewLine()

            printNewLine()
            if IS_BONUS_SEEING == True:
                print("Bonus widzący jest aktywny odaj liczbę wieksza od "+ str(MIN_VAULE_TO_RANDRANGE + 21) + " i mniejsza od "  + str(MAX_VAULE_TO_RANDRANGE - 21))
            else:
                print("Podaj liczbę")
            printNewLine()

            try:
                 lp = int(input(">> "))
            except ValueError:
                 GAMER_FAIL += 1
                 print("Podałeś błędną wartość! Błędy: ",str(getFail()))
                 continue

            printNewLine()
            if lp > RandVal:
                GAMER_FAIL += 1
                sleep(1)
                if IS_BONUS_SEEING == True:
                    if lp > MIN_VAULE_TO_RANDRANGE + 20 and lp < MAX_VAULE_TO_RANDRANGE - 20:

                        print("(Widzący)")

                        if lp - 10 > RandVal:
                            print("Liczba o 10 miejsza od podanej jest większa od wylosowanej")
                        elif lp - 10 < RandVal:
                            print("Liczba o 10 miejsza od podanej jest mniejsza od wylosowanej")
                        else:
                            print("Liczba o 10 miejsza od podanej jest tą właściwą")

                        if lp - 20 > RandVal:
                            print("Liczba o 20 miejsza od podanej jest większa od wylosowanej")
                        elif lp - 20 < RandVal:
                            print("Liczba o 20 miejsza od podanej jest mniejsza od wylosowanej")
                        else:
                            print("Liczba o 20 miejsza od podanej jest tą właściwą")


                        print("Podana liczba jest zbyt duza! (Fail: " + str(getFail()) + ")")



                        IS_BONUS_SEEING = False
                    else:
                        print("Błędna wartość")
                        continue

                else:
                    print("Podana liczba jest zbyt duza! (Fail: " + str(getFail()) +")")
                    continue
            elif lp < RandVal:
                GAMER_FAIL += 1
                sleep(1)

                if IS_BONUS_SEEING == True:
                    if lp > MIN_VAULE_TO_RANDRANGE + 20 and lp < MAX_VAULE_TO_RANDRANGE - 20:
                        print("(Widzący)")

                        if lp + 10 > RandVal:
                            print("Liczba o 10 większa od podanej jest większa od wylosowanej")
                        elif lp - 10 < RandVal:
                            print("Liczba o 10 większa od podanej jest mniejsza od wylosowanej")
                        else:
                            print("Liczba o 10 większa od podanej jest tą właściwą")

                        if lp + 20 > RandVal:
                            print("Liczba o 20 większa od podanej jest większa od wylosowanej")
                        elif lp - 20 < RandVal:
                            print("Liczba o 20 większa od podanej jest mniejsza od wylosowanej")
                        else:
                            print("Liczba o 20 większa od podanej jest tą właściwą")



                        print("Podana liczba jest zbyt mała! (Fail: " + str(getFail()) + ")")

                        IS_BONUS_SEEING = False
                    else:
                        print("Błędna wartość")
                        continue
                else:
                    print("Podana liczba jest zbyt mała! (Fail: " + str(getFail()) + ")")
                continue
            else:
                if IS_BONUS_BUGGER == True:
                    wynik = 100 // 3
                    sleep(1)
                    print("Gratulacje! wygrałeś, Twoja liczba porażek wynosi: 3 (Bugger)")
                    IS_BONUS_BUGGER = False
                else:
                    wynik = 100 // getFail()
                    sleep(1)
                    print("Gratulacje! wygrałeś, Twoja liczba porażek wynosi: " + str(getFail()))

                print("Otrzymujesz: " + str(wynik))

                GAMER_SCORE += wynik
                GAMER_FAIL = 0
                RandVal = 0
                print("Masz: " + str(getScore()) + " Punktów")
                zapisz()
                print("Czy chcesz spróbować jeszcze raz? (tak/nie)")
                odp = input(">> ")
                if odp.lower() == "tak":
                    continue
                elif odp.lower() == "nie":
                    IS_PLAY_GAME = False
                    zapisz()

                    continue
        else:
            print("Błąd losowania!")
            continue
    else:
        printMenu()
        printNewLine()
        wczytajZapisz()
        print("Co chcesz zrobić?")
        wl = input(">> ")

        if wl.lower()  == "g":


            IS_PLAY_GAME = True
            continue
        elif wl.lower() == "s":
            print("Posiadasz: " + str(getScore()) + " punktów")
            printNewLine()
            showShop()
            printNewLine()
            print("Co chcesz zrobić?")
            wl = input(">> ")
            if wl.lower() == "w":
                if IS_BONUS_SEEING == False:
                    if getScore() >= 100:
                        IS_BONUS_SEEING = True
                        GAMER_SCORE -= 100
                        zapisz()
                        print("Wykupiłes bonus widzącego!")
                        continue
                    else:
                        print("Masz za mało punktów!")
                        continue
                else:
                    print("Posiadasz juz ten bonus!")
                    continue
            if wl.lower() == "b":
                if IS_BONUS_BUGGER == False:
                    if getScore() >= 50:
                        IS_BONUS_BUGGER = True
                        GAMER_SCORE -= 100
                        zapisz()
                        print("Wykupiłes bonus widzącego!")
                        continue
                    else:
                        print("Masz za mało punktów!")
                        continue
                else:
                    print("Posiadasz juz ten bonus!")
                    continue
            elif wl.lower() == "e":
                continue
        elif wl.lower() == "z":
            printRules()
            printNewLine()
            continue
        elif wl.lower()  == "p":
            printNewLine()
            print("Posiadasz " + str(getScore()) + " Punktów")
            printNewLine()
            continue
        elif wl.lower() == "e":
            break
        else:
            continue
