def get_ranges(numbers):
    first = last = numbers[0]
    for n in numbers[1:]:
        if n-1 == last:
            last = n
        else:
            yield first, last
            first = last = n
    yield first, last


def format_string(ranges):
    string = ''
    for i, r in enumerate(ranges):
        a, b = r
        range_string = str(a) + '-' + str(b) if a != b else str(a)
        if i != len(ranges) - 1:
            range_string += ','
        string += range_string

    return string


def format_ranges(numbers):
    numbers = sorted(numbers)
    ranges = list(get_ranges(numbers))
    return format_string(ranges)
