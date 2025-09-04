import matplotlib as mpl
import matplotlib.pyplot as plt

def main():
    plt.rcParams["text.usetex"] = True
#    plt.rcParams["font.family"] = "serif"
    plt.rcParams['text.latex.preamble'] = r'\usepackage[T1]{fontenc} \usepackage{amsmath,amssymb,bm} \usepackage{helvet} \usepackage{sansmath} \sansmath \renewcommand*\familydefault{\sfdefault} \DeclareSymbolFont{sfletters}{OML}{cmbrm}{m}{it} \DeclareMathSymbol{\stau}{\mathord}{sfletters}{"1C}'

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
    plt.savefig("fig_helvetica_like.pdf",bbox_inches="tight")
    plt.close()

if __name__ == '__main__':
    main()
