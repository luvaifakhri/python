#Luwai Fakhrudin Fakhri 31/08/2025

my_tuple = (5, 10, 15, 20, 25, 15)

print (my_tuple[0])
print (my_tuple[-3])
print (my_tuple[1:5])

try :
    my_tuple[1] = 100
except:
    print ("Error: Tuples are immutable - cannot change an item.")
    
# Concatenation
tuple1 = (30,35)
tuple2 = my_tuple + tuple1
print (tuple2)

# Repetition
new_tuple = my_tuple * 2
print (new_tuple)

# Membership Test
if 15 in my_tuple:
    print ("True")
else:
    print ("False")

# Tuple Functions:
print (my_tuple.count(15))
print (my_tuple.index(20))
print (len(my_tuple))

#list -> tuple
list1 =[1,2,3]
tuple3 = tuple(list1)
print (tuple3)

#tuple -> list
list2 = list(tuple3)
print (list1)

