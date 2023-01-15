from bayesian_network_backend import BayesNetwork
from gui import Gui

def main():
    N = BayesNetwork(path_to_network_file="networks/Network1.xdsl")
    print("Before:")
    print(N.current_state)

    gui = Gui(N, N.current_state['drzewo'].keys())

    # trees = {
    #     'brzoza': 0.3,
    #     'dab': 0.3,
    #     'swierk': 0.35,
    #     'sosna': 0.05000000000000004
    # }

    # N.update_trees(tree_data=trees)
    # print("After:")
    # print(N.current_state)


if __name__ == '__main__':
    main()
