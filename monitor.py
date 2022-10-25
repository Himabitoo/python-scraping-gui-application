import tkinter,json
import tkinter as tk

class Application(tkinter.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master

        #read json file
        self.json_loads = open('en_settings.json', 'r')
        self.json_data = json.load(self.json_loads)
        self.json_title = self.json_data['application']['title']
        self.json_version = self.json_data['application']['version']
        self.json_geometry = self.json_data['application']['geometry']

        #Application status
        self.master.title(self.json_title)
        self.master.geometry(self.json_geometry)
        self.pack()
        self.create_layout_frames()
        self.create_label_frames()
        self.create_widgets()

    #creating functions ----------------------------------------------------d
    def create_layout_frames(self):

        #generate
        self.header_frame = tk.Frame(master=self.master,pady=10)
        self.bottom_frame = tk.Frame(master=self.master)
        self.container1 = tk.Frame(master=self.master,bg='#778899')
        # self.container2 = tk.Frame(master=self.master,bg='#b0c4de')
        # self.container3 = tk.Frame(master=self.master,bg='#e6e6fa')

        #pack
        self.header_frame.pack(side='top',fill='x', expand=False)
        self.bottom_frame.pack(side='bottom',fill='x', expand=False)
        self.container1.pack(fill='both', expand=True)
        # self.container2.pack(side='left',fill='both', expand=True)
        # self.container3.pack(side='left',fill='both', expand=True)

        #call function
        self.label_header()
        self.label_footer()

    def label_header(self):
        self.title_label = tk.Label(master=self.header_frame,text=self.json_title)
        self.title_label.pack(side='left')

    def label_footer(self):
        self.footer_text = tk.Label(master=self.bottom_frame,text= 'version: ' + str(self.json_version))
        self.footer_text.pack(side='right')


    def create_label_frames(self):

        #generate
        self.ScpitingUrlframe = tk.LabelFrame(self.container1,text="スクレイピングURL",width=100,height=100)

        #pack
        self.ScpitingUrlframe.pack(ipadx=10,ipady=10,padx=10,pady=10)

    def create_widgets(self):

        #generate
        # self.label_url = tkinter.Label(master=self.ScpitingUrlframe,text='スクレイピング先URL')
        self.url_box = tkinter.Entry(master=self.ScpitingUrlframe,width=50)

        #pack
        # self.label_url.pack()
        self.url_box.pack()

if __name__ == "__main__":

    master = tk.Tk()
    app = Application(master=master)
    app.mainloop()
