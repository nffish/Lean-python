sum = 0
n = 99
while n>0:
    sum += n
    n = n-2
print(sum)




##exercise
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello,'+name+'!')



##break
n=1
while n<=100:
    if n>10:
        break
    print(n)
    n += 1
print('END')

##continue
n=0
while n < 10:
    n = n+1
    if n%2 ==0: # 如果n是偶数
        continue
    print(n)
    
