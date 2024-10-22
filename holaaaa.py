# pedimos al usuario que ingrese una palabra
import time
import  os 

frase = input("ingrese una palabra: ")

#dividimos las frase en palabras

palabras = frase.split()

# contamos el numero de palabras

numeroDePalabrasQueTendra = len(palabras)

#mostramos el resultado
print(f"su cantidad fue de: {numeroDePalabrasQueTendra}")

class Computadora:#se crea una clase 
    def __init__(self,nombre,Ram):#inicializamos los atributos 
        self.nombre = nombre #declaramos los atributos con valores 
        self.ram = Ram 

    def  apagar(self):#se crea un metodo o una accion del objeto 
        print(f"Apagando el equipo {self.nombre} con {self.ram} de RAM...")
        time.sleep(2)
        os.system( 'shutdown /s /t 0')
    def Salir(self):
        print("Salio Del Servidor")

time.sleep(4)


print ("Conectando a la Base De Datos Del Servidor...")
time.sleep(4)
while(True):#se crea un bucle si es verdadero se acaba y si es falsa la condicion se va a ejecutar el bucle
    tiempo = input("Desea apagar el dispositivo? apagar//no") 

    if tiempo == "apagar":
        equipo = Computadora("Mi PC", "8GB")  # Crear una instancia de la clase Apagar
        equipo.apagar()#se manda a llamar el objeto
        break #se acaba el bucle
    else:
        print("no se puede apagar el dispositivo")
        time.sleep(2)
        Salir = input ("Desea salir del Servidor")
        if Salir == "Si" or Salir == "si":
            equipo = Computadora("Asus","16GB" )
            equipo.Salir()
        else:
            array=[" Sigue adentro  del servidor "]
            print (array[0])
            x = ["hola bienvenido a esta inteligencia artificia","¿Desea hacer algo en especifico?"]
            print(x[0])
            url = 'https://www.google.com'
            respuesta = input(x[1])
            if respuesta == "si" or respuesta == "Si" or respuesta == "Sii" or respuesta == "Siii" or respuesta == "siii" or respuesta == "Siiii" or respuesta == "Siiii" or respuesta == "Si porfavor" or respuesta == "Si porfavor" or respuesta == "si porfa" or respuesta == "Si porfa" or respuesta == "sii":
                arrays = ["que desea hacer?"]
                Respuesta1 = input(arrays[0])

                if Respuesta1 == "Abre el navegador" or Respuesta1 == "abre el navegador" or  Respuesta1 == "Abre el Chrome"or Respuesta1 == "Abre el chrome" or  Respuesta1 == "Abre google" or Respuesta1 == "abre google":
                 os.system(f'start {url}')
                elif Respuesta1 == "deseo hacer una operacion" or Respuesta1 == "Deseo hacer una operacion"or Respuesta1=="operacion"or Respuesta1 == "Operacion"or Respuesta1 == "2+2"or Respuesta1 == "1+1"or Respuesta1 == "5+5"or Respuesta1 == "10+10"or Respuesta1 == "DESEA HACER UNA OPERACION"or Respuesta1 == "Desea hacer4 unas operacion"or Respuesta1 == "deseo hacer una resta"or Respuesta1 == "Deseo hacer una resta"or Respuesta1 == "deseo hacer una multiplicacion"or Respuesta1 == "Deseo hacer una multiplicacion"or Respuesta1 == "deseo hacer una division"or Respuesta1 == "Deseo hacer una division"or Respuesta1 == "resta" or Respuesta1 == "suma"or Respuesta1 == "multiplicacion"or Respuesta1 == "Division":
                 operationRMDS = input("Que operacion desea hacer + - x /")
                 if operationRMDS == "+":
                     operation = int(input("Querido usuario ingrese un  numero"))
                     operation2 = int(input("Querido usuario ingrese el segundo numero")) 
                     suma = operation + operation2
                     print(f'la respuesta de la suma de {operation} y {operation2} es {suma}')
                elif operationRMDS == "-":
                    resta = operation - operation2
                    print(f'la respuesta de la resta de {operation} y {operation2} es {resta}')
                elif operationRMDS == "x":
                    multi = operation * operation2
                    print()
                elif operationRMDS == "/":
                    division = operation / operation2
                    print(f'la respuesta de division es {operation}y {operation2} es {division}')
                
                
                

                

                
