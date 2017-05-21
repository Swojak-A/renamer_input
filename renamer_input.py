import os

relative_path = "files"

modify_directory_names = False

def rename(file, phrase_to_change, changed_phrase):
    print("Found the file: " + file)
    new_file_name = file[:file.rfind("/") + 1] + file[file.rfind("/") + 1:].replace(phrase_to_change, changed_phrase)
    print("Renaming to: " + new_file_name)
    os.rename(file, new_file_name)
    print("Success! File renamed!\n")

item_dict = {}

def create_item_dict(relative_path):
    relative_path_full = relative_path + "/"
    for item in os.listdir(relative_path):
        #print(relative_path_full + item)
        if os.path.isdir(relative_path_full + item):
            item_dict[relative_path_full + item] = "directory"
            create_item_dict(relative_path_full + item)
        else:
            item_dict[relative_path_full + item] = "file"

def file_count(dict):
    count = 0
    for e in dict:
        if dict[e] == "file":
            if phrase_to_change in e[e.rfind("/") + 1:]:
                count += 1
        elif modify_directory_names == True:
            if dict[e] == "directory":
                if phrase_to_change in e[e.rfind("/") + 1:]:
                    count += 1
    return count

def swipe_dict(dict, func=None):
    count = 0
    for e in dict:
        if dict[e] == "file":
            if phrase_to_change in e[e.rfind("/") + 1:]:
                if func is not None:
                    func(e, phrase_to_change, changed_phrase)
                count += 1
        elif modify_directory_names == True:
            if dict[e] == "directory":
                if phrase_to_change in e[e.rfind("/") + 1:]:
                    if func is not None:
                        func(e, phrase_to_change, changed_phrase)
                    count += 1
    return count



print(
"""
=== renamer_input - changing file names according to user input ===

PLEASE FOLLOW THE INSTRUCTIONS
""")

#1. asking for right placement of files
#input('1. Put the files you want to rename in the "/files" directory in the renamer_input folder and press Enter to continue\n')

create_item_dict(relative_path)
print(item_dict)

#print("We found the following files: \n" + str(item_dict(relative_path)) + "\n")

#2. getting phrase that user want to be changed
phrase_to_change = input("2. Type a phrase you want to change and press Enter: \n")

#3. checking if there are files that qualify to be changed and then renaming them
count = swipe_dict(item_dict)
print(count)

if count > 0:
    print("There is %s files matching criteria \n" % count)

    changed_phrase = input("3. Type phrase intended to replace phrase you wanted to change and press Enter: \n")

    swipe_dict(item_dict, rename)

    print("No more files matching criteria \n")
else:
    print("\nNo files matching criteria \n")

input("Press Enter to close the program")