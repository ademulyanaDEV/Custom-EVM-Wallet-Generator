from eth_account import Account

def generate_wallets(n):
    wallets = []
    for _ in range(n):
        # Generate a new wallet
        acct = Account.create()
        private_key = acct._private_key.hex()  # Use _private_key instead of privateKey
        address = acct.address  # Get wallet address
        wallets.append((private_key, address))
    return wallets

def save_wallets_to_file(wallets, filename='addres.txt'):
    with open(filename, 'w') as f:
        for private_key, address in wallets:
            f.write(f'{private_key} {address}\n')

def main():
    # Ask user how many wallets to generate
    num_wallets = int(input("Masukkan jumlah wallet yang ingin di-generate: "))
    wallets = generate_wallets(num_wallets)
    save_wallets_to_file(wallets)
    print(f"{num_wallets} wallet berhasil di-generate dan disimpan di addres.txt")

if __name__ == "__main__":
    main()
