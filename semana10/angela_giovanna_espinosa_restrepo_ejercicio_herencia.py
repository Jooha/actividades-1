# Herencia v2.7.10
# Programa  que detecta el tipo de vehiculo y da sus caracteirsticas.
# Lee el tipo de vehivulo y sus caracteristicas desde un archivo de texto que se suministra como argumento de linea de comandos, como vehiculoX.txt.
# Al final muestra los datos pedidos en la ventana de comandos.


# Desarrollado por Angela Giovanna Espinosa Restrepo
# Octubre 13 de 2015


# Importar libreria sys para manejo de argumentos de linea de comandos
import sys


divline = "="*80

divline = "="*80
print divline
cadena = "VEHICULOS Y CARACTERISTICAS PRINCIPALES"
print cadena.center(80)
print divline


 
# ------------------ Inicio de definicion de funciones empleadas ------------------ #

# Funcion que lee las lineas de un archivo de texto.
def leer_lineas_archivo(nombre_archivo):
	lineas = ()
	try:
		archivo = open(nombre_archivo, 'r')
		lineas = archivo.readlines()
		archivo.close()
	except IOError:
		print("Error leyendo archivo " + nombre_archivo + "!")
		
	return lineas

# Funcion que guarda la informacion definida de las lineas especificadas en un archivo.
# Retorna un array de 2 columnas por tantas filas como lineas de archivo.
# La primera columna almacena la caracteristica 
# La segunda columna almacena el valor de dicha caracteristica.


def guardar_info(linea_a_guardar, numero_linea):
	array_respuesta = [0 for x in range(2)]
	
	arreglo_campos = linea_a_guardar.split("=")
	
	caracteristica_guardar = arreglo_campos[0]
	
	arreglo_caracteristicas = caracteristica_guardar
	
	array_respuesta[0] = caracteristica_guardar
	
	parametro_caracteristica = str(arreglo_campos[1])	
	
	array_respuesta[1] = parametro_caracteristica
	
	return array_respuesta

#-----------------------------------------------------------Fin Definicion De Funciones------------------------------------------------------------------#

#--------------------------------------------------------------Definicion de Clases----------------------------------------------------------#

class vehiculo(object):
	def __init__(self,modelo,n_ejes, cc_motor):
		self.modelo=modelo
		self.cc_motor=cc_motor
		self.n_ejes=n_ejes
		
	def mostrar_detalles(self):
		return 'Sus caracteristicas son: \n\nModelo: '+str(self.modelo)+'\nCilindraje del motor: '+str(self.cc_motor)+'\nNumero de ejes: '+str(self.n_ejes) 
	def arrancar(self):
		return 'El Vehiculo Terrestre arrancara en 10 minutos.'
	def apagar(self):
		return 'El vehiculo se encuentra apagando.'
	def acelerar(self):
		return 'Dum!! va a demasiada velocidad.'
		

class vehiculo_aereo(vehiculo):
	def __init__(self,modelo,n_ejes, cc_motor, n_alas,n_alerones,flaps):
		vehiculo.__init__(self,modelo,n_ejes, cc_motor)
	
	
		self.n_alas=n_alas
		self.n_alerones=n_alerones
		self.flaps=flaps

	def mostrar_detalles(self):
		return 'Sus caracteristicas son: \n\nModelo: '  +self.modelo+'\nNumero de ejes: '+str(self.n_ejes)+'\nCilindraje del motor: '+str(self.cc_motor)+'\nNumero de alas: '+str(self.n_alas)+'\nNumero de alerones: '+str(self.n_alerones)+'\nNumero de flaps: '+str(self.flaps)
	def despegar(self):
		return 'shshshshsh nos estamos elevando.'
	def aterrizar(self):
		return 'Bammm acabamos de aterrizar.'

class vehiculo_anfibio(vehiculo):
	def __init__( self, modelo, n_ejes, cc_motor, helices, n_turbinas, tamano_popa):
		vehiculo.__init__(self,modelo,n_ejes, cc_motor)
	
	
		self.helices=helices
		self.n_turbinas=n_turbinas
		self.tamano_popa=tamano_popa
		
	def mostrar_detalles(self):
		return 'Sus caracteristicas son:\n\nModelo: ' +self.modelo+'\nNumero de ejes: '+str(self.n_ejes)+'\nCilindraje del motor: '+str(self.cc_motor)+'\nNumero de helices: '+str(self.helices)+'\nNumero de turbinas: '+str(self.n_turbinas)+'\ntamano de popa: '+str(self.tamano_popa)
	def amarizar(self):
		return 'glulgu aumentando profundidad.'
	def sumergirse(self):
		return 'Porfavor aprochar los cinturones nos vamos a sumergir a gran velocidad.'
		
class vehiculo_espacial(vehiculo_aereo):
	def __init__(self,modelo,n_ejes, cc_motor,n_alas,n_alerones,n_cohetes, capacidad_astro, tamano_tanque):
		vehiculo_aereo.__init__(self,modelo,n_ejes, cc_motor, n_alas,n_alerones,flaps)
		self.n_cohetes=n_cohetes
		self.capacidad_astro=capacidad_astro
		self. tamano_tanque= tamano_tanque
		
	def mostrar_detalles(self):
		return 'Sus caracteristicas son:\n\nModelo: ' +str(self.modelo)+'\nNumero de ejes: '+str(self.n_ejes)+'\nCilindraje del motor: '+str(self.cc_motor)+'\nNumero de alas: '+str(self.n_alas)+'\nNumero de alerones: '+str(self.n_alerones)+'\nNumero de flaps: '+str(self.flaps)+'\nNuemro de Cohetes: '+str(self.n_cohetes)+'\nCapacidad astro: '+str(self.capacidad_astro)+'\nTamano tanque: '+str(self.tamano_tanque)
	def planear(self):
		return 'Les ensenare a volar.'
	def despegar(self):
		return 'Mantengase en su aciento sin alarmarse el despegue sera en 2 minutos.'
	def aterrizar(self):
		return 'Les informo que por primera vez en la vida terrestre un vehiculo espacial llega a mercurio , festejen!!.'
	
#-------------------------------------------------------------Fin Definicion De Funciones Empleadas-------------------------------------------------------------------#

#------------------------------------------------------------------Inicio De Logica Del Programa-------------------------------------------------------------------#
# Funcion que introduce el archivo especificado en la linea de comandos
archivo_vehiculox = sys.argv[1]

#Variable que almacena las lineas del archivo y su contenido
lineas_archivo_vehiculox = tuple(leer_lineas_archivo(archivo_vehiculox))

#Variable que almacena el numero de lineas de archivo
numero_lineas_vehiculox = len(leer_lineas_archivo(archivo_vehiculox))

# Array que contendran la informacion de las caracteristicas del vehiculo
# Se crea array caracteristicas con dimensiones 2 columnas y tantas filas como  numero de lineas haya en el archivo de vehiculoX.txt
# caracteristica[indice][0] -> Caracteristica del vehiculo
# caracteristica[indice][1] -> Valor Caracteristica
caracteristicas_vehiculox = [[columnas for columnas in range(2)] for filas in range(numero_lineas_vehiculox)]

# Almacenar informacion de las caracteristicas del vehiculo en array caracteristicas

for x in range (0,numero_lineas_vehiculox):
	linea_guardada = guardar_info(lineas_archivo_vehiculox[x], x+1)
	
	caracteristicas_vehiculox[x][0] = linea_guardada[0]
	caracteristicas_vehiculox[x][1] = linea_guardada[1]

#Variable que almacena el tipo de vehiculo

tipo_n = str(caracteristicas_vehiculox[0][1])
tipo = tipo_n.replace("\n","")

#Variables que almacenan informacion que sera heredada

modelo_n = str(caracteristicas_vehiculox[1][1])
modelo = modelo_n.replace('\n', ' ' )

cc_motor = int(caracteristicas_vehiculox[2][1])
n_ejes = int(caracteristicas_vehiculox[3][1])

#Si el tipo de vehiculo es vehiculo Terrestre


if (tipo == "vehiculo"):
	print "\n..................................Vehiculo Terrestre............................" 
	v1 = vehiculo (modelo,cc_motor,n_ejes)
	
	print v1.mostrar_detalles()
	print (' ')
	print v1.arrancar()
	print (' ')
	print v1.acelerar()
	print (' ')
	print v1.apagar()
	print (' ')
	print divline


#Si el tipo de Vehiculo es Aereo, heredara caracteristicas de vehiculo Terrestre.

if (tipo == 'vehiculo_aereo' ):

	print "\n....................................Vehiculo Aereo..............................."
	n_alas = int(caracteristicas_vehiculox[4][1])
	n_alerones = int(caracteristicas_vehiculox[5][1])
	flaps = int(caracteristicas_vehiculox[6][1])
	v1 = vehiculo(modelo,cc_motor,n_ejes)
	va1 = vehiculo_aereo(v1.modelo,v1.cc_motor,v1.n_ejes, n_alas,n_alerones,flaps)
	print (' ')
	print va1.mostrar_detalles()
	print (' ')
	print va1.despegar()
	print (' ')
	print va1.aterrizar()
	print (' ')
	print divline

#Si el tipo de Vehiculo es Anfibio, heredara caracteristicas de vehiculo Terrestre.

if (tipo == "vehiculo_anfibio"):
	print "\n..................................Vehiculo Anfibio.............................." 
	
	helices = int(caracteristicas_vehiculox[4][1])
	n_turbinas = int(caracteristicas_vehiculox[5][1])
	tamano_popa = int(caracteristicas_vehiculox[6][1])
	v1 = vehiculo(modelo,cc_motor,n_ejes)
	van1 = vehiculo_anfibio(v1.modelo,v1.cc_motor,v1.n_ejes, helices,n_turbinas,tamano_popa)
	print (' ')
	print van1.mostrar_detalles()
	print (' ')
	print van1.amarizar()
	print (' ')
	print van1.sumergirse()
	print (' ')
	print divline
#Si el tipo de vehiuclo es espacial, heredara caracteristicas de Vehiculo Aereo y de vehiculo.

if (tipo == "vehiculo_espacial"):
	print "\n..................................Vehiculo Espacial............................"
	
	n_alas = int(caracteristicas_vehiculox[4][1])
	n_alerones = int(caracteristicas_vehiculox[5][1])
	n_cohetes = int(caracteristicas_vehiculox[6][1])
	capacidad_astro = int(caracteristicas_vehiculox[7][1])
	tamano_tanque = int(caracteristicas_vehiculox[8][1])
	flaps = int(caracteristicas_vehiculox[9][1])


	v1 = vehiculo(modelo,cc_motor,n_ejes)
	va1 = vehiculo_aereo(v1.modelo,v1.cc_motor,v1.n_ejes, n_alas,n_alerones,flaps)
	ve1 = vehiculo_espacial(v1.modelo,v1.cc_motor,v1.n_ejes,va1.n_alas,va1.n_alerones,va1.flaps,n_cohetes,capacidad_astro,tamano_tanque)
	print (' ')
	print ve1.mostrar_detalles()
	print (' ')
	print ve1.despegar()
	print (' ')
	print ve1.planear()
	print (' ')
	print ve1.aterrizar()
	print (' ')
	print divline
#-----------------------------------------------------------Fin Logica De Programa-----------------------------------------------------------------#














