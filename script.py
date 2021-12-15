f = open('d:/1.txt', 'r')
output = open('d:/2.txt', 'w')
stf = [line.rstrip() for line in f]
st = []
sum0, sum1, sum2 = 0, 0, 0
for sl in stf:
    st.append(sl.split(';')[1:])
for el in st:
    summiddle = (int(el[0]) + int(el[1]) + int(el[2])) / 3
    sum0 += int(el[0])
    sum1 += int(el[1])
    sum2 += int(el[2])
    output.write(str(round(summiddle,9)))
    output.write('\n')
sum0 = round(sum0/len(st), 9)
sum1 = round(sum1/len(st), 9)
sum2 = round(sum2/len(st), 9)
out = str(sum0) + ' ' + str(sum1) + ' ' + str(sum2)
output.write(out)
f.close()
output.close()
