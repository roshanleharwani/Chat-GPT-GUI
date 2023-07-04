import ttkbootstrap as ttk


class Query(ttk.Entry):
    def __init__(self, parent=None, style="default", var=None):
        super().__init__(master=parent, bootstyle=style, width=50, textvariable=var)
        self.place(relx=0.5, rely=0.5, anchor="center")
