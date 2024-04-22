
from web3 import Web3
from eth_account import Account
from colorama import init, Fore, Back, Style
import webbrowser

init()

print(Fore.GREEN + """                      Bản quyền thuộc về https://t.me/Justice0210
            Ngoài ra mình bán tool check live Twitter (X), Tool đọc mail,
                            ae nào cần có thể ủng hộ mình :3""" + Style.RESET_ALL)

webbrowser.open('https://youtu.be/eYEZZ5huOBo') 

web3 = Web3(Web3.HTTPProvider("https://bsc-dataseed1.binance.org:443"))
def create_phrase():
    def create_metamask_wallet():
        Account.enable_unaudited_hdwallet_features()
        acct, mnemonic = Account.create_with_mnemonic()
        address = acct.address
        return mnemonic, address
    quantity = int(input('Nhập số acc cần tạo: '))
    f = open('Metamask Phrase.txt','a')
    for i in range(quantity):
        mnemonic, address = create_metamask_wallet()
        print(f"""
        {i + 1}
        Mnemonic: {mnemonic}
        Address: {address}

        """)
        f.write(f'{address} | {mnemonic}\n')

def create_private_key():
    quantity = int(input('Nhập số acc cần tạo: '))
    f = open('Metamask Private.txt','a')
    for i in range(quantity):
        new_acct = web3.eth.account.create()
        print(f"""
        {i + 1}
        Private: {Web3.toHex(new_acct.privateKey)}
        Address: {new_acct.address}

        """)
        f.write(f'{new_acct.address} | {Web3.toHex(new_acct.privateKey)}\n')

# CHẠY CÁI NÀO THÌ BỎ COMMENT CÁI ĐÓ

# Tạo ví với cụm 12 ký tự
# create_phrase()

# Tạo ví với private key
# create_private_key()



