import matplotlib as mpl
import matplotlib.pyplot as plt

def main():
    plt.rcParams["text.usetex"] = True
    plt.rcParams["font.family"] = ["Times"]
    plt.rcParams["mathtext.fontset"] = "stix"

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
    plt.savefig("fig_times_like.pdf",bbox_inches="tight")
    plt.close()

if __name__ == '__main__':
    main()
