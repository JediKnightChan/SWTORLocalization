import os
from STBEditor import STBWork

stb_work = STBWork()
directory = "./translations/Class Storylines/Bounty Hunter/Dromund Kaas/0 EN"
total_words_num = 0


for root, subdirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        with open(filepath, "rb") as f:
            stb_strings = stb_work.open_stb_file(f.read())
            for stb_string in stb_strings:
                total_words_num += stb_string.count_words()

print(total_words_num)
