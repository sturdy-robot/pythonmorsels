def get_earliest(*args):
    dates = [date.split('/') for date in args]
    max_date = dates[0]
    for date in dates:
        if date[2] < max_date[2]:
            max_date = date
        elif date[2] == max_date[2]:
            if (
                date[0] >= max_date[0]
                and date[0] == max_date[0]
                and date[1] < max_date[1]
                or date[0] < max_date[0]
            ):
                max_date = date

    return f'{max_date[0]}/{max_date[1]}/{max_date[2]}'
