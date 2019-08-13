
class STBWork:

    def getuint(self, fcont, offset, i):  # the function to read reversed (LE?) integers
        sum = 0
        for d in range(i):
            a = fcont[offset]
            sum += a * (256 ** d)
            offset += 1

        return sum

    def inc(self, i, x):
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

    def open_stb_file(self, ocont):
        strings = []
        magic = self.getuint(ocont, 0, 4)
        if (magic & 0xFFFFFF) != 1:
            print("NOT .STB FILE")
            return 0
        num_strings = self.getuint(ocont, 3, 4)
        for i in range(num_strings):
            id = self.getuint(ocont, 7 + i * 26, 8)
            id2 = self.getuint(ocont, 7 + i * 26 + 4, 4)
            bitflag = self.getuint(ocont, 7 + i * 26 + 8, 2)
            version = self.getuint(ocont, 7 + i * 26 + 10, 4)
            lens = self.getuint(ocont, 7 + i * 26 + 14, 4)
            offset = self.getuint(ocont, 7 + i * 26 + 18, 4)
            len2 = self.getuint(ocont, 7 + i * 26 + 22, 4)

            text = ocont[offset:offset + lens:]
            text = text.decode("utf-8")
            text = text.strip()

            curstring = STBString(id, id2, bitflag, version, lens, offset, len2, text)
            strings.append(curstring)
        return strings


class STBString:
    def __init__(self, id, id2, bitflag, version, lens, offset, len2, text):
        self.id = id
        self.id2 = id2
        self.bitflag = bitflag
        self.version = version
        self.lens = lens
        self.offset = offset
        self.len2 = len2
        self.text = text

    def count_words(self):
        return len(self.text.split())
