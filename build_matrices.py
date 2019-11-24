import argparse
import mixed
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--data')
parser.add_argument('--formula')
parser.add_argument('--X')
parser.add_argument('--Z')
parser.add_argument('--L')

args = parser.parse_args()

data = pd.read_feather(args.data)
with open(args.formula, 'r') as file:
    formula = file.read().strip()

X, Z, L, _ = mixed.get_matrices(data, formula)

X.tofile(args.X)
Z.tofile(args.Z)
L.tofile(args.L)