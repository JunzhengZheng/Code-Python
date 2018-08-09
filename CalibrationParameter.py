# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:32:03 2018

@author: kk
"""

import os
import sys
sys.path.append(os.path.join('C:/Users/kk/Desktop/DeeCamp项目实践/uArm-Python-SDK-2.0/'))
import ArmSwift
import Kinematics
import numpy as np
'''
Swift = ArmSwift.uArmSwift()
initX, initY, initZ = Swift.get_position()
Swift.set_position(initX, initY, initZ)
X, Y, Z = Swift.get_position()
Angle1, Angle2, Angle3 = Swift.get_servo_angle()

Angle1  = Angle1

Xsimu, Ysimu, Zsimu = Kinematics.Angle2XYZ(Angle1-90, 90-Angle2, Angle2+Angle3)

deltaX = X - Xsimu
deltaY = Y - Ysimu
deltaZ = Z - Zsimu
print([deltaX, deltaY, deltaZ])
'''
X = np.array(0)
Position = [0,0,0]
f=open('ArmCoord.txt', 'w+')
f.write(str(X))

f.write(str(X))
f.write(str(X))
f.write('/n')
p= f.readline

f.close()
print(os.path)

# Swift.disconnect()