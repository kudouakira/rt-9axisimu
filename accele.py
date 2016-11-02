#!/usr/bin/env python

import rospy
import time
from sensor_msgs.msg import Imu

x=0
y=0
z=0
spe=0
dis=0

def acceleration_callback(message):
    global x,y,z
    x = message.linear_acceleration.x
    y = message.linear_acceleration.y
    z = message.linear_acceleration.z

#def integrate(time,value):
#    global dis,spe
#    spe = value * time
#    dis = 1/2 * (value * time * time)

def integrate(time,value):
    global dis,spe
    spe = spe + (value*time)
    dis = (spe*time) + (0.5*value*time*time)
    

if __name__ == '__main__':
    rospy.init_node('accele')
    sub = rospy.Subscriber('/imu/data_raw', Imu, acceleration_callback)

    f=open('accele.txt', 'w')
 
    a=0
#    b=0
#    c=0
    n=0
    p=0
    q=0
    h=0
    while not  (n==600):
        n += 1
        q += 1
        print str(x)
        a+=x
#        b+=y
#        c+=z
        
        if (q==100):
            o=a/100
#            p=b/10
#            r=c/10
            h+=10
            integrate(h,o)
#            integrate(h,p)
#            integrate(h,r)
            f.write(str(spe) +'    '+ str(dis))
            f.write('\n')
            q=0
            a=0
#            b=0
#            c=0
        time.sleep(0.1)

f.close()
