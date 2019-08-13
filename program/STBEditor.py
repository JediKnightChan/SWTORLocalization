class STBWork():
    def __init__(self):

        self.defs = ["Взломщик", "Сит", "Дарт Нигилус", "Сатил Шан", "Раздиратели", "Инфопланшет", "Кхем Вал",
                     "Кворрен"]
        self.olds = {"Slicer": ["взломщики", "взломщик", "Взломщики", "Взломщик"], "Sith": ["Сит", "Ситы"],
                     "Darth Nihilus": ["Нигилус"], "Satele Shan": ["Сатил"],
                     "Flesh Raiders": ["Раздирател", "раздирател"], "Datapad": ["инфопланшет"], "Khem Val": ["Кхем"],
                     "Quarren": ["Кворрен"]}

        self.news = {"Ледоруб": ["ледорубы", "ледоруб", "Ледорубы", "Ледоруб"], "сит": ["сит", "ситы"],
                     "ситх": ["ситх", "ситхи"], "Дарт Нихилус": ["Нихилус"],
                     "Дарт Найлус": ["Найлус"], "Сатель Шан": ["Сатель"], "Пожиратели": ["Пожирател", "пожирател"],
                     "Датапад": ["датапад"], "Кем Вал": ["Кем"], "Куаррен": ["Куаррен"], "Кваррен": ["Кваррен"]}

    def getuint(self, fcont, offset, i):  # the function to read reversed (LE?) integers
        sum = 0
        for d in range(i):
            a = fcont[offset]
            sum += a * (256 ** d)
            offset += 1

        return sum

    def inc(self, i, x):  ##increasing i by x (for inc offset or nowloc)
        i += x

        return i

    def tole(self, d, i):  # turning an integer into an array of bytes in LE
        p = []
        num = d
        for c in range(i):
            a = num % 256
            p.append(a)
            num = num // 256

        return p

    def repstbfile(self, ocont, oldns, newns):
        strings = []
        # with open(filestbn, "rb") as filestb:
         #   ocont = filestb.read()
        magic = self.getuint(ocont, 0, 4)
        if (magic & 0xFFFFFF) != 1:
            print("NOT .STB FILE")
            return 0
        num_strings = self.getuint(ocont, 3, 4)
        for i in range(num_strings):
            id = self.getuint(ocont, 7 + i * 26, 4)
            id2 = self.getuint(ocont, 7 + i * 26 + 4, 4)
            bitflag = self.getuint(ocont, 7 + i * 26 + 8, 2)
            version = self.getuint(ocont, 7 + i * 26 + 10, 4)
            lens = self.getuint(ocont, 7 + i * 26 + 14, 4)
            offset = self.getuint(ocont, 7 + i * 26 + 18, 4)
            len2 = self.getuint(ocont, 7 + i * 26 + 22, 4)

            text = ocont[offset:offset + lens:]
            text = text.decode("utf-8")

            for nf_ind in range(len(oldns)):
                text = text.replace(oldns[nf_ind], newns[nf_ind])
            text = text.strip()

            curstring = STBString(id, id2, bitflag, version, lens, offset, len2, text)
            strings.append(curstring)

        ncont = b""
        ncont += bytes(self.tole(1, 3))  # adding header 01 00 00
        ncont += bytes(self.tole(num_strings, 4))  # adding number of strings
        text_offset = 7 + num_strings * 26

        for i in range(num_strings):  # adding chars
            curstring = strings[i]
            nowtext = curstring.text.strip()
            temp = b""
            temp += bytes(self.tole(curstring.id, 4))
            temp += bytes(self.tole(curstring.id2, 4))
            temp += bytes(self.tole(curstring.bitflag, 2))
            temp += bytes(self.tole(curstring.version, 4))
            bytetext = nowtext.encode("utf-8")
            temp += bytes(self.tole(len(bytetext), 4))
            temp += bytes(self.tole(text_offset, 4))
            temp += bytes(self.tole(len(bytetext), 4))
            text_offset += len(bytetext)

            ncont += temp

        for i in range(num_strings):
            curstring = strings[i]
            nowtext = curstring.text.strip()

            ncont += nowtext.encode("utf-8")

        return ncont


class STBString():
    def __init__(self, id, id2, bitflag, version, lens, offset, len2, text):
        self.id = id
        self.id2 = id2
        self.bitflag = bitflag
        self.version = version
        self.lens = lens
        self.offset = offset
        self.len2 = len2
        self.text = text
