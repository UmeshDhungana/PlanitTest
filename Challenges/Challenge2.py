string = str(input("Enter input string: "))
count = dict()

for s in string:
    if s not in count.keys():
        count[s] = 1
        # print(count)
    else:
        count[s] += 1
        # print(count)

k = list(count.keys())      #list of keys
# print(k)
v = list(count.values())    #list of values
# print(v)

# print(k[max(v)])
print("Character with highest occurrence: ",k[v.index(max(v))])   #index for the 1st occurance


