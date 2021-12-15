import requests
f = open('d:/1.txt', 'r')
output = open('d:/2.txt', 'w')
stf = [line.rstrip() for line in f]
print(stf[0])
fil = stf[0]
c = 0
while fil != 'We':
    response = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + fil).text
    fil = response
    print(response)
    c = fil.count('We')
    if c > 0:
        break
output.write(response)
f.close()
output.close()
#k = 0
#k1 = 0
#output = open('c:/2.txt', 'r')
#for line in output:
#    k += 1
#    k1 += line.count('\n')
#print(k, k1)
#output.close()