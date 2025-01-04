def print_grade(dictname: dict):
    """
    print dict key and value
    :param dictname: dict instance
    """
    for key, value in dictname.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    empty_dict = {}
    print(empty_dict)

    grades = {
        'Name': 'Dylan',
        'Mathématiques': 90,
        'Physique': 94,
        'Français': 86,
        'Chinois': 92
    }

    empty_dict.update(grades)
    print(empty_dict)

    grades.update({
        'Anglais': 96
    })
    print(grades)

    grades['Physique'] = 96
    print(grades)

    grades.pop('Chinois')
    print(grades)

    print('\n')
    print_grade(grades)
