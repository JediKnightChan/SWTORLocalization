import os
from STBWork import STBWork, STBString

directory = "../trans/"
filenames = os.listdir(directory)
filenames = ["tu.stb"]
s = STBWork()

for filename in filenames:
    if ".stb" in filename:
        stb_strings = []
        with open(directory + filename, "rb") as f:
            cont = f.read()
            strs = s.read_stb(cont)
        for stb_str in strs:
            text = stb_str.text
            print(text)

            text = " {} ".format(text)
            text = text.replace(" \"", " «").replace(">\"", ">«").replace("\"", "»").replace(" - ", " — ")

            text = "." + text
            text = text.replace(". Сит", ". Ушкамарарара").replace("! Сит", "! Ушкамарарара").replace("? Сит", "? Ушкамарарара")
            text = text.replace("Ситуа", "ёщкёщ")
            text = text.replace("Сити", "кщащащащаща").replace("сити", "кщащащащаща")
            text = text.replace(" Сит", " сит")
            text = text.replace("кщащащащаща", "Сити").replace("ёщкёщ", "Ситуа")

            text = text.replace("Кмяушкмяушкмяуш", "Сит", 1).replace("Ушкамарарара", "Сит")
            text = text[2:]
            text = text.replace("$", "").strip()
            print(text)
            id = stb_str.id
            id2 = stb_str.id2
            bitflag = stb_str.bitflag
            version = stb_str.version
            stb_string = STBString(id, id2, bitflag, version, None, None, None, text)
            stb_strings.append(stb_string)
        ncont = s.write_stb(stb_strings)
        with open(directory + filename, "wb") as f:
            f.write(ncont)

