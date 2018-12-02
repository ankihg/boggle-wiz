import argparse
from run import run

parser = argparse.ArgumentParser()
parser.add_argument('--num_rows', help='number of rows on board', type=int)
parser.add_argument('--num_cols', help='number of columns on board', type=int)
parser.add_argument('--min_vow', help='minimum number of vowels on board', type=int)
parser.add_argument('--min_cons', help='minimum number of consonants on board', type=int)

args = parser.parse_args()
run(args.num_rows, args.num_cols, args.min_vow, args.min_cons)
