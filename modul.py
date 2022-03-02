import re


class Kutya:
    def __init__(self, nev, fajta, eletkor):
        self.nev = nev
        self.fajta = fajta
        self.eletkor = int(eletkor)

def kutyalista():
    kutyak = []
    print('add meg a kutyád adatait!')
    print('ha valamelyiket üresen hagyod a bekérés befejeződik')
    no = 1 
    while True:
        print(f'add meg az {no}. kutya adatait')
        n = input('\tneve: ')
        if len(n) == 0: break
        f = input('\tfajtaja: ')
        if len(f) == 0: break
        k = input('\tkora: ')
        if len(k) == 0: break
        kutyak.append(Kutya(n, f, k ))
        no += 1
    return kutyak

def vizslak_szama(kutyak):
    c = 0
    for k in kutyak:
        if k.fajta == 'vizsla':
            c += 1
    return c 

def legoregebb_kutya_fajtaja(kutyak):
    maxi = 0 
    for i in range(1, len(kutyak)):
        if kutyak [i].eletkor > kutyak[maxi].eletkor:
            maxi = i
            return kutyak[maxi].fajta 
        
def osszes_T_fajtaju(kutya, ker_fajta):
    kutyanevek = []
    for k in kutya:
        if k.kutya.lower() == ker_fajta.lower():
            kutyanevek.append(k.nev)
    if len(kutyanevek) == 0:
            print(f'nicns {ker_fajta} fajtájú')
    else: print(f'{kutyanevek} mind {ker_fajta}')



