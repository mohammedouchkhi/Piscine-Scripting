def do_punishment(first_part, second_part, nb_lines):
    res = ""
    for x in range(nb_lines):
        res += first_part.strip() + " " + second_part.strip() + ".\n"
    return res