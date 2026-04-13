import numpy as np

x = np.array([[1,2,3]])
y = np.array([[1,2,3]]).reshape(3,1)
z = np.random.randint(1,10,size =(4,4))
print(y)
print(np.dot(x,y))
print(z)

print(np.linalg.eigvals(z))