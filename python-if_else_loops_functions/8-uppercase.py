def uppercase(str):
    for upper in range(len(str)):
        case = ord(str[upper])
        if case >= 97 and case <= 122:
            case = chr(case - 32)
        else:
            case = chr(case)
        print("{}".format(case), end='')
    print('')
