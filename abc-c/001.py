#!/usr/bin/env python
# -*- conding: utf-8 -*-

Deg,Dis=map(int,input().split())
direction=["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW","N"]
power=[0.0,0.3,1.6,3.4,5.5,8.0,10.8,13.9,17.2,20.8,24.5,28.5,32.7]
speed=int((Dis/60.0+0.05)*10+0.0001)/10.0
Dir=direction[int(Deg+112.5)//225]
for i in range(len(power)):
    if speed>=power[i]:wind=i
if wind==0:print("C 0")
else:print(Dir,wind)
