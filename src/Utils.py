def PrintDict(ar_dict):
    """
    Convenience function for printing a dictionary to console.
    Useful for debugging.
    :param ar_dict:
    """
    print("Keys> ", [x for x in ar_dict.keys( )])
    print("Values> ", [x for x in ar_dict.values( )])


from enum import Enum, unique

@unique
class ObjectType(Enum):
    """
    Enum representing the variety of artifacts appearing in sonet app.
    """
    NA = 0  # NA stands for Not Assigned
    SPACECRAFT = 1

@unique
class SpacecraftType(Enum):
    """
    Enum representing the kind of spacecrafts.
    """
    NA = 0  # NA stands for Not Assigned
    CREWED = 1
    CARGO = 2


if __name__ == "__main__":
    d = {'key1': 'value1', 'key2': 'value1'}
    PrintDict(d)
