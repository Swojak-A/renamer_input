import os

relative_path = "files"
relative_path_full = relative_path + "/"

def rename(file, phrase_to_change, changed_phrase):
    print("Found the file: " + file)
    new_file_name = file.replace(phrase_to_change, changed_phrase)
    print("Renaming to: " + new_file_name)
    os.rename(file, new_file_name)
    print("Success! File renamed!\n")

def check_file(file, relative_path_full, phrase_to_change):
    if os.path.isfile(relative_path_full + file) == True and phrase_to_change in file:
        return True

def item_dict(relative_path):
    relative_path_full = relative_path + "/"
    for item in os.listdir(relative_path):
        print(print(relative_path_full + file))


def file_count(relative_path, phrase_to_change):
    count = 0
    relative_path_full = relative_path + "/"
    for file in os.listdir(relative_path):
        print(relative_path_full + file)
        if check_file(file, relative_path_full, phrase_to_change) == True:
            count += 1
        elif os.path.isdir(relative_path_full + file):
            count += file_count(relative_path_full + file, phrase_to_change)
    return count

print(
"""
=== renamer_input - changing file names according to user input ===

PLEASE FOLLOW THE INSTRUCTIONS
""")

#1. asking for right placement of files
#input('1. Put the files you want to rename in the "/files" directory in the renamer_input folder and press Enter to continue\n')

print("We found the following files: \n" + str(os.listdir(relative_path)) + "\n")

# #2. getting phrase that user want to be changed
# phrase_to_change = input("2. Type a phrase you want to change and press Enter: \n")
#
# #3. checking if there are files that qualify to be changed and then renaming them
# count = file_count(relative_path, phrase_to_change)
#
# if count > 0:
#     print("There is %s files matching criteria \n" % count)
#
#     changed_phrase = input("3. Type phrase intended to replace phrase you wanted to change and press Enter: \n")
#
#     for file in os.listdir(relative_path):
#         if check_file(file, relative_path_full, phrase_to_change) == True:
#             rename(relative_path_full + file, phrase_to_change, changed_phrase)
#     print("No more files matching criteria \n")
# else:
#     print("\nNo files matching criteria \n")
#
# input("Press Enter to close the program")