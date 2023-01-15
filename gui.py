import tkinter as tk
import os 
import matplotlib
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend. Please set `export DISPLAY=172.22.160.1:0` ')
    matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


class Gui:
    def __init__(self, network, trees_names=None, title='Statystyki lasu', dims="1000x900"):
        self.network = network
        if trees_names is None:
            trees_names = ['brzoza', 'dab', 'swierk', 'sosna',  'Inne']
        self.window = tk.Tk()
        self.trees_entries = {name:None for name in trees_names}

        self.build_window(title, dims, trees_names)
        self.window.mainloop()

    def get_stats(self):
        trees_data = {}
        all = 0
        for key, val in self.trees_entries.items():
            trees_data[key] = int(val.get())
            all += trees_data[key]

        for key, val in trees_data.items():
            trees_data[key] = float(val/all)

        print(trees_data)
        self.network.update_trees(tree_data=trees_data)

        # get data from network
        # data = {
        #     'rodzaj_lisci':
        #         {
        #             'igly':10,
        #             'blaszki':40,
        #             'łuski':50
        #         },
        #     'kolor kory': {
        #         'bialy':10,
        #         'czarny':30,
        #         'brazowy':60
        #         }
        # }

        data = self.network.current_state

        # display charts
        row = len(self.trees_entries.keys())+2

        label = tk.Label(master=self.window, text='Statystki na temat lasu:')
        label.grid(row=row, column=0, pady=10, padx=15)

        row += 1
        it = 0
        for key, values in data.items():
            if key != 'drzewo':
                print(key, row, it)
                self.plot(key, values.keys(), values.values(), row, it)
                it+=1
                row += int(it/5)


    def plot(self, title, data_labels, data_values, row, col):

        fig = plt.Figure(figsize=(4, 4),
                     dpi=65)

        # adding the subplot
        plot1 = fig.add_subplot(1, 1, 1)

        # plotting the graph
        plot1.bar(data_labels, data_values)

        plot1.set_xlabel(title)
        plot1.set_ylabel('udzial')
        plot1.set_title(title)

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig,
                                   master=self.window)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().grid(row=row, column=col, pady=15, padx=5)

        # creating the Matplotlib toolbar
        # toolbar = tk.NavigationToolbar2Tk(canvas,
        #                                self.window)
        # toolbar.update()

        # placing the toolbar on the Tkinter window
        # canvas.get_tk_widget().pack()

    def build_window(self, title, dims, trees_names):
        self.window.title(title)
        self.window.geometry(dims)

        label = tk.Label(master=self.window, text='     Podaj ilość drzew w twoim lesie:     ')
        label.grid(row=0, column=0,pady=10, padx=25)

        for idx, tree in enumerate(trees_names):
            label = tk.Label(master=self.window, text = tree)
            label.grid(row=idx+1, column=0, pady=5, padx=23)

            entry = tk.Entry(self.window)
            entry.insert(tk.END, '0')
            entry.grid(row=idx+1, column=1, pady=5, padx=22)
            self.trees_entries[tree] = entry

        button = tk.Button(
            master=self.window,
            command=self.get_stats,
            text="Wylicz statystyki",
            width=20,
            height=2
        )

        button.grid(row=len(trees_names)+1, column=1, pady=15, padx=5)




# gui = Gui()
