
def search_dictionary_item(item, dictionary):
    for dict in dictionary.keys():
        if(item in dict):
            print("{}:\t{}".format(dict,dictionary[dict]))