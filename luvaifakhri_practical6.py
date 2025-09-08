#Luwai Fakhrudin Fakhri 31/08/2025

list1 = []

list1.append(20)
list1.append(50)
list1.append(5)
print ("A) After appending 3 numbers :", list1)

list1.insert(0,"Hello")
print ("B) After inserting the string :", list1)

list1.extend([78,5,3])
print ("C) After extending the list :", list1)

list1.pop()
print ("D) After removing the last element :", list1)

#list1.sort()
#E) Sorting only works for same data types

list1.reverse()
print ("F) After reversing the list :", list1)


print ("G) Count how many times (5) occurs :", list1.count(5))