class nodo: #objeto
    # x=0
    # y=0
    # GLX=0
    # GLY=0
    def set_nodo(self,x,y,glx,gly):
        self.x=x
        self.y=y
        self.GLX=glx
        self.GLY=gly 

    def __init__(self):
        self.x=0
        self.y=0
        self.GLX=0
        self.GLY=0        

class elemento:
    # N=nodo() #Nodo inicial
    # F=nodo() #Nodo final

    def __init__(self,N1,F1,L1):
        self.N=N1
        self.F=F1
        self.L=L1
         

lista_nodos=list()
obj_nodo=nodo()
obj_nodo.set_nodo(3,4,5,6)
lista_nodos.append(obj_nodo)#lista_nodos[0]=nodo1
obj_nodo=nodo()
obj_nodo.set_nodo(0,0,1,2)
lista_nodos.append(obj_nodo)#lista_nodos[1]=nodo2
obj_nodo=nodo()
obj_nodo.set_nodo(3,0,3,4)
lista_nodos.append(obj_nodo)#lista_nodos[2]=nodo3

lista_elementos=list()
obj_elemento=elemento(lista_nodos[1],lista_nodos[2],3)
lista_elementos.append(obj_elemento)
obj_elemento=elemento(lista_nodos[1],lista_nodos[0],5)
lista_elementos.append(obj_elemento)

# print (len(lista_nodos)) 
# for l in lista_nodos:
#     print (l.GLX)

# print (len(lista_elementos))
# for l in lista_elementos:
#     print (l.N.x,l.F.x)

matriz1=[[],[]]#elemento 1
matriz2=[[],[]]#elemento 2

matriz1[0].append('K1')
matriz1[0].append(lista_elementos[0].N.GLX)
matriz1[0].append(lista_elementos[0].N.GLY)
matriz1[0].append(lista_elementos[0].F.GLX)
matriz1[0].append(lista_elementos[0].F.GLY)

matriz1.insert(1,[lista_elementos[0].N.GLX])
matriz1.insert(2,[lista_elementos[0].N.GLY])
matriz1.insert(3,[lista_elementos[0].F.GLX])
matriz1.insert(4,[lista_elementos[0].F.GLY])

ladx=(lista_elementos[0].F.x-lista_elementos[0].N.x)/lista_elementos[0].L
lady=(lista_elementos[0].F.y-lista_elementos[0].N.y)/lista_elementos[0].L

