from eth_account import Account

# Fungsi untuk menghasilkan wallet dengan alamat yang diakhiri dengan substring tertentu
def generate_wallets_with_suffix(n, suffix="ADE"):
    wallets = []
    generated_count = 0  # Penghitung jumlah total wallet yang dihasilkan
    while len(wallets) < n:
        # Generate wallet baru
        acct = Account.create()
        private_key = acct._private_key.hex()
        address = acct.address
        generated_count += 1
        
        # Cek apakah alamat diakhiri dengan suffix yang diinginkan (huruf besar/kecil diperhatikan)
        if address[-len(suffix):] == suffix:
            wallets.append((private_key, address))
        
        # Cetak log setiap 10k wallet yang di-generate
        if generated_count % 10000 == 0:
            print(f"{generated_count} wallet telah di-generate, {len(wallets)} di antaranya cocok dengan akhiran '{suffix}'")

    return wallets

# Fungsi untuk menyimpan wallet ke file
def save_wallets_to_file(wallets, filename='addres.txt'):
    with open(filename, 'w') as f:
        for private_key, address in wallets:
            f.write(f'{private_key} {address}\n')

def main():
    # Meminta jumlah wallet yang ingin dihasilkan
    num_wallets = int(input("Masukkan jumlah wallet yang ingin di-generate: "))
    suffix = input("Masukkan akhiran alamat wallet yang diinginkan (contoh: 0ADE): ")
    
    # Generate wallet dengan suffix yang diinginkan
    wallets = generate_wallets_with_suffix(num_wallets, suffix)
    
    # Simpan hasilnya ke file
    save_wallets_to_file(wallets)
    print(f"{num_wallets} wallet berhasil di-generate dan disimpan di addres.txt")

if __name__ == "__main__":
    main()