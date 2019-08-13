import shutil
import os


def find_string_with_substring_in_list(substring, string_list):
    for string in string_list:
        if substring in string:
            return string
    return False


def extract_files_to_trans(source_directory, prefix):
    destination_directory = "../trans/"

    with open("name.txt") as file:
        swtor_paths = file.readlines()

    for top, dirs, short_names in os.walk(source_directory):
        for short_name in short_names:
            filename = os.path.join(top, short_name).replace("\\", "/")
            shutil.copy(filename, destination_directory + prefix + short_name)

            swtor_path = find_string_with_substring_in_list(short_name, swtor_paths)
            if swtor_path:
                swtor_path = swtor_path.replace("\n", "")
            else:
                raise ValueError("Could not find swtor path. Short name: {}, paths: {}".format(short_name, swtor_paths))
            print("{} = {}".format(swtor_path, prefix + short_name))


if __name__ == '__main__':
    beginning_of_source_directory = "../translations/"
    end_of_source_directory = "Инквизитор/Инкв/3/event_and_finale/"
    source_directory = beginning_of_source_directory + end_of_source_directory

    prefix = "si_3_ef" + "_"
    extract_files_to_trans(source_directory, prefix)
