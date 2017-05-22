import os

relative_path = "files"

modify_directory_names = False

item_dict = {}

def create_item_dict(relative_path):
    relative_path_full = relative_path + "/"
    for item in os.listdir(relative_path):
        if os.path.isdir(relative_path_full + item):
            item_dict[relative_path_full + item] = "directory"
            create_item_dict(relative_path_full + item)
        else:
            item_dict[relative_path_full + item] = "file"

def rename(file, phrase_to_change, changed_phrase):
    try:
        print("Found the item: " + file)
        #removing the "directory/directory/" part of the file, so it was unchanged
        new_file_name = file[:file.rfind("/") + 1] + file[file.rfind("/") + 1:].replace(phrase_to_change, changed_phrase)
        print("Renaming to: " + new_file_name)
        os.rename(file, new_file_name)
        print("Success! Item renamed! \n")
        return 1
    except Exception as err:
        print("An error occurred: {x}. \nItem not renamed! \n".format(x=err))
        return 0

def item_count():
    return 1

def condition_check(dictionary, e, item_type, phrase_to_change):
    if dictionary[e] == item_type and phrase_to_change in e[e.rfind("/") + 1:]:
        return True

def browse_item_dict(item_dict, item_type, func):
    count = 0
    items = (e for e in item_dict if condition_check(item_dict, e, item_type, phrase_to_change) == True)
    for item in items:
        if func == item_count:
            count += func()
        elif func == rename:
            count += func(item, phrase_to_change, changed_phrase)
    return count

def count_return(mod, func1, func2):
    if mod == False:
        return func1, 0
    if mod == True:
        return func1, func2


if __name__ == "__main__":
    print(
"""
=== renamer_input - changing file names according to user input ===

PLEASE FOLLOW THE INSTRUCTIONS
""")

    #1. asking for right placement of files
    input('1. Put the files you want to rename in the "/files" directory in the renamer_input folder and press Enter to continue\n')

    create_item_dict(relative_path)

    print("We found the following files: \n" + str(list(k for k, v in item_dict.items() if v == "file")) + "\n")

    mod_dir_user_input = input('Do you also want to change the directory (folder) names [type "YES" to approve and press Enter OR press Enter to decline]: \n')

    if "y" in mod_dir_user_input.lower():
        modify_directory_names = True
        print("We found the following directories: \n" + str(
            list(k for k, v in item_dict.items() if v == "directory")) + "\n")

    #2. getting phrase that user want to be changed
    phrase_to_change = input("2. Type a phrase you want to change and press Enter: \n")

    #3. checking if there are files that qualify to be changed and then renaming them
    file_count, directory_count = count_return(modify_directory_names,
                                               browse_item_dict(item_dict, "file", item_count),
                                               browse_item_dict(item_dict, "directory", item_count))

    if (file_count + directory_count) > 0:
        if modify_directory_names is False:
            print("There is %s files matching criteria \n" % file_count)
        if modify_directory_names is True:
            print("There is {x} files and {y} directories matching criteria \n".format(x=file_count, y=directory_count))

        changed_phrase = input("3. Type phrase intended to replace phrase you wanted to change and press Enter: \n")

        no_of_renamed_file, no_of_renamed_dir = count_return(modify_directory_names,
                                                                browse_item_dict(item_dict, "file", rename),
                                                                browse_item_dict(item_dict, "directory", rename))

        print("No more files matching criteria \n")
        if modify_directory_names is False:
            print("Summary: %s files was renamed \n" % no_of_renamed_file)
        if modify_directory_names is True:
            print("Summary: {x} files and {y} directories was renamed \n".format(x=no_of_renamed_file, y=no_of_renamed_dir))
    else:
        print("\nNo items matching criteria \n")

    input("Press Enter to close the program")