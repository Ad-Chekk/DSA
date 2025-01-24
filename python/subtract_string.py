tar = str(input())
ref= str(input())
# refe = 'i'
# tar.replace('i', " ")
output = []
out = tar

for i in ref:
    for s in tar:
        if(i==s):
            output.append(i)
            out=out.replace(i, "")
print(out) 
print(output)