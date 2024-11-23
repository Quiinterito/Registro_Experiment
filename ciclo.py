from datetime import datetime
import statistics

class registro_experimentos:
    def __init__(self, nombre , fecha , tipo_experimento , resultados_obtenidos):
        self.nombre = nombre
        self.fecha = fecha
        self.tipo_experimento = tipo_experimento
        self.resultados_obtenidos = resultados_obtenidos   


def registrar_experimento(experimento):  
    nombre = input("Ingrese el nombre del experimento: ")
    fecha_str = input("Ingrese la fecha del experimento en el formato dd/mm/aaaa: ") 
    try:
        fecha = datetime.strptime(fecha_str, '%d/%m/%Y')
    except ValueError:
        print("¡El formato ingresado no es valido!")
        return
    tipo_experimento = input("Ingrese el tipo de experimento: ")
    resultados_str = input("Ingrese los resultados obtenidos separados por comas ejemplo: 5, 7, 8: ")
    try:
        tarea  = list(map(float, resultados_str.split(',')))
    except ValueError:
        print("¡Los resultados ingresados no son validos!")
        return
    registro = registro_experimentos(nombre, fecha, tipo_experimento, tarea)
    experimento.append(registro)
    print("Experimento registrado exitosamente.")  
    
def mostrar_experimentos(experimento):
    if not experimento:
        print("No hay experimentos registrados.")
        return
    for i , registro in enumerate(experimento , start=1):
        print("--------------------------------")
        print(f"\nExperimento #{i}:")
        print("--------------------------------")
        print(f"Nombre: {registro.nombre}")
        print(f"Fecha: {registro.fecha.strftime('%d/%m/%Y')}")
        print(f"Tipo de experimento: {registro.tipo_experimento}")
        print(f"Resultados obtenidos: {registro.resultados_obtenidos}")
        print("--------------------------------")
        
        
def promedio(experimento):
    if not experimento:
        print("No hay experimentos registrados.")
        return
    for tarea in experimento:
        promedio = statistics.mean(tarea.resultados_obtenidos)
        maximo = max(tarea.resultados_obtenidos)
        minimo = min(tarea.resultados_obtenidos)
        print("--------------------------------")
        print(f"Promedio: {promedio}")
        print(f"Maximo: {maximo}")
        print(f"Minimo: {minimo}")
        print("--------------------------------")
        
def generar_reporte(experimento):
    if not experimento:
        print("No hay experimentos registrados.")
        return
    
    with open('reporte.txt', 'w') as reporte:
        for tarea in experimento:
            reporte.write(f"Experimento: {tarea.nombre}\n")
            reporte.write(f"Fecha: {tarea.fecha.strftime('%d/%m/%Y')}\n")
            reporte.write(f"Tipo de experimento: {tarea.tipo_experimento}\n")
            reporte.write(f"Resultados obtenidos: {tarea.resultados_obtenidos}\n")
            reporte.write("--------------------------------\n")
            print("Reporte generado exitosamente.")
        
        
        
        
        
        
def menu(experimento):
    while True:
        print("\n---------- Menu -----------")
        print("1. Registrar experimento")
        print("2. Mostrar experimentos")
        print("3. Mostrar promedio de los experimentos")
        print("4. Generar reporte")
        print("5. Salir")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            registrar_experimento(experimento)
        elif opcion == "2":
            mostrar_experimentos(experimento)
        elif opcion == "3":
            promedio(experimento)
        elif opcion == "4":
            generar_reporte(experimento)
        elif opcion == "5": 
            break
        else:
            print("Opcion no valida.")
            
            
            
if __name__ == "__main__":
    experimento = []
    menu(experimento)
    
    
    
    
        
        
        
        
        
        
        
   
        
    
    
    
    



    


    

    
