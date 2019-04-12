# string we want to change
st = 'abcdefghijklmnopqrstuvwxyz'
#string we will print the output to
output = ''

#loop through the range of length of ST
for x in range(len(st)):
    # if there is a remainder or if its odd it will continue
    if x%2 != 0:
        # change the output string
        output = output + st[x]
#print output string
print(output)