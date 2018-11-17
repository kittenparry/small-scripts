import tkinter as tk
import binascii

'''
	A small GUI program to convert a string of text to hex and vice versa.
	Shortcuts:
	Enter - Str to Hex and select all of the results
	Ctrl + C - Copies the results (duh) and selects all of the input  
'''
class Gui(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.row_top = tk.Frame(master)
        self.row_mid = tk.Frame(master)
        self.row_bot = tk.Frame(master)
        self.row_top.grid(row=0, column=0, sticky="ew", padx=(10,0))
        self.row_mid.grid(row=1, column=0)
        self.row_bot.grid(row=2, column=0, sticky="ew", padx=(10,0))
        self.var = int()
        self.strings()
        self.add_elements()
    def add_elements(self):
        self.text_top = tk.Text(self.row_top, width=30, height=4, wrap='word')
        self.text_bot = tk.Text(self.row_bot, width=30, height=4, wrap='word', state='disabled')
        self.text_top.bind("<Return>", self.str_to_hex_event)
        self.text_bot.bind("<Control-c>", self.txt_copy)
        self.butt_left = tk.Button(self.row_mid, text=self.str_butt_left, command=self.str_to_hex)
        self.butt_right = tk.Button(self.row_mid, text=self.str_butt_right, command=self.hex_to_str)
        self.scrolly_top = tk.Scrollbar(self.row_top, orient='vertical', command=self.text_top.yview)
        self.scrolly_bot = tk.Scrollbar(self.row_bot, orient='vertical', command=self.text_bot.yview)
        self.text_top.configure(yscrollcommand=self.scrolly_top.set)
        self.text_bot.configure(yscrollcommand=self.scrolly_bot.set)
        #TODO: radio button selection isn't working, disabling for now
        self.radio_left = tk.Radiobutton(self.row_mid, text="", variable=self.var, value=0, command=self.radio, state='disabled')
        self.radio_right = tk.Radiobutton(self.row_mid, text="", variable=self.var, value=1, command=self.radio, state='disabled')
        self.radio_left.select()
        self.els = [self.text_top, self.text_bot, self.radio_left, self.butt_left,
                    self.butt_right, self.radio_right]
        for e in self.els:
            e.pack(side="left", pady=2, padx=1)
        self.scrolly_top.pack(side="left", fill="y")
        self.scrolly_bot.pack(side="left", fill="y")
        self.text_top.focus()
    def radio(self):
        print(self.var)
        if self.var == 0:
            self.text_top.bind("<Return>", self.str_to_hex_event)
            print("bind 0")
        elif self.var == 1:
            self.text_top.bind("<Return>", self.hex_to_str_event)
            print("bind 1")
    def str_to_hex_event(self, event):
        self.str_to_hex()
        return 'break'
    def hex_to_str_event(self, event):
        self.hex_to_str()
        return 'break'
    def str_to_hex(self):
        self.text_bot.configure(state='normal')
        self.dump = self.text_top.get('1.0', 'end - 1c').encode('utf-8').hex()
        self.text_bot.delete('1.0', 'end')
        self.text_bot.insert('end', self.dump)
        self.text_bot.configure(state='disabled')
        self.sel_all(self.text_bot)
    def hex_to_str(self):
        self.text_bot.configure(state='normal')
        try:
            self.dump = binascii.a2b_hex(self.text_top.get('1.0', 'end - 1c')).decode('utf-8', 'ignore')
        except binascii.Error:
            self.dump = self.str_hex_err
        self.text_bot.delete('1.0', 'end')
        self.text_bot.insert('end', self.dump)
        self.text_bot.configure(state='disabled')
        self.sel_all(self.text_bot)
    def sel_all(self, txt):
        txt.focus()
        txt.tag_add('sel', '1.0', 'end - 1c')
    def txt_copy(self, event):
        self.sel_all(self.text_top)
    def strings(self):
        self.str_butt_left = "Str to Hex"
        self.str_butt_right = "Hex to Str"
        self.str_hex_err = "Error: Non-hexadecimal digit!"

if __name__ == '__main__':
    root = tk.Tk()
    root.title("String-Hex Converter")
    root.geometry("280x180+800+100")
    app = Gui(master=root)
    app.mainloop()
