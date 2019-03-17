import take_photo as tk
import recognize_face as rf
import number_to_speech as nts

def main():
    steps = input('''
    Bienvenidos... Sistema creado por Wildin Mota para la exposicion de UCATECI
    Opciones
    a. Presiona 1 para entrenar el modelo
    b. Presione 2 para probar
    > ''')
    if(steps == '1'):
        tk.create_dataset()
        rf.run()
    elif(steps == '2'):
        image_recognized = tk.recognize()
    else:
        print('Opcion no Valida')
        main()

if __name__ == '__main__':
    main()