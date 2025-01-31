#fibonacci series 0 1 1 2 3 5 8 13


size_of_series = int(input())
list_of_fibo = []

list_of_fibo.insert(0,0)
list_of_fibo.insert(1,1)
for i in range(2,nu):
    list_of_fibo.append(list_of_fibo[i-1]+list_of_fibo[i-2])
    
print("".join(str(list_of_fibo)))    
    
    
    
    