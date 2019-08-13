from GameWork import TorEditor


blocked_substrings = [".epp", ".fxe", ".tex", ".dds", ".jba", ".acb", ".mat", ".gr2", ".dat", ".fxspec", ".mph"
                      ".prt", ".dyc", ".mag", ".bnk", "/art/dynamic/", "/resources/anim/", "/resources/guixml/",
                      "/resources/gfx/credits/", "/resources/engine/utility/", "/resources/art/static/area/",
                      "/resources/art/fx/particles/", "/resources/gfx/gfx_production/", "/resources/bnk2/streamed/",
                      ".not", ".fxa", ".amx", ".mph", ".swf", ".tbl", ".svy",
                      "/resources/global.dep", ".stb", "/resources/systemgenerated/compilednative/", "/resources/systemgenerated/prototypes/",
                      "/resources/systemgenerated/buckets/"
                      ]
required_substrings = ["/"]


def filter_function(string):
    return all([substr not in string for substr in blocked_substrings]) \
           and all([substr in string for substr in required_substrings])


def main_filter_strings():
    with open("hashes.txt") as file:
        strings = file.readlines()

    strings = filter(filter_function, strings)

    for string in strings:
        print(string.strip())


def extract_paths(paths_file_name, processed=False):
    tor_paths = []
    with open(paths_file_name) as file:
        strings = file.readlines()
    for string in strings:
        if processed:
            tor_paths.append(string.strip())
        else:
            if "/" in string:
                tor_paths.append(string[string.index("/"):string.rindex("#")])
    return tor_paths


if __name__ == '__main__':
    tor_editor = TorEditor("C:/Program Files (x86)/Electronic Arts/BioWare/Star Wars - The Old Republic/")
    tor_paths = extract_paths("left_hashnames.txt", True)
    tor_paths = list(filter(lambda string: "/resources/systemgenerated/" in string, tor_paths))
    i = 0
    for tor_path in tor_paths:

        if i % 100 == 0:
            print(i, "/", len(tor_paths))
        if "de-de" not in tor_path and "fr-fr" not in tor_path:
            byte_cont = tor_editor.extract_file(tor_path, save=False)
            if byte_cont and (b"harkun" in byte_cont or b"Harkun" in byte_cont):
                print(tor_path)
                tor_editor.extract_file(tor_path)
        i += 1
