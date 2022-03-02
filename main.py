import modul as n

kutyamenhely = n.kutyalista()

#teszt
print(f'a menhelyen {len(kutyamenhely)} kutyus van')

#1.feladat

print(f'a vizslák száma a menhelyen {n.vizslak_szama(kutyamenhely)}')

#2.

print(f'legöregebb {n.legoregebb_kutya_fajtaja(kutyamenhely)}')

#3.

fajta = input('milyen fajtájú kutyát keresel? ')
n.osszes_T_fajtaju(kutyamenhely,fajta)
