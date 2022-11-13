Array_A = [5,7,9,11,13] 
SumArray_A = 0
print(("ArrayA= ")+str(Array_A)) 
Array_Length = len(Array_A)
print(("Array Lenght = ")+str(Array_Length)) 
for x in range(Array_Length):
  SumArray_A += Array_A[x]
print(("Sumation of Array = ")+str(SumArray_A))
