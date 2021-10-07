import csv
import argparse


def read_csv_file(filename, new_file, delimiter=None, quotes=None):
    args = {}
    if delimiter:
        args['delimiter'] = delimiter
    if quotes:
        args['quotechar'] = quotes
  
    with open(filename, 'r') as fp:
        if not delimiter and not quotes:
            args['dialect'] = csv.Sniffer().sniff(fp.read())
            fp.seek(0)
        
        content = csv.reader(fp, **args)

        with open(new_file, 'w', newline='') as fw:
            csv_writer = csv.writer(fw)

            for row in content:
                csv_writer.writerow(row)


parser = argparse.ArgumentParser()
parser.add_argument('old_file', type=str)
parser.add_argument('new_file', type=str)
parser.add_argument('--in-delimiter', action='store', type=str)
parser.add_argument('--in-quote', action='store', type=str)
args = parser.parse_args()

read_csv_file(args.old_file, args.new_file, args.in_delimiter, args.in_quote)
