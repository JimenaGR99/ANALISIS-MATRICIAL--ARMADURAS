class nodo: 
    
    def set_nodo(self,x,y,glx,gly):
        self.x=x # x--> Coordenada en x
        self.y=y # y--> Coordenada en y
        self.GLX=glx # GLX--> Grado de libertad en x
        self.GLY=gly # GLY--> Grado de libertad en y

    def __init__(self):
        self.x=0
        self.y=0
        self.GLX=0
        self.GLY=0        

#Se define la información contenida en el elemento
class elemento:
    #Se define la dirección del vector del elemento
    def __init__(self,N1,F1,L1):
        self.N=N1 # N--> Nodo donde inicia el vector de dirección
        self.F=F1 # F--> Nodo donde finaliza el vector de dirección
        self.L=L1 # L--> Longitud del elemento
     
class calculo_matriz:

    def __init__(self) :
        #Se define la información general de la armadura
        self.A= 0.0 #A--> 39.718 Define el área de la sección transversal de la armadura (ft2)
        self.E= 0.0 #E-->4385941.18896 Indica el módulo de elasticidad del material da la armadura (kLb/ft2)
        self.lista_nodos=list()
        self.lista_elementos=list()
        self.matriz1=[[]] #Matriz del elemento 1
        self.matriz2=[[]] #Matriz del elemento 2
        self.K_T=[[0 for x in range(6)] for y in range(6)]  #K_T--> Matriz de rigidez total de la armadura


    def Llenar_datos(self,x,y,GLX,GLY):
        #Se define la información del nodo
        self.lista_nodos=list() #Se crea una lista para almacenar la información de cada nodo   
        obj_nodo=nodo()
        obj_nodo.set_nodo(x,y,GLX,GLY) #Información del Nodo 1
        self.lista_nodos.append(obj_nodo)
        print(self.lista_nodos)




# obj_nodo=nodo()
# obj_nodo.set_nodo(3,4,5,6) #Información del Nodo 1
# lista_nodos.append(obj_nodo) #Se agrega la información corresponde al Nodo 1 en la lista--> lista_nodos[0]=nodo1
# obj_nodo=nodo()
# obj_nodo.set_nodo(0,0,1,2) #Información del nodo 2
# lista_nodos.append(obj_nodo) #Se agrega la información correspondiente al nodo 2 en la lista--> lista_nodos[1]=nodo2
# obj_nodo=nodo()
# obj_nodo.set_nodo(3,0,3,4) #Información del Nodo 3
# lista_nodos.append(obj_nodo)#Se agrega la información correspondiente al nodo 3 en la lista--> lista_nodos[2]=nodo3

    def llenar_elementos(self,N,F,L):
        self.lista_elementos=list() #Se crea una lista para almacenar la información de cada elemento
        obj_elemento=elemento(N,F,L) #Información del elemento 
        self.lista_elementos.append(obj_elemento) #Se agrega la información del elemento 1 en la lista
        # obj_elemento=elemento(lista_nodos[1],lista_nodos[0],5) #Información del elemento 2
        # lista_elementos.append(obj_elemento) #Se agrega la información del elemento 2 en la lista

    def RealizarCalculo(self):
        #Se calculan los cosenos directores de cada elemento
        #Elemento 1
        lamda_x_1=(self.lista_elementos[0].F.x-self.lista_elementos[0].N.x)/self.lista_elementos[0].L #Coseno director en x del elemento 1
        lamda_y_1=(self.lista_elementos[0].F.y-self.lista_elementos[0].N.y)/self.lista_elementos[0].L #Coseno director en y del elemento 1
                #Elemento 2
        lamda_x_2=(self.lista_elementos[1].F.x-self.lista_elementos[1].N.x)/self.lista_elementos[1].L #Coseno director en x del elemento 2
        lamda_y_2=(self.lista_elementos[1].F.y-self.lista_elementos[1].N.y)/self.lista_elementos[1].L #Coseno director en y del elemento 2
        #Se agregan los datos de la matriz del elemento 1
        self.matriz1[0].append(0) #K1--> Indica que la matriz de rigidez pertenece al elemento 1
        self.matriz1[0].append(self.lista_elementos[0].N.GLX) #Grado de libertad del nodo inicial en x
        self.matriz1[0].append(self.lista_elementos[0].N.GLY) #Grado de libertad del nodo inicial en y
        self.matriz1[0].append(self.lista_elementos[0].F.GLX) #Grado de libertad del nodo final en x
        self.matriz1[0].append(self.lista_elementos[0].F.GLY) #Grado de libertad del nodo final en y

        self.matriz1.insert(1,[self.lista_elementos[0].N.GLX]) #Grado de libertad del nodo inicial en x
        self.matriz1.insert(2,[self.lista_elementos[0].N.GLY]) #Grado de libertad del nodo inicial en y
        self.matriz1.insert(3,[self.lista_elementos[0].F.GLX]) #Grado de libertad del nodo final en x
        self.matriz1.insert(4,[self.lista_elementos[0].F.GLY]) #Grado de libertad del nodo final en y
        ''' A continuación se genera la información para calcular la matriz de rigidez del elemento 1 mediante el análisis matricial
        '''
        self.matriz1[1].append(lamda_x_1**2) 
        self.matriz1[2].append(lamda_x_1*lamda_y_1)
        self.matriz1[3].append(-lamda_x_1**2)
        self.matriz1[4].append(-lamda_x_1*lamda_y_1)

        self.matriz1[1].append(lamda_x_1*lamda_y_1)
        self.matriz1[2].append(lamda_y_1**2)
        self.matriz1[3].append(-lamda_x_1*lamda_y_1)
        self.matriz1[4].append(-lamda_y_1**2)

        self.matriz1[1].append(-lamda_x_1**2)
        self.matriz1[2].append(-lamda_x_1*lamda_y_1)
        self.matriz1[3].append(lamda_x_1**2)
        self.matriz1[4].append(lamda_x_1*lamda_y_1)

        self.matriz1[1].append(-lamda_x_1*lamda_y_1)
        self.matriz1[2].append(-lamda_y_1**2)
        self.matriz1[3].append(lamda_x_1*lamda_y_1)
        self.matriz1[4].append(lamda_y_1**2)

        #Se agregan los datos de la matriz del elemento 1
        self.matriz2[0].append(0) #K2--> Indica que la matriz de rigidez pertenece al elemento 2
        self.matriz2[0].append(self.lista_elementos[1].N.GLX) #Grado de libertad del nodo inicial en x
        self.matriz2[0].append(self.lista_elementos[1].N.GLY) #Grado de libertad del nodo inicial en y
        self.matriz2[0].append(self.lista_elementos[1].F.GLX) #Grado de libertad del nodo final en x
        self.matriz2[0].append(self.lista_elementos[1].F.GLY) #Grado de libertad del nodo final en y

        self.matriz2.insert(1,[self.lista_elementos[1].N.GLX]) #Grado de libertad del nodo inicial en x
        self.matriz2.insert(2,[self.lista_elementos[1].N.GLY]) #Grado de libertad del nodo inicial en y
        self.matriz2.insert(3,[self.lista_elementos[1].F.GLX]) #Grado de libertad del nodo final en x
        self.matriz2.insert(4,[self.lista_elementos[1].F.GLY]) #Grado de libertad del nodo final en y
        ''' A continuación se genera la información para calcular la matriz de rigidez del elemento 2 mediante el análisis matricial
        '''
        self.matriz2[1].append(lamda_x_2**2) 
        self.matriz2[2].append(lamda_x_2*lamda_y_2)
        self.matriz2[3].append(-lamda_x_2**2)
        self.matriz2[4].append(-lamda_x_2*lamda_y_2)

        self.matriz2[1].append(lamda_x_2*lamda_y_2)
        self.matriz2[2].append(lamda_y_2**2)
        self.matriz2[3].append(-lamda_x_2*lamda_y_2)
        self.matriz2[4].append(-lamda_y_2**2)

        self.matriz2[1].append(-lamda_x_2**2)
        self.matriz2[2].append(-lamda_x_2*lamda_y_2)
        self.matriz2[3].append(lamda_x_2**2)
        self.matriz2[4].append(lamda_x_2*lamda_y_2)

        self.matriz2[1].append(-lamda_x_2*lamda_y_2)
        self.matriz2[2].append(-lamda_y_2**2)
        self.matriz2[3].append(lamda_x_2*lamda_y_2)
        self.matriz2[4].append(lamda_y_2**2)


        print (self.matriz1, self.matriz2)

        #Creación de la matriz de rigidez total

        mayor_1 = 0
        menor_1 = 0


        for i,valor in enumerate(self.matriz1[0],start=0):
            
            if i==1:
                mayor_1=valor
                menor_1=valor
            
            if valor >= mayor_1:
                mayor_1=valor
                
            if valor < menor_1:
                menor_1=valor 

        print(menor_1,mayor_1)  

        mayor_2 = 0
        menor_2 = 0


        for i,valor in enumerate(self.matriz2[0],start=0):
            
            if i==1:
                mayor_2=valor
                menor_2=valor
            
            if valor >= mayor_2:
                mayor_2=valor
                
            if valor < menor_2:
                menor_2=valor 

        #print(menor_2,mayor_2)  



        if menor_1<=menor_2:
            menor_t=menor_1
        else:
            menor_t=menor_2

        if mayor_1>=mayor_2:
            mayor_t=mayor_1
        else :
            mayor_t=mayor_2

        #print(mayor_t,menor_t)

        for a in range(0,6):
            
            for b in range(0,6):
                self.K_T[a][b]=0        #llenar de ceros la matriz 


        for i in range(menor_t,mayor_t+1):
            
            bandera=0
            aux=[0,0]
            aux1=[0,0]
            
            if(i in self.matriz1[0] and i in self.matriz2[0] ):
                GAuxM1=self.matriz1[0].index(i) # posicion en columna para el Grado de libertad i para la matriz 1
                GAuxM2=self.matriz2[0].index(i) #posicion en columna para el Grado de libertad i para la matriz 2
                for b in range(1,5):
                    if  self.matriz1[0][b] == self.matriz2[0][b]:
                        self.K_T[i-1][b-1]=self.matriz1[GAuxM1][b]/self.lista_elementos[0].L+self.matriz2[GAuxM2][b]/self.lista_elementos[1].L



        for x, item in enumerate(K_T, start=0):
                    
            for y,tem1 in enumerate(K_T[x],start=0):
                if(self.K_T[x][y]==0):
                    
                    if(x+1 in self.matriz1[0]):
                        
                        GAuxM1=self.matriz1[0].index(x+1)
                        for it, item2 in enumerate(self.matriz1[0],start=0):
                            if  self.matriz1[0][it]==y+1:
                                GY=self.matriz1[0][it]
                                self.K_T[x][y]=self.matriz1[GAuxM1][it]/self.lista_elementos[0].L

                    
                    if(x+1 in self.matriz2[0]):
                        
                        GAuxM1=self.matriz2[0].index(x+1)
                        for it, item2 in enumerate(self.matriz2[0],start=0):
                            if  self.matriz2[0][it]==y+1:
                                
                                GY=self.matriz2[0][it]
                                self.K_T[x][y]=self.matriz2[GAuxM1][it]/self.lista_elementos[1].L


        print (self.K_T)
            
                

        



   
        
