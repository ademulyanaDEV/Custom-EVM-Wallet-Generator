from eth_account import Account

# Fungsi untuk menghasilkan wallet dengan alamat yang diakhiri dengan substring tertentu
def generate_wallets_with_suffixes(suffixes):
    wallets = []
    generated_count = 0  # Penghitung jumlah total wallet yang dihasilkan
    
    while True:
        # Generate wallet baru
        acct = Account.create()
        private_key = acct._private_key.hex()
        address = acct.address
        generated_count += 1

        # Cek apakah alamat diakhiri dengan salah satu suffix yang diinginkan (huruf besar/kecil diperhatikan)
        for suffix in suffixes:
            if address[-len(suffix):] == suffix:
                wallets.append((private_key, address, suffix))
                print(f"Ditemukan wallet dengan suffix '{suffix}': {address}")
                return wallets
        
        # Cetak log setiap 10k wallet yang di-generate
        if generated_count % 10000 == 0:
            print(f"{generated_count} wallet telah di-generate, belum ada yang cocok dengan suffix.")

# Fungsi untuk menyimpan wallet ke file
def save_wallets_to_file(wallets, filename='addres.txt'):
    with open(filename, 'w') as f:
        for private_key, address, suffix in wallets:
            f.write(f'{private_key} {address} (Suffix: {suffix})\n')

def main():
    # Meminta jumlah kategori suffix yang ingin dihasilkan
    num_suffixes = int(input("Masukkan jumlah kategori yang ingin dicari: "))
    
    # Meminta input kategori suffix dari user
    suffixes = []
    for i in range(num_suffixes):
        suffix = input(f"Masukkan akhiran alamat wallet untuk kategori {i+1}: ")
        suffixes.append(suffix)
    
    # Generate wallet dengan salah satu suffix yang diinginkan
    wallets = generate_wallets_with_suffixes(suffixes)
    
    # Simpan hasilnya ke file
    save_wallets_to_file(wallets)
    print(f"Wallet berhasil di-generate dan disimpan di addres.txt")

if __name__ == "__main__":
    main()
