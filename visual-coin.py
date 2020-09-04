import argparse
import graph
import data
from pathlib import Path

import datetime

parser = argparse.ArgumentParser(description='Get accumulative daily transaction for assets in blockchain networks')

# visual-coin [-h] -a | --assets -output | -o [--quite | -q]
parser.add_argument('--asset', '-a', nargs="+", required=True,
                    help='input asset ids separated by space')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--output', '-o', nargs='+', choices=['png', 'pdf', 'mp4', 'gif', 'mov', 'avi'],
                   help='input output filetypes separated by space')
group.add_argument('--show', '-s', action="store_true",
                   help='show the graph')
parser.add_argument('--dir', '-d', default=str(Path.cwd()) + "/out",
                    help='input directory for output files')
parser.add_argument('--name', '-n',
                    help='input filename for the output file')

args = parser.parse_args()
assets = args.asset
filetypes = args.output

# TODO: if filename exists, auto-increment


try:
    current_fig = graph.draw_graph(assets)
except (data.AssetError, data.RequestError, graph.StyleError):
    pass
else:
    if filetypes:
        if not args.name:
            args.name = '_'.join(assets) + datetime.date.today().strftime("%y%m%d")
        print("Program running...Press ^C to exit.")
        # generate output path with dir/filename
        path = Path(args.dir) / args.name
        graph.get_exports(current_fig, filetypes, path)
        print("Export succeeded.")
    else:
        graph.show_graph()
