#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:49:16 2023

From OSM point places of NE Italy To OSM point places in Trentino, by
limited longitudes and latitudes of Trentino

@author: lixiaoyue
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:49:16 2023

From OSM point places of NE Italy To OSM point places in Trentino, by
limited longitudes and latitudes of Trentino

@author: lixiaoyue
"""
import pandas as pd
import requests
from time import sleep
from csv import writer
import sys,os
import re
#region="Trentino"
# variable 1 CorrdinateBox
def ifInBox(latitude, longitude):
    inBox=False
    inBox=inBox or 46.671853<=float(latitude)<=46.971215 and 10.381315<=float(longitude)<=11.206114
    inBox=inBox or 45.783669<=float(latitude)<=47.014468 and 11.206114<=float(longitude)<=11.962911
    inBox=inBox or 46.531540<=float(latitude)<=47.094276 and 11.962911<=float(longitude)<=12.478587
    return inBox      
    

inputTables=["osm_global_place/natural.txt","osm_global_place/places.txt","osm_global_place/pofw.txt","osm_global_place/pois.txt","osm_global_place/traffic.txt","osm_global_place/transport.txt","osm_global_place/waterways.txt","osm_global_place/railways.txt","osm_global_place/roads.txt","osm_global_place/natural_a.txt","osm_global_place/places_a.txt","osm_global_place/pofw_a.txt","osm_global_place/pois_a.txt","osm_global_place/traffic_a.txt","osm_global_place/transport_a.txt","osm_global_place/buildings_a.txt","osm_global_place/landuse_a.txt", "osm_global_place/water_a.txt"]
outputTables=["osm_local_place/natural.txt","osm_local_place/places.txt","osm_local_place/pofw.txt","osm_local_place/pois.txt","osm_local_place/traffic.txt","osm_local_place/transport.txt","osm_local_place/waterways.txt","osm_local_place/railways.txt","osm_local_place/roads.txt","osm_local_place/natural_a.txt","osm_local_place/places_a.txt","osm_local_place/pofw_a.txt","osm_local_place/pois_a.txt","osm_local_place/traffic_a.txt","osm_local_place/transport_a.txt","osm_local_place/buildings_a.txt","osm_local_place/landuse_a.txt","osm_local_place/water_a.txt"]
#indexOfCoordinates=[6,7,6,6,6,6,7,9,12,6,7,6,6,6,6,7,6,6]
indexOfCoordinates=[5,6,5,5,5,5,6,8,11,5,6,5,5,5,5,6,5,5]

with open("osm_local_place/natural.txt", "a") as f:
    f.write("gid"+"\t"+"osm_id"+"\t"+"code"+"\t"+"fclass"+"\t"+"name"+"\t"+"coordinates"+"\n")
with open("osm_local_place/places.txt", "a") as f:
    f.write("gid"+"\t"+"osm_id"+"\t"+"code"+"\t"+"fclass"+"\t"+"population"+"\t"+"name"+"\t"+"coordinates"+"\n")
with open("osm_local_place/pofw.txt", "a") as f:
    f.write("gid"+"\t"+"osm_id"+"\t"+"code"+"\t"+"fclass"+"\t"+"name"+"\t"+"coordinates"+"\n")
with open("osm_local_place/pois.txt", "a") as f:
    f.write("gid"+"\t"+"osm_id"+"\t"+"code"+"\t"+"fclass"+"\t"+"name"+"\t"+"coordinates"+"\n")
with open("osm_local_place/traffic.txt", "a") as f:
    f.write("gid"+"\t"+"osm_id"+"\t"+"code"+"\t"+"fclass"+"\t"+"name"+"\t"+"coordinates"+"\n")
with open("osm_local_place/transport.txt", "a") as f:
    f.write("gid"+"\t"+"osm_id"+"\t"+"code"+"\t"+"fclass"+"\t"+"name"+"\t"+"coordinates"+"\n")
for i in range(0, 6):  
    dataList=[]
    dataList1=[]
    j=0
    with open(inputTables[i], "r") as f:
        next(f)
        for line in f.readlines():
            dataList.append(line)
            dataList1=dataList[j].strip("\n").split("\t")
            
            j=j+1
            longitude=dataList1[indexOfCoordinates[i]].split(" ")[0].split("(")[1]
            latitude=dataList1[indexOfCoordinates[i]].split(" ")[1].split(")")[0]
            #print(longitude + " "+latitude)
            #print(longitude + " "+latitude)
            if ifInBox(latitude, longitude):
                with open(outputTables[i], "a") as f:
                    for columns in range(0, indexOfCoordinates[i]):
                        f.write(dataList1[columns]+"\t")
                    f.write("POINT("+longitude+" "+latitude+")"+"\n")
    print(outputTables[i]+" Done!")  
         
with open("osm_local_place/waterways.txt", "a") as f:
    f.write("gid"+"\t"+"osm_id"+"\t"+"code"+"\t"+"fclass"+"\t"+"width"+"\t"+"name"+"\t"+"coordinates"+"\n")
with open("osm_local_place/railways.txt", "a") as f:
    f.write("gid"+"\t"+"osm_id"+"\t"+"code"+"\t"+"fclass"+"\t"+"name"+"\t"+"layer"+"\t"+"bridge"+"\t"+"tunnel"+"\t"+"coordinates"+"\n")
with open("osm_local_place/roads.txt", "a") as f:
    f.write("gid"+"\t"+"osm_id"+"\t"+"code"+"\t"+"fclass"+"\t"+"name"+"\t"+"ref"+"\t"+"oneway"+"\t"+"maxspeed"+"\t"+"layer"+"\t"+"bridge"+"\t"+"tunnel"+"\t"+"coordinates"+"\n") 
for i in range(6, 9):  
    dataList=[]
    dataList1=[]
    j=0
    coordinatePairNumber=0
    with open(inputTables[i], "r") as f:
        next(f)
        for line in f.readlines():
            dataList.append(line)
            dataList1=dataList[j].strip("\n").split("\t")
            j=j+1
            #longitude=dataList1[indexOfCoordinates[i]].split(" ")[0].split("(")[1]
            #latitude=dataList1[indexOfCoordinates[i]].split(" ")[1].split(")")[0]
            coordinates=dataList1[indexOfCoordinates[i]]
            newcoordinates="MULTILINESTRING(("
            coordinateTemp=coordinates.split("((")[1].split("))")[0]
            coordinatePairNumber=coordinateTemp.count(',')+1
            #print(coordinateTemp)
            #print(coordinatePairNumber)
            for npair in range(0, coordinatePairNumber):
                    #each pair of longitude latitude
                    coordinatePair=coordinateTemp.split(",")[npair]
                    longitude=coordinatePair.split(" ")[0]
                    latitude=coordinatePair.split(" ")[1]
                    #print(longitude+ " " +latitude)
                    if ifInBox(latitude, longitude):
                        newcoordinates=newcoordinates+longitude+" "+latitude+","           
            newcoordinates=newcoordinates+"))"
            if newcoordinates!="MULTILINESTRING(())":
                newcoordinates=newcoordinates.replace(",))", "))")
                with open(outputTables[i], "a") as f:
                    for columns in range(0, indexOfCoordinates[i]):
                        f.write(dataList1[columns]+"\t")
                    f.write(newcoordinates+"\n")
    print(outputTables[i]+" Done!")   

with open("osm_local_place/natural_a.txt", "a") as f:
    f.write("gid"+"\t"+"osm_id"+"\t"+"code"+"\t"+"fclass"+"\t"+"name"+"\t"+"coordinates"+"\n")
with open("osm_local_place/places_a.txt", "a") as f:
    f.write("gid"+"\t"+"osm_id"+"\t"+"code"+"\t"+"fclass"+"\t"+"population"+"\t"+"name"+"\t"+"coordinates"+"\n")
with open("osm_local_place/pofw_a.txt", "a") as f:
    f.write("gid"+"\t"+"osm_id"+"\t"+"code"+"\t"+"fclass"+"\t"+"name"+"\t"+"coordinates"+"\n")
with open("osm_local_place/pois_a.txt", "a") as f:
    f.write("gid"+"\t"+"osm_id"+"\t"+"code"+"\t"+"fclass"+"\t"+"name"+"\t"+"coordinates"+"\n")
with open("osm_local_place/traffic_a.txt", "a") as f:
    f.write("gid"+"\t"+"osm_id"+"\t"+"code"+"\t"+"fclass"+"\t"+"name"+"\t"+"coordinates"+"\n")
with open("osm_local_place/transport_a.txt", "a") as f:
    f.write("gid"+"\t"+"osm_id"+"\t"+"code"+"\t"+"fclass"+"\t"+"name"+"\t"+"coordinates"+"\n")    
with open("osm_local_place/buildings_a.txt", "a") as f:
    f.write("gid"+"\t"+"osm_id"+"\t"+"code"+"\t"+"fclass"+"\t"+"name"+"\t"+"type"+"\t"+"coordinates"+"\n")
with open("osm_local_place/landuse_a.txt", "a") as f:
    f.write("gid"+"\t"+"osm_id"+"\t"+"code"+"\t"+"fclass"+"\t"+"name"+"\t"+"coordinates"+"\n")
with open("osm_local_place/water_a.txt", "a") as f:
    f.write("gid"+"\t"+"osm_id"+"\t"+"code"+"\t"+"fclass"+"\t"+"name"+"\t"+"coordinates"+"\n")
for i in range(9, 18):  
    dataList=[]
    dataList1=[]
    j=0
    coordinatePairNumber=0
    with open(inputTables[i], "r") as f:
        next(f)
        for line in f.readlines():
            dataList.append(line)
            dataList1=dataList[j].strip("\n").split("\t")
            j=j+1
            #longitude=dataList1[indexOfCoordinates[i]].split(" ")[0].split("(")[1]
            #latitude=dataList1[indexOfCoordinates[i]].split(" ")[1].split(")")[0]
            coordinates=dataList1[indexOfCoordinates[i]]
            #print(coordinates)
            newcoordinates="MULTIPOLYGON((("
            coordinateTemp=coordinates.split("(((")[1].split(")))")[0]
            coordinatePairNumber=coordinateTemp.count(',')+1
            #print(coordinateTemp)
            #print(coordinatePairNumber)
            for npair in range(0, coordinatePairNumber):
                    #each pair of longitude latitude
                    coordinatePair=coordinateTemp.split(",")[npair]
                    longitude=coordinatePair.split(" ")[0]
                    latitude=coordinatePair.split(" ")[1]
                    oneLeft=False
                    twoLeft=False
                    oneRight= False
                    twoRight= False
                    if "((" in longitude:
                        twoLeft=True
                        #newcoordinates=newcoordinates+"(("
                        longitude=longitude.split("((")[1]
                    if "(" in longitude and "((" not in longitude:
                        oneLeft=True
                        #newcoordinates=newcoordinates+"("
                        longitude=longitude.split("(")[1]
                    if "))" in latitude:
                        #print(latitude)
                        latitude=latitude.split("))")[0]
                        twoRight= True
                        #print(latitude)
                    if ")" in latitude and "))" not in latitude:
                        #newcoordinates=newcoordinates+")"
                        latitude=latitude.split(")")[0]
                        oneRight= True
                    #print(line+":"+longitude+ " " +latitude)
                    if ifInBox(latitude, longitude):
                        if twoLeft==True:
                            newcoordinates=newcoordinates+"(("
                        if oneLeft==True:
                            newcoordinates=newcoordinates+"("
                        if twoRight==True:
                            newcoordinates=newcoordinates+longitude+" "+latitude+")),"
                                #print(newcoordinates)
                        if oneRight==True:
                            newcoordinates=newcoordinates+longitude+" "+latitude+"),"
                        if oneRight==False and twoRight==False:
                            newcoordinates=newcoordinates+longitude+" "+latitude+","    
                        if npair==coordinatePairNumber-1:
                            newcoordinates=newcoordinates.strip(",")                         
            newcoordinates=newcoordinates+")))"
            # if newcoordinates conatins any digit 
            if bool(re.search(r'\d',newcoordinates)):
                with open(outputTables[i], "a") as f:
                    for columns in range(0, indexOfCoordinates[i]):
                        f.write(dataList1[columns]+"\t")
                    newcoordinates=newcoordinates+"\n"
                    f.write(newcoordinates.replace(",)))\n", ")))\n"))

    print(outputTables[i]+" Done!") 
print(" ALL TABLES WERE Done!")
  