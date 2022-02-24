def by_occurrance_then_name(item_dict):
    """
    TEST: sort dictionary items descendingly by count
    >>> by_occurrance_then_name({'item_1': 1, 'item_2': 2, 'item_3': 3})
    ['item_3', 'item_2', 'item_1']

    TEST: sort alphabetically by name in case of a tie
    >>> by_occurrance_then_name({'item_a': 3, 'item_c': 3, 'item_b': 2, 'item_d': 1})
    ['item_a', 'item_c', 'item_b', 'item_d']

    TEST: no error in case of an empty dict
    >>> by_occurrance_then_name({})
    []
    """
    # short version: sorted_items = [k for k, _ in sorted(item_dict.items(), key = lambda item: (-item[1], item[0]))]
    def sort_by_occurrance_and_name(item):
        return ((-item[1], item[0])) 
    full_sorted_list = sorted(item_dict.items(), key = sort_by_occurrance_and_name)
    sorted_items = [k for k, _ in full_sorted_list]
    return sorted_items

###
# TESTING
###
if __name__ == "__main__":
    import doctest
    doctest.testmod()