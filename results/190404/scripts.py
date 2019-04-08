# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 06:37:22 2019

@author: dawnduan
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import pandas as pd
import csv
from collections import defaultdict
#os.chdir("C:/RAWSim-O/results/190404/fcfs/fcfs-100/1_6/10/1-1-1-6-0.85-Letter-Fixed-7200-PPFAR-TAFCFS-SAConstantRatio-ISEmptiest-PSFixed-RPDummy-OBDefault-RBSamePod-MMNoChange-5")


def getValFrExp(path):
    os.chdir(path)
    #print(path)
    if len(os.listdir(path)) < 10:
        print(path)
    orFile = "orderprogression.csv"
    outFile = "output.log"
    #simCompTm = 
    with open(orFile, newline='') as File:  
        reader = csv.reader(File)
        row = None 
        for row in reader:
            pass
        
    simCompTm = row[0].split(";")[0]
    
    f = open(outFile, "r")
    ctt =f.read()
    
    val = []
    with open(outFile, "r") as File:
        lines = File.readlines()
        for i in [-5, -6, -7]:
            val.append(float(lines[i].split()[1]))
    val.append(float(simCompTm))
    return val

def getValFrExp1(path, data):
    os.chdir(path)
    orFile = "orderprogression.csv"
    outFile = "output.log"
    #simCompTm = 
    with open(orFile, newline='') as File:  
        reader = csv.reader(File)
        row = None 
        for row in reader:
            pass
        
    simCompTm = row[0].split(";")[0]
    
    f = open(outFile, "r")
    ctt =f.read()
    
    val = []
    sw = {-5:"Avg Turnover",
          -6:"Avg Throughput",
          -7:"Distance Travelling" }
    with open(outFile, "r") as File:
        lines = File.readlines()
        for i in [-5, -6, -7]:
            data[sw[i]].append(float(lines[i].split()[1]))
    #data["Sim Completion"]
    data["Sim Completion"].append(float(simCompTm))
    return val

def a_order(path, fl_nm):
    # write to execel
    data = [["Avg Turnover",
             "Avg Throughput",
             "Distance Travelling", 
             "Sim Completion"]]
    data_dict = defaultdict(list)
# get table values
    for inst_sz in sorted(os.listdir(path_or_sz)):  # 1,6 2,12.  
        data.append([inst_sz])
        path_pr = os.path.join(path_or_sz, inst_sz)
        
        for f in sorted(os.listdir(path_pr)): 
            p_sizes = os.path.join(path_pr, f)
            
            t = next(os.walk(p_sizes))[1][0]
            p_seeds = os.path.join(p_sizes, t)
            data.append(getValFrExp(p_seeds))
            getValFrExp1(p_seeds, data_dict)
            # add mean and variance
        data.append(pd.DataFrame.from_dict(data_dict).mean().values)
        data.append(pd.DataFrame.from_dict(data_dict).std().values)
            # add space
        data.append([])
    
        
    os.chdir('C:/RAWSim-O/results/190404/fcfs/results')
    file = fl_nm+'.csv'
    with open(file, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile, 
                            delimiter=',', 
                            quotechar='|', 
                            quoting=csv.QUOTE_MINIMAL)
        [writer.writerow(r) for r in data]
    csvFile.close()


###
# MAIN
###
    


# get sheet values
#path_ta='C:/RAWSim-O/results/190404/fcfs/Random'
#path_ta='C:/RAWSim-O/results/190404/fcfs/fcfs'
path_ta='C:/RAWSim-O/results/190404/fcfs/ShortestDistance'
os.chdir(path_ta)
for order_sz in sorted(os.listdir(path_ta)):
    path_or_sz = os.path.join(path_ta, order_sz)
    a_order(path_or_sz, order_sz)
            