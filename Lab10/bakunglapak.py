import tkinter as tk
import tkinter.messagebox as tkmsg
from tkinter.messagebox import askretrycancel, showinfo

class Product(object):
    def __init__(self, nama, harga, stok):
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok

    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    def get_stok(self):
        return self.__stok

    def set_stok(self, jumlah):
        self.__stok -= jumlah

class Buyer(object):
    def __init__(self):
        self.__daftar_beli = {}

    def add_daftar_beli(self, produk, jumlah,harga):
        if produk in self.__daftar_beli:
            self.__daftar_beli[produk] += jumlah

        else :
            self.__daftar_beli[produk] = jumlah
        # self.__daftar_beli[produk] = harga
    def get_daftar_beli(self):
      return self.__daftar_beli



# GUI Starts from here

# Toplevel adalah sebuah class yang mirip dengan Frame namun akan terbuka
# secara terpisah dengan Window utama (jadi membuat top-level window yang
# terpisah)
class WindowLihatBarang(tk.Toplevel):
    def __init__(self, product_dict, master = None):
        super().__init__(master)
        self.product_dict = product_dict
        
        self.wm_title("Daftar Barang")
        self.create_widgets()

    def create_widgets(self):
        # create a grid, row 0 means first row , column 0 first column
        self.lbl_judul = tk.Label(self, \
                                  text = 'Daftar Barang Yang Tersedia',fg="#073B4C").grid(row = 0, column = 1)
        self.lbl_nama = tk.Label(self, \
                                 text = 'Nama Produk',fg="#073B4C").grid(row = 1, column = 0)
        self.lbl_harga = tk.Label(self, \
                                  text = 'Harga',fg="#073B4C").grid(row = 1, column = 1)
        self.lbl_stok = tk.Label(self, \
                                 text = 'Stok Produk',fg="#073B4C").grid(row = 1, column = 2)

        i = 2
        # start from two , so it wont stack with label stock
        for nama, barang in sorted(self.product_dict.items()):
            tk.Label(self, \
                     text = f"{nama}",fg="#118AB2").grid(row = i, column= 0)
            tk.Label(self, \
                     text = f"{barang.get_harga()}",fg="#118AB2").grid(row = i, column= 1)
            tk.Label(self, \
                     text = f"{barang.get_stok()}",fg="#118AB2").grid(row = i, column= 2)
            i += 1

        self.btn_exit = tk.Button(self,bg="#ED1C24",fg="#235789", text = "EXIT", \
                                  command = self.destroy).grid(row = i, column=1)


class WindowBeliBarang(tk.Toplevel):
    def __init__(self, buyer, product_dict, master = None):
        super().__init__(master)
        self.buyer = buyer
        self.product_dict = product_dict
        self.wm_title("Beli Barang")
        # create a frame within 280 width 200 height
        self.geometry("280x200")
        self.create_widgets()

    def create_widgets(self):
        # nama_barang and jumlah is equal to whatever user input in entry, using get()
        self.nama_barang = tk.StringVar()
        self.jumlah = tk.StringVar()
        self.lbl_form = tk.Label(self, \
                                  text = 'Form Beli Barang',fg="#301014").grid(row = 0, column = 1)
        self.lbl_nama_product = tk.Label(self, \
                                 text = 'Nama Produk',fg="#f39237").grid(row = 1, column = 0)
        self.ent_nama_barang=tk.Entry(self,textvariable=self.nama_barang,bg="#39A9DB",fg="#D63230")
        self.ent_nama_barang.grid(row = 1, column = 1)
        self.lbl_jumlah = tk.Label(self, \
                                 text = 'Jumlah',fg="#19647E").grid(row = 2, column = 0)
        self.ent_jumlah_barang=tk.Entry(self,textvariable=self.jumlah,bg="#39A9DB",fg="#D63230")
        self.ent_jumlah_barang.grid(row = 2, column = 1)
        self.btn_buy = tk.Button(self,bg="#107E7D",fg="#044B7F", text = "BELI", \
                                  command = self.beli_barang).grid(row = 3, column=1)
        self.btn_exit = tk.Button(self,bg="#95190C",fg="#79B791",text = "EXIT", \
                                  command = self.destroy).grid(row = 4, column=1)

        
       

    def beli_barang(self):
        # get the entry input
        nama_barang = self.nama_barang.get()
        jumlah = int(self.jumlah.get())
        # if empty then show the retry and cancel modal. 
        if nama_barang == "":
            #source: https://www.pythontutorial.net/tkinter/tkinter-askretrycancel/
            # if retry button is click then it will return true, if cancel then it will return false
            ans = askretrycancel(title="Nama Barang Kosong",message=f"Nama barang masih kosong. tolong diisi ya!")
            # so if its cancel then ans will be false, and if complement of false(true) then destory the window
            if not ans:
                self.destroy()
        
        # if not in list of product
        elif nama_barang not in self.product_dict:
            #source: https://www.pythontutorial.net/tkinter/tkinter-askretrycancel/
            # if retry button is click then it will return true, if cancel then it will return false
            ans = askretrycancel(title="Barang Not Found",message=f"Barang dengan nama {nama_barang} tidak ditemukan dalam BakungLapak.")
            # so if its cancel then ans will be false, and if complement of false(true) then destory the window
            if not ans:
                self.destroy()
        # if stock is sold
        elif self.product_dict[nama_barang].get_stok() - jumlah < 0:
            showinfo(title="Stok Empty",message="Maaf, stok produk telah habis",icon="warning")
            
        else :
        # if can buy then add barang to daftar beli buyer
        # and reduce the barang stock
            barang = self.product_dict[nama_barang]
            buyer.add_daftar_beli(barang, jumlah,barang.get_harga())
            barang.set_stok(jumlah)
            self.ent_nama_barang.delete(0, tk.END)
            self.ent_jumlah_barang.delete(0, tk.END)
            tkmsg.showinfo("Berhasil!", f"Berhasil membeli {nama_barang} sejumlah {jumlah}")


class WindowCheckOut(tk.Toplevel):
    def __init__(self, buyer, master = None):
        super().__init__(master)
        self.wm_title("Daftar Barang")
        # get list of barang bought by buyer
        self.daftar_dibeli = buyer.get_daftar_beli()
        self.create_widgets()

    def create_widgets(self):
        # create a grid
        self.lbl_judul_barang = tk.Label(self, \
                                  text = 'Keranjangku',fg="#8FC93A").grid(row = 0, column = 1)
        self.lbl_nama_barang = tk.Label(self, \
                                text = 'Nama Produk',fg="#0072BB").grid(row = 1, column = 0)
        self.lbl_harga_barang = tk.Label(self, \
                                text = 'Harga',fg="#0072BB").grid(row = 1, column = 1)
        self.lbl_jumlah_barang = tk.Label(self, \
                                text = 'jumlah',fg="#0072BB").grid(row = 1, column = 2)
     
        # if empty dictionary then create a label belum ada barang yang dibeli
        if self.daftar_dibeli == {}:
            self.lbl_none = tk.Label(self, \
                                  text = 'Belum ada barang yang dibeli :(',fg="#41658A").grid(row = 2, column = 1)
            self.btn_exit = tk.Button(self,bg="#95190C",fg="#79B791", text = "EXIT", \
                                        command = self.destroy).grid(row = 3, column=1)
        else:
            i = 2
            # else start with index two so it wont stack with the label
            for barang, jumlah in sorted(self.daftar_dibeli.items()):
                tk.Label(self, \
                        text = f"{barang.get_nama()}",fg="#41658A").grid(row = i, column= 0)
                tk.Label(self, \
                        text = f"{barang.get_harga()}",fg="#41658A").grid(row = i, column= 1)
                tk.Label(self, \
                        text = f"{jumlah}",fg="#41658A").grid(row = i, column= 2)
                i += 1

            self.btn_exit = tk.Button(self, bg="#95190C",fg="#79B791",text = "EXIT", \
                                        command = self.destroy).grid(row = i, column=1)


class MainWindow(tk.Frame):

    def __init__(self, buyer, product_dict, master = None):
        super().__init__(master)
        
        self.buyer = buyer
        self.product_dict = product_dict
        
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, \
                              text = 'Selamat datang di BakungLapak. Silahkan pilih Menu yang tersedia',font='Helvetica 10 bold')
        # create a button that have a function, function will be called everytime button is pressed
        self.btn_lihat_daftar_barang = tk.Button(self, \
                                                 text = "LIHAT DAFTAR BARANG", \
                                                 command = self.popup_lihat_barang,font='Helvetica 10',width="30",bg="#618B4A",fg="#D7F9F1")
        self.btn_beli_barang = tk.Button(self, \
                                         text = "BELI BARANG", \
                                         command =self.popup_beli_barang,font='Helvetica 10',width="30",bg="#285943",fg="#d7fff1" )
        self.btn_check_out = tk.Button(self, \
                                       text = "CHECK OUT", \
                                       command = self.popup_check_out,font='Helvetica 10',width="30",bg="#166088",fg="#C0D6DF")
        self.btn_exit = tk.Button(self, \
                                  text = "EXIT", \
                                  command = self.destroy,font='Helvetica 10',width="30",bg="#FF495C",fg="#FCFCFC")

        self.label.pack()
        self.btn_lihat_daftar_barang.pack()
        self.btn_beli_barang.pack()
        self.btn_check_out.pack()
        self.btn_exit.pack()

    # semua barang yand dijual
    def popup_lihat_barang(self):
        WindowLihatBarang(self.product_dict)

    # menu beli barang
    def popup_beli_barang(self):
        WindowBeliBarang(self.buyer, self.product_dict)

    # menu riwayat barang yang dibeli
    def popup_check_out(self):
        WindowCheckOut(self.buyer)

if __name__ == "__main__":

    buyer = Buyer()

    product_dict = {"Kebahagiaan" : Product("Kebahagiaan", 999999, 1),
                    "Kunci TP3 SDA" : Product("Kunci TP3 SDA", 1000000, 660)}
                    
    m = MainWindow(buyer, product_dict)
    m.master.title("BakungLapak")
    m.master.mainloop()
