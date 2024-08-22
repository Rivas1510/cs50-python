print("""
ESTUDIANDES
----------------
opciones disponibles


(1) mostrar listas de estudiantes
(2) mostrar promedios 
(3) salir
""")

lista_de_estudiantes=[{
    "nombre": "tiare baeza",
    "edad": 23,
    "rut": "20.452.650-8",
    "notas": [6.9,6.8,6.8]
}, {
    "nombre": "romina Pereira",
    "edad": 23,
    "rut": "25.243.948-2",
    "notas": [6.9,6.8,6.9]
}, {
    "nombre": "Bethania Mahotier",
    "edad": 23,
    "rut": "25.224.948-6",
    "notas": [7.0,6.9,6.8]
}]

opcion=input("seleciona la opcion que deseas: ")
if(opcion == "1"):
    print("esta es la lista de estudiantes: ")
    for estudiante in lista_de_estudiantes:
        print(f"el nombre es{estudiante['nombre']}")
        print(f"el rut es{estudiante['rut']}")
    
        
if(opcion =="2"):
    print("estos son los promedios")
    for estudiante in lista_de_estudiantes:
        lista_notas = estudiante["notas"]
        suma = 0
        for nota in lista_notas :
            suma = suma + nota

        promedio = suma/len(lista_notas)
        promedio_aprox = round(promedio,1)
        print(f"el estudiante {estudiante['nombre']}tuvo el promedio es {promedio_aprox}")
if(opcion =="3"):
    print("gracias por usar la aplicacion: ")
