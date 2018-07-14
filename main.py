'''
Programa que acepte 2 numeros y muestre el resultado de la suma de ellos.
El programa antes de realizar la suma debe validar el usuario con reconocimiento facial,
solamente podra usarlo usted y el profesor. Al momento de mostrar el resultado,
el programa lo mostrara en pantalla y una voz vocalizara el resultado de la suma.
La voz que anunciara el resultado sera la suya.
'''

import take_photo as tk
import recognize_face as rf
import number_to_speech as nts


def main():
    steps = input("Bienvenidos... Programa por Wildin Mota\n Opciones\na. Presiona 1 para crear dataset y training data(Solo se permite el ID 1, 2 no mas)\nb. Presione 2 para hacer suma\n> ")
    print('\n Use el ID 2 profesor para probar')
    if(steps == '1'):
        tk.create_dataset()
        rf.run()
    elif(steps == '2'):
        suma = str(sum())
        sum_array = list(suma) # ['5', '4']

        image_recognized = tk.recognize()
        if image_recognized:
            print(f'El resultado es {suma}')
            nts.speech_number(sum_array)
    else:
        print('Opcion no Valida')
        main()

def sum():
    numero1 = int(input('Dame el numero> '))
    numero2 = int(input('Dame el numero2> '))

    return numero1 + numero2

if __name__ == '__main__':
    main()