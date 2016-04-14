def import_book(path):
    print path
    # path = "./Books/"
    filenames = glob.glob(path + '*.txt')
    print filenames
    text = []
    for file in filenames:
#        Each line in book is element in list
        text += open(file, 'r')
#    Returns List
    return text