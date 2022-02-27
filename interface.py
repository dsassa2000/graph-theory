import tkinter as tk
import networkx as nx
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib as mpl
from tkinter import *
import numpy as np
import math

fenetre = tk.Tk()
fenetre.title("GRAPH MANIPULATOR")
fenetre.geometry("480x360")
fenetre.config(bg='#339999')
Acceuil=tk.Frame(fenetre)
Acceuil.config(bg='#66CCCC')
boutton_A=Button(Acceuil,text='Nouveu Graphe',width='20',height='5',command=lambda:Acceuil1())
boutton_A.pack(padx=50,pady=50)
Button(Acceuil, text='Decodage de Prufer',width='20',height='5',command=lambda: g.action4()).pack(
    padx=5,pady=30)
def Acceuil1():
    Acceuil.forget()
    frame_1.pack()


frame_1 = tk.Frame(fenetre)
frame_1.config(bg='#66CCCC')
label_1 = tk.Label(frame_1, text='Saisir le nombre des sommets : ')
label_1.pack(padx=20,pady=20)
entry_1 = tk.Entry(frame_1)
entry_1.pack()
button_1 = tk.Button(frame_1, text='submit_1',bg='#99FFCC', command=lambda: g.action_1())
button_1.pack(padx=10,pady=10)

frame_2 = tk.Frame(fenetre)
frame_2.config(bg='#66CCCC')
label_2 = tk.Label(frame_2,  text="Saisir la matrice d'adjacence du graphe  : ")
label_2.pack(padx=20,pady=20)
frame_2a = tk.Frame(frame_2)
frame_2a.pack()
button_2 = tk.Button(frame_2, text="submit_2",bg='#99FFCC', command=lambda: g.action_2())
button_2.pack(padx=20,pady=20)

frame_3 = tk.Frame(fenetre)
label_3 = tk.Label(frame_3, text="saisir le poids des arcs : ")
label_3.pack()
frame_3a = tk.Frame(fenetre)
frame_3a.pack()
entry_3 = tk.Entry(frame_3)
button_3 = tk.Button(frame_3, text="submit_3",bg='#99FFCC', command=lambda: g.action_3())
button_3.pack()
#Menu des algorithmes
menu_algo = tk.Frame(fenetre)
l = tk.Label(menu_algo, text="Algorithmes", bg="#66CC99")
l.place(x=250, y=25, anchor="center")

frame = tk.Frame(menu_algo, highlightbackground="blue",
                 highlightthickness=1, width=500, height=200, bd=0,bg='#66CC99')
frame.pack(side=LEFT)
Button(frame, text='Afficher Graphe', command=lambda: g.dessiner_graph_non_oriente()).pack(
    padx=10, pady=10)
Button(frame, text='Connexité', command=lambda: g.popup_window()).pack(
    padx=10, pady=10)
Button(frame, text='Coloration', command=lambda: g.coloration_du_graphe()).pack(
    padx=10, pady=10)
Button(frame, text='Kruskal', command=lambda: g.kruskaldessiner()).pack(
    padx=10, pady=10)
Button(frame, text='Djikstra', command=lambda: g.dijkstra(1)).pack(
    padx=10, pady=10)
Button(frame , text="retour à l'Acceuil",width='15',height='2',bg='#99FFCC', command=lambda: revenir2()).pack(
    padx=10, pady=10,side=BOTTOM)
def revenir2():
    menu_algo.forget()
    Acceuil.pack()    

####################################### frame prufer #######################################
frame_p = tk.Frame(fenetre)
frame_p.config(bg='#66CCCC')
label_p = tk.Label(frame_p, text='entrer le cardinal de prufer : ')
label_p.pack(padx=20,pady=20)
entry_p = tk.Entry(frame_p)
entry_p.pack()
button_p= tk.Button(frame_p, text='confirmer',bg='#99FFCC', command=lambda : g.print_prufer())
button_p.pack(padx=20,pady=20)
frame_p2=tk.Frame(fenetre)
frame_p2.config(bg='#66CCCC')
label_p2=tk.Label(frame_p2,  text="entrer la sequence  : ")
label_p2.pack(padx=20,pady=20)
button_p2= tk.Button(frame_p2,text="entrer", command= lambda : g.saisir())
button_p2.pack(padx=20,pady=20)
boutton_revenir=tk.Button(frame_p2,text="retour à l'Acceuil",width='15',height='2',bg='#99FFCC',command=lambda : revenir1())
boutton_revenir.pack(padx=10,pady=10,side=BOTTOM)
def revenir1():
        frame_p2.forget()
        Acceuil.pack()   


################################################ le code #################################################
class Arc:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2


class Graphe:
    G = nx.Graph()
    k = nx.DiGraph()
    text_var = []
    entries1 = []
    entries2 = []
    matrix = []
    arc = []
    poids = []
    AdjList = defaultdict(list)
    k = nx.Graph()
    parent = []
    rang = []
    spm = []
    entries=[]
    def action_1(self):
        self.afficher_mat()
        frame_1.forget()
        frame_2.pack()

    def action_2(self):
        self.matget()
        self.convert()
        self.list_arc()
        self.remove_arc()

        frame_2.forget()
        for i in range(len(self.arc)):
            self.entries2.append(tk.Entry(frame_3a, width=3))
            self.entries2[i].pack()
        frame_3.pack()
    def action_3(self):
        self.add_poids()
        frame_3.forget()
        frame_3a.forget()
        menu_algo.pack() 
    def action4(self):
        Acceuil.forget()
        frame_p.pack()       

    def afficher_mat(self): #afficher la matrice d'adjacence
        self.nsommet = entry_1.get()
        print(self.nsommet)
        for i in range(int(self.nsommet)):
            self.text_var.append([])
            self.entries1.append([])
            for j in range(int(self.nsommet)):
                self.text_var[i].append(tk.StringVar())
                self.entries1[i].append(
                    tk.Entry(frame_2a, textvariable=self.text_var[i][j], width=3))
                self.entries1[i][j].grid(row=i, column=j)

    def matget(self): #entrer la matrice d'adjacence 
        for i in range(int(self.nsommet)):
            self.matrix.append([])
            for j in range(int(self.nsommet)):
                self.matrix[i].append(self.text_var[i][j].get())
        print(self.matrix)

    def convert(self):  #convertir la matrice d'adjacence en liste d'adjecence
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if int(self.matrix[i][j]) == 1:
                    self.AdjList[i].append(j)
        for i in self.AdjList:
            print(i, end="")
            for j in self.AdjList[i]:
                print(" -> {}".format(j), end="")
                print()

    def list_arc(self): #faire une liste des arcs avec leurs poids
        for i in self.AdjList:
            for j in self.AdjList[i]:
                self.arc.append(Arc(i, j))

    def remove(self, obj1): #supprimer un objet
        for obj in self.arc:
            if (obj1.s1 == obj.s2 and obj1.s2 == obj.s1):
                self.arc.remove(obj)

    def remove_arc(self): #supprimer les aretes duppliquées 
        for obj in self.arc:
            self.remove(obj)

    def add_poids(self): #ajouter le poids de chaque aretes
        for i in range(len(self.entries2)):

            # print(self.entries2[i].get())
            self.arc[i].poids = self.entries2[i].get()
        for obj in self.arc:
           print(obj.poids)
    def dessiner_graph_non_oriente(self):
        for obj in self.arc:
                self.G.add_node((obj.s1+1))

                self.G.add_edge((obj.s1+1),(obj.s2+1),weight=obj.poids)
        pos1=nx.spring_layout(self.G) 
        labels = nx.get_edge_attributes(self.G,'weight')
        nx.draw_networkx_edge_labels(self.G,pos=pos1,edge_labels=labels)
        nx.draw(self.G,pos=pos1,with_labels=True)
        plt.show()
 ############################################### Kruskal ##################################################     
    def trouver_parent(self, sommet):
        if self.parent[sommet] == sommet:
            return sommet
        return self.trouver_parent(self.parent[sommet])

    def Kruskal(self):


        #tri des objets de la classe arc 

        self.arc.sort(key=lambda Arc: "poids")

        self.parent = [None] * int(self.nsommet)
        self.rang = [None] * int(self.nsommet)

        for n in range(int(self.nsommet)):
            #chaque sommet est le parent de lui meme dans le debut
            self.parent[n] = n
            self.rang[n] = 0  #le rang de chaque sommet est 0 dans le debut  

        for Arc in self.arc:
            root1 = self.trouver_parent(Arc.s1)
            root2 = self.trouver_parent(Arc.s2)

            #les parents de la source et la sommet destinataire n'existe pas dans la meme sous ensemble
            #ajouter le poids à l'arbre couvrant
            if root1 != root2:
                self.spm.append(Arc)
                if self.rang[root1] < self.rang[root2]:
                    self.parent[root1] = root2
                    self.rang[root2] += 1
                else:
                    self.parent[root2] = root1
                    self.rang[root1] += 1

        print("\n l'arbre couvrante de poids minimum est :", end=' ')
        L = 0
        for Arc in self.spm:
            L += int(Arc.poids)
        print("\n la somme des poids des arc est : L =  " + str(L))
########################################### Afficher Kruskal ########################################   
    def kruskaldessiner(self):
        g.Kruskal()
        for obj in self.spm:
            self.k.add_node((obj.s1+1))

            self.k.add_edge((obj.s1+1), (obj.s2+1), weight=obj.poids)
        pos1 = nx.spring_layout(self.k)
        labels = nx.get_edge_attributes(self.k,'weight')
        nx.draw_networkx_edge_labels(self.k,pos=pos1,edge_labels=labels)
        nx.draw(self.k, pos=pos1, with_labels=True)
        plt.show()
####################################### Coloration ############################################################
    def coloration_du_graphe(self):
        for obj in self.arc:
                self.G.add_node((obj.s1+1))

                self.G.add_edge((obj.s1+1),(obj.s2+1),weight=obj.poids)
        pos1=nx.spring_layout(self.G) 
        labels = nx.get_edge_attributes(self.G,'weight')
        nx.draw_networkx_edge_labels(self.G,pos=pos1,edge_labels=labels)
  
        color_lookup = nx.coloring.greedy_color(self.G)       
        low, *_, high = sorted(color_lookup.values())
        norm = mpl.colors.Normalize(vmin=low, vmax=high, clip=True)
        mapper = mpl.cm.ScalarMappable(norm=norm, cmap=mpl.cm.coolwarm)
        nx.draw(self.G,pos=pos1,node_color=[mapper.to_rgba(i) 
                    for i in color_lookup.values()], with_labels=True)
        plt.show()
        print(nx.coloring.greedy_color(self.G))
################################ Dijkstra ############################################################## 
    def Afficher(self, src, dist):
        
        print("les chemins les plus courts allant de ", src, " est : ")
        for noeud in range(len(self.mat1)):
            print((noeud+1), "\t", dist[noeud])        
    
    def minDistance(self, dist, S, T):
 
        # Initialiser la distance minimale pour le nœud
        min = math.inf
        min_index = -1
 
        for v in T:
            if dist[v-1] < min:
                min = dist[v-1]
                min_index = v-1
 
        # supprimer de T et ajouter dans S
        T.remove(min_index+1)
        S.append(min_index+1)
        return min_index
     
    def dijkstra(self, src):
        self.mat1= np.empty((int(self.nsommet),int(self.nsommet)))
        for obj in self.arc:
            for i in range(int(self.nsommet)):
                for j in range(int(self.nsommet)):
                    if(i==obj.s1 and j==obj.s2 or i==obj.s2 and j==obj.s1):
                      self.mat1[i][j]=int(obj.poids)
                      self.mat1[j][i]=int(obj.poids)
                    else:
                       self.mat1[i][j]==0
                       self.mat1[j][i]==0
 
        dist = [math.inf] * len(self.mat1)
        precedence = [-1] * len(self.mat1)
        dist[src-1] = 0
        precedence[src-1] = src-1
        S = []
        T = [(i+1) for i in range(len(self.mat1))]
 
        while len(S) < len(self.mat1):
 
            # Choisir un sommet u qui n'est pas dans l'ensemble S et
            # qui a une valeur de distance minimale
            u = self.minDistance(dist, S, T)
 
            # relaxation des sommets

            for v in range(len(self.mat1)):
                if (self.mat1[u][v] > 0) and (dist[v] > (dist[u] + self.mat1[u][v])):
                    dist[v] = dist[u] + self.mat1[u][v]
                    precedence[v] = u
        self.Afficher(src, dist) 
###################################### Connexitée ##################################################        
    def popup_window(self):
        self.connexite()

        window = tk.Toplevel()

        label = tk.Label(window, text=self.cx)
        label.pack(fill='x', padx=50, pady=5)

        button_close = tk.Button(window, text="Close", command=window.destroy)
        button_close.pack(fill='x')

    def connexite(self):
        if nx.is_connected(self.G) == True:
            self.cx = "le graphe est connexe"
        else:
            self.cx = "Graphe non connexe" 
    def print_prufer(self):
    
        self.n=entry_p.get() 
        frame_p.forget()
        for i in range(int(self.n)):
             self.entries.append(tk.Entry(frame_p2,width=3))
             self.entries[i].pack()  
        frame_p2.pack()
    def saisir(self):
        self.prufer = [0 for i in range(int(self.n))]
        for i in range(int(self.n)):
            self.prufer[i]= self.entries[i].get()
        printTreeEdges(self.prufer,int(self.n))           
##################################################### Decodage de prufer ######################################            
    
def printTreeEdges(prufer, m):
      
        nb_sommets = m + 2
      
    # initialiser le tableau de sommets
        sommet_set = [0] * nb_sommets
      
    # nombre d'occurence dans le code  
        for i in range(nb_sommets - 2):
            sommet_set[int(prufer[i]) - 1] += 1
      
        print("les arcs de E(G) est :")
      
    # trouver le min des feuilles n'existe pas dans prufer 
        j = 0
        P=nx.Graph()
        for i in range(nb_sommets - 2):
            for j in range(nb_sommets):
              
            # si j+1 n'existe pas dans prufer set 
                if (sommet_set[j] == 0):
                    P.add_node((j+1))
                    P.add_edge((j+1),int(prufer[i]))
                  
                # supprimer de Prufer set et afficher 
                # pair. 
                    sommet_set[j] = -1
                    print("(" , (j + 1),", ",int(prufer[i]),") ",sep = "",end = "")
                    sommet_set[int(prufer[i]) - 1] -= 1
                    c=prufer[i]
                    break
      
        j = 0
      
    # pour le dernier element
        for i in range(nb_sommets):
            if (sommet_set[i] == 0 and j == 0):
                 print("(", (i + 1),", ", sep="", end="")
                 j += 1
                 P.add_node((i+1))
                 P.add_edge((i+1),int(c))
            elif (sommet_set[i] == 0 and j == 1):
               print((i + 1),")")
               P.add_edge((i+1),int(c))
        
        pos1=nx.spring_layout(P) 
        nx.draw(P,pos=pos1,with_labels=True)
        plt.show()

      

####################################################### Main #################################################           
g = Graphe()


Acceuil.pack()
fenetre.mainloop()