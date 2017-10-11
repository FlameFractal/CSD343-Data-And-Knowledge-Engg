# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 17:26:43 2017

@author: Samarjoy Pandit
"""

Graph = {
        "O" : ["Z","S"],
        "Z" : ["A", "O"],
        "A" : ["Z", "S", "T"],
        "S" : ["O","A","F"],
        "T" : ["A", "L"],
        "L" : ["M","T"],
        "M" : ["L","D"],
        "D" : ["M","C"],
        "C" : ["P","R","D"],
        "P" : ["R","C","B"],
        "R" : ["S","P","C"],
        "F" : ["S","B"],
        "B" : ["P","G","F","U"],
        "G" : ["B"],
        "U" : ["B","H"],
        "H" : ["V","E"],
        "E" : ["H"],
        "V" : ["H","I"],
        "I" : ["V","N"],
        "N" : ["I"]
        }

def GetDegree(g):
    
    for node in g:
        print('Degree of', node, ':', len(g[node]))

def FindPath(g, start_vertex, end_vertex, path=[]):

        if path == None:
            path = []
            
        path = path + [start_vertex]
        
        if start_vertex == end_vertex:
            return path
        
        if start_vertex not in g:
            return None
        
        for vertex in g[start_vertex]:
            if vertex not in path:
                extended_path = FindPath(g, vertex, end_vertex, path)
                if extended_path: 
                    return extended_path
                
        return None
    
def getshortestpath(x):
    
    min = 10000
    minp = []
    
    for p in x:
        if(len(p) < min):
            min = len(p)
            minp = p
    
    return minp

def APSP(g, n):
    
    s = 0
    for k in g:
        if(k != n):
            r = FindPath(g, n, k)
            sp = getshortestpath(r)
            if(len(sp) > 0):
                s = s + len(sp) - 1
    
    return s

def closeness(g, node):
    
    s = APSP(g, node)
    if(s == 0):
        str = 'INFINITY'
    else:
        C = ((float)(len(g))/(float)(s))
        str = '' + repr(C)
    
    print('Closeness for', node, 'is:', str)
        
    
GetDegree(Graph)
print('Path:', FindPath(Graph, 'A', 'Q'))
closeness(Graph, 'A')
