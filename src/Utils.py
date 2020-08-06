def PrintDict(ar_dict):
    """
    Convenience function for printing a dictionary in console.
    Useful for debugging.
    :param ar_dict:
    """
    print("Keys> ", [x for x in ar_dict.keys()])
    print("Values> ", [x for x in ar_dict.values()])

if __name__ == "__main__":

    d ={'key1' : 'value1', 'key2' : 'value1'}
    PrintDict(d)