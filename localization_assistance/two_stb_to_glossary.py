from STBWork import STBWork

stb_work = STBWork()
en_filename = "../extracted/npc.stb"
ru_filename = "./resources_stb/rus/npc.stb"
file_content = ""

with open(en_filename, "rb") as en_file:
    en_strings = stb_work.read_stb(en_file.read())

with open(ru_filename, "rb") as ru_file:
    ru_strings = stb_work.read_stb(ru_file.read())

if len(ru_strings) != len(en_strings):
    raise ValueError("Diff lens: {} and {}".format(len(en_strings), len(ru_strings)))
else:
    for i in range(len(ru_strings)):
        ru_text = ru_strings[i].text.strip('?!$ ')
        en_text = en_strings[i].text.strip('?!$ ')
        file_content += "{} = {}\n".format(en_text, ru_text)

    with open("npc.txt", "wb") as file:
        file.write(file_content.encode("utf-8"))
