from collections import deque

def isSameTreeDict(n: dict, k: dict) -> bool:
    queue = deque([(1, 1)])
    
    while queue:
        node1_val, node2_val = queue.popleft()
        
        node1 = n.get(node1_val, None)
        node2 = k.get(node2_val, None)
        
        if not node1 and not node2:
            continue
            
        if not node1 or not node2 or node1 != node2:
            return False
            
        if node1['left'] or node2['left']:
            queue.append((node1['left'], node2['left']))
            
        if node1['right'] or node2['right']:
            queue.append((node1['right'], node2['right']))
            
    return True

n = {
    1: {'left': None, 'right': 2},
    2: {'left': None, 'right': 3},
    3: {'left': None, 'right': 4},
    4: {'left': None, 'right': 5},
    5: {'left': None, 'right': None}
}

k = {
    1: {'left': None, 'right': 2},
    2: {'left': None, 'right': 3},
    3: {'left': None, 'right': 4},
    4: {'left': None, 'right': 5},
    5: {'left': None, 'right': None}
}

print(isSameTreeDict(n, k))