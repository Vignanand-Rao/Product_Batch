
# 1 = Range GCD Query with Point Updates

from math import gcd
class SegTree:
    def __init__(self,a):
        self.n=len(a)
        self.t=[0]*(4*self.n)
        self.build(a,1,0,self.n-1)
    def build(self,a,p,l,r):
        if l==r:
            self.t[p]=a[l]
            return
        m=(l+r)//2
        self.build(a,p*2,l,m)
        self.build(a,p*2+1,m+1,r)
        self.t[p]=gcd(self.t[p*2],self.t[p*2+1])
    def update(self,p,l,r,i,x):
        if l==r:
            self.t[p]=x
            return
        m=(l+r)//2
        if i<=m:
            self.update(p*2,l,m,i,x)
        else:
            self.update(p*2+1,m+1,r,i,x)
        self.t[p]=gcd(self.t[p*2],self.t[p*2+1])
    def query(self,p,l,r,ql,qr):
        if ql<=l and r<=qr:
            return self.t[p]
        m=(l+r)//2
        if qr<=m:
            return self.query(p*2,l,m,ql,qr)
        if ql>m:
            return self.query(p*2+1,m+1,r,ql,qr)
        return gcd(self.query(p*2,l,m,ql,qr),self.query(p*2+1,m+1,r,ql,qr))
    def change(self,i,x):
        self.update(1,0,self.n-1,i,x)
    def get(self,l,r):
        return self.query(1,0,self.n-1,l,r)
n=int(input())
a=list(map(int,input().split()))
st=SegTree(a)
q=int(input())
for _ in range(q):
    x=list(map(int,input().split()))
    if x[0]==1:
        st.change(x[1],x[2])
    else:
        print(st.get(x[1],x[2]))


# 2. Range Product Query with Point Updates

mod=1000000007
class SegTree:
    def __init__(self,a):
        self.n=len(a)
        self.t=[1]*(4*self.n)
        self.build(a,1,0,self.n-1)
    def build(self,a,p,l,r):
        if l==r:
            self.t[p]=a[l]%mod
            return
        m=(l+r)//2
        self.build(a,p*2,l,m)
        self.build(a,p*2+1,m+1,r)
        self.t[p]=(self.t[p*2]*self.t[p*2+1])%mod
    def update(self,p,l,r,i,x):
        if l==r:
            self.t[p]=x%mod
            return
        m=(l+r)//2
        if i<=m:
            self.update(p*2,l,m,i,x)
        else:
            self.update(p*2+1,m+1,r,i,x)
        self.t[p]=(self.t[p*2]*self.t[p*2+1])%mod
    def query(self,p,l,r,ql,qr):
        if ql<=l and r<=qr:
            return self.t[p]
        m=(l+r)//2
        if qr<=m:
            return self.query(p*2,l,m,ql,qr)
        if ql>m:
            return self.query(p*2+1,m+1,r,ql,qr)
        return (self.query(p*2,l,m,ql,qr)*self.query(p*2+1,m+1,r,ql,qr))%mod
    def change(self,i,x):
        self.update(1,0,self.n-1,i,x)
    def get(self,l,r):
        return self.query(1,0,self.n-1,l,r)
n=int(input())
a=list(map(int,input().split()))
st=SegTree(a)
q=int(input())
for _ in range(q):
    x=list(map(int,input().split()))
    if x[0]==1:
        st.change(x[1],x[2])
    else:
        print(st.get(x[1],x[2]))



# 3. Range Bitwise OR Query with Point Updates

class SegTree:
    def __init__(self,a):
        self.n=len(a)
        self.t=[0]*(4*self.n)
        self.build(a,1,0,self.n-1)
    def build(self,a,p,l,r):
        if l==r:
            self.t[p]=a[l]
            return
        m=(l+r)//2
        self.build(a,p*2,l,m)
        self.build(a,p*2+1,m+1,r)
        self.t[p]=self.t[p*2]|self.t[p*2+1]
    def update(self,p,l,r,i,x):
        if l==r:
            self.t[p]=x
            return
        m=(l+r)//2
        if i<=m:
            self.update(p*2,l,m,i,x)
        else:
            self.update(p*2+1,m+1,r,i,x)
        self.t[p]=self.t[p*2]|self.t[p*2+1]
    def query(self,p,l,r,ql,qr):
        if ql<=l and r<=qr:
            return self.t[p]
        m=(l+r)//2
        if qr<=m:
            return self.query(p*2,l,m,ql,qr)
        if ql>m:
            return self.query(p*2+1,m+1,r,ql,qr)
        return self.query(p*2,l,m,ql,qr)|self.query(p*2+1,m+1,r,ql,qr)
    def change(self,i,x):
        self.update(1,0,self.n-1,i,x)
    def get(self,l,r):
        return self.query(1,0,self.n-1,l,r)
n=int(input())
a=list(map(int,input().split()))
st=SegTree(a)
q=int(input())
for _ in range(q):
    x=list(map(int,input().split()))
    if x[0]==1:
        st.change(x[1],x[2])
    else:
        print(st.get(x[1],x[2]))



#4. K-th One in a Binary Array


class SegTree:
    def __init__(self,a):
        self.n=len(a)
        self.t=[0]*(4*self.n)
        self.build(a,1,0,self.n-1)
    def build(self,a,p,l,r):
        if l==r:
            self.t[p]=a[l]
            return
        m=(l+r)//2
        self.build(a,p*2,l,m)
        self.build(a,p*2+1,m+1,r)
        self.t[p]=self.t[p*2]+self.t[p*2+1]
    def update(self,p,l,r,i,x):
        if l==r:
            self.t[p]=x
            return
        m=(l+r)//2
        if i<=m:
            self.update(p*2,l,m,i,x)
        else:
            self.update(p*2+1,m+1,r,i,x)
        self.t[p]=self.t[p*2]+self.t[p*2+1]
    def kth(self,p,l,r,k):
        if l==r:
            return l
        m=(l+r)//2
        if self.t[p*2]>=k:
            return self.kth(p*2,l,m,k)
        return self.kth(p*2+1,m+1,r,k-self.t[p*2])
    def change(self,i,x):
        self.update(1,0,self.n-1,i,x)
    def get(self,k):
        if self.t[1]<k:
            return -1
        return self.kth(1,0,self.n-1,k)
n=int(input())
a=list(map(int,input().split()))
st=SegTree(a)
q=int(input())
for _ in range(q):
    x=list(map(int,input().split()))
    if x[0]==1:
        st.change(x[1],x[2])
    else:
        print(st.get(x[1]))



# 5. First Element Greater Than or Equal to X in a Range


class SegTree:
    def __init__(self,a):
        self.n=len(a)
        self.t=[0]*(4*self.n)
        self.build(a,1,0,self.n-1)
    def build(self,a,p,l,r):
        if l==r:
            self.t[p]=a[l]
            return
        m=(l+r)//2
        self.build(a,p*2,l,m)
        self.build(a,p*2+1,m+1,r)
        self.t[p]=max(self.t[p*2],self.t[p*2+1])
    def update(self,p,l,r,i,x):
        if l==r:
            self.t[p]=x
            return
        m=(l+r)//2
        if i<=m:
            self.update(p*2,l,m,i,x)
        else:
            self.update(p*2+1,m+1,r,i,x)
        self.t[p]=max(self.t[p*2],self.t[p*2+1])
    def find(self,p,l,r,ql,qr,x):
        if r<ql or l>qr or self.t[p]<x:
            return -1
        if l==r:
            return l
        m=(l+r)//2
        ans=self.find(p*2,l,m,ql,qr,x)
        if ans!=-1:
            return ans
        return self.find(p*2+1,m+1,r,ql,qr,x)
    def change(self,i,x):
        self.update(1,0,self.n-1,i,x)
    def get(self,l,r,x):
        return self.find(1,0,self.n-1,l,r,x)
n=int(input())
a=list(map(int,input().split()))
st=SegTree(a)
q=int(input())
for _ in range(q):
    x=list(map(int,input().split()))
    if x[0]==1:
        st.change(x[1],x[2])
    else:
        print(st.get(x[1],x[2],x[3]))



# 6. Count Zeros in a Range with Point Updates


class SegTree:
    def __init__(self,a):
        self.n=len(a)
        self.t=[0]*(4*self.n)
        self.build(a,1,0,self.n-1)
    def build(self,a,p,l,r):
        if l==r:
            self.t[p]=1 if a[l]==0 else 0
            return
        m=(l+r)//2
        self.build(a,p*2,l,m)
        self.build(a,p*2+1,m+1,r)
        self.t[p]=self.t[p*2]+self.t[p*2+1]
    def update(self,p,l,r,i,x):
        if l==r:
            self.t[p]=1 if x==0 else 0
            return
        m=(l+r)//2
        if i<=m:
            self.update(p*2,l,m,i,x)
        else:
            self.update(p*2+1,m+1,r,i,x)
        self.t[p]=self.t[p*2]+self.t[p*2+1]
    def query(self,p,l,r,ql,qr):
        if ql<=l and r<=qr:
            return self.t[p]
        m=(l+r)//2
        if qr<=m:
            return self.query(p*2,l,m,ql,qr)
        if ql>m:
            return self.query(p*2+1,m+1,r,ql,qr)
        return self.query(p*2,l,m,ql,qr)+self.query(p*2+1,m+1,r,ql,qr)
    def change(self,i,x):
        self.update(1,0,self.n-1,i,x)
    def get(self,l,r):
        return self.query(1,0,self.n-1,l,r)
n=int(input())
a=list(map(int,input().split()))
st=SegTree(a)
q=int(input())
for _ in range(q):
    x=list(map(int,input().split()))
    if x[0]==1:
        st.change(x[1],x[2])
    else:
        print(st.get(x[1],x[2]))



# 8. Maximum Pair Sum in a Range


class SegTree:
    def __init__(self,a):
        self.n=len(a)
        self.t=[(float('-inf'),float('-inf'))]*(4*self.n)
        self.build(a,1,0,self.n-1)
    def build(self,a,p,l,r):
        if l==r:
            self.t[p]=(a[l],float('-inf'))
            return
        m=(l+r)//2
        self.build(a,p*2,l,m)
        self.build(a,p*2+1,m+1,r)
        self.t[p]=self.merge(self.t[p*2],self.t[p*2+1])
    def merge(self,a,b):
        x=[a[0],a[1],b[0],b[1]]
        x.sort(reverse=True)
        return (x[0],x[1])
    def update(self,p,l,r,i,x):
        if l==r:
            self.t[p]=(x,float('-inf'))
            return
        m=(l+r)//2
        if i<=m:
            self.update(p*2,l,m,i,x)
        else:
            self.update(p*2+1,m+1,r,i,x)
        self.t[p]=self.merge(self.t[p*2],self.t[p*2+1])
    def query(self,p,l,r,ql,qr):
        if ql<=l and r<=qr:
            return self.t[p]
        m=(l+r)//2
        if qr<=m:
            return self.query(p*2,l,m,ql,qr)
        if ql>m:
            return self.query(p*2+1,m+1,r,ql,qr)
        return self.merge(self.query(p*2,l,m,ql,qr),self.query(p*2+1,m+1,r,ql,qr))
    def change(self,i,x):
        self.update(1,0,self.n-1,i,x)
    def get(self,l,r):
        a,b=self.query(1,0,self.n-1,l,r)
        return a+b
n=int(input())
a=list(map(int,input().split()))
st=SegTree(a)
q=int(input())
for _ in range(q):
    x=list(map(int,input().split()))
    if x[0]==1:
        st.change(x[1],x[2])
    else:
        print(st.get(x[1],x[2]))



# 9. Range Maximum Frequency of a Value in a Sorted Array

from bisect import bisect_left,bisect_right
n=int(input())
a=list(map(int,input().split()))
q=int(input())
for _ in range(q):
    l,r=map(int,input().split())
    ans=0
    while l<=r:
        x=a[l]
        j=bisect_right(a,x,l,r+1)
        ans=max(ans,j-l)
        l=j
    print(ans)

