import glob

# ===============================
# IMPORT FILE FUNCTION
# ===============================
def inputFile(path):
    print path
    filenames = glob.glob(path+"*.txt")
    print filenames
    text =[]
    for file in filenames:
        text += open(file,'r')
    return text

inputText = inputFile("./Input/")
print inputText
