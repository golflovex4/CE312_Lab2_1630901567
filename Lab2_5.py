Array_A= [["Number ID","Name","Count","Status"],]
Array_A.insert(1,["1","Rubber","0","Out of stock"])
Array_A.insert(2,["2","Ruler","5","In stock"])
Array_A.insert(3,["3","Pencil","1","In stock"])
Array_A.insert(4,["4","Pen","10","In stock"])
Array_A.insert(5,["5","Colour Pencil","5","In stock"])
Array_A.insert(6,["6","A4 Paper","0","Out of stock"])
print("---------------In Stock--------------------") 
for x in Array_A:
  if x[3] == "In stock":
    print(x)
print("---------------Out of Stock--------------------") 
for x in Array_A:
  if x[3] == "Out of stock":
    print(x)
#("---------------Cut Stock--------------------")
Array_A[2][2] = 4 
Array_A[3][2] = 0
Array_A[4][2] = 8
Array_A[5][2] = 4
Array_A[3][3] = "Out of stock"

print("---------------Stock--------------------") 
for x in Array_A:
  print(x)
