# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 15:52:52 2018

@author: kk
"""

import Kinematics
import Build_uArm
from Visualization import ShowState
import os
import sys
sys.path.append(os.path.join('C:/Users/kk/Desktop/DeeCamp项目实践/uArm-Python-SDK-2.0/'))
import ArmSwift
import time
import Planning
import numpy as np
import Structure
import copy


#Swift = ArmSwift.uArmSwift()
#initX, initY, initZ = Swift.get_position()


Angle = [0,0,0]

PositionStart = [250, 100, 30]
PositionEnd = [200, -150, 30]
Position = PositionStart
X,Y,Z = Position


Angle[0],Angle[1],Angle[2] = Kinematics.XYZ2Angle(X,Y,Z)
uArm = Build_uArm.BuildArm(Angle[0],Angle[1],Angle[2])
objStart = Structure.Obstacle(Center = PositionStart[0:2], Angle = 0, Size = [40, 40, PositionStart[2]], Type = 'cuboid')
objEnd = copy.deepcopy(objStart)
objEnd.Center = PositionEnd[0:2]
objEnd.H = PositionEnd[2]
obst = Structure.Obstacle(Center = [200,0], Angle = -45, Size = [80, 40, 50], Type = 'cuboid')
ShowState(uArm,Target=None,ShowAxes=True,xlim=[-300,300],ylim=[-300,300],Height=300,obstacle = obst)

ControlPoint, deltaAngle = Planning.GenControlPoint(obj1=objStart,obj2=objEnd,obst=obst)
print(ControlPoint)
#ControlPID = Planning.pid()
#path = Planning.StrightPath(Position1=PositionStart, Position2=PositionEnd)
path = Planning.BezierPath(PositionStart, PositionEnd, ControlPoint)
flag = Planning.CheckPath(path)
print(path)

if flag:
    for i in range(len(path)):
        if type(path) == list:
            Position = path[i]
        elif type(path) == np.ndarray:
            Position = list(path[i])
        
        X,Y,Z = Position   
        #Swift.set_pump(True)
        #Swift.set_position(X,Y,Z)
        #Swift.set_wrist(90+deltaAngle)

        Angle[0],Angle[1],Angle[2] = Kinematics.XYZ2Angle(X,Y,Z)
                
        #print(Angle)
        uArm = Build_uArm.BuildArm(Angle[0],Angle[1],Angle[2])
        ShowState(uArm,Target=None,ShowAxes=True,xlim=[-300,300],ylim=[-300,300],Height=300,obstacle = obst)
'''
while Swift.is_moving():
    pass
time.sleep(0.5)
Swift.set_pump(False)    
Swift.disconnect()          


for i in range(3):
        PositionError[i] = PositionEnd[i]-Position[i]
    Control = ControlPID.update(PositionError)
    print(Control)    
    for i in range(3):
        Position[i] = Position[i] + Control[i]
        
while Swift.is_moving():
    pass


    
    #plt.savefig("Figure/1.png")



    AngleError[i] = AngleEnd[i] - Angle[i]
    MaxFlag = AngleError[i] >= MaxAngle
    MinFlag = AngleError[i] <= -MaxAngle
    AngleSat[i] = (1-MaxFlag-MinFlag)*AngleError[i] + MaxFlag*MaxAngle + MinFlag*-MaxAngle
    MotorSpeed[i] = 0.5 * MotorSpeed[i] + 0.5 * AngleSat[i]
    Angle[i] = round(Angle[i] + MotorSpeed[i]*1)
#print(AngleError)
#print(MotorSpeed)
if sum([abs(AngleError[0]), abs(AngleError[1]), abs(AngleError[2])])<1:
    break

import random
for i in range(10000):
    Angle[0],Angle[1],Angle[2] = random.randint(-90,90), random.randint(-5,90), random.randint(1,180)
    X,Y,Z = Kinematics.Angle2XYZ(Angle[0],Angle[1],Angle[2])
    AngleR[0],AngleR[1],AngleR[2] = Kinematics.XYZ2Angle(X,Y,Z)
    if abs(Angle[0]-AngleR[0]) + abs(Angle[1]-AngleR[1]) + abs(Angle[2]-AngleR[2]) > 0.1:
        print(X,Y,Z)
        print(Angle)
        print(AngleR)
'''       
    