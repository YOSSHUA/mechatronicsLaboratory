#!/usr/bin/env python
import random
from math import *
from threading import Thread

import rospy
from geometry_msgs.msg import *
from std_srvs.srv import *
from turtlesim.msg import *
from turtlesim.srv import *
import time
import heapq
idxObj = 0 #Objetivo actual
objs = [[2.25,5.5],[1.5, 10.0],[5.75,7],[10.0, 4.0], [7.75,6.5],[5.5, 9.0]]  #Objetivos
other =[] #Posiciones de otras tortugas
lastDistance = 10000
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
  x2 =objs[idxObj][0]
  y2 =objs[idxObj][1]  
  d = sqrt(((x - x2)**2 + (y - y2)**2)  )  
  return d

def dist(x1,y1,x2,y2):
  return sqrt((x2 - x1)**2 + (y2 - y1)**2)

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
  rutas = {}
  movs =[[0,1],[1,0], [-1,0],[0,-1], [1,1], [1,-1], [-1,1], [-1,-1]]
  
  myX = int (myX*100)
  myY = int (myY*100)
  
  
  pq = MyHeap(key = heuristic)  
  pq.push([myX, myY, -1,-1, 0])
  # cur = [myX, myY, fatherX, fatherY, distUsed]
  while len(pq._data) > 0:
    cur = pq.pop()
    d =distanciaObj(cur[0]/100.00, cur[1]/100.00)     
    if d <= 0.6:        
      rutas[tuple([cur[0],cur[1]])] = tuple([cur[2], cur[3]])    
      return getRoute(rutas, [cur[0], cur[1]], myX, myY)
      break
    if tuple([cur[0],cur[1]]) not in rutas.keys():      
      # Visitado
      rutas[tuple([cur[0],cur[1]])] = tuple([cur[2], cur[3]])
      for i in movs:
        aux = cur[:]
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


class TurtleBot:

    def __init__(self):
        # Crea un nodo para esta tortuga de nombre 'turtlebot_controller'
        # se asegura de que sea unico con anonymous = True
        rospy.init_node('turtlebot_controller', anonymous=True)
        
        
        self.velocity_publisher = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)

        self.pose_subscriber = rospy.Subscriber('/turtle2/pose', Pose, self.turtle_pose)

        self.pose = Pose()
        self.pose_target_turtles = dict()

        self.rate = rospy.Rate(10)

        self.vel_msg = Twist()
        self.total_turtles = 7
        self.goal_turtle_name = None
        
    def turtle_pose(self, data):
        
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)
        self.pose.theta = round(self.pose.theta, 4)

    def turtle_target_pose(self, data, name):
        
        data.x = round(data.x, 4)
        data.y = round(data.y, 4)
        data.linear_velocity = round(data.linear_velocity, 4)
        self.pose_target_turtles[name] = data


    def euclidean_distance(self, goal_pose):
        
        return sqrt(pow((goal_pose.x - self.pose.x), 2) +
                    pow((goal_pose.y - self.pose.y), 2))


    def targets_path(self, tollerance=0.1, pen_offline=None):
        
        self.goal_turtle_name = None
        global idxObj, objs, other
        other =[] #Posiciones de otras tortugas
        trayectoria = []
        while idxObj < len(objs):
            bandera = False
            xIni = self.pose.x
            yIni = self.pose.y
            if len(trayectoria) == 0:
              other = [ [self.pose_target_turtles[k].x, self.pose_target_turtles[k].y] for k in self.pose_target_turtles.keys()]              
              #print(other) 
              trayectoria = a_star(xIni,yIni)
            if len(trayectoria) != 0:
                trayectoria[-1] = objs[idxObj]
            #print(trayectoria)
            for goal in trayectoria:
                #print(goal, idxObj)
                p_ = Pose(x=goal[0], y =goal[1], theta=0)
                #while(dist(p_.x, p_.y, self.pose.x, self.pose.y) >= 0.1):
                self.move_to_goal(p_)
                self.goal_turtle_name = self.get_closer_turtle()
                if self.goal_turtle_name in self.pose_target_turtles.keys():
                    if self.euclidean_distance(self.pose_target_turtles[self.goal_turtle_name]) < 1:
                        #print ('Turtle %s to close' % self.goal_turtle_name)
                        other = [ [self.pose_target_turtles[k].x, self.pose_target_turtles[k].y] for k in self.pose_target_turtles.keys()]
                        #print(other)
                        xIni = self.pose.x
                        yIni = self.pose.y                        
                        trayectoria = a_star(xIni, yIni)
                        bandera = True
                        break
            if bandera:
                continue
            else: 
                if (len(trayectoria) != 0):
                    self.move_to_goal(Pose(x=trayectoria[-1][0], y = trayectoria[-1][1], theta = 0))               
                    idxObj +=1
                    print('llegue al punto' , objs[idxObj-1])
                trayectoria = []


    def get_closer_turtle(self):
        
        min_distance = float("inf")
        min_turtle = None

        for name, pose in self.pose_target_turtles.items():
            distance = self.euclidean_distance(pose)

            if distance < min_distance:
                min_distance = distance
                min_turtle = name

        self.goal_turtle_name = min_turtle

        return self.goal_turtle_name

   
    def rota(self, goal_pose):
      tol = 0.08
      targetTheta = atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)
      theta = self.pose.theta
      dtheta = targetTheta - theta
      if dtheta < 0: 
          dtheta += 2 * pi
#      if abs(dtheta+2*pi)<abs(dtheta):
#          dtheta += 2*pi
#      elif abs(dtheta-2*pi)<abs(dtheta):
#          dtheta-=2*pi
      motion = Twist()
      motion.linear.x = 0;
      while(abs(dtheta) > tol):
          #print(dtheta, targetTheta, theta)
          
          motion.angular.z = dtheta*1.5
          self.velocity_publisher.publish(motion)
          #time.sleep(0.1)
          targetTheta = atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)
          theta = self.pose.theta
          dtheta = targetTheta - theta
          if dtheta < 0: 
            dtheta += 2 * pi
#          if abs(dtheta+2*pi)<abs(dtheta):
#              dtheta += 2*pi
#          elif abs(dtheta-2*pi)<abs(dtheta):
#              dtheta-=2*pi

    def move_to_goal(self, goal_pose):
      self.rota(goal_pose)
      lastDistance = 100000
      motion = Twist()
      distance = dist(goal_pose.x, goal_pose.y, self.pose.x, self.pose.y)
      
      while distance > 0.1 and distance <= lastDistance:
        #print(self.pose.x, self.pose.y,distance,lastDistance)
        motion.linear.x = distance*1.5
        self.velocity_publisher.publish(motion)
        #time.sleep(0.2)
        lastDistance = distance
        distance = dist(goal_pose.x, goal_pose.y, self.pose.x, self.pose.y)


    def main(self):
        
        thread = controller(args=[self])
        thread.start()
        time.sleep(2)
        self.targets_path()
        rospy.spin()


class controller(Thread):

    def __init__(self, args=()):
        super(controller, self).__init__()
        self.args = args[0]
        self.vel_msg = Twist()
        self.rate = rospy.Rate(10)
        self.total_turtles = self.args.total_turtles
        return

    def get_others_pose(self, t):
        if t != 2:       
            name = 'turtle' + str(t)
            rospy.Subscriber('/%s/pose' % name, Pose, self.args.turtle_target_pose, name)

    def run(self):
        for t in range(1, self.total_turtles):
            self.get_others_pose(t)


if __name__ == '__main__':
    try:
        tur = TurtleBot()
        tur.main()
    except rospy.ROSInterruptException:
        pass
