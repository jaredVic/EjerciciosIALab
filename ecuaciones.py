import random
import time

A= False

print("Ejercicio 2 Practica 1 Sistema de Ecuaciones por busqueda Aleatoria\n")

while(A==False):
    B= random.randint(-100, 100)
    D= random.randint(-100, 100)
    E= random.randint(-100, 100)
    F= random.randint(-100, 100)
    
    G=(16*B)-(6*D)+(4*E)+(F)
    H=(B)-(8*D)+(E)+(F)
    I=(16*B)+(2*D)-(4*E)+(F)
    J=(9*B)+(8*D)-(3*E)+(F)
    
    if G==-16 and H==-64 and I==-4 and J==-64:
        A=True
        print("|B=%d\n"%(B))
        print("|D=%d\n"%(D))
        print("|E=%d\n"%(E))
        print("|F=%d\n"%(F))
        
print("Los Numeros son: B=%d, D=%d, E=%d, F=%d" %(B,D,E,F))
