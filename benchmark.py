import argparse

from haraka import dice_simulate as rs
from dice.pure import dice_simulate as pu
from dice.optimized import dice_simulate as op

parser = argparse.ArgumentParser(
    prog="Benchmark",
    description="Used to run benchmarks",
    epilog="Don't trust everying!",
)

parser.add_argument(
    "-s",
    "--sim",
    type=int,
    help="number of simulations to run",
    required=True,
)
parser.add_argument(
    "-k",
    "--kind",
    type=str,
    help="which simulation to run",
    choices=["rs", "pu", "op"],
    required=True,
)


args = parser.parse_args()

if __name__ == "__main__":
    if args.kind == "rs":
        data = rs(args.sim)
    elif args.kind == "pu":
        data = pu(args.sim)
    elif args.kind == "op":
        data = op(args.sim)
        