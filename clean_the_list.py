def clean_list(items):
    if not items:
        return []
    new_list = []
    for x in items:
        x = x.strip()
        x = x.capitalize()
        new_list.append(x)
    if 'Milk' not in new_list:
        new_list += ['Milk']

    cleaned = []

    for index, item in enumerate(new_list, start=1):
        cleaned.append(f"{index}/ {item}")

    return cleaned