def normalize_gender(src_gender):
    """Returns "F", "M", "unknown" if none provided, "corrupted" otherwise."""
    if src_gender is None:
        return 'unknown'
    elif type(src_gender) is not str:
        return 'corrupted'

    gender = src_gender.lower()

    if gender == 'female' or gender == 'f':
        return 'F'
    elif gender == 'male' or gender == 'm':
        return 'M'
    else:
        return 'corrupted'