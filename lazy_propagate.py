def init(tree,data,s,e,node):
    if s == e: 
        tree[node] = data[s]
        return tree[node]
    mid = s+e>>1
    tree[node] = init(tree,data,s,mid,node*2)+init(tree,data,mid+1,e,node*2+1)
    return tree[node]

def propagate(tree,lazy,s,e,node):
    if lazy[node]:
        if s != e:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        tree[node] += lazy[node]*(e-s+1)
        lazy[node] = 0

def update(tree,lazy,s,e,node,l,r,val):
    propagate(tree,lazy,s,e,node)
    if e < l or r < s: return
    elif l <= s and e <= r:
        lazy[node] += val
        propagate(tree,lazy,s,e,node)
        return
    mid = s+e>>1
    update(tree,lazy,s,mid,node*2,l,r,val)
    update(tree,lazy,mid+1,e,node*2+1,l,r,val)
    tree[node] = tree[node*2]+tree[node*2+1]

def query(tree,lazy,s,e,node,l,r):
    propagate(tree,lazy,s,e,node)
    if e < l or r < s: return 0
    elif l <= s and e <= r: return tree[node]
    mid = s+e>>1
    return query(tree,lazy,s,mid,node*2,l,r)+query(tree,lazy,mid+1,e,node*2+1,l,r)

# 참조 
# https://baeharam.github.io/posts/algorithm/lazy-propagation/
# http://blog.naver.com/PostView.nhn?blogId=kks227&logNo=220824350353&parentCategoryNo=&categoryNo=292&viewDate=&isShowPopularPosts=true&from=search