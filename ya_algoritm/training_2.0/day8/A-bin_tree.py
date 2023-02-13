import sys


def add(node, value):
    child = TREE.get(node)
    if node and node > value:
        if child[0]:
            add(child[0], value)
        else:
            TREE[node][0] = value
            TREE[value] = [None, None]
    elif node and node <= value:
        if child[1]:
            add(child[1], value)
        else:
            TREE[node][1] = value
            TREE[value] = [None, None]


def printtree(root):
    level = 0

    def dfs(node, level):
        child = TREE.get(node)
        if node:
            dot = '.' * level
            ans = f'{dot}{node}' if dot else f'{node}'
            print(ans)
            level += 1
            dfs(child[0], level)
            dfs(child[1], level)

    dfs(root, level)


TREE = {}
ROOT = None

ADD = 'ADD'
ALREADY = 'ALREADY'
DONE = 'DONE'
YES = 'YES'
SEARCH = 'SEARCH'
NO = 'NO'
PRINTTREE = 'PRINTTREE'

val = None
for row in sys.stdin:
    arr = row.split()
    if len(arr) == 1:
        cmd = arr[0]
    else:
        cmd, val = arr[0], int(arr[1])

    if cmd == ADD:
        if TREE.get(val):
            print(ALREADY)
        else:
            if ROOT:
                add(ROOT, val)
            else:
                TREE[val] = [None, None]
                ROOT = val
            print(DONE)

    if cmd == SEARCH:
        print(YES if TREE.get(val) else NO)

    if cmd == PRINTTREE:
        printtree(ROOT)
