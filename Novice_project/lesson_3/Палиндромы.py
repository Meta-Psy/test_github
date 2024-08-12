palindroms = []
symbols = []
antisymbols = []
while True:
    palindrom = str(input('Введите слово-палиндром: ')).lower()
    for word in palindrom:
        symbols.append(word)
    for word2 in palindrom:
        antisymbols.append(word2)
    antisymbols.reverse()
    if symbols == antisymbols:
        print(f'{palindrom} это палиндром')
        palindroms.append(palindrom)
        print(palindroms)
        symbols.clear()
        antisymbols.clear()
    elif palindrom.lower == 'палиндромы':
        print(palindroms)
    else:
        print(f'слово {palindrom} не палиндром')
        symbols.clear()
        antisymbols.clear()
