## https://matplotlib.org/stable/users/explain/text/pgf.html

## https://tex.stackexchange.com/questions/151529/combining-helvetica-and-symbol-fonts-with-mathspec

import matplotlib as mpl
import matplotlib.pyplot as plt

def main():
    mpl.use("pgf") # default: 'xelatex'
    plt.rcParams.update({
        "font.family": "serif",  # use serif/main font for text elements
        "text.usetex": True,     # use inline math for ticks
        "pgf.rcfonts": False,    # don't setup fonts from rc parameters
        "pgf.preamble": "\n".join([
             r"\usepackage{mathspec}",
             r"\setmathsfont(Digits,Latin)[Uppercase=Italic,Lowercase=Italic]{Helvetica}",
             r"\setmathsfont(Greek)[Uppercase=Regular,Lowercase=Italic]{Symbol}",
             r"\setmainfont{Helvetica}",
             r"\usepackage[italic]{mathastext}",
        ])
    })

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
    plt.xlabel(r"x $x$")
    plt.ylabel(r"y $y$")
    plt.savefig("fig_helvetica_2.pdf",backend="pgf",bbox_inches="tight")
    plt.close()

if __name__ == '__main__':
    main()
