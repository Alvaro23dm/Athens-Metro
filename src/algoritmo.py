import numpy as np
import math

#Recogemos los valores de las distancias entre las estaciones
linea1v= [2, 3, 3, 1, 3, 2, 1, 2, 1, 2, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 3, 2, 2]
linea2v= [1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1]
linea3v= [2, 2, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 3, 2, 1, 2]

#Coordenadas de las diferentes paradas
coords1= [(37.948020, 23.643555), (37.944960, 23.665285), (37.955250, 23.680465), (37.960395, 23.697005), (37.962360, 23.703330), (37.968455, 23.709115), (37.976755, 23.720130), (37.975985, 23.725390), (37.984030, 23.727970), (37.992960, 23.730195), (37.999495, 23.722800), (38.006820, 23.727635), (38.011505, 23.728560), (38.019805, 23.731630), (38.023735, 23.735990), (38.032785, 23.744700), (38.037040, 23.750120), (38.041430, 23.754835), (38.046200, 23.766000), (38.043280, 23.783310), (38.045120, 23.792945), (38.056225, 23.804915), (38.065955, 23.804020), (38.073225, 23.808160)]
coords2= [(38.006200, 23.699565), (38.002675, 23.713540), (37.999230, 23.722350), (37.992140, 23.721200), (37.986770, 23.720710), (37.984030, 23.727970), (37.980235, 23.732985), (37.974790, 23.735535), (37.968675, 23.729410), (37.964245, 23.726410), (37.957655, 23.728335), (37.956315, 23.734575), (37.949160, 23.737245), (37.940150, 23.740645)]
coords3= [(37.991943646495294, 23.681824181482877), (37.98788544901346, 23.69417183226092), (37.97861493926421, 23.711489283485477), (37.97613325627219, 23.725645376311636), (37.97557765744567, 23.735388988331344), (37.976384690492, 23.74725138982627), (37.97928551690222, 23.752894712757204), (37.98713032615161, 23.7570626527695), (37.99317636620734, 23.76346963530805), (37.9931763035513, 23.77617247597929), (38.00005863496867, 23.78573200567021), (38.00457751669346, 23.79472497303984), (38.00926998017484, 23.80566058144109), (38.01728319195408, 23.81229651390254), (38.021615695016074, 23.821198550543656), (38.023937395711805, 23.833592430297703), (38.005700256051306, 23.86964791076203), (37.98364308961606, 23.86989187513544), (37.913033763503805, 23.895841658938313), (37.936886131362456, 23.944804496149146)]

coords= coords1 + coords2 + coords3

#Creamos la matriz del tamaño pertinente llena de 0s
lineasv= linea1v + linea2v + linea3v
tam= len(lineasv) + 1
lineas= np.zeros((tam, tam), dtype= "int64")

#Metemos los valores correspondientes a las líneas
"""Nº Nodo -> Ciudad
0-> Piraeus
1-> Faliro
2-> Moschato
3-> Kallithea
4-> Tavros
5-> Petrolona
6-> Thissio
7-> Monastiraki [transbordo con 3]
8-> Omonia [transbordo con 2]
9-> Victoria
10-> Attiki [transbordo con 2]
11-> Aghios Nikolaos
12-> Kato Patissia
13-> Aghios Eleftherios
14-> Ano Patissia
15-> Perissos
16-> Pefkakia
17-> Nea Ionia
18-> Iraklio
19-> Irini
20-> Neratziotissa
21-> Maroussi
22-> KAT
23-> Kifissia
----------------------------------------
24-> Aghios Antonios
25-> Sepolia
26-> Attiki [transbordo con 1]
27-> Larissa Station
28-> Metaxourghio
29-> Omonia [transbordo con 1]
30-> Panepistimio
31-> Syntagma [transbordo con 3]
32-> Akropoli
33-> Sygrou
34-> Neos Kosmos
35-> Aghios Ioannis
36-> Dafni
37-> Aghios Dimitrios
-----------------------------------------
38-> Egaleo
39-> Eleonas
40-> Kerameikos
41-> Monastiraki [transbordo con 1]
42-> Syntagma [transbordo con 2]
43-> Evangelismos
44-> Megaro Moussikis
45-> Ambelokipi
46-> Panormou
47-> Katehaki
48-> Ethniki Amyna
49-> Holargos
50-> Nomismatokopio
51-> Aghia Paraskevi
52-> Halandri
53-> Plakentias
54-> Pallini
55-> Kantza
56-> Koropi
57-> Airport"""
numite= 0
for e in lineasv:
    lineas[numite][numite+1]= e
    lineas[numite+1][numite]= e

    numite+= 1

#Metemos los valores de los transbordos a mano
transbordost= [6, 5, 6, 5] #Monastiraki - Omonia - Attiki - Syntagma
lineas[7][41]= transbordost[0]
lineas[41][7]= transbordost[0]
lineas[8][29]= transbordost[1]
lineas[29][8]= transbordost[1]
lineas[10][26]= transbordost[2]
lineas[26][10]= transbordost[2]
lineas[31][42]= transbordost[3]
lineas[42][31]= transbordost[3]

#Quitamos los valores de conexión entre el final de una línea y el comienzo de otra
lineas[23][24]= 0
lineas[24][23]= 0
lineas[37][38]= 0
lineas[38][37]= 0

#Creamos una clase Nodo, que almacenará el camino recorrido, el tiempo almacenado y la heurística (el tiempo aéreo al destino)
class Nodo:
    camino= []
    tiempo= 0
    h= 0

    def __init__(self, camino, tiempo, h):
        self.camino= camino
        self.tiempo= tiempo
        self.h= h

    def getTiempo(self):
        return self.tiempo

    def getCamino(self):
        return self.camino

    def getH(self):
        return self.tiempo + self.h

    def toString(self):
        print("Se tarda {} minutos\nRecorre las paradas: {}".format(self.tiempo, self.camino))

#Definimos una funcion para obtener el tiempo de un viaje directo entre dos nodos dados según el teorema de Haversine
def dist(nodoa, nodob):
    lata, lona= coords[nodoa]
    latb, lonb= coords[nodob]
    
    dlon= math.radians(lonb - lona)
    dlat= math.radians(latb - lata)
    r= 6371

    a= math.sin(dlat/2)**2 + math.cos(lata) * math.cos(latb) * math.sin(dlon/2)**2
    c= 2 * math.asin(math.sqrt(a))

    km= r * c

    return (km/80)*60

#Definimos una función para obtener las salidas posibles de Nodos dado
def conexos(nodo):
    con= []
    ite= 0
    for e in lineas[nodo]:
        if e!=0:
            con.append(ite)
        ite+=1

    return con

#Definimos una función para obtener el índice del elemento con menor valor dentro de array de Nodos dado
def menor(arr):
    nodo= 0
    min= arr[0].getH()
    ite= 0

    for e in arr:
        if e.getH() < min:
            nodo= ite
            min= e.getH()
        ite+=1

    return nodo

#Definimos una función para realizar el algoritmo A* sobre la matriz
def aestrella(nodoini, nodofin):
    pri= Nodo([nodoini], 0, dist(nodoini, nodofin))
    estaciones= []
    estaciones.append(pri)
    
    if(nodoini==nodofin):
        return pri

    while True:
        if not estaciones:
            print("Error, no existe camino")

        estmin= menor(estaciones)
        tAnt= estaciones[estmin].getTiempo()
        cAnt= estaciones[estmin].getCamino()
        estaciones.pop(estmin)

        nodoAct= cAnt[len(cAnt)-1]

        for e in conexos(nodoAct):
            if e not in cAnt:
                nodoSig= Nodo(cAnt + [e], tAnt + lineas[nodoAct][e], dist(e, nodofin))
                estaciones.append(nodoSig)

            if e == nodofin:
                return nodoSig

#Aquí escribir las estaciones inicio y destino según su código numérico descrito anteriormente :3
aestrella(38, 23).toString()


