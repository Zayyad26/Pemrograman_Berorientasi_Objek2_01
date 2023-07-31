import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Matakuliah import *
class FrmMatakuliah:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='KODEMK:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMAMK:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='SKS:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PRODI:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKodemk = Entry(mainFrame) 
        self.txtKodemk.grid(row=0, column=1, padx=5, pady=5)
        self.txtKodemk.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtNamamk = Entry(mainFrame) 
        self.txtNamamk.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtSks = Entry(mainFrame) 
        self.txtSks.grid(row=2, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('idmk','kodemk','namamk','sks','prodi')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idmk', text='IDMK')
        self.tree.column('idmk', width="55")
        self.tree.heading('kodemk', text='KODEMK')
        self.tree.column('kodemk', width="55")
        self.tree.heading('namamk', text='NAMAMK')
        self.tree.column('namamk', width="55")
        self.tree.heading('sks', text='SKS')
        self.tree.column('sks', width="55")
        self.tree.heading('prodi', text='PRODI')
        self.tree.column('prodi', width="55")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKodemk.delete(0,END)
        self.txtKodemk.insert(END,"30")
        self.txtNamamk.delete(0,END)
        self.txtNamamk.insert(END,"30")
        self.txtSks.delete(0,END)
        self.txtSks.insert(END,"30")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data matakuliah
        obj = Matakuliah()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["idmk"],d["kodemk"],d["namamk"],d["sks"],d["prodi"]))
    def onCari(self, event=None):
        kodemk = self.txtKodemk.get()
        obj = Matakuliah()
        a = obj.get_by_kodemk(kodemk)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kodemk = self.txtKodemk.get()
        obj = Matakuliah()
        res = obj.get_by_kodemk(kodemk)
        self.txtKodemk.delete(0,END)
        self.txtKodemk.insert(END,obj.kodemk)
        self.txtNamamk.delete(0,END)
        self.txtNamamk.insert(END,obj.namamk)
        self.txtSks.delete(0,END)
        self.txtSks.insert(END,obj.sks)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kodemk = self.txtKodemk.get()
        namamk = self.txtNamamk.get()
        sks = self.txtSks.get()
        prodi = self.txtProdi.get()
        # create new Object
        obj = Matakuliah()
        obj.kodemk = kodemk
        obj.namamk = namamk
        obj.sks = sks
        obj.prodi = prodi
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kodemk(kodemk)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kodemk = self.txtKodemk.get()
        obj = Matakuliah()
        obj.kodemk = kodemk
        if(self.ditemukan==True):
            res = obj.delete_by_kodemk(kodemk)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmMatakuliah(root2, "Aplikasi Data Matakuliah")
    root2.mainloop()
