def solution(blocks):
    hash_prev = [0]
    ans = -1
    for i in range(len(blocks)):
        b = blocks[i]
        lim_m = (b - 255 - pow(256, 2)) // 65536 + 1

        is_correct = False
        cur_hash = []
        for r in range(256):
            for m in range(1, lim_m + 10):
                for h_prev in hash_prev:
                    h = (37 * (m + r + h_prev)) % 256
                    if h < 100 and h == b - 256 * r - pow(256, 2) * m:
                        cur_hash.append(h)
                        is_correct = True
                        print(
                            "i:",
                            i,
                            "r:",
                            r,
                            "m:",
                            m,
                            "h:",
                            h,
                            "lim_m:",
                            lim_m,
                            "hash",
                            hash_prev,
                        )
        hash_prev = cur_hash[:]

        if not is_correct:
            return i

    return ans


if __name__ == "__main__":
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    # t = time.time()
    print(solution(arr))
    # print(time.time() - t)
