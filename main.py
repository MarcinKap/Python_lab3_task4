import sys

import cv2
import img as img

from open_cv_operations import load_image, resize_image, rotate_image, change_color_image


def main():
    while True:

        print("1 - wczytaj obraz\n"
              "9 - exit\n"
              "\nWybierz: ", end='')

        code = input()

        if code == '1':
            print('\nOtwieranie obrazu...')
            img = load_image()
            print("krok 1: zmiana wielkości")
            img = resize_image(img)
            print("krok 2: obrót")
            img = rotate_image(img)
            print("krok 3: zmiana koloru")
            img = change_color_image(img)


            continue

        elif code == '9':
            sys.exit()

        else:
            print("Error - zła wartość ")

if __name__ == '__main__':
    main()
