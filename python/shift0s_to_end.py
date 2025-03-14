# Example 1 :

# N=8 and arr = [4,5,0,1,9,0,5,0].

# There are 3 empty packets in the given set. These 3 empty packets represented as O should be pushed towards the end of the array

# Input :

# 8  – Value of N

# [4,5,0,1,9,0,5,0] – Element of arr[O] to arr[N-1],While input each element is separated by newline

# Output:

# 4 5 1 9 5 0 0 0





arr = [6,0,1,8,0,2]


index = n-1
zerosat = []
output = []

for i in range(0,len(arr)):
    if(arr[i]==0):
        zerosat.append(i)
        
        
for i in range(0,len(arr)):
    if(i in zerosat):
        continue
    
    output.insert(i, arr[i])
    
rem = len(arr)-len(output)
while(rem!=0):
    output.append(0)
    rem = rem -1
    
    
print(output)    
    