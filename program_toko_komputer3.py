from prettytable import PrettyTable

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def quick_sort(list_produk, low, high, key, direction="ascending"):
    if low < high:
        pi = partition(list_produk, low, high, key, direction)
        quick_sort(list_produk, low, pi - 1, key, direction)
        quick_sort(list_produk, pi + 1, high, key, direction)

def partition(list_produk, low, high, key, direction):
    i = low - 1
    pivot = list_produk[high].data.__getattribute__(key)

    for j in range(low, high):
        current_element = list_produk[j].data.__getattribute__(key)
        if (direction == "ascending" and current_element < pivot) or (direction == "descending" and current_element > pivot):
            i += 1
            list_produk[i], list_produk[j] = list_produk[j], list_produk[i]

    list_produk[i + 1], list_produk[high] = list_produk[high], list_produk[i + 1]
    return i + 1

class LinkedListCircular:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def size(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next
            if current_node == self.head:
                break
        return count

    def add_first(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

    def add_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

    def add_after(self, node_data, new_data):
        new_node = Node(new_data)
        current_node = self.head
        while current_node is not None:
            if current_node.data == node_data:
                next_node = current_node.next
                current_node.next = new_node
                new_node.next = next_node
                if current_node == self.tail:
                    self.tail = new_node
                break
            current_node = current_node.next
            if current_node == self.head:
                break

    def delete_first(self):
        if self.is_empty():
            return
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            self.tail.next = self.head
            del temp

    def delete_last(self):
        if self.is_empty():
            return
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            current_node = self.head
            prev_node = None
            while current_node.next is not self.head:
                prev_node = current_node
                current_node = current_node.next
            prev_node.next = self.head
            self.tail = prev_node

    def delete_after(self, node_data):
        current_node = self.head
        prev_node = None
        while current_node is not None:
            if current_node.data == node_data:
                next_node = current_node.next
                if next_node == self.head:
                    self.tail = prev_node
                prev_node.next = next_node
                break
            prev_node = current_node
            current_node = current_node.next
            if current_node == self.head:
                break

    def search(self, nama):
        current_node = self.head
        while current_node is not None:
            if current_node.data.nama == nama:
                return current_node.data
            current_node = current_node.next
        return None

    def print_list(self):
        if self.is_empty():
            print("Daftar produk kosong.")
        else:
            table = PrettyTable(["Nama", "Harga (Rp)", "Stok", "Merek", "Kategori"])
            current_node = self.head
            while True:
                table.add_row([current_node.data.nama, "{:,}".format(current_node.data.harga), current_node.data.stok, current_node.data.merek, current_node.data.kategori])
                current_node = current_node.next
                if current_node == self.head:
                    break
            print(table)

    def quick_sort(self, key, direction="ascending"):
        nodes = [node for node in self]
        quick_sort(nodes, 0, self.size() - 1, key, direction)
        self.head = nodes[0]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = self.head

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next
            if current_node == self.head:
                break

    def search_by_name(self, nama):
        found_products = []
        current_node = self.head
        while True:
            if current_node.data.nama.lower() == nama.lower():
                found_products.append(current_node.data)
            current_node = current_node.next
            if current_node == self.head:
                break
        return found_products

    def search_by_category(self, kategori):
        found_products = []
        current_node = self.head
        while True:
            if current_node.data.kategori.lower() == kategori.lower():
                found_products.append(current_node.data)
            current_node = current_node.next
            if current_node == self.head:
                break
        return found_products

class Produk:
    def __init__(self, nama, harga, stok, merek, kategori):
        self.nama = nama
        self.harga = harga
        self.stok = stok
        self.merek = merek
        self.kategori = kategori

    def __str__(self):
        return f"Nama: {self.nama}\nHarga: Rp{self.harga:,}\nStok: {self.stok}\nMerek: {self.merek}\nKategori: {self.kategori} \n"

class KatalogProduk:
    def __init__(self):
        self.produk = LinkedListCircular()

    def create(self, produk):
        self.produk.add_last(produk)

    def read(self):
        print("\n--- Toko Komputer ---")
        self.produk.print_list()

    def update(self, nama, produk_baru):
            current_node = self.produk.head
            while current_node is not None:
                if current_node.data.nama == nama:
                    current_node.data = produk_baru
                    break
                current_node = current_node.next

            if current_node is None:
                print(f"Produk dengan nama '{nama}' tidak ditemukan.")

    def delete(self, nama):
        current_node = self.produk.head
        prev_node = None
        while current_node is not None:
            if current_node.data.nama == nama:
                if prev_node is None:  
                    self.produk.delete_first()
                else:
                    prev_node.next = current_node.next
                    if current_node == self.produk.tail:  
                        self.produk.tail = prev_node
                break
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            print(f"Produk dengan nama '{nama}' tidak ditemukan.")

    def get_available_categories(self):
        categories = set()
        current_node = self.produk.head
        while True:
            categories.add(current_node.data.kategori)
            current_node = current_node.next
            if current_node == self.produk.head:
                break
        return sorted(list(categories))

    def search_by_brand(self, merek):
        found_products = []
        current_node = self.produk.head
        while True:
            if current_node.data.merek.lower() == merek.lower():
                found_products.append(current_node.data)
            current_node = current_node.next
            if current_node == self.produk.head:
                break
        return found_products

    def get_available_brands(self):
        brands = set()
        current_node = self.produk.head
        while True:
            brands.add(current_node.data.merek)
            current_node = current_node.next
            if current_node == self.produk.head:
                break
        return sorted(list(brands))

def main():
    katalog = KatalogProduk()

    produk_baru = [
        Produk("AOC 27G4 Gaming Monitor", 2678000, 5, "AOC", "Monitor Gaming"),
        Produk("INTEL Core i5 13400F", 3500000, 3, "INTEL", "Processor"),
        Produk("LENOVO Legion 9i 16IRX8", 76999000, 2, "LENOVO", "Laptop Gaming"),
        Produk("ASUS ROG Zephyrus G16 GU603ZU", 24199000, 4, "ASUS", "Laptop Gaming"),
        Produk("MSI TITAN 18 HX RTX4090 i9 14900HX", 88499000, 2, "MSI", "Laptop Gaming"),
        Produk("ACER PREDATOR HELIOS 16 PH16 RTX4080 i9 13900HX", 32999000, 1, "ACER", "Laptop Gaming"),
        Produk("NVIDIA GeForce RTX 3060", 4475000, 4, "GIGABYTE", "Vga Card"),
        Produk("AMD Ryzen 5 5600G", 2179000, 5, "AMD", "Processor"),
        Produk("MSI PRO B660M-A DDR4", 1800000, 7, "MSI", "Motherboard"),
        Produk("DDR4 32GB (2x16GB) Corsair Vengeance LPX", 1350000, 6, "CORSAIR", "RAM"),
        Produk("NVMe M.2 1TB Samsung 980 Pro", 3200000, 4, "Samsung", "SSD"),
        Produk("ASUS Vivobook Pro 14 OLED M3401Q1-KM043W", 13000000, 2, "ASUS", "Laptop"),
        Produk("AMD Ryzen 9 7950X", 14000000, 6, "AMD", "Processor"),
        Produk("NVIDIA GeForce RTX 4070 Ti", 10000000, 2, "COLORFUL", "Vga Card"),
        Produk("RADEON RX 6900 XT", 7980000, 5, "GIGABYTE", "Vga Card"),
        Produk("RADEON RX 6600 XT", 3654000, 3, "SAPPHIRE", "Vga Card"),
        Produk("INTEL ARC A580", 3309000, 6, "ASROCK", "Vga Card"),
        Produk("INTEL Core i3 13100F", 1885000, 4, "INTEL", "Processor"),
        Produk("ADVAN Workplus AMD RYZEN 5 6600H 14'' FHD IPS", 6929000, 8, "ADVAN", "Laptop"),
        Produk("LENOVO IdeaPad Slim 3i i3-1215U", 6579000, 8, "LENOVO", "Laptop"),
        Produk("INTEL Core i9 13900KS", 12510000, 2, "INTEL", "Processor"),
        Produk("LENOVO LOQ Gaming i5-12450HX", 11999000, 4, "LENOVO", "Laptop Gaming"),
        Produk("KOORUI 24E4 Inch Gaming Monitor", 1565000, 4, "KOORUI", "Monitor Gaming"),
        Produk("GIGABYTE G34WQC Gaming Monitor", 5239000, 3, "GIGABYTE", "Monitor Gaming"),
        Produk("GIGABYTE B760 Aorus Elite AX", 3539000, 5, "GIGABYTE", "Motherboard"),
        Produk("ASUS ROG STRIX B760-G Gaming WIFI", 3809000, 4, "ASUS", "Motherboard"),
        Produk("PNY XLR8 Gaming DDR5 MAKO RGB 32GB (2x16GB)", 1830000, 4, "PNY", "RAM"),
        Produk("TEAMGROUP Delta TUF Alliance 32GB 2x16GB DDR5 5600Mhz ", 1665000, 6, "TEAMGROUP", "RAM"),
        Produk("TEAMGROUP MP33 M.2 2280 NVME 512GB", 625000, 7, "TEAMGROUP", "SSD"),
        Produk("PNY CS2241 M.2 NVME 2TB", 2040000, 5, "PNY", "SSD"),
        Produk("ADATA XPG SX8200 PRO M.2 NVME 512GB", 635000, 3, "ADATA", "SSD"),
    ]

    for produk in produk_baru:
        katalog.create(produk)

    while True:
        print("\n--- Toko Komputer ---")
        print("1. Tambah Produk")
        print("2. Lihat Produk")
        print("3. Urutkan Produk")
        print("4. Pencarian Produk")
        print("5. Ubah Produk")
        print("6. Hapus Produk")
        print("7. Keluar")

        pilihan = int(input("\nMasukkan pilihan: "))

        if pilihan == 1:
            nama_produk = input("Masukkan nama produk: ")
            if not nama_produk:
                print("Nama produk tidak boleh kosong!")
                continue

            harga_produk = input("Masukkan harga produk: ")
            if not harga_produk.isdigit() or int(harga_produk) < 0:
                print("Harga produk harus berupa angka positif!")
                continue
            harga_produk = int(harga_produk)

            stok_produk = input("Masukkan stok produk: ")
            if not stok_produk.isdigit() or int(stok_produk) < 0:
                print("Stok produk harus berupa angka positif!")
                continue
            stok_produk = int(stok_produk)

            merek_produk = input("Masukkan merek produk: ")
            if not merek_produk:
                print("Merek produk tidak boleh kosong!")
                continue

            kategori_produk = input("Masukkan kategori produk: ")
            if not kategori_produk:
                print("Kategori produk tidak boleh kosong!")
                continue

            produk_baru = Produk(nama_produk, harga_produk, stok_produk, merek_produk, kategori_produk)
            katalog.create(produk_baru)

        elif pilihan == 2:
            katalog.read()

        elif pilihan == 3:
            while True:
                print("\n--- Pilihan Urutkan Produk ---")
                print("1. Berdasarkan Nama")
                print("2. Berdasarkan Kategori")
                print("3. Berdasarkan Harga")
                print("4. Kembali ke Menu Utama")

                pilihan_sort = int(input("Masukkan pilihan: "))

                if pilihan_sort == 1:
                    while True:
                        print("\n--- Urutkan Berdasarkan Nama ---")
                        print("1. Ascending (A-Z)")
                        print("2. Descending (Z-A)")
                        print("3. Kembali ke Menu Urutkan")

                        pilihan_arah = input("Masukkan pilihan (1/2): ")

                        if pilihan_arah in ("1", "2"):
                            key = "nama"
                            direction = "ascending" if pilihan_arah == "1" else "descending"
                            katalog.produk.quick_sort(key, direction)
                            katalog.read()
                            break
                        elif pilihan_arah == "3":
                            break
                        else:
                            print("Pilihan tidak valid. Masukkan '1' atau '2'.")

                elif pilihan_sort == 2:
                    while True:
                        print("\n--- Urutkan Berdasarkan Kategori ---")
                        print("1. Ascending (A-Z)")
                        print("2. Descending (Z-A)")
                        print("3. Kembali ke Menu Urutkan")

                        pilihan_arah = input("Masukkan pilihan (1/2): ")

                        if pilihan_arah in ("1", "2"):
                            key = "kategori"
                            direction = "ascending" if pilihan_arah == "1" else "descending"
                            katalog.produk.quick_sort(key, direction)
                            katalog.read()
                            break
                        elif pilihan_arah == "3":
                            break
                        else:
                            print("Pilihan tidak valid. Masukkan '1' atau '2'.")

                elif pilihan_sort == 3:
                    while True:
                        print("\n--- Urutkan Berdasarkan Harga ---")
                        print("1. Ascending (Termurah)")
                        print("2. Descending (Termahal)")
                        print("3. Kembali ke Menu Urutkan")

                        pilihan_arah = input("Masukkan pilihan (1/2): ")

                        if pilihan_arah in ("1", "2"):
                            key = "harga"
                            direction = "ascending" if pilihan_arah == "1" else "descending"
                            katalog.produk.quick_sort(key, direction)
                            katalog.read()
                            break
                        elif pilihan_arah == "3":
                            break
                        else:
                            print("Pilihan tidak valid. Masukkan '1' atau '2'.")

                elif pilihan_sort == 4:
                    break
                else:
                    print("Pilihan tidak valid!")

        elif pilihan == 4:
            while True:
                print("\n--- Pencarian Produk ---")
                print("1. Pencarian Berdasarkan Merek")
                print("2. Pencarian Berdasarkan Kategori")
                print("3. Kembali ke Menu Utama")

                pilihan_pencarian = int(input("Masukkan pilihan: "))

                if pilihan_pencarian == 1:
                    available_categories = katalog.get_available_categories()
                    print("\n--- Kategori Tersedia ---")
                    for index, category in enumerate(available_categories, 1):
                        print(f"{index}. {category}")
                    kategori_cari = input("\nMasukkan nomor kategori yang ingin dicari: ")
                    if kategori_cari.isdigit() and 1 <= int(kategori_cari) <= len(available_categories):
                        kategori_cari = available_categories[int(kategori_cari) - 1]
                        found_products = katalog.produk.search_by_category(kategori_cari)
                        if found_products:
                            print("\n--- Produk Ditemukan ---")
                            table = PrettyTable(["Nama", "Harga (Rp)", "Stok", "Merek", "Kategori"])
                            for product in found_products:
                                table.add_row([product.nama, "{:,}".format(product.harga), product.stok, product.merek, product.kategori])
                            print(table)
                        else:
                            print(f"Tidak ditemukan produk dengan kategori '{kategori_cari}'.")
                    else:
                        print("Input tidak valid.")

                elif pilihan_pencarian == 2:
                    available_brands = katalog.get_available_brands()
                    print("\n--- Merek Produk Tersedia ---")
                    for index, brand in enumerate(available_brands, 1):
                        print(f"{index}. {brand}")
                    brand_choice = input("\nMasukkan nomor merek yang ingin dicari: ")
                    if brand_choice.isdigit() and 1 <= int(brand_choice) <= len(available_brands):
                        chosen_brand = available_brands[int(brand_choice) - 1]
                        found_products = katalog.search_by_brand(chosen_brand)
                        if found_products:
                            print("\n--- Produk Ditemukan ---")
                            table = PrettyTable(["Nama", "Harga (Rp)", "Stok", "Merek", "Kategori"])
                            for product in found_products:
                                table.add_row([product.nama, "{:,}".format(product.harga), product.stok, product.merek, product.kategori])
                            print(table)
                        else:
                            print(f"Tidak ditemukan produk dari merek '{chosen_brand}'.")
                    else:
                        print("Input tidak valid.")

                elif pilihan_pencarian == 3:
                    break
                else:
                    print("Pilihan tidak valid. Masukkan '1' atau '2'.")

        elif pilihan == 5:
            nama_produk = input("Masukkan nama produk yang ingin diubah: ")

            nama_baru = input("Masukkan nama baru: ")
            harga_baru = int(input("Masukkan harga baru: "))
            stok_baru = int(input("Masukkan stok baru: "))
            merek_baru = input("Masukkan merek baru: ")
            kategori_baru = input("Masukkan kategori baru: ")

            produk_baru = Produk(nama_baru, harga_baru, stok_baru, merek_baru, kategori_baru)
            katalog.update(nama_produk, produk_baru)

        elif pilihan == 6:
            nama_produk = input("Masukkan nama produk yang ingin dihapus: ")
            katalog.delete(nama_produk)

        elif pilihan == 8:
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
