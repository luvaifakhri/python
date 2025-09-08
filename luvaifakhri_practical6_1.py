#Luwai Fakhrudin Fakhri 31/08/2025

list = []

list.append(20)
list.append(50)
list.append(5)
print ("A) After appending 3 numbers :", list)

list.insert(1,200)
print ("B) After inserting the number :", list)

print ("C) Exending the list :", list.extend([78,5,3]))

print ("D) Removing the last element :", list.pop())

list.sort()
print ("E) Sorting the list :", list)

list.reverse()
print ("F) Reversing the list :",list)

print ("G) Count how many times (5) occurs :", list.count(5))

print ("H) Slicing the list  :", list[5:7])

print ("I) Sum of all element in the list :", sum(list))

print ("J) Number of element in list :", len(list))

copy_list = list.copy()
print ("K) Copied list :", copy_list)

copy_list.clear()
print ("L) Clear the list :" ,copy_list)
