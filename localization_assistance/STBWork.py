class STBWork:

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

    #        def read_stb(self, ocont, app):
    def read_stb(self, ocont):
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
            #                               app.progressBar.setValue(i/(num_strings - 1) * 100)
            # for name in oldns:
            # print(oldns[name])
            # for nf_ind in range(len(oldns[name])):

            text = text.strip()

            curstring = STBString(id, id2, bitflag, version, lens, offset, len2, text)
            if text != "":
                strings.append(curstring)

        return strings

    def write_stb(self, strings):
        num_strings = len(strings)
        ncont = b""
        ncont += bytes(self.tole(1, 3))  # adding header 01 00 00
        ncont += bytes(self.tole(num_strings, 4))  # adding number of strings
        text_offset = 7 + num_strings * 26

        print("1st part started")
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

            if i % 50 == 0:
                print(round(i/num_strings, 2))

        print("1st part completed")
        for i in range(num_strings):
            curstring = strings[i]
            nowtext = curstring.text

            ncont += nowtext.encode("utf-8")

            if i % 1000 == 0:
                print(round(i/num_strings, 2))

        print("2nd part completed")
        return ncont

    def count_words(self, ocont):
        words_num = 0
        stb_strings = self.read_stb(ocont)
        for stb_string in stb_strings:
            text = stb_string.text
            words_num += text.count(" ")
        return words_num


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
