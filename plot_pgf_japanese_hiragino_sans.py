## https://matplotlib.org/stable/users/explain/text/pgf.html

## https://tex.stackexchange.com/questions/151529/combining-helvetica-and-symbol-fonts-with-mathspec

import matplotlib as mpl
import matplotlib.pyplot as plt

def main():
    mpl.use("pgf")
    plt.rcParams["pgf.texsystem"] = "lualatex"
#    plt.rcParams["pgf.texsystem"] = "xelatex"
    plt.rcParams["text.usetex"] = True
    plt.rcParams["font.family"] = "Hiragino Sans" ## use Hiragino Sans W4
    plt.rcParams["pgf.rcfonts"] = False

    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"
    plt.rcParams["xtick.major.pad"] = 8
    plt.rcParams["ytick.major.pad"] = 8
    plt.rcParams["xtick.major.width"] = 1.5
    plt.rcParams["ytick.major.width"] = 1.5
    plt.rcParams["xtick.major.size"] = 8
    plt.rcParams["ytick.major.size"] = 8
    plt.rcParams["font.size"] = 30
    plt.rcParams["axes.linewidth"] = 2

    plt.figure(figsize=(8,4))
    plt.plot(range(5))
    plt.xlabel(r"エックス $x$")
    plt.ylabel(r"ワイ $y$")
    plt.savefig("fig_japanese_hiragino_sans.pdf",backend="pgf",bbox_inches="tight")
    plt.close()

if __name__ == '__main__':
    main()
