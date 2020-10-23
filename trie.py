from collections import deque

class node:
    def __init__(self):
        self.g = dict()
        self.is_end = False
        self.s = ''

class trie:
    def __init__(self):
        self.root = node()
    
    def add(self,key):
        cur = self.root

        for k in key:
            if k not in cur.g:
                cur.g[k] = node()
            cur = cur.g[k]
        
        cur.is_end = True
        cur.s = key
    
    def search(self,key):
        cur = self.root

        for k in key:
            if k not in cur.g:
                return False
            cur = cur.g[k]
        
        return cur.is_end
    
    def start_with(self,key):
        cur = self.root

        for k in key:
            if k not in cur.g:
                return None
            cur = cur.g[k]
        
        q = deque()
        q.append(cur)
        ret_list = []
        while q:
            now = q.popleft()
            if now.is_end:
                ret_list.append(now.s)
            for k in now.g.keys():
                q.append(now.g[k])
        return ret_list

            