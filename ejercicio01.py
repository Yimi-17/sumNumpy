import sys
import numpy as np
array_1=range(1000)
print(array_1)

#Muestra cuanto de memoria utiliza el array
print(sys.getsizeof(16)*len(array_1))

array_2=np.arange(1000)
#Muestra cuanto de memoria utiliza el array creado con numpy
print(array_2.size*array_2.itemsize)