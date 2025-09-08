#Luvai Fakhruddin Fakhri 29/08/2025

print ("Find prime numbers in a range.")
lower = int(input("Enter the LOWER LIMIT number : "))
upper = int(input("Enter the UPPER LIMIT number : "))
found = False

for i in range (lower , upper+1):
    flag = 1
    if i == 1 :
        flag = 1
    else :
        for j in range (2 , i):
            if i % j == 0:
                flag = 0
                break
    if flag == 1 :
        print (i)
        found = True
        
if not found :
    print ("There is no prime number in this range")
