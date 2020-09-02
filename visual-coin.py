import argparse
import graph
import data
from pathlib import Path

import datetime


parser = argparse.ArgumentParser(description='Get accumulative daily transaction for assets in blockchain networks')

# visual-coin [-h] -a | --assets -output | -o [--quite | -q]
parser.add_argument('--assets', '-a', nargs="+", required=True,
                    help='input asset ids separated by space')
parser.add_argument('--output', '-o', nargs='+', choices=['png', 'pdf', 'mp4', 'gif', 'mov', 'avi'],
                    help='input output filetypes separated by space')
parser.add_argument('--dir', '-d', default=str(Path.cwd())+"/out",
                    help='input directory for output files')
parser.add_argument('--name', '-n',
                    help='input filename for the output file')
parser.add_argument('--quiet', '-q', action="store_true",
                    help='draw plots as daemon')


args = parser.parse_args()
assets = args.assets
filetypes = args.output



# if filename exists, auto-increment


if not args.quiet:
    print("Showing the figure. Press ^C to exit.")
    graph.draw_graph(assets)
    graph.show_graph()
else:
    if not args.name:
        # generate_default_name
        args.name = '_'.join(assets) + datetime.date.today().strftime("%y%m%d")
    print("Running... Press ^C to exit.")
    print(assets)
    current_fig = graph.draw_graph(assets)
    path = args.dir + '/' + args.name
    graph.get_exports(current_fig, filetypes, path)

