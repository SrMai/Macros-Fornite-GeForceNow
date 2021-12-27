import subprocess as sub
import sys
import keyboard
from time import sleep
from pynput import keyboard as kb
from pynput.mouse import Button, Controller


#Variables pynput
mouse = Controller()
#Variables teclas
TeclaPared = "c";
TeclaSuelo = "x";
TeclaTecho = "v";
TeclaEscalera = "z";
TeclaCombo = "e";
TeclaEditar = "g";
SePuede = 1;
    
def VerMenu():
    print("Si esta es la primera vez que entras, tendras que configurar tus teclas a continuación")
    print("1.- Modificar Teclas")
    print("2.- Restablecer Ajustes")
    print("3.- Ver Teclas")
    print("0.-Salir")
    sub.call('bash Macro/macroBackspace.sh', shell=True)
    OpcionPrincipal = int(input("Selecciona la opcion mas conveniente: "))
    sub.call('bash Macro/macroBackspace.sh', shell=True)
    if OpcionPrincipal == 1:
        ModificarTeclas()
    elif OpcionPrincipal == 2:
        RestablecerTeclas()
    elif OpcionPrincipal == 3:
        VerTeclas()
    else:
        Salir()
def ModificarTeclas():
    print("||||||||| Acontinuación toca la tecla con la que quieres construir las paredes. |||||||||")
    TeclaPared = str(input("Tecla Pared : "))
    print("Tecla Pared:")
    print(TeclaPared)
    print("  ")
    print("||||||||| Acontinuación toca la tecla con la que quieres construir los suelos. |||||||||")
    TeclaSuelo = str(input("Tecla Suelo : "))
    print("Tecla Suelo:")
    print(TeclaSuelo)
    print("  ")
    print("||||||||| Acontinuación toca la tecla con la que quieres construir los techos. |||||||||")
    TeclaTecho = str(input("Tecla Techo : "))
    print("Tecla Techo:")
    print(TeclaTecho)
    print("  ")
    print("||||||||| Acontinuación toca la tecla con la que quieres construir las Escaleras. |||||||||")
    TeclaEscalera = str(input("Tecla Escalera : "))
    print("Tecla Escalera:")
    print(TeclaEscalera)
    print("  ")
    print("Guardado Exitoso")
    print("Pulsa cualquier tecla para regresar al menu principal")
    OpcionTecla = str(input())   
    if OpcionTecla == 1:
        sub.call('clear', shell=True)
        VerMenu()
    else:
        sub.call('clear', shell=True)
        VerMenu()

def RestablecerTeclas():
    TeclaPared = "c";
    TeclaSuelo = "x";
    TeclaTecho = "v";
    TeclaEscalera = "z";
    print("Ajustes restablecidos con exito")
    print("")
    print("Pulsa cualquier tecla para regresar al menu principal")
    OpcionTecla = str(input())   
    if OpcionTecla == 1:
        sub.call('clear', shell=True)
        VerMenu()
    else:
        sub.call('clear', shell=True)
        VerMenu()

def ConstruirSuelo():
    keyboard.press_and_release('x') 
    mouse.press(Button.left)
    mouse.release(Button.left)
    keyboard.press_and_release('q') 

def ConstruirPared():
    keyboard.press_and_release('z') 
    mouse.press(Button.left)
    mouse.release(Button.left)
    keyboard.press_and_release('q') 
    
def ConstruirTecho():
    keyboard.press_and_release('v') 
    mouse.press(Button.left)
    mouse.release(Button.left)
    keyboard.press_and_release('q') 

def ConstruirEscalera():
    keyboard.press_and_release('c') 
    mouse.press(Button.left)
    mouse.release(Button.left)
    keyboard.press_and_release('q') 
    
def EditarPared():
    keyboard.press_and_release('u')
    mouse.release(Button.left)
    keyboard.press_and_release('u') 
    
def MacroCombo():
    keyboard.press_and_release('x') 
    mouse.press(Button.left)
    mouse.release(Button.left)
    keyboard.press_and_release('z') 
    mouse.press(Button.left)
    mouse.release(Button.left)
    keyboard.press_and_release('c') 
    mouse.press(Button.left)
    mouse.release(Button.left)
    keyboard.press_and_release('q')
    

def pulsa(tecla):
    if tecla == kb.KeyCode.from_char('x'):
        print("Se ha construido Suelo x")
        ConstruirSuelo()
        print("Termino Tarea")
        VerTeclas()
        sys.exit()
    elif tecla == kb.KeyCode.from_char('z'):
        print("Se ha construido Pared z")
        ConstruirPared()
        print("Termino Tarea")
        VerTeclas()
    elif tecla == kb.KeyCode.from_char('v'):
        print("Se ha construido Techo v")
        ConstruirTecho()
        print("Termino Tarea")
        VerTeclas()
    elif tecla == kb.KeyCode.from_char('c'):
        print("Se ha construido Escalera c")
        ConstruirEscalera()
        print("Termino Tarea")
        VerTeclas()
    elif tecla == kb.KeyCode.from_char('e'):
        print("Se ha construido Combo E")
        MacroCombo()
        print("Termino Tarea")
        VerTeclas()
    elif tecla == kb.KeyCode.from_char('g'):
        print("Se ha editado pared g")
        EditarPared()
        print("Termino Tarea")
        VerTeclas()
    elif tecla == kb.KeyCode.from_char('X'):
        print("Se ha construido Suelo X")
        ConstruirSuelo()
        print("Termino Tarea")
        VerTeclas()
    elif tecla == kb.KeyCode.from_char('Z'):
        print("Se ha construido Pared Z")
        ConstruirPared()
        print("Termino Tarea")
        VerTeclas()
    elif tecla == kb.KeyCode.from_char('V'):
        print("Se ha construido Techo V")
        ConstruirTecho()
        print("Termino Tarea")
        VerTeclas()
    elif tecla == kb.KeyCode.from_char('C'):
        print("Se ha construido Escalera C")
        ConstruirEscalera()
        print("Termino Tarea")
        VerTeclas()
    elif tecla == kb.KeyCode.from_char('E'):
        print("Se ha construido Combo E")
        MacroCombo()
        print("Termino Tarea")
        VerTeclas()
    elif tecla == kb.KeyCode.from_char('G'):
        print("Se ha editado pared G")
        EditarPared()
        print("Termino Tarea")
        VerTeclas()
    elif tecla == kb.KeyCode.from_char('*'):
        print("Termino Tarea")
        Pausa()

def VerTeclas():
    keyboard.press_and_release('backspace')
    sub.call('clear', shell=True)
    keyboard.press_and_release('backspace')
    print("Tecla Pared:" + TeclaPared)
    print("Tecla Suelo:" + TeclaSuelo)
    print("Tecla Techo:" + TeclaTecho)
    print("Tecla Escalera:" + TeclaEscalera)
    print("Tecla Combo:" + TeclaCombo)
    print("Tecla Editar:" + TeclaEditar)
    if SePuede == 1:
        with kb.Listener(pulsa) as escuchador:
            escuchador.join()
    else:
        print("Tranquilo viejo")
        sleep(.5)
        VerTeclas()
        
   
    #OpcionTecla = str(input())   
    #if OpcionTecla == 1:
    #    sub.call('clear', shell=True)
    #    VerMenu()
    #else:
    #    sub.call('clear', shell=True)
    #    VerMenu()

def Pulsa(Tecla):
    if Tecla == kb.KeyCode.from_char('*'):
        keyboard.press_and_release('backspace')
        VerTeclas()
    elif Tecla == kb.KeyCode.from_char('/'):
        Salir()
        
def Pausa():
    sub.call('clear', shell=True)
    print("Pulsa '*' para quitar la pausa, ó '/' para salir")
    with kb.Listener(Pulsa) as escuchador:
        escuchador.join()

def Salir():
    sub.call('clear', shell=True)
    sub.call('exit', shell=True)
    print("Se Desactivo El Programa")
    sys.exit()
    
VerTeclas()
