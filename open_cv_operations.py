import sys

import cv2
import imutils as imutils
from cv2 import imread, imwrite, rotate, ROTATE_90_CLOCKWISE
from numpy import integer
from pip._vendor.distlib.compat import raw_input


def load_image():
    img = cv2.imread('photo.jpg', cv2.IMREAD_UNCHANGED)

    cv2.imshow('image', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img


def resize_image(img):
    while True:

        print("1 - Nie zmieniaj wielkości obrazu\n"
              "2 - Zmniejsz obraz o 50%\n"
              "3 - Zmniejsz obraz o 30%\n"
              "9 - exit\n"
              "\nWybierz: ", end='')

        code = input()

        if code == '1':
            print('\nBrak działań na obrazie...')
            scale_percent = 100  # percent of original size
            print('Original Dimensions : ', img.shape)
            break
        elif code == '2':
            print('\nZmniejsz obraz o 50%...')

            print('Original Dimensions : ', img.shape)
            scale_percent = 50  # percent of original size

            break
        elif code == '3':
            print('\nZmniejsz obraz o 30%...')

            print('Original Dimensions : ', img.shape)
            scale_percent = 70  # percent of original size

            break
        elif code == '9':
            sys.exit()
        else:
            print("Error - zła ")

    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    imwrite('photo2.jpg', img)  # zapisz miany w systemie plików
    cv2.imshow("zdjecie po obrocie", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img


def rotate_image(img):
    while True:

        print("1 - nie obracaj obrazu\n"
              "2 - obróc obraz o 90 stopni zgodnie z ruchem wskazówek\n"
              "3 - obróc obraz o 90 stopni zgodnie przeciwnie do ruchu wskazówek\n"
              "4 - obróc obraz o podaną wartość kątową\n"
              "9 - exit\n"
              "\nWybierz: ", end='')

        code = input()
        cv2.destroyAllWindows()

        if code == '1':
            print('\nBrak działań na obrazie...')
            cv2.imshow("zdjecie po obrocie", img)
            break
        elif code == '2':
            print('\nObracanie obrazu o 90 stopni zgodnie z ruchem wskazówek...')

            img = rotate(img, ROTATE_90_CLOCKWISE)  # obróć obrazek
            cv2.imshow("zdjecie po obrocie", img)

            break
        elif code == '3':
            print('\nObracanie obrazu o 90 stopni przeciwnie do ruchu wskazówek...')

            img = imutils.rotate(img, 270)  # obróć obrazek
            cv2.imshow("zdjecie po obrocie", img)
            break
        elif code == '4':
            print('\nPodaj wartość w kątach do obrotu...')
            angle = int(input())
            img = imutils.rotate(img, angle)  # obróć obrazek

            cv2.imshow("zdjecie po obrocie", img)
            break
        elif code == '9':
            sys.exit()
        else:
            print("Error - zły numer ")

    imwrite('photo2.jpg', img)  # zapisz miany w systemie plików
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img


def change_color_image(img):
    while True:

        print("1 - nie zmieniaj kolorów\n"
              "2 - czarno-biały obraz\n"
              "3 - negatyw\n"
              "4 - rozmazanie\n"
              "9 - exit\n"
              "\nWybierz: ", end='')

        code = input()
        cv2.destroyAllWindows()

        if code == '1':

            print('\nBrak działań na obrazie...')

            break
        elif code == '2':
            print('\nObracanie obrazu o 90 stopni zgodnie z ruchem wskazówek...')
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imshow("zdjecie po obrocie", img)
            break
        elif code == '3':
            print('\nObracanie obrazu o 90 stopni przeciwnie do ruchu wskazówek...')

            img = cv2.bitwise_not(img)
            cv2.imshow("negatyw", img)
            break
        elif code == '4':
            print('\nRozmazanie...')

            img = cv2.GaussianBlur(img,(5,5),0)

            cv2.imshow("negatyw", img)
            break
        elif code == '9':
            sys.exit()
        else:
            print("Error - zły numer ")

    imwrite('photo2.jpg', img)  # zapisz miany w systemie plików
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img
