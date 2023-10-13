'''given a directedgraph with N nodes and M edges. Each node is associated with lowercaseenglish alphabet.
Beauty of a path is defined as the number of most frequently occuring alphabet.
find the most beautiful path and return the maximum beauty value it has
complete the function beauty in code.
Function must return an integer, the beauty of most beautiful path. If the value is very large return -1.

function has the following parameters
n: integer, number of nodes
m: integer. number of directed edges
S: string of length n where ith alphabet denoted the alphabets associated with ith node
X: list of length m
Y: list of length m
input:-
n=6
m=6
s='xzyabc'
x=[1,3,2,5,4,6]
y=[2,1,3,4,3,4]
output:- -1
explanation: we have path with infinite beauty i.e 1->2->3->1 (xzyz..)

input:-
n=5
m=4
s='abaca'
x=[1,1,3,4]
y=[2,3,4,5]

output:-3
explanation: we have path with maximum beauty is (1->3->4->5) ir (aaca)
'''


def beauty(n, m, s, X, Y):
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    
    for i in range(m):
        x, y = X[i], Y[i]
        graph[x].append(y)
    
    max_beauty = 0
    def dfs(node, path, freq, visited):
        nonlocal max_beauty
        if node in visited:
            return
        freq[s[node-1]] += 1
        beauty = freq[s[node-1]]
        if beauty > max_beauty:
            max_beauty = beauty
        
        visited.add(node)
        for nei in graph[node]:
            dfs(nei, path+[nei], freq, visited)
        visited.remove(node)
        freq[s[node-1]] -= 1
    
    for i in range(1, n+1):
        freq = {}
        for ch in set(s):
            freq[ch] = 0
        dfs(i, [i], freq, set())
    
    if max_beauty > n//2:
        return max_beauty
    else:
        return -1




n = 5
m = 4
s = 'gooda'
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(beauty(n, m, s, x, y))

