
size = int(input())

list = []

for i in range(0, size):
    list.append(int(input()))
    
print(list) 
even_sum=0
odd_sum=0
for i in range(0, size):
    if(list[i]%2==0):
        even_sum=even_sum+list[i]
    else:
      odd_sum=odd_sum+list[i] 
       
print(even_sum,"this is even")
print(odd_sum,"this is odd")