import pyautogui as pa
import os
import webbrowser as m
import time


def abrirChrome():
    print('Abriendo chrome')
    url = "instagram.com"
    m.register('chrome', None, m.BackgroundBrowser(
        "C://Users//Fran//AppData//Local//Google//Chrome//Application//chrome.exe"))
    h = m.get('chrome')
    h.open(url)


def darLike():
    cont = 0
    for i in range(5):
        print("ejecucion numero: ", i)
        time.sleep(1)
        try:
            pa.click('corazon.png')
            cont += 1
        except TypeError:
            print("No se pudo dar like")
        time.sleep(1)
        pa.press('pagedown')
    return cont


def sacarLike():
    cont = 0
    for i in range(5):
        print("ejecucion numero: ", i)
        time.sleep(1)
        try:
            pa.click('c2.png')
            cont += 1
        except TypeError:
            print("No se pudo quitar like")
        time.sleep(1)
        pa.press('pagedown')
    return cont


def main():

       print('Ejecucion')

       print("1 - Dar likes")
       print("2 - Sacar likes")
       n = int(input("ingresa opcion: "))

       abrirChrome()

       if(n == 1):
              print("opcion dar likes")
              cont = darLike()
       else:
              print("opcion sacar like")
              cont = sacarLike()

       print("cantidad likes dados: ", cont)
       os.system("pause")


if __name__ == "__main__":
    main()


'''print("posicion es --> ",pa.position())'''

'''print(pa.KEYBOARD_KEYS) --> MUESTRA TECLADAS DISPONIBLES'''
