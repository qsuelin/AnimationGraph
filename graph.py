import data
import console

import matplotlib.pyplot as plt
import csv
import numpy as np
import matplotlib.animation as animation
from matplotlib.pyplot import MultipleLocator


# get data from data module, get filepath from console
# data: dict
# assets = console.ConsoleArgs.assets
# filetypes = console.ConsoleArgs.filetypes


config_dict = {
    'eos': {'color': '#1F0027', 'label': "EOS"},
    'etc': {'color': '#5DB400', 'label': "ETC"},
    'btc': {'color': '#FFA533', 'label': 'BTC'},
    }

fig, ax = plt.subplots()
yarrs_dict = {}
dayarr = None
lines_dict = {}


def draw_graph(assets) -> "Figure":
    global fig, ax, yarrs_dict, dayarr, lines_dict
    assets_accumulation = data.get_assets_accumulation(assets)
    yarrs_dict = get_ys(assets_accumulation)
    dayarr = get_x(assets_accumulation)
    lines_dict = get_lines(assets_accumulation, dayarr, yarrs_dict)
    draw_fig(dayarr)
    current_fig = plt.gcf()
    # plt.show()
    return current_fig


def draw_fig(dayarr) -> None:
    plt.yscale('log')
    ax.yaxis.grid()
    plt.style.use('ggplot')
    ax.set_title('Cumulative Transactions from Origin Day', fontsize=15, fontfamily='sans-serif', weight='bold')
    plt.xlabel('Days from Network Origin', weight='bold')
    plt.ylabel('Cumulative Transaction Count', weight='bold')
    plt.legend(loc='lower right', shadow=True, prop={'weight': 'bold'})
    plt.xlim((0, len(dayarr)))


def get_exports(fig: "Figure", filetypes: list):
    print(dayarr, lines_dict, yarrs_dict)
    ani = animation.FuncAnimation(fig, animate, len(dayarr),
                                  fargs=[dayarr, lines_dict, yarrs_dict],
                                  interval=1, blit=False, repeat=False)

    for the_type in filetypes:
        get_the_export(the_type, ani)


def get_the_export(filetype, ani):
    pics = ['png', 'pdf']
    vids = ['mp4', 'avi', 'mov']
    if filetype in pics:
        print('inside pic')
        plt.savefig(f'fig.{filetype}')
    elif filetype == "gif":
        writergif = animation.PillowWriter(fps=1000)
        ani.save("animation.gif", writer=writergif)
    elif filetype in vids:
        writervideo = animation.FFMpegWriter(fps=1000)
        ani.save(f'animation.{filetype}', writer=writervideo)
    else:
        raise Exception("unsupported output type")


# Given assets in dict, return dict, k: asset, v: line2D_obj
def get_lines(accumulation_dict: dict, dayarr, yarrs_dict) -> dict:
    global fig, ax

    lines_dict = {}
    for asset in accumulation_dict:
        lines_dict[asset] = get_line(asset, ax, dayarr, yarrs_dict)
    return lines_dict


def animate(num, dayarr, lines_dict, yarrs_dict):
    for assetid, line in lines_dict.items():
        line.set_data(dayarr[:num], yarrs_dict[assetid][:num])
    return list(lines_dict.values())


def get_line(assetid: str, ax, dayarr, yarrs_dict) -> 'axes obj':
    yarr = yarrs_dict[assetid]
    return ax.plot(dayarr, yarr, color=config_dict[assetid]['color'], linewidth=3.0, label=config_dict[assetid]['label'])[0]


# given dict of assets, v: list
def get_x(accumulation_dict: dict):
    num_days = get_maxlength(accumulation_dict)
    x = [i for i in range(num_days)]
    return np.array(x)


def get_maxlength(accumulation_dict:dict) -> int:
    return max([len(i) for i in accumulation_dict.values()])


# k: assetid, v: np.array
def get_ys(accumulation_dict: dict) -> dict:
    global yarrs_dict
    num_days = get_maxlength(accumulation_dict)
    for asset in accumulation_dict:
        for i in range(len(accumulation_dict[asset]), num_days):
            accumulation_dict[asset].append(None)
        yarrs_dict[asset] = np.array(accumulation_dict[asset])

    return yarrs_dict


if __name__ == '__main__':
    current_fig = draw_graph(['eos', 'btc'])
    get_exports(current_fig, ['png', 'gif', 'mp4'])
