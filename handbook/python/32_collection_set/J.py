trans = {
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'KH',
    'Ц': 'TC',
    'Ч': 'CH',
    'Ш': 'SH',
    'Щ': 'SHCH',
    'Ы': 'Y',
    'Э': 'E',
    'Ю': 'IU',
    'Я': 'IA',
}
skip = {'Ь', 'Ъ'}

ans = []
for ch in list(input()):

    if ch.upper() in skip:
        continue

    letter = trans.get(ch.upper())
    if letter:
        if ch.islower():
            ans.append(letter.lower())
        else:
            if len(letter) > 1:
                ans.append(letter.capitalize())
            else:
                ans.append(letter)
    else:
        ans.append(ch)

print(''.join(ans))
