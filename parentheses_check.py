def check_parentheses_sequence(seq):

    if len(seq) % 2 != 0:
        return False

    # matching opening brackets to closing brackets
    brackets = dict((('(', ')'),
                ('[', ']'),
                ('{', '}')))
    open_brackets = [b for b in brackets]

    stack = []

    for s in seq:
        if s in open_brackets:
            stack.append(s)

        elif len(stack) != 0 and s == brackets[stack[-1]]:
                stack.pop()

        else:
            return False

    if len(stack) == 0:
        return True

    else:
        return False


def check_parentheses_sequence_slow(seq):

    while '[]' in seq or '()' in seq or '{}' in seq:
        seq = seq.replace('[]', '')
        seq = seq.replace('()', '')
        seq = seq.replace('{}', '')

    return True if len(seq) == 0 else False


if __name__ == '__main__':

    sequence_1 = '{()}[[{()}]]'
    sequence_2 = '{()}[[{(){]]'

    print('Fast computation:')
    print(check_parentheses_sequence(sequence_1))
    print(check_parentheses_sequence(sequence_2))

    print()
    print('Slow computation:')
    print(check_parentheses_sequence_slow(sequence_1))
    print(check_parentheses_sequence_slow(sequence_2))