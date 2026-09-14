import array

#creation
arr1 = array.array('i', [10,20,30,40,50])
print(arr1)

arr2 = array.array('i', [60,70,80,90,100])
print(arr2)

#traversal
for element in arr1:
    print(element , end=' ')

#insertion

arr1.insert(3 , 35)
print("\nAfter insertion: ", arr1)

#deletion
arr1.remove(30)
print("After deletion:", arr1)

arr1[2] = 30
print(arr1)

#sorting

arr3 = array.array('i' , [4,7,9,2,4,1,5])
print(arr3)

arr3 = sorted(arr3)
print("After sorting:", arr3)

sorted_arr3 = array.array('i', sorted(arr3))
print("Sorted array:", sorted_arr3)

#merging

arr4  = arr1 + arr2 
print(arr4)

#splitting

ix = int(len(arr4)/2)
ix

print(arr4[:ix])
print(arr4[ix:])
