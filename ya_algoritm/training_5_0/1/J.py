from sys import stdin


def find_next_wdix():
    print("find _ next _ w_idx")
    pass


def insert_word(word, type):
    global w_idx

    # scan row to end and insert word
    start_x, start_y = w_idx[0], w_idx[1]
    if not (doc[start_y]):
        doc[start_y].append((0, len(word) * c, type))
        w_idx = (start_x + 1, start_y)
        print(f"init: {doc=}, {start_x=}, {start_y=}, {word=}, {w_idx=}, {coord_x=}")
        return

    if len(doc[start_y]) <= start_x:
        last_offset = doc[start_y][-1][1]
        if last_offset + len(word) * c <= w:
            doc[start_y].append((last_offset, last_offset + len(word) * c, type))
            w_idx = (start_x + 1, start_y)
        else:
            find_next_wdix()
    else:
        # present element
        find_next_wdix()
    print(f"init: {doc=}, {start_x=}, {start_y=}, {word=}, {w_idx=}, {coord_x=}")

    # for y_ind, y_row in enumerate(doc, start_y):
    #     if len(y_row) <= start_x:
    #         y_row.append()
    #     for x_ind, x_row in enumerate(y_row, start_x):


def insert_img(img: dict):
    if img["layout"] == "embedded" and int(img["height"]) < h:
        ...
    pass


if __name__ == "__main__":
    w, h, c = map(int, input().split())
    doc = [[] for _ in range(1)]
    coord_x = [0 for _ in range(20)]
    coord_y = [0 for _ in range(20)]
    w_idx = (0, 0)
    for words in stdin:
        if words:
            arr = words.split("(")
            print(arr)
            for el in arr:
                if el.startswith("image") and el.find("layout") != -1:
                    param = el.strip().rstrip(")")[6:].split()
                    img = dict([tuple(p.split("=")) for p in param])
                    print(img)
                    insert_img(img)
                elif el:
                    print(el)
                    insert_word(el.rstrip(), "W")
                else:
                    print(f"{el=}, skip")
        else:
            print(f"{words=}, paragraph start")

    # print(timeit('main()', number=2))
