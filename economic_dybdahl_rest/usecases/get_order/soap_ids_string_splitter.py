def split_soap_id_string(soap_ids_string):
    if not soap_ids_string:
        return []

    split_str = soap_ids_string.split(',')
    trimmed = [str(s).replace(']', '').replace('[', '').replace('\'', '').replace('"', '').strip() for s in split_str]
    if len(trimmed) == 1 and not trimmed[0]:
        return []
    else:
        return trimmed
