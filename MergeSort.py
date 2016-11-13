x=[38,27,43,3,9,82,10,1]
y=[4,2,5,3,1]

def mergeSort(a):
    n=len(a)
    if n==1:
        return a
    else:
        L1=a[:(n/2)]
        L2=a[(n/2):]
        L1=mergeSort(L1)
        L2=mergeSort(L2)
        return merge(L1, L2)

def merge(a, b):
    c=[]
    while len(a)!=0 and len(b)!=0:
        if a[0]<b[0]:
            c.append(a[0])
            a.pop(0)
        else:
            c.append(b[0])
            b.pop(0)
    while len(a)!=0:
        c.append(a[0])
        a.pop(0)
    while len(b)!=0:
        c.append(b[0])
        b.pop(0)
    return c
