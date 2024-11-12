code = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "ZH",
    "З": "Z",
    "И": "I",
    "Й": "I",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "KH",
    "Ц": "TC",
    "Ч": "CH",
    "Ш": "SH",
    "Щ": "SHCH",
    "Ы": "Y",
    "Э": "E",
    "Ю": "IU",
    "Я": "IA",
    "Ъ": "",
    "Ь": "",
}

out = open("transliteration.txt", "a", encoding="UTF-8")

with open("cyrillic.txt", encoding="UTF-8") as f:
    for row in f.readlines():
        ans = []
        for ch in row.rstrip():
            eng_ch = code.get(ch.upper(), None)
            if eng_ch is not None:
                if not eng_ch:
                    continue
                if ch == ch.upper() and len(eng_ch) > 1:
                    ans.append(eng_ch.capitalize())
                else:
                    ans.append(eng_ch.lower() if ch == ch.lower() else eng_ch)
            else:
                ans.append(ch)

        print("".join(ans), file=out)

out.close()
