import tkinter as tk


class Gui:
    def __init__(self, trees_names=None, title='Statystyki lasu', dims="500x500"):
        if trees_names is None:
            trees_names = ['Brzoza', 'Dab', 'Jesion', 'Sosna', 'Swierk', 'Inne']
        self.window = tk.Tk()
        self.trees_entries = {name:None for name in trees_names}


        self.build_window(title, dims, trees_names)

        self.window.mainloop()

    def get_stats(self):
        trees_data = {}
        for key, val in self.trees_entries.items():
            trees_data[key] = val.get()

        print(trees_data)



    def build_window(self, title, dims, trees_names):
        self.window.title(title)
        self.window.geometry(dims)

        label = tk.Label(master=self.window, text='Podaj ilość drzew w twoim lesie:')
        label.grid(row=0, column=1,pady=10, padx=5)

        for idx, tree in enumerate(trees_names):
            label = tk.Label(master=self.window, text = tree)
            label.grid(row=idx+1, column=1, pady=5, padx=3)

            entry = tk.Entry(self.window)
            entry.insert(tk.END, '0')
            entry.grid(row=idx+1, column=2, pady=5, padx=2)
            self.trees_entries[tree] = entry

        print(self.trees_entries)
        button = tk.Button(
            master=self.window,
            command=self.get_stats,
            text="Wylicz statystyki",
            width=20,
            height=2
        )

        button.grid(row=len(trees_names)+1, column=2, pady=15, padx=5)




gui = Gui()
