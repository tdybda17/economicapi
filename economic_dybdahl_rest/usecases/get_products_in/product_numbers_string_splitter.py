def split_product_number_string(product_numbers_string):
    if not product_numbers_string:
        return []

    split_str = product_numbers_string.split(',')
    trimmed = [str(s).replace(']', '').replace('[', '').replace('\'', '').replace('"', '').strip() for s in split_str]
    if len(trimmed) == 1 and not trimmed[0]:
        return []
    else:
        return trimmed
