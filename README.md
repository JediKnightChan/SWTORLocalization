
# SWTOR Localization

Star Wars: The Old Republic fan-localization project

## Quick Start

### Game translation

1) Specify your game folder in `localization_assistance/Gamework.py`
and run it to extract all known .stb files. Copy them into `resources_stb/en_all/`
2) Copy the directory you want to translate from
`localization_assistance/resources_stb/...` to `translations/.../0_EN/`
3) Use `localization_assistance/translation_tool.html` to open and
translate .stb files. (Blank lines can help you to understand the dialog 
structure.) Place translated files to `translations/.../`
4) Specify `xml` in `format` parameter in `tor.extract_everything()` in `Gamework.py` 
and copy extracted files to `resources_xml/`. Use 3rd-party programs to translate big files such as `npc.xml`
and convert them back to .stb using `localization_assistance/xml_to_stb.py`
5) Collect the translated content into `trans/` with `localization_assistance/files_to_trans.py`. 
Copy the game paths of the files you want to collect to `localization_assistance/name.txt`
and specify all required parameters in .py file (end_of_source_directory, prefix), then run .py file
6) Execute `localization_assistance/files_unification.py` to replace quotes, dashes, Sith, etc.
7) Edit `trans/settings.txt` (game path, filename in `trans/`) and `trans/info.txt`
8) Package the files from `trans/` into `trans.zip` specifying this password: `iz20Wo4suqmUcZHFXL8G` (7-zip, ZipCrypto)
9) Copy this package to your localization program directory, reinstall translation

### Modifying localization program 

Localization program is based on PyQT5. Graphics files contain "gui" prefix. After editing the source files,
build them into executable with pyinstaller.

> pyinstaller --onefile --icon=icon.ico --noconsole main.py

Then build the setup executable with Inno Script Studio (don't forget to edit paths in `program/Build/base24_12.iss`)


## Directories

### Program

SWTOR localization program that installs translation by modifying the game content.

### Localization assistance

Different tools for game localization (such as .stb to .xml file converter).

### Trans

Translated game files to be inserted into the game content.

### Translations

Original and translated game files.