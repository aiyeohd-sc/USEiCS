№2
print("x,y, z, w, F" )
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            for w in range(0,2):
                F = (x and not(y)) or (y==z) or not(w)
                if F == False:
                    print(x,y,z,w,F)



№5
for n in range(1, 1000):
    n2 = bin(n)[2:]
    if n%5 == 0:
        n2= n2 + bin(n)[2:]
    else:
        n2 = n2 + '1'
    if n % 7 == 0:
            n2 = n2+ bin(7)[2:]
    else:
        n2 = n2 + '1'
    r = int(n2,2)
    if r < 1728404:
        print(n, n2)

or

def tri(n):
    n3 = ""
    while n > 0:
        n3 = str(n%3) + n3
        n //=3
    return n3
for n in range(1, 1000):
    n3 = tri(n)
    if n % 3 == 0:
        n3 = n3 + n3[-2] + n3[-1]
    else:
        n33 = tri(n%3 *3)
        n3 = n3 +n33
    r = int(n3, 3)
    if r <= 150:
        print(n, r)


№6
from turtle import *
color('green')
tracer(0)
screensize(10000, 10000)
l = 30
for i in range(4):
    forward(l*5)
    right(90)
    forward(l*10)
    right(90)
up()
for x in range(0, 50):
    for y in range(0, 50):
        setpos(x*l, y*l)
        dot(4, 'red')
done()


№8
from itertools import product
mass = product('АГИЛМОРТ', repeat=5)
k = 1
for word in mass:
    word = "".join(word)
    if k % 2 ==0:
        if word[0]!= "А" and word[0]!="Г":
            if word.count('Р') >= 2:
                print(k,word)
or


from itertools import permutations
mass = permutations('0123456789ABC', r = 7)
counter = 0
for word in mass:
    sos = "".join(word)
    sos = sos.replace("1", 'w').replace('3', 'w').replace('5', 'w').replace('7', 'w').replace('9', 'w')
    if "wB" not in sos and 'Bw' not in sos and word[0] != "0":
        counter +=1
print(counter)


№9
counter = 0
for line in open('9.txt'):
    a = [int(x) for x in line.split()]
    p = [ x for x in a if a.count(x) == 1]
    if len(p)==5:
        s = sorted(p)
        d = 2*(s[0] + s[4])
        s1 = s[1]+s[2]+s[3]
        if d >= s1:
            counter += 1
    print(counter)

№14
 for x in range(1,2031):
    counter = 0
    s = (3**100)-x
    while s>0:
        if s%3==0:
            counter+=1
        s //= 3
    if counter==1:
        print(x)
or

s ="0123456789ABCDEFGHIJK"
for x in s:
    x1 =int(f"82934{x}2",21)
    x2 =int(f'2924{x}{x}7', 21)
    x3 =int(f'67564{x}8', 21)
    if (x1+x2+x3)%20==0:
        print((x1+x2+x3)//20)
or

counter=0
s = 2*(2401**525)+3*(343**524)-4*(49**523)+5*(49**522)-6*(7**521)- 35
while s>0:
    if s%49<=9:
        counter+=1
    s//=49
print(counter)
for x in range(1,200):
    print(chr(x))


№16
import sys
sys.setrecursionlimit()
sys.setrecursionlimit(43500)
def  g(n):
    if n <= 9:
        return 3*n
    if n>9:
        return g(n-4)+2
def f(n):
    return g(n-1)+g(n-3)
print(f(42999))

or

b =dict()
def f(n):
    if n < 10:
        b[n] = n
    if n >= 10:
        b[n] = 3*n +b[n-3]
for n in range(1, 6500):
    f(n)
print((b[6250] +2*b[6244]) / b[6238])
№ 17

lst = [int(x) for x in open('9.txt')]
counter= 0
lst2 = []
mx= max( x for x in lst if 10000<= x<= 99999 and x%100==37)
for i in range(0, len(lst)-1):
    if (10000<= abs(lst[i]) <= 99999) + (10000<= abs(lst[i+1]) <= 99999)==1:
        if (lst[i]+lst[i+1])**2 > mx**2:
            counter += 1
            lst2.append(lst[i]+lst[i+1])
print(counter)
print(max(lst2))

№19,20,21
def f(a, m):
    if a <= 15: return m %2 == 0
    if m == 0: return 0
    h = [f(a - 3, m - 1), f(a - 8, m - 1), f(a // 3, m - 1)]
    return any(h) if m%2 !=0 else all(h)
print([ s for s in range(16, 1000) if f(s, 2)])
print([ s for s in range(16, 1000) if not f(s, 1) and f(s, 3)])
print([ s for s in range(16, 1000) if not f(s, 2) and f(s,4)])

or

def f(a, b, m):
    if a + b >= 81:
        return m %2 == 0
    if m == 0: return 0
    h = [f(a + 1, b, m -1), f(a * 2, b, m-1), f(a, b +1, m-1), f(a, b *2, m - 1)]
    return any(h) if m%2 != 0 else any(h)

print([s for s in range(1, 74) if f(7, s, 2)])
print([s for s in range(1, 74) if not f(7, s, 1) and f(7, s, 3)])
print([s for s in range(1, 74) if not f(7, s, 2) and f(7, s, 4)])

№23
def f(xn, xk):
    if xn == xk: return 1
    if xn<xk or xn == 28: return 0
    return f(xn-3, xk)+f(xn//3, xk)+f(xn//2, xk)
print(f(46, 20)*f(20, 3))

or

def f(xn, xk):
    if xn == xk: return 1
    if xn>xk: return 0
    return f(xn+1, xk)+f(xn+2, xk)+f(xn*2, xk)
print(f(5, 13)*f(13, 25))
№27
f =open('9.txt')
data = []
for s in f:
    s =s.replace(',','.')
    data.append([float(x) for x in s.split()])
print(len(data))

def dist(p1, p2):
    x1,y1,x2,y2 = *p1, *p2
    return ((x2-x1)**2 +(y2-y1)**2)**0.5

def getCluster(p0):
    cluster = [p for p in data if dist(p0, p)<2]
    if len(cluster)!=0:
        for p in cluster:
            data.remove(p)
        nextCluster = [getCluster(p) for p in cluster]
        cluster += sum(nextCluster, [])
    return cluster

clusters = []
while len(data)!=0:
    cluster = getCluster(data[0])
    print(len(cluster))
    clusters.append(cluster)

def centored(cluster):
    m = []
    for p in cluster:
        sm = sum(dist(p, p1) for p1 in cluster)
        m.append([sm, p])
    return min(m)[1]

centroids = [centored(cluster) for cluster in clusters]
Px = int(sum(x for x,y in centroids)/len(centroids)*1000)
Py = int(sum(y for x,y in centroids)/len(centroids)*1000)
print(Px, Py)

