from xml.dom import minidom
import os
from STBWork import *


s = STBWork()
root_dir_xml = input("Enter xml input dir: ")
root_dir_stb = input("Enter stb output dir: ")
end_of_filenames = os.listdir(root_dir_xml)
#end_of_filenames = ["qst.xml", "tutorials.xml", "titles.xml"]
#end_of_filenames = ["npc.xml"]
print(end_of_filenames)
npc_mod = False
for end_of_filename in end_of_filenames:
    filename_xml = root_dir_xml + end_of_filename
    filename_stb = root_dir_stb + end_of_filename.replace(".xml", ".stb")

    xmldoc = minidom.parse(filename_xml)
    text_list = xmldoc.getElementsByTagName('text')
    stb_strings = []

    for text_el in text_list:
        text = text_el.firstChild.nodeValue.strip()
        if npc_mod:
            text = text.replace("?", "").replace("!", "").strip()
        id = int(text_el.attributes["id1"].value)
        id2 = int(text_el.attributes["id2"].value)
        bitflag = int(text_el.attributes["bitflag"].value)
        version = int(text_el.attributes["version"].value)
        stb_string = STBString(id, id2, bitflag, version, None, None, None, text)
        stb_strings.append(stb_string)

    stb_cont = s.write_stb(stb_strings)
    with open(filename_stb, "wb") as stb:
        stb.write(stb_cont)
