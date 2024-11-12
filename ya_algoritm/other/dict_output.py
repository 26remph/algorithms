from collections import deque


def solution(names):
    def dfs(d, path):
        if isinstance(d, int):
            res = ".".join(path), d
            path.pop()
            return res

        for key, val in d.items():
            path.append(key)
            res = dfs(val, path)
            if res is not None:
                ans.append(res)

    ans = []
    dfs(names, path=[])
    return ans


def solution_stack(names: dict):
    ans = []

    stack = deque(names.items())
    visited = set()

    root = []
    while stack:
        k, v = stack.popleft()
        root.append(k)
        if isinstance(v, dict):
            if k not in visited:
                stack.extend(v.items())
        else:
            # print('.'.join(root), v)
            ans.append((".".join(root), v))

            root.pop()

        visited.add(k)

    return ans


if __name__ == "__main__":
    a = {
        "a": 1,
        "b": 2,
        "c": {
            "d": 1,
            "e": {
                "f": 5,
            },
        },
    }

    ans = [("a", 1), ("b", 2), ("c.d", 1), ("c.e.f", 5)]
    # res = solution(a)
    res = solution_stack(a)
    assert res == ans, f"{ans=}, {res=}"
