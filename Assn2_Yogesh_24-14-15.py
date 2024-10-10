#Assignment : 2
#Yogesh
#24-14-15
#AM609: Data Science Tools and Techniques 

import numpy as np


print("Q1\n")
# a) Create a variable named var1 that stores an array of numbers from 0 to 30,inclusive. Print var1 and its shape. Hint : arange

var1 = np.arange(1,31)
print("output of a):\n",var1,"\nShape: ",np.shape(var1))


# b) Change var2 to a validly-shaped two-dimensional matrix and store it in a new variable called var2. Print var2 and its shape. Hint: Use the reshape function

var2 = np.reshape(var1,(6,5))
print("\nOutput of b):\n",var2,"\nShape: ",np.shape(var2))

# c) Create a third variable, var3 that reshapes it into a valid three-dimensional shape. Print var3 and its shape.

var3 = np.reshape(var1,(5,3,2))
print("\nOutput of c):\n",var3,"\nShape: ",np.shape(var3))

# d) Use two-dimensional array indexing to set the first value in the second row of var2 to -1. Now look at var1 and var3. Did they change? Explain what’s going on. (Hint: does reshape return a view or a copy?)
var2[1,0] = -1
print("\nOutput of d)\n var2 : \n",var2,"\n var1\n",var1,"\nvar3:\n",var3)

# Explaination :

# e) Another thing that comes up a lot with array shapes is thinking about how to aggregate over specific dimensions. Figure out how the NumPy sum function works (and the axis argument in particular) and do the following:
# (i) Sum var3 over its second dimension and print the result.
print("\nOutput of  e)\n(i)\n",np.sum(var3,axis=1))

# (ii) Sum var3 over its third dimension and print the result.
print("\nOutput of  e)\n(ii)\n",np.sum(var3,axis=2))

# (iii) Sum var3 over both its first and third dimensions and print the result.
print("\nOutput of  e)\n(iii)\n",np.sum(var3,axis=(0,2)))


# f) Write code to do the following:
# (i) Slice out the second row of var2 and print it.
print("\nOutput of f)\n(i)\n",var2[1])
      
# (ii) Slice out the last column of var2 using the -1 notation and print it.
print("\nOutput of f)\n(i)\n",var2[:,-1])
      
# (iii) Slice out the top right 2 × 2 submatrix of var2 and print it.
print("\nOutput of f)\n(i)\n",var2[:2,-2:])



#Q2
#a)

vector = np.arange(10)
vector = vector + 1
print("\nOutput of a):\n",vector)

#b)

A = np.vstack([vector, vector, vector, vector, vector, vector, vector, vector, vector, vector])
print("\nOutput of b):\n",A,"\nShape: ",np.shape(A))

for i in range(0,10):
    for j in range (0,10):
        A[i][j] = i+j

print(A)


#c) d) e)
import numpy.random as npr
data = np.exp(npr.randn ( 50 , 5 ) )
print("\nOutput of c):\n",data)

mean = np.mean(data, axis = 0)
variance = np.var(data, axis = 0)

print("\nOutput of d) and e)\n mean :",mean,"\nvariance :",variance)

#f)
#1) subtracting the mean off of each column,and 2) dividing each column by its standard deviation. Do this via broadcasting, and store the result in a matrix called normalized. To verify that you successfully did it, compute the mean and standard deviation of the columns of normalized and print them out.
print("output of f)\n")
std = np.std(data ,axis = 0)
print("standard deviation :\n",std)
data_new = data - mean
print(" data new\n",data_new)
normalized = data_new/std
print("normalized data \n",normalized)
mean_new = np.mean(normalized, axis=0)
std_new = np.std(normalized, axis=0)

print("\n mean of normalized :\n",mean_new,"\nStandard deviation of normalized :\n",std_new)


#Q3

def vendermonde(N):
    vec = np.arange(N) + 1
    vec = vec.reshape(-1,1)
    b = np.arange(N)
    global vender
    vender = vec**b
    return vender

vendermonde(12)

X = np.ones(12)
X = X.T
print(X)
b = np.matmul(vender,X)
inv_vender = np.linalg.inv(vender)
new = np.matmul(inv_vender , b)
print(new)
g = np.matmul(inv_vender,b)
print(g)
np.linalg.solve(vender,b)


x = 0
h = 0.1

for i in range(10):
    x =x+h
    print(x)




#Github link : https://github.com/Wo0oM/Yogesh_24-14-15.git
