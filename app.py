from bayesian_network_backend import BayesNetwork
from gui import Gui

def main():
    N = BayesNetwork(path_to_network_file="networks/Network1.xdsl")
    print("Before:")
    print(N.current_state)

    gui = Gui(N, N.current_state['drzewo'].keys())


if __name__ == '__main__':
    main()
