import json
import urllib.request

####################    Methods' definitions    ####################
def getJSONobjectFromString(s):
    return json.loads(s)

def showAllUAbuildings():
    contents = urllib.request.urlopen('https://www.sigua.ua.es/api/pub/edificio/all/items').read()
    json = getJSONobjectFromString(contents)
    for item in json:
        print(f"ID: {item['id']}\nNombre: {item['nombre']}\nPlantas: {item['plantas']}\n\n")

def askValidInput():
    validInputs = ['0','1','2','3','4']
    valid = False
    while not valid:
        inputValue = input("\nSelect an option\n\n" +
                "0: exit\n\n" +
                "1: Listado de todos los edificios de la Universidad de Alicante\n\n" +
                "2: Listado de datos de volumen de todos los edificios de la Universidad de Alicante\n\n" +
                "3: Listado de las estancias de un edificio concreto de la Universidad de Alicante\n\n" +
                "4: Listado de departamentos de la Universidad de Alicante\n\n\n")
        if inputValue in validInputs:
            valid = True
            return inputValue
        else:
            print('\nNOT VALID INPUT. It must be an integer between 0 and 4. \n\n')

####################    Here the execution starts    ####################
#uaSocket = connectTo('www.sigua.ua.es', 80)
inputValue = askValidInput()
while inputValue !='0':
    if inputValue == '1':
        showAllUAbuildings()
    elif inputValue == '2':
        pass
    elif inputValue == '3':
        pass
    else:   #input==4
        pass
    inputValue = askValidInput()
