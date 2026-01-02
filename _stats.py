''' Metrics to help sanity check the randomness'''


def get_jaro_match_between(mixed_order, known_order):
    '''Gather a characters from each list that are aligned with some deviation allowed

    The deviation being, with len(mixed_order) -> a, len(known_order) -> b:

            ⌊ max(a, b) * 0.5 ⌋ - 1

    Args:
        mixed_order (list[str]): The randomized items
        known_order (list[str]): The sorted items

    Returns:
        tuple(list[str], list[str]):
    '''

    tolerance = ( max(len(mixed_order), len(known_order)) // 2 ) - 1
    _matched_x = [0] * len(mixed_order)
    _matched_y = [0] * len(known_order)

    for idx_x, itm_x in enumerate(mixed_order):
        l_bound = max(idx_x - tolerance, 0)
        u_bound = min(idx_x + tolerance, len(known_order))

        for idx_y, itm_y in enumerate(known_order[l_bound:u_bound], start=l_bound):
            if itm_x == itm_y and itm_y not in _matched_y:
                _matched_x.insert(idx_x, itm_x)
                _matched_y.insert(idx_y, itm_y)

    return (
        [maybe_itm for maybe_itm in _matched_x if maybe_itm != 0],
        [maybe_itm for maybe_itm in _matched_y if maybe_itm != 0]
    )


def count_jaro_transposition_for(mixed_order, known_order):
    '''How many things need to be rearranged so that the lists match.

    After finding the matched characters, compare their current positions between the two lists

    Args:
        mixed_order (list[str]): The randomized items
        known_order (list[str]): The sorted items

    Returns:
        float:
    '''

    t_count = 0

    for idx, itm in enumerate(mixed_order):
        if itm is not known_order[idx]:
            t_count += 1

    return t_count // 2


def get_jaro_edit_distance_from(mixed_order, known_order):
    '''An implementation of the jaro distance metric.

    Helpful check in determining how varied/randomized a shuffled deck of cards is given their
        original positions.

    Args:
        mixed_order (list[str]): The randomized items
        known_order (list[str]): The sorted items

    Returns:
        tuple(float, tuple(list[str], list[str]), int):
    '''

    mixed_match, known_match = get_jaro_match_between(mixed_order, known_order)
    transposition_count = count_jaro_transposition_for(mixed_match, known_match)

    match_count = len(mixed_match)

    a = match_count / len(mixed_order)
    b = match_count / len(known_order)
    c = (match_count - transposition_count) / match_count

    return (1/3) * ( a + b + c ), (mixed_match, known_match), transposition_count


def count_peapods_from(mixed_order, known_order):
    '''Finding pairs of consecutive cards.

    Another helpful check in determining variance for cards compared to their original positions.
        When going over the cards each group of two are peapods - either ripe and green.
            * Ripe is in order.
            * Green is random

    Args:
        mixed_order (list[str]): The randomized items
        known_order (list[str]): The sorted items

    Returns:
        tuple(int, int):
    '''

    item_count = len(mixed_order)
    _ripe_counter = 0
    _green_counter = 0
    known_order_dict = { _val: _idx for _idx, _val in enumerate(known_order) }

    for idx_xf, itm_xf in enumerate(mixed_order):
        if idx_xf < item_count - 1:
            # Forward Check
            if known_order_dict[itm_xf] - known_order_dict[mixed_order[idx_xf + 1]] == -1:
                _ripe_counter += 1
            else:
                _green_counter += 1
            # Look-back Check
            if known_order_dict[itm_xf] - known_order_dict[mixed_order[max(idx_xf - 1, 0)]] == -1:
                _ripe_counter += 1
            else:
                _green_counter += 1

    return _ripe_counter, _green_counter
