import json
import urllib.request
from Exceptions import *

####################    Methods' definitions    ####################
def getJSONobjectFromString(s):
    return json.loads(s)

def getBuildingIDbyName(buildingName):
    contents = urllib.request.urlopen('https://www.sigua.ua.es/api/pub/edificio/all/items').read()
    jsonAllBuildings = getJSONobjectFromString(contents)
    for item in jsonAllBuildings:
        if item['nombre'].upper() == buildingName.upper():
            return item['id']
    raise notValidName()

def getDepartmentData(id, minOcupantes):
    contents = urllib.request.urlopen('https://www.sigua.ua.es/api/agregados/seo/departamento/all/items').read()
    jsonAllDepartmentsProperties = getJSONobjectFromString(contents)
    for item in jsonAllDepartmentsProperties:
        if item['id'].split('{')[1].split(',')[0].upper() == id.upper() and item['ocupantes'] >= minOcupantes:
            properties = {  "superficie": item['superficie'],
                            "estancias": item['estancias'],
                            "ocupantes": item['ocupantes']}
            return properties
    return ''

def showAllUAbuildings():
    contents = urllib.request.urlopen('https://www.sigua.ua.es/api/pub/edificio/all/items').read()
    json = getJSONobjectFromString(contents)
    print()
    for item in json:
        print(f"ID: {item['id']}\nNombre: {item['nombre']}\nPlantas: {item['plantas']}\n\n")

def showVolumeBuildingsData():
    contents = urllib.request.urlopen('https://www.sigua.ua.es/api/agregados/seo/edificio/all/items').read()
    json = getJSONobjectFromString(contents)
    print()
    for item in json:
        id = item['id'].split('{')[1].split(',')[0]
        print(f"ID: {id}\nSuperficie: {item['superficie']}\nEstancias: {item['estancias']}\nOcupantes: {item['ocupantes']}\n\n")

def showBuildingRooms():
    try:
        userInput = input('\nInsert the ID or the name of the building: ')
        buildingID = int(userInput)
        #it's an id
        contents = urllib.request.urlopen(f'https://www.sigua.ua.es/api/pub/estancia/edificio/{userInput}/items').read()
        json = getJSONobjectFromString(contents)
        rooms = json['features']
        for room in rooms:
            properties = room['properties']
            print(f"CódigoEstancia: {properties['codigo']}\nDenominación: {properties['denominacion']}\nSuperficie: {properties['superficie']}\nNombreActividad: {properties['nombre_actividad']}\n\n ")

    except ValueError:
       #It's a name
        try:
           buildingID = str(getBuildingIDbyName(userInput))
           contents = urllib.request.urlopen(f'https://www.sigua.ua.es/api/pub/estancia/edificio/{buildingID}/items').read()
           json = getJSONobjectFromString(contents)
           rooms = json['features']
           for room in rooms:
               properties = room['properties']
               print(f"CódigoEstancia: {properties['codigo']}\nDenominación: {properties['denominacion']}\nSuperficie: {properties['superficie']}\nNombreActividad: {properties['nombre_actividad']}\n\n ")

        except notValidName as e:
           print(e.info)

def showAllDepartments():
    minOcupantes = int(input('\nPoner el numero minimo de ocupantes por departamento (0 si no hay): '))
    contents = urllib.request.urlopen('https://www.sigua.ua.es/api/pub/departamentosigua/all/items').read()
    json = getJSONobjectFromString(contents)
    print()
    print('Cargando datos...\n')
    counter = 0
    for item in json:
        id = item['id']
        departmentProperties = getDepartmentData(id, minOcupantes)
        if departmentProperties != '':
            counter = counter + 1
            estancias = departmentProperties['estancias']
            ocupantes = departmentProperties['ocupantes']
            superficie = departmentProperties['superficie']
            print(f"ID: {id}\nEstancias: {estancias}\nOcupantes: {ocupantes}\nSuperficie: {superficie}\n\n ")
    if counter == 0:
        print(f'No hay departamentos con el numero minimo de ocupantes igual a {minOcupantes}.\n\n')

def askValidInput():
    validInputs = ['0','1','2','3','4']
    valid = False
    while not valid:
        inputValue = input("\nSELECCIONAR UNA OPCION\n\n" +
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
        showVolumeBuildingsData()
    elif inputValue == '3':
        showBuildingRooms()
    else:   #inputValue==4
        showAllDepartments()
    inputValue = askValidInput()
