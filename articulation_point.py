count = 0
def dfs(x,is_root,visited,cut):
    global count
    count += 1
    visited[x] = count
    ret = visited[x]

    cnt = 0
    for n in graph[x]:

        '''
        자식 노드가 아직 방문하지 않은 지점이라면 갈 수 있는 지점 중 가장 낮은 번호의 지점을 찾는다
        낮은 번호의 지점이 현재 값이거나 높다면 현재 지점은 단절점이 된다.
        '''
        if not visited[n]:
            cnt += 1

            low = dfs(n,False,visited,cut)
            if not is_root and low >= visited[x]:
                cut.add(x)
            ret = min(ret,low)
        # 이미 방문을 한 곳이라면 현재 지점을 거쳐 갈 수 있는 지점 중 가장 작은 지점을 갖고 있는다.
        else:
            ret = min(ret,visited[n])
    
    # 현재 지점이 루트이고 자식이 2개 이상이라면 단절점
    if is_root and cnt >= 2:
        cut.add(x)
    return ret

'''
참고
https://www.crocus.co.kr/1164
https://bowbowbow.tistory.com/3
'''