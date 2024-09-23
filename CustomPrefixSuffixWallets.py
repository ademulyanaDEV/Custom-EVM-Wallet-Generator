from eth_account import Account

# Fungsi untuk menghasilkan wallet dengan alamat yang diawali dan diakhiri dengan substring tertentu
def generate_wallets_with_prefix_suffix(n, prefix="00", suffix="0000"):
    wallets = []
    generated_count = 0  # Penghitung jumlah total wallet yang dihasilkan
    while len(wallets) < n:
        # Generate wallet baru
        acct = Account.create()
        private_key = acct._private_key.hex()
        address = acct.address
        
        # Hapus "0x" dari alamat untuk pengecekan
        address_no_0x = address[2:]
        generated_count += 1

        # Cek apakah alamat diawali dan diakhiri dengan prefix dan suffix yang diinginkan
        if address_no_0x.startswith(prefix) and address_no_0x.endswith(suffix):
            wallets.append((private_key, address))
        
        # Cetak log setiap 10k wallet yang di-generate
        if generated_count % 10000 == 0:
            print(f"{generated_count} wallet telah di-generate, {len(wallets)} di antaranya cocok dengan awalan '{prefix}' dan akhiran '{suffix}'")

    return wallets

# Fungsi untuk menyimpan wallet ke file
def save_wallets_to_file(wallets, filename='addres.txt'):
    with open(filename, 'w') as f:
        for private_key, address in wallets:
            f.write(f'{private_key} {address}\n')

def main():
    # Meminta jumlah wallet yang ingin dihasilkan
    num_wallets = int(input("Masukkan jumlah wallet yang ingin di-generate: "))
    prefix = input("Masukkan awalan alamat wallet yang diinginkan (contoh: 00): ")
    suffix = input("Masukkan akhiran alamat wallet yang diinginkan (contoh: 0000): ")
    
    # Generate wallet dengan prefix dan suffix yang diinginkan
    wallets = generate_wallets_with_prefix_suffix(num_wallets, prefix, suffix)
    
    # Simpan hasilnya ke file
    save_wallets_to_file(wallets)
    print(f"{num_wallets} wallet berhasil di-generate dan disimpan di addres.txt")

if __name__ == "__main__":
    main()
