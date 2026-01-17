import os

def funcion1():
    print('esta es funcion 1')


def funcion2():
    os.system('clear')


def funcion3():
    print('esta es funcion 3')

def main():
    funcion2()   
    funcion1()
    funcion3()


if __name__ == "__main__":
    main()
