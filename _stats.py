def count_jaro_match(x, y, z):
    _matched = []

    for idx, itm in enumerate(x):
        l_bound = max(idx - z, 0)
        u_bound = min(idx + z, len(y))

        if itm in y[l_bound:u_bound] and itm not in _matched:
            _matched.append(itm)

    return _matched

def get_jaro_match(mixed_order, known_order):
    seq_tol = ( max(len(mixed_order), len(known_order)) // 2 ) - 1
    mixed_matches = count_jaro_match(mixed_order, known_order, seq_tol)
    known_matches = count_jaro_match(known_order, mixed_order, seq_tol)

    return mixed_matches, known_matches

def count_jaro_transposition(mixed_ref, known_ref):
    t_count = 0

    for idx, itm in enumerate(mixed_ref):
        if itm is not known_ref[idx]:
            t_count += 1

    return t_count / 2

def get_jaro_similarity(mixed_order, known_order):
    mixed_match, known_match = get_jaro_match(mixed_order, known_order)
    transposition_count = count_jaro_transposition(mixed_match, known_match)

    match_count = len(mixed_match)

    a = match_count / len(mixed_order)
    b = match_count / len(known_order)
    c = (match_count - transposition_count) / match_count

    return (1/3) * ( a + b + c ), (mixed_match, known_match), transposition_count
