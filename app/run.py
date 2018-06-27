from imap import iMap

if __name__ == '__main__': 
    root = tk.Tk()
    root.title('iMap - A simple batch image geocoder.')
    root.resizable(width=False, height=False)
    app = iMap(master=root)
    app.mainloop()