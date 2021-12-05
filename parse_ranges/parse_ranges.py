def parse_ranges(args):
    ranges = [arg.strip() for arg in args.split(',')]
    for rn in ranges:
        x, y = rn.split('-')
        yield from range(int(x), int(y) + 1)
