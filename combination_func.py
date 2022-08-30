#!/usr/bin/env python3
# Returns the combination from an input array.


def choice_array(arr, return_array=True, verbose=1):

    """
    Produces all possible, order-indepenent combinations obtained from the 
    original array. See the wikipedia: https://en.wikipedia.org/wiki/Combination
    Input must be an array, non-array objects will be autocorrected.
    Currently only returns an ordered output.
    """

    # Required libraries
    import numpy as np
    from collections import Counter

    # Sanity check for inputs
    if type(arr) != np.ndarray:
        if verbose >= 1:
            print("Input isn't a numpy array, automatically converting...")
        arr = np.array(arr)

    # Get length and squared length of original array, squared len will be output len
    _len = len(arr)
    _outlen = _len ** _len
    
    # Create output array
    _outarr = np.empty(shape=(_outlen, _len), dtype=arr.dtype)

    # Fill in array with np.repeat and np.tile
    for _i in range(_len):
        # Create two integers for repeat and tile
        _lenrepeat = int( _outlen / (_len ** (_i + 1)) )
        _lentile = int( _len ** _i )
        # Append repeated items to output
        _outarr[:, _i] = np.tile(np.repeat(arr, _lenrepeat), _lentile)

    # Finally, use list comprehension to process array and return
    # If output is ordered, also sort each item <- not working, functionality removed!
    _outobj = [
      np.unique(_arritem) for _arritem in _outarr
    ]

    # Return list of unique objects. 
    # Since numpy arrays are not hashable, turn them into tuples first. 
    # See: https://stackoverflow.com/questions/63576206/get-unique-values-in-a-list-of-numpy-arrays
    _outkeys = list(Counter(map(tuple, _outobj)).keys())

    # Finally, either return a converted array, or return the keys as-is.
    if return_array:
        return [ np.array(_keyitem) for _keyitem in _outkeys ]
    return _outkeys

