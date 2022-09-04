def key_list_to_string(keys):
    rows_str = ""
    for row in keys:
        rows_str += row + ","
    rows_str = "(" + rows_str[:-1] + ")"
    return rows_str