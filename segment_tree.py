import math

N = 5
h = 2**int(math.ceil(math.log2(N)+1))
tree = [0]*h
data = []

def init(tree,s,e,node):
    if s == e:
        tree[node] = data[s]
        return tree[node]
    mid = s+e>>1
    tree[node] = init(tree,s,mid,node*2)+init(tree,mid+1,e,node*2+1)
    return tree[node]

def query(tree,s,e,node,l,r):
    if e < l or l < s: return 0
    elif l <= s and e <= r: return tree[node]
    mid = s+e>>1
    return query(tree,s,mid,node*2,l,r) + query(tree,mid+1,e,node*2+1,l,r)

def update(tree,s,e,node,i,val):
    if e < i or i < s: return tree[node]
    elif s == e:
        tree[node] = val
        return tree[node]
    mid = s+e>>1
    tree[node] = update(tree,s,mid,node*2,i,val) + update(tree,mid+1,e,node*2+1,i,val)
    return tree[node]