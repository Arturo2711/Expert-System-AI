from swiplserver import PrologMQI
from dietaConsola import calculaCalorias, caloriasQuemadas

# Funcion para hacer la consulta en prolog 
def query_swi_prolog(consulta):

    with PrologMQI() as mqi:
        with mqi.create_thread() as prolog_thread:
            prolog_thread.query("consult('SistemaExperto.pl')")
            result = prolog_thread.query(consulta)
            return result

# Calorias del usuaro NOTA: CAMBIA LOS INPUT POR LA INFORMACION DEL USUARIO 
# NO OLVIDES PONERLE EL CAST A FLOAT
calorias = calculaCalorias('any', caloriasQuemadas(
    float(input("Ingrese los kg:")), float(input("Ingrese el FA:"))))

# NO LO TOQUES PREGUNTA SI TIENES DUDAS 
caloriasDesayuno = int(calorias*0.30)
caloriasComida = int(calorias*0.40)
caloriasColacion = int(calorias*0.10)
caloriasCena = int(calorias*0.20)

#NO MODIFIQUES ESTAS CONSULTAS 
consultaDesayuno = "desayuno(Comida1, Comida2, Comida3, Comida4, KCal, Carbos, Grasas, Proteina, {})".format(caloriasDesayuno)
consultaComida = "comida(Comida1, Comida2, Comida3, Comida4, KCal, Carbos, Grasas, Proteina, {})".format(caloriasComida)
consultaCena = "cena(Comida1, Comida2, Comida3, KCal, Carbos, Grasas, Proteina, {})".format(caloriasCena)
consultaColacion= "colacion(Comida1, Comida2, KCal, Carbos, Grasas, Proteina, {})".format(caloriasColacion)
print(consultaDesayuno)
print(consultaComida)
print(consultaColacion)
print(consultaCena)
 
r1 = query_swi_prolog(consultaDesayuno) #CADA CONSULTA RETORNA UNA LISTA DE DICCIONARIOS
longitud = len(r1)
print("DESAYUNO :", r1[0])  #CADA LLAVE DEL DICCIONARIO SON LAS VARIBLES QUE LE PUSISTE A LA CONSULTA EJE:COMIDA1, COMIDA2 ,ETC
#print(r1[int(longitud/2)])
#print(r1[longitud-2])

r2 = query_swi_prolog(consultaComida)
longitud = len(r2)
print("COMIDA", r2[0])
#print(r2[int(longitud/2)])
#print(r2[longitud-2])

r3 = query_swi_prolog(consultaColacion)
longitud = len(r3)
print("COLACION", r3[0])
#print(r3[int(longitud/2)])
#print(r3[longitud-2])

r4 = query_swi_prolog(consultaCena)
longitud = len(r1)
print("CENA", r4[0])
#print(r4[int(longitud/2)])
#print(r4[longitud-2])

