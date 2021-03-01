import sys
import heapq

while True:
    n,m = map(int,sys.stdin.readline().rstrip().split(" "))
    if n == 0 and m == 0:
        break
    start,end = map(int,sys.stdin.readline().rstrip().split(" "))
    graph = []
    minheap = []
    dist = {}
    path = {}
    deletelst = []   #여기까지 변수 설정 deletelst는 뒤에보면암

    for i in range(n):
        dist[i] = 10000  #dist 최대값
        graph.append({})
        deletelst.append(set([]))  #지울 간선 담는 데 중복떄매 집합의 리스트로 
        path[i] = [] # backtracking용 경로저장

    for _ in range(m): #graph
        u,v,p = map(int,sys.stdin.readline().rstrip().split(" "))
        graph[u][v] = p 

    dist[start] = 0
    heapq.heappush(minheap,(0,start))

    while minheap: #다익스트라
        dist_check, tostart = heapq.heappop(minheap)

        if dist_check > dist[tostart]:
            continue
        togos = graph[tostart].keys()

        for togo in togos:
            
            dist_new = graph[tostart][togo] + dist_check
            if dist[togo] == dist_new:
                path[togo].append(tostart) # 다수 경로 존재하므로 동일할 때도 경로 저장
            if dist[togo] > dist_new:
                dist[togo] = dist_new # 업데이트시 경로 저장
                heapq.heappush(minheap,(dist_new,togo))
                path[togo] = [tostart]
    
    deleted = {}
    todelete = [end] 

    while todelete: #백트래킹하면서 지울 경로들 deletelst에 저장
        temp_todelete = set([])
        for de in todelete: # todelete이 지울 지울 목적지 노드 리스트, 이거 왜 리스트냐면 
            for d in path[de]: # 하나로 최소경로가 둘 이상일 경우, 얘가 리스트라서 그 while문 돌리려면 리스트
                deletelst[d].add(de) # 지울 간선 추가
                temp_todelete.add(d) # 다음 for문 갈 거
        todelete = list(temp_todelete - set([start])) # 다음 for문 갈 거에서 start로 돌아간거 제거

    for i,todel in enumerate(deletelst): # 지우는거
        todels = list(todel)
        for td in todels:
            del(graph[i][td])
        
    minheap = []
    dist = {}
    
    for i in range(n): # weight재설정
        dist[i] = 10000

    dist[start] = 0
    heapq.heappush(minheap,(0,start))

    while minheap: # 다익스트라!
        dist_check, tostart = heapq.heappop(minheap)
        if dist_check > dist[tostart]:
            continue
        togos = graph[tostart].keys()

        for togo in togos:
            dist_new = graph[tostart][togo]+dist[tostart]
            if dist[togo] > dist_new:
                dist[togo] = dist_new
                heapq.heappush(minheap,(dist_new,togo))

    if dist[end] == 10000: # weight처음상태면 -1
        print(-1)
    else: #아니면 이거
        print(dist[end])
