import numpy as np
import matplotlib.pyplot as plt

import heapq
class MyHeap(object):
   def __init__(self, initial=None, key=lambda x:x):
       self.key = key
       self.index = 0
       if initial:
           self._data = [(key(item), i, item) for i, item in enumerate(initial)]
           self.index = len(self._data)
           heapq.heapify(self._data)
       else:
           self._data = []

   def push(self, item):
       heapq.heappush(self._data, (self.key(item), self.index, item))
       self.index += 1

   def pop(self):
       return heapq.heappop(self._data)[2]


def valide(x,y):
  return 1 <= x <= 1000 and 1 <= y <= 1000

def distanciaObj(x,y):
  global objs, idxObj  
  return ((x - objs[idxObj][0])**2 + (y - objs[idxObj][1])**2)**(1/2)

def dist(x1,y1,x2,y2):
  return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)

def heuristic(lista):
  global objs, other, idxObj
  x = lista[0]/100.00
  y = lista[1]/100.00
  distUsed = lista[4]
  
  nearEnemy = 0
  for i in other:
    if dist(x,y, i[0], i[1]) <= 1:
      nearEnemy += 1000 
  return distanciaObj(x,y)+ distUsed + nearEnemy

def getRoute(rutas, cur, myX, myY):
  ans = []
  while cur != [myX, myY]:
    ans.insert(0,[cur[0]/100.00, cur[1]/100.00])
    padre = rutas[tuple(cur)]    
    cur = [padre[0], padre[1]]
  return ans

def a_star(myX, myY):
  global idxObj
  global rutas
  movs =[[0,1],[1,0], [-1,0],[0,-1], [1,1], [1,-1], [-1,1], [-1,-1]]
  
  myX = int (myX*100)
  myY = int (myY*100)
  
  
  pq = MyHeap(key = heuristic)  
  pq.push([myX, myY, -1,-1, 0])
  # cur = [myX, myY, fatherX, fatherY, distUsed]
  while len(pq._data) > 0:
    cur = pq.pop()
    if distanciaObj(cur[0]/100.00, cur[1]/100.00) <= 0.6:  
      rutas[tuple([cur[0],cur[1]])] = tuple([cur[2], cur[3]])    
      return getRoute(rutas, [cur[0], cur[1]], myX, myY)
      break
    if tuple([cur[0],cur[1]]) not in rutas.keys():
      # Visitado
      rutas[tuple([cur[0],cur[1]])] = tuple([cur[2], cur[3]])
      for i in movs:
        aux = cur.copy()
        # Nos movemos
        aux[0] += 60*i[0]
        aux[1] += 60*i[1]
        # Las coord de mi padre
        aux[2] = cur[0] 
        aux[3] = cur[1]
        aux[4] += 60
        if valide(aux[0], aux[1]):
          pq.push(aux)
  return []

idxObj = 0 #Objetivo actual
objs = [[1.5,10]]  #Objetivos
other =[[3,3], [1,5], [7,7], [5,5], [3,4], [4,3], [1,2]] #Posiciones de otras tortugas
xIni = 3.00 # X actual
yIni = 1.00 # Y actual
rutas = {}
ruta = a_star(xIni, yIni)

print(ruta)
plt.scatter([i[0] for i in ruta], [i[1] for i in ruta])
plt.scatter([i[0] for i in other], [i[1] for i in other], color="red")
plt.show()
# Rutas generadas
plt.scatter([i[0]/100 for i in rutas.keys()], [i[1]/100 for i in rutas.keys()])
plt.scatter([i[0] for i in other], [i[1] for i in other], color="red")
plt.show()



