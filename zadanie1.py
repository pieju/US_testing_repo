import datetime
imię=input('podaj imię')
print(imię)
wiek=int(input('podaj wiek'))
print(wiek)
dzisiaj = datetime.date.today()
rok=dzisiaj.year
if wiek>rok:
    print("Mów mi python, mam 32 lat. Witaj w moim świecie", imię , "Jesteś starszy ode mnie.")
else:
    print("Mów mi python, mam 32 lat. Witaj w moim świecie", imię , "Jesteś młodszy ode mnie.")