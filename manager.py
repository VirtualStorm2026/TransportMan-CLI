try:
    import sys
    import os
    import json
    import time
    from pathlib import Path
except ImportError:
    print("Uno o mas modulos no se pudieron cargar correctamente o no fueron encontrados. Error RMIF1")
    input("Presione una tecla para salir...")
    sys.exit()

print("Modulos importados correctamente.")


# Checks the game version.
CURRENT_VERSION=("registeredVersion=VSC_0.1.4-alpha")
version_file = Path("version.txt")

# Checks if the license exists.
license_file = Path("LICENSE")

if version_file.exists():
    file_version = version_file.read_text(encoding="utf-8").strip("=")
    if file_version==CURRENT_VERSION:
        pass
    else:
        print("La version en version.txt es diferente a la registrada. Puede deberse por alguna modificacion. Por favor reinstale el juego. Error VM01")
        input("Presione alguna tecla para salir...")
        sys.exit()
else:
    print("El juego no iniciara si no esta el archivo de version. Error VFNF01")
    input("Presione alguna tecla para salir...")
    sys.exit()
        
if license_file.exists():
    pass
else:
    print("El juego no iniciara si no esta el archivo de licencia. Error LFNF01")
    input("Presione alguna tecla para salir...")
    sys.exit()

# Stablishes essential variables.

# Game variables
onMain = 0
ingame = 0
continueOption = 0
isInfiniteMode = False

# High Score variables
high_scores = {}
score = 0
all_scores = {}

# Save/Current game data
money = 0
buses = {}
busesS = 0
busesM = 0
busesL = 0
availableTurns = 99
diffList = {
    0: "none",
    1: "Facil",
    2: "Estandar",
    3: "Dificil",
    4: "Infinito"
}
diffTurnList = {
    0: 0,
    1: 60,
    2: 35,
    3: 20,
    4: 0
}
saveData = {}
loadedSaveData = {}

# Selection system variables
seleccion = 0
currentDiff = diffList.get(seleccion)
initialTurns = diffTurnList.get(seleccion)

# Debug stuff
debugNames = {
    "rvldev-03",
    "managerdev",
    "alchemist64",
    "insider",
    "lemmetakealook",
    "businessman"
}
isDebugEnabled = False

# Loops and functions

# Clear screen
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Load/Save data screen		
def main_screen():
    print("Bienvenido a Manager alpha2!")
    print(" ")
    print("1. Crear partida")
    print("2. Cargar partida")
    print("3. Salir")
 
# Simplification of exit system
def exitKey(should_exit=True):
    if should_exit==True:
        print("Presione cualquier tecla para salir...")
    else:
        print("Presione cualquier tecla para continuar...")
     
time.sleep(1)
    
print ( "Cargando..." ) 

time.sleep(2)

# Initialization loop
name = input("Introduce tu nombre: ")

# Checks if the typed name is a valid debug name

if name in debugNames:
    isDebugEnabled = True
    print("DEBUG: Debug activado")

if isDebugEnabled == True:
    print(f"DEBUG: currentDiff value = {currentDiff}")

# High Score file logic

try:  
    with open( "highscores.json", "r", encoding = "utf-8" ) as hsfile:
        print("")
except FileNotFoundError:
    print ( "No se ha encontrado un archivo de puntaje." )
    time.sleep ( 1)
    makeHS = input ( "Desea crear un archivo de puntaje? Y/N" ).lower ( )
    if makeHS == "y":
      print ("Guardando... no cierres el programa.")
      time.sleep ( 2)
      if isDebugEnabled == True:
          print("DEBUG: Writing information to highscores.json...")
    try:
          with open ("highscores.json", "w", encoding = "utf-8") as hsfile:
              high_scores[name] = score
              json.dump(high_scores, hsfile, indent = 4)
    except json.JSONDecodeError as e:
          print("El archivo es corrupto o no valido. Error: HSFC2")
    except PermissionError:
          print("No se tiene los permisos necesarios para crear el archivo. Intenta iniciar en Administrador? Error HSPE09")
          exitKey()
          sys.exit()
    except Exception as e:
          print(e)
          print("Ocurrio un error desconocido.")
          exitKey()
          sys.exit()
          
doSave = input("Desea guardar su puntaje? Y/N: ").lower()

# High Score saving logic

if doSave == "y":
    score = int(input("DESARROLLADOR: Introduzca un puntaje: "))
    print("Guardando...")
    time.sleep(2)
    try:
        with open("highscores.json", "r", encoding = "utf-8") as hsfile:
            all_scores = json.load(hsfile)
    except Exception as e:
        print(e)
        print("Algo salio mal en el guardado. Error: HSWF3")
        input("Presione una tecla para salir... ")
        sys.exit()
    if name not in all_scores or score > int(all_scores[name]):
        all_scores[name] = score
        print("Nuevo record detectado!")
    else:
        print("No has superado tu record...")
    sorted_scores = dict(sorted(all_scores.items(), key=lambda item: int(item[1]), reverse=True))
    try:
        if isDebugEnabled == True:
            print("DEBUG: Writing information to highscores.json...")
        with open("highscores.json", "w", encoding = "utf-8") as hsfile:
            json.dump(sorted_scores, hsfile, indent = 4)
    except Exception as e:
        print(e)
        print("Algo salio mal en el guardado. Error: HSWF3")
        input("Presione una tecla para salir...")
        sys.exit()
else:
    print("Su puntaje no sera guardado.")
    
print("Iniciando...")

time.sleep(2)

onMain = 1

# Main save/load data loop

while onMain == 1:
    clear_screen()
    main_screen()
    print(" ")
    menuSel = int(input("Seleccione una opcion: "))
    if menuSel == 1:
        makeSave = str(input("Desea crear una nueva partida? Esto sobreescribira cualquier partida existente! Y/N ").lower())
        if makeSave == "y":
            clear_screen()
            try:
                with open("save.json", "w", encoding = "utf-8") as saveFile:
                    if isDebugEnabled == True:
                        print("DEBUG: save.json opened")
                    if isDebugEnabled == True:
                        try:
                            money = int(input("DESARROLLADOR: Introduzca dinero. "))
                            busesS = int(input("DESARROLLADOR: Introduzca cantidad de buses pequeños. "))
                            busesM = int(input("DESARROLLADOR: Introduzca cantidad de buses medianos. "))
                            busesL = int(input("DESARROLLADOR: Introduzca cantidad de buses largos. "))
                            availableTurns = int(input("DESARROLLADOR: Introduzca turnos disponibles. "))
                            seleccion = int(input("DESARROLLADOR: Introduzca dificultad (1, 2, 3, 4): "))
                            currentDiff = diffList.get(seleccion)
                            initialTurns = diffTurnList.get(seleccion)
                            
                        except TypeError:
                            print("Se introdujo un tipo de datos incorrecto.")
                            exitKey()
                            sys.exit()
                    else:
                            clear_screen()
                            print("En toda dificultad, empezaras siempre con 10000 Pepos.")
                            time.sleep(2)
                            print("Selecciona una dificultad: ")
                            print("1: Facil: 60 turnos (Recomendado para empezar)")
                            print("2: Estandar: 35 turnos (Ideal para partidas normales)")
                            print("3: Dificil: 20 turnos (Para los que buscan un reto)")
                            print("4: Sin Fin (No hay turnos)")
                            seleccion = int(input("Seleccion: "))
                            try:
                                if seleccion == 1:
                                    print("Dificultad facil escogida.")
                                    print("Guardando...")
                                    time.sleep(2)
                                    availableTurns = diffTurnList.get(seleccion)
                                    initialTurns = diffTurnList.get(seleccion)
                                    currentDiff = diffList.get(seleccion)
                                    money = 10000
                                    busesS = 0
                                    busesM = 0
                                    busesL = 0
                                    isInfiniteMode = False
                                elif seleccion == 2:
                                    print("Dificultad estandar escogida.")
                                    print("Guardando...")
                                    time.sleep(2)
                                    availableTurns = diffTurnList.get(seleccion)
                                    initialTurns = diffTurnList.get(seleccion)
                                    currentDiff = diffList.get(seleccion)
                                    money = 10000
                                    busesS = 0
                                    busesM = 0
                                    busesL = 0
                                    isInfiniteMode = False
                                elif seleccion == 3:
                                    print("Dificultad dificil escogida.")
                                    print("Guardando...")
                                    time.sleep(2)
                                    availableTurns = diffTurnList.get(seleccion)
                                    initialTurns = diffTurnList.get(seleccion)
                                    currentDiff = diffList.get(seleccion)
                                    money = 10000
                                    busesS = 0
                                    busesM = 0
                                    busesL = 0
                                    isInfiniteMode = False
                                elif seleccion == 4:
                                    print("Modo infinito seleccionado.")
                                    print("Guardando...")
                                    time.sleep(2)
                                    availableTurns = diffTurnList.get(seleccion)
                                    initialTurns = diffTurnList.get(seleccion)
                                    currentDiff = diffList.get(seleccion)
                                    money = 10000
                                    busesS = 0
                                    busesM = 0
                                    busesL = 0
                                    isInfiniteMode = True
                            except TypeError:
                                print("No seleccionaste una opcion valida.")
                                exitKey(should_exit=0)

                    # Stores save data, ready to save in save.json.
                    saveData[name] = seleccion, availableTurns, initialTurns, currentDiff, money, busesS, busesM, busesL, isInfiniteMode
                    json.dump(saveData, saveFile, indent = 4)

                    if isDebugEnabled == True:
                        print("DEBUG: Data saved succesfully in save.json.")

                    print("Se creo el guardado!")
                    exitKey(should_exit=0)

            except json.JSONDecodeError:
                print("El archivo esta corrupto o ha sido modificado. Error SFME4")

            except Exception as e:
                print(e)
                print("Algo salio mal creando el guardado. Error SFME5")
                input("Presione cualquier tecla para salir...")
                sys.exit()

    elif menuSel == 2:
        clear_screen()
        print("Se cargara un archivo de guardado.")
        print("Se cargara desde la carpeta donde hayas puesto el script.")
        print("Si no existe, por favor crea una seleccionando la opcion 1.")
        print(" ")

        doLoadSave = str(input("Desea cargar el guardado? Y/N: "))

        # Save load loop
        if doLoadSave == "y":
            print("Cargando guardado...")
            time.sleep(2)
            try:
                if isDebugEnabled == True:
                    print("DEBUG: Trying to read save.json...")

                with open("save.json", "r", encoding = "utf-8") as saveFile:
                    saveData = json.load(saveFile)
                    print(f"DEBUG: Data found on save.json: {saveData}")
                    print("Guardado cargado!")
                    exitKey(should_exit=False)
                    onMain = 0
                    ingame = 1

            except FileNotFoundError:
                print("No se pudo encontrar un guardado. Por favor crea uno usando la opcion 1. Error SFLE5")
                exitKey()
                sys.exit()

            except json.JSONDecodeError as e:
                print("El guardado esta corrupto o dañado. Error SFCE6")
                print(f"Detalles: {e}")
                exitKey()
                sys.exit()

            except PermissionError:
                print("Permiso denegado. No se puede leer el guardado. Intenta iniciar en Administrador. Error SVPE7")
                exitKey()
                sys.exit()

            else:
                pass

    elif menuSel == 3:
        sys.exit()
        
#=================
# Main game loop
#=================
        
while ingame == 1:
    
    with open("save.json", "r", encoding = "utf-8") as loadedSave:
        
        loadedSaveData = json.load(loadedSave)
        user_data = loadedSaveData.get(name)
        if user_data is None:
            
            if isDebugEnabled == True and (initialTurns != diffTurnList.get(seleccion) or currentDiff != diffList.get(seleccion)):
                
                print("Se detecto un guardado modificado, contiene datos ilegales o esta corrupto.")
                time.sleep(2)
                
                print("Se detecto que esta en modo desarrollador.")
                
                time.sleep(2)
                
                loadCorruptSave = str(input("Esta seguro que desea iniciar este guardado? Y/N: "))
                if loadCorruptSave == "y":
                    pass
                    
                else:
                    print("No se cargara el guardado. Por favor borra el guardado y/o sobreescribelo con uno original. Error STFE")
                    
                    exitKey()
                    
                    sys.exit()
                    
            print("El archivo esta corrupto o no es un guardado propio. Error SUME0")
            
            exitKey()
            
            sys.exit()
            
        seleccion = user_data[0]
        
        availableTurns = user_data[1]
        
        initialTurns = user_data[2]
        
        currentDiff = user_data[3]
        
        if initialTurns == diffTurnList.get(seleccion) and currentDiff == diffList.get(seleccion):
            pass
            
        elif isDebugEnabled == True and (initialTurns != diffTurnList.get(seleccion) or currentDiff != diffList.get(seleccion)):
            
            print("Se detecto un guardado modificado, contiene datos ilegales o esta corrupto.")
            
            time.sleep(2)
            
            print("Se detecto que esta en modo desarrollador.")
            time.sleep(2)
            
            loadCorruptSave = str(input("Esta seguro que desea iniciar este guardado? Y/N: "))
            if loadCorruptSave == "y":
                pass

            else:
                
                print("No se cargara el guardado. Por favor borra el guardado y/o sobreescribelo con uno original. Error STFE")
                
                exitKey()
                
                sys.exit()
                
        else:
            
            print("El archivo esta corrupto o modificado. Error SFTE")
            
            exitKey()
            
            sys.exit()
            
        money = user_data[4]
        
        busesS = user_data[5]
        
        busesM = user_data[6]
        
        busesL = user_data[7]
        
        isInfiniteMode = user_data[8]
    
    clear_screen()
        
    print("MENU PRINCIPAL")
    
    print(f"DIFICULTAD: {currentDiff}")
    
    if isDebugEnabled==True:
        print("DEBUG/DESARROLLADOR: ACTIVO")
    else:
        pass
        
    print(f"TURNOS DISPONIBLES: {availableTurns}/{initialTurns}")
    
    print(f"Saldo: {money}")
    
    print(f"Buses pequeños: {busesS}")
    
    print(f"Buses medianos: {busesM}")
    
    print(f"Buses grandes: {busesL}")
    
    print("")
    
    print("OPCIONES")
    
    print("1: Finanzas")
    
    print("2. Catalogo")
    
    print("3. Pruebas")

    print("4. Guardar y salir")
    
    try:
        continueOption = int(input("Introduce tu opcion: "))
    except TypeError:
        pass
    except Exception as e:
        print(e)
        print("Error desconocido. Introdujiste correctamente tu opcion?")
        exitKey(should_exit=0)

    clear_screen()
    
    if continueOption == 1:
        if money >= 2000:
            money = money-2000
            print("Has gastado 2000 en aire. Gracias por tu compra!")
            exitKey(should_exit=0)
        else:
            print("Te falta dinero!")
            exitKey(should_exit=0)
    elif continueOption == 2:
        busesS = busesS+1
        print("Si conseguiste ese bus legalmente, verdad?")
        print("Bus pequeño  +1")

    elif continueOption == 4:
        clear_screen()
        makeSave = str(input("Estas seguro de que quieres salir? Y/N: ").lower())
        if makeSave == "y":
            print("Guardando...")
            time.sleep(2)
            try:
                with open("save.json", "w", encoding = "utf-8") as saveFile:
                    if isDebugEnabled==True:
                        print("DEBUG: save.json opened.")
                    saveData[name] = seleccion, availableTurns, initialTurns, currentDiff, money, busesS, busesM, busesL, isInfiniteMode
                    json.dump(saveData, saveFile, indent = 4)
                    print("Guardado!")
                    exitKey()
                    sys.exit()
            except Exception as e:
                print(e)
                print("Un error ha ocurrido.")
                exitKey()
                sys.exit()