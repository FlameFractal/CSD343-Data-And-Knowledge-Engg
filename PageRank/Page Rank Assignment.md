## Page Rank Assignment

**Group 26:**

- Samarjoy
- Saksham
- Vishal
- Saurabh
- Akanksha

```python
import numpy as np

# define matrix A
A = np.array([[-1, 0, 0, 1/3], [1/2, -1, 0, 1/3], [1/2, 1/2, -1, 1/3], [0, 1/2, 1, -1], [1, 1, 1, 1]]) 

#define matrix B
B = np.array([0, 0, 0, 0, 1])

# use least squares to minimise residual error and calculate one possible solution
sol= np.linalg.lstsq(A, B)
print('W = ',sol[0][0])
print('X = ',sol[0][1])
print('Y = ',sol[0][2])
print('Z = ',sol[0][3])

# verify the solution by checking r=w*r
sol_transpose = np.array([[0.12903226],  [0.19354839], [0.29032258], [0.38709677]])
Acopy = np.array([[0, 0, 0, 1/3], [1/2, 0, 0, 1/3], [1/2, 1/2, 0, 1/3], [0, 1/2, 1, 0]])
print("\n\nVerification r=w*r\n\n",Acopy,"\n*\n",tra,"\n=\n",np.dot(Acopy,sol_transpose))
```


![](https://dl2.pushbulletusercontent.com/bnS9IgUj69YgUi4VQwoyHNtHyZ1G2SIm/image.png)