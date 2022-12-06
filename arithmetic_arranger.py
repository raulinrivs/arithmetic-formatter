def arithmetic_arranger(list, answers=False):
    string = []
    if len(list) > 5:
        return 'Error: Too many problems.'
    for item in list:
        item = item.replace(' ', '')
        if item.find('+') != -1:
            values = item.split('+')
            if len(values[0]) > 4 or len(values[1]) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            if values[0].isdigit() and values[1].isdigit():
                values.append(str(int(values[0]) + int(values[1])))
                values.insert(1, '+')
                values[0] = str(values[0])
                values[1] = str(values[1])
                string.append(values)
            else:
                return 'Error: Numbers must only contain digits.'
        elif item.find('-') != -1:
            values = item.split('-')
            if len(values[0]) > 4 or len(values[1]) > 4:
                return 'Error: Numbers cannot be more than four digits.'
            if values[0].isdigit() and values[1].isdigit():
                values.append(str(int(values[0]) - int(values[1])))
                values.insert(1, '-')
                values[0] = str(values[0])
                values[1] = str(values[1])
                string.append(values)
            else:
                return 'Error: Numbers must only contain digits.'
        else:
            return "Error: Operator must be '+' or '-'."
    string = string_compose(string, answers)
    return string


def string_compose(list, answers):
    lines = ['', '', '', '']
    
    for item in list:
        if len(item[0]) > len(item[2]):
            bigger_len = len(item[0])
        else:
            bigger_len = len(item[2])

        # if item[3][0] == '-':
        #     lines[3] = f'{lines[3]} {item[3]}    '
        if len(item[3]) == bigger_len:
            lines[3] = f'{lines[3]}  {" " * (bigger_len - len(item[3]))}{item[3]}    '
        elif len(item[3]) - bigger_len == 1:
            lines[3] = f'{lines[3]} {" " * (bigger_len - len(item[3]))}{item[3]}    '
        elif len(item[3]) - bigger_len == 2:
            lines[3] = f'{lines[3]}{" " * (bigger_len - len(item[3]))}{item[3]}    '

        lines[0] = f'{lines[0]}  {" " * (bigger_len - len(item[0]))}{item[0]}    '
        lines[1] = f'{lines[1]}{item[1]} {" " * (bigger_len - len(item[2]))}{item[2]}    '
        lines[2] = f'{lines[2]}{"-" * bigger_len}--    '

    if answers:
        return f'{lines[0][:-4]}\n{lines[1][:-4]}\n{lines[2][:-4]}\n{lines[3][:-4]}'
    else:
        return f'{lines[0][:-4]}\n{lines[1][:-4]}\n{lines[2][:-4]}'
