class User():
    def __init__(self, user_name, tipe):
        """
        Constructor untuk class User
        """
        self.user_name = user_name
        self.type = tipe


class Seller(User):
    def __init__(self, user_name, tipe):
        """
        Constructor untuk class Seller
        """
        # inherit constructor from parent(User) class to child(Seller) class
        super().__init__(user_name, tipe)
        self.income = 0
        self.list_barang_jual = []

    def lihat_produk_jualan_saya(self, seller):
        print("\nBerikut merupakan barang jualan saya")
        print("-------------------------------------")
        print("  Nama Product  |   Harga   | Stock ")
        print("-------------------------------------")
        sorted_product = []
        # for every product in list_product
        # append only the products of seller in the params
        for product in list_product:
            if seller == product.seller:
                sorted_product.append(
                    f"{product.name:<16} | {product.price:<11} | {product.stock:<7}"
                )
        # for every products of seller in the params
        # print the sorted version
        for product in sorted(sorted_product):
            print(product)
        print("-------------------------------------\n")


class Buyer(User):
    def __init__(self, user_name, tipe, saldo):
        # inherit constructor from parent(User) class to child(Buyer) class
        super().__init__(user_name, tipe)
        self.saldo = saldo
        self.list_barang_beli = []

    def lihat_all_produk(self):
        print("\nBerikut merupakan product di Dekdepedia")
        print("------------------------------------------------")
        print("  Nama Product  |   Harga   | Stock |  Penjual  ")
        print("------------------------------------------------")
        sorted_product = []
        # for every objects in list_product
        for product in list_product:
            # append the object
            sorted_product.append(
                f"{product.name:<16} | {product.price:<11} | {product.stock:<7} | {product.seller:<7}"
            )
        # print the sorted version
        for product in sorted(sorted_product):
            print(product)

        print("------------------------------------------------\n")

    def beli_produk(self, barang):
        not_exist = True

        # for every product in list of products
        for product in list_product:
            # if the product match with params and product is available also the saldo is enough to buy the product
            # It means you can buy the product
            if barang == product.name and product.stock > 0 and self.saldo >= product.price:
                # reduce saldo
                self.saldo -= product.price
                # reduce stock
                product.stock -= 1
                # You can bought the product means that product is exist
                not_exist = False
                # Append to the list_barang_beli of buyer
                self.list_barang_beli.append(
                    f"{product.name:<16} {product.price:<7} {product.seller:<8}"
                )
                # for every user, if the type is seller then add the income with product price
                for user in list_user:
                    if user.type == "SELLER":
                        if user.user_name == product.seller:
                            user.income += product.price

                print(f"Berhasil membeli {product.name} dari {product.seller}")
            # if the barang is match but the product isnt available then print the stock is out
            elif barang == product.name and product.stock == 0:
                not_exist = False
                print("Maaf, stok produk telah habis.")
            # if the barang is match but you dont have enough money to buy
            # then print you dont have enough money to buy the product
            elif barang == product.name and self.saldo < product.price:
                not_exist = False
                print(
                    f"Maaf, saldo Anda tidak cukup untuk membeli {product.name}."
                )
        # if no product matched with the params then the not exist is true
        # if not exist true then it will print no product match
        if not_exist:
            print(
                f"Barang dengan nama {barang} tidak ditemukan dalam Dekdepedia.”"
            )

    def show_buy_history(self):
        print("\nBerikut merupakan product di Dekdepedia")
        print("--------------------------------------")
        print("  Nama Product  |   Harga   | Penjual")
        print("--------------------------------------")

        for product in sorted(self.list_barang_beli):
            product = product.split()
            # index 0 is Nama Product, index 1 is Harga, index 2 is Penjual
            print(f"{product[0]:<16} | {product[1]:<11} | {product[2]:<7}")
        print("--------------------------------------")


class Product():
    def __init__(self, nama, harga, stock, seller):
        self.name = nama
        self.price = harga
        self.stock = stock
        self.seller = seller


def get_user(name, list_user):
    """
    Method untuk mengembalikan user dengan user_name sesuai parameter
    """
    for user in list_user:

        if user.user_name == name:
            return user
    return None


def check_user_valid(user):
    split_user = user.split()
    # punctuation without "-"/hypens and "_"/underscore
    punctuation = """!"#$%&'()*+,./:;<=>?@[\]^`{|}~"""
    valid = True

    try:
        # if two words or more then it may be valid,
        # but if only one words or maybe zero words it'll return not valid
        if len(split_user) > 1:
            user_type = split_user[0]
            username = split_user[1]
            # if the punctuation is in the username then give valid false value
            for punc in punctuation:
                if punc in username:
                    valid = False
            if valid:

                if user_type == "SELLER" and len(split_user) == 2:
                    if username in users:
                        print("Username sudah terdaftar")
                    else:
                        # append the instantiated objects to the list
                        list_user.append(Seller(username, user_type))
                        # append also the username to the users list, for username exist check
                        users.append(username)

                elif user_type == "BUYER" and len(split_user) == 3 and int(
                        split_user[2]) > 0:
                    if username in users:
                        print("Username sudah terdaftar")
                    else:
                        # append the instantiated objects to the list
                        list_user.append(
                            Buyer(username, user_type, int(split_user[2])))
                        # append also the username to the users list, for username exist check
                        users.append(username)
                # if type isnt seller or buyer, or the saldos isn't positive integer, the format is wrong
                else:
                    valid = False

        else:
            valid = False
    # if the saldo isn't integer give valid False value
    except ValueError:
        valid = False
    # if not valid then print not valid
    if not valid:
        print("Akun tidak valid.")


def after_login(user):
    print(f"Anda telah masuk dalam akun {user.user_name} sebagai {user.type}")
    print(f"Selamat datang {user.user_name}")
    if user.type == "SELLER":
        print("""
berikut menu yang bisa Anda lakukan:
1. TAMBAHKAN_PRODUK
2. LIHAT_DAFTAR_PRODUK_SAYA
3. LOG_OUT""")
    elif user.type == "BUYER":
        print("""
1. LIHAT_SEMUA_PRODUK
2. BELI_PRODUK
3. RIWAYAT_PEMBELIAN_SAYA
4. LOG_OUT
""")
    while True:
        if user.type == "SELLER":
            print(f"Pemasukkan anda {user.income}")
            choice = int(input("Apa yang ingin Anda lakukan ?"))
            if choice == 1:

                product = input("Masukkan data produk: ")
                product = product.split()

                # product name existing checking
                if product[0] in products:
                    print("Produk sudah pernah terdaftar.")
                else:
                    # append the instantiated object to the list
                    list_product.append(
                        Product(product[0], int(product[1]), int(product[2]),
                                user.user_name))
                    # products list containing all the products name of the products
                    # for product existing checking
                    products.append(product[0])

            elif choice == 2:
                user.lihat_produk_jualan_saya(user.user_name)

            elif choice == 3:
                print(f"Anda telah keluar dari akun {user.user_name}")
                break
        elif user.type == "BUYER":
            print(f"Saldo anda {user.saldo}")
            choice = int(input("Apa yang ingin Anda lakukan? "))
            if choice == 1:
                user.lihat_all_produk()
            elif choice == 2:
                buy = input("Masukkan barang yang ingin dibeli: ")
                user.beli_produk(buy)

            elif choice == 3:
                user.show_buy_history()
            elif choice == 4:
                print(f"Anda telah keluar dari akun {user.user_name}")
                break


list_user = []
users = []
products = []
list_product = []


def main():
    while True:
        print("Selamat datang di Dekdepedia!")
        print("Silakan memilih salah satu menu di bawah:")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")

        pilih = input("Pilihan Anda: ")

        if (pilih == "1"):
            banyak_user = int(input("Jumlah akun yang ingin didaftarkan : "))

            print("Data akun: ")
            for i in range(banyak_user):
                data_user = input(str(i + 1) + ". ")
                # for every user please check the valid or username existance with this function
                check_user_valid(data_user)

        elif (pilih == "2"):
            user_name_login = input("user_name : ")

            user_logged_in = get_user(user_name_login, list_user)

            if user_logged_in == None:
                print(
                    f"Akun dengan username {user_name_login} tidak ditemukan")
            else:

                after_login(user_logged_in)

        elif (pilih == "3"):
            print("Terima kasih telah menggunakan Dekdepedia!")
            exit()


if __name__ == "__main__":
    main()