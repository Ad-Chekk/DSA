string_inp= input()  ## aa bb aa

list_inp = list(map(str, string_inp.split()))
print(list_inp)  

dicto = {}   # dictonary

for i in range(0,len(list_inp)):
        num=list_inp[i]
        dicto[num]=dicto.get(num, 0) + 1   ##add key,value  dicto[key]=dicto.get(key, value) + 1 
        get function check for value and if it dosent exist then it sets it to zero
 

# del dicto['key_name']     #to delete a key and value
# dicto.pop('key_name', None) # to delete values
    
print(dicto) 
keyss=[]
value=[]

for keys in dicto:     
    if(keys in dicto):
     keyss.append(dicto[keys])   ##list for keys only
     value.append(keys)          ##list for values only 
print(keyss) 
print(value)
print(" ".join(map(str, keyss)))  # 1 2 3 1 3     give input in space seperated format