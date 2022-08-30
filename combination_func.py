#!/usr/bin/env python3
# Returns the combination from an input array.


def combination_all(input_arr):
    """
    Returns all possible combinations. Use the itertools package.
    Input can also be a single string if each input is a single character.
    """
    import itertools

    _out_list = []
    for _i in range(len(input_arr)):
        _out_list.append(list(
            itertools.combinations( input_arr, _i+1 )  # Use the combinations function to find all combi for a particular length
        ))

    # Flatten list
    _out_list = [_item for _list in _out_list for _item in _list]

    return _out_list
