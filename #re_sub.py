#re_sub

import re

list1 = ['asdl1fksagh;lk1df','asd1glkj34t34tgj1hkl1', '1111']
list2 = [i for i in list1]
list3 = ['' for i in list1]
list4 = ['' for i in list1]

count = 1
theend = False
while theend == False:
    list3 = [i for i in list2]
    loop = False
    for i in range(len(list1)):
        print(count, i)
        count += 1
        rese = re.search('1', list3[i])
        if rese != None:
            list4[i] += ", " + rese.group()
            list2[i] = re.sub('1', '', list2[i], count=1)
            print(list2[i])
            loop = True
    if loop == False:
        theend = True

for i in range(len(list4)):
    if list4[i][:2] == ', ':
       list4[i] = list4[i][2:]

print(list4)
print(list2)