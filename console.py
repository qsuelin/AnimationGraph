import argparse
parser = argparse.ArgumentParser()
#
# parser.add_argument('assets')
# parser.parse_args()




class ConsoleArgs:
    # assets: list of string
    # filetype: list of string
    assets = []
    filetypes = []

    def __init__(self):
        self.assetid = 'eos'
        self.filetype = 'mp4'
