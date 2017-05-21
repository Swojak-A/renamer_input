import os

print(os.listdir())
for folder in os.listdir():
    if os.path.isdir(folder) == True:
        os.chdir(folder)
        for file in os.listdir():
            if os.path.isfile(file) == True:
                os.rename(file, folder + " _ set _ " + file)
        path = os.getcwd()
        os.chdir(path.replace(folder, ""))

    # for file in os.listdir(folder):
    #     os.rename(file)