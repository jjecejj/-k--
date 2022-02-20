import numpy as np
import random
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def line(x, y, z, x1, y1, z1):
    return ((x - x1) ** 2 + (y - y1) ** 2 + (z - z1) ** 2) ** 0.5

class Klaster:
    def __init__(self, x, y, z, N_clust):
        self.x = x
        self.y = y
        self.z = z
        self.N_clust = N_clust

        random.seed(1)#Зерно генератора случайных чисел

        A = []
        for i in range(0, N_clust):
            A.append([random.randint(0, max(self.x)), random.randint(0, max(self.y)), random.randint(0, max(self.z))])
        while (True):
            M = np.array(A)
            L = []
            B = []

            for i in range(0, N_clust):
                L.append([])
                for i1 in range(0, len(self.x)):
                    L[i].append(line(A[i][0], A[i][1], A[i][2], self.x[i1], self.y[i1], self.z[i1]))
            Min = []
            for i in range(0, len(self.x)):
                m = 10**10
                for i1 in range(0, N_clust):
                    if (m > L[i1][i]): m = L[i1][i]
                Min.append(m)

            for i in range(0,N_clust):B.append([])

            for i in range(0, len(self.x)):
                for i1 in range(0, N_clust):
                    if (L[i1][i] == Min[i]):B[i1].append(i)

            for i in range(0, N_clust):
                X, Y, Z = 0,0,0
                for i1 in range(0, len(B[i])):
                    X += self.x[B[i][i1]]
                    Y += self.y[B[i][i1]]
                    Z += self.z[B[i][i1]]
                if(len(B[i])>0):A[i] = [int(X / len(B[i])),int(Y / len(B[i])),int( Z / len(B[i]))]

            if ((A==M).all()):break

        self.A=np.array(A)
        self.B=B

    def get_indexes(self):
       M=[]
       for i in range(0,len(self.x)):
           for i1 in range(0,self.N_clust):
               for i2 in range(0,len(self.B[i1])):
                   if(self.B[i1][i2]==i):M.append(i1)
       return np.array(M)

    def plot(self):
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        A = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        for i in range(0, self.N_clust):
            m = '#' + random.choice(A) + random.choice(A) + random.choice(A) + random.choice(A) + random.choice(A) + random.choice(A)
            for i1 in range(0,len(self.x)):
                for i2 in range(0, len(self.B[i])):
                    if (self.B[i][i2] == i1):ax.scatter(self.x[i1], self.y[i1],self.z[i1],c=m)
        plt.show()

    def what_cluster(self, x, y, z):
        M=[]
        for i in range(0,self.N_clust):M.append(line(x,y,z,self.A[i][0],self.A[i][1],self.A[i][2]))
        for i in range(0,self.N_clust):
            if(min(M)==line(x,y,z,self.A[i][0],self.A[i][1],self.A[i][2])):return i

X,Y,Z=[],[],[]
for i in range(0,500):
    X.append(random.randint(0,100))
    Y.append(random.randint(0,100))
    Z.append(random.randint(0,100))

sys = Klaster(np.array(X), np.array(Y), np.array(Z), 3)#Входные Данные
print(sys.what_cluster(59,46,79))
print(sys.get_indexes())
sys.plot()