Array_A = [7,5,10,14,3,9,7]
Array_B = [9,10,3,4,2,5,7,1]
Array_C = []
ValueA = 0
ValueB = 0
ValueC = 0
print(("ArrayA = ")+str(Array_A)) 
print(("ArrayB = ")+str(Array_B))
Array_LengthA = len(Array_A) 
Array_LengthB = len(Array_B)
print(("Array LenghtA = ")+str(Array_LengthA)) 
print(("Array LenghtB = ")+str(Array_LengthB))
ValueA = Array_A.count(7) 
ValueB = Array_B.count(7)
print(("7 in ArrayA = ")+str(ValueA)) 
print(("7 in ArrayB = ")+str(ValueA))
Array_A.append(1)
Array_B.append(14)
Array_C = Array_A.copy()
Array_C.extend(Array_B)
ValueC = Array_C.count(7)
Array_C.sort()
Array_C.remove(7)
Array_D = Array_C.copy()
Array_D.reverse()
print(("ArrayC = ")+str(Array_C)) 
print(("ArrayD = ")+str(Array_D))
