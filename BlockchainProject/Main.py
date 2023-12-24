import argparse
import json
import hashlib
from time import time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.wallets = {}

        # Generate a genesis block
        self.create_block(proof=100)

    def create_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]) if self.chain else None,
        }

        # Clear the list of transactions after creating a block
        self.current_transactions = []

        self.chain.append(block)
        return block

    def create_transaction(self, sender, recipient, amount):
        if sender not in self.wallets or recipient not in self.wallets:
            print("Invalid sender or recipient.")
            return None

        sender_private_key = self.wallets[sender]['private_key']
        sender_public_key = self.wallets[sender]['public_key']

        # Verify sender's balance
        if self.get_balance(sender) < amount:
            print("Insufficient funds.")
            return None

        # Create a transaction dictionary
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            'block_index': len(self.chain) + 1,  # Add block index to transaction
        }

        # Sign and encrypt the transaction
        signed_transaction = self.sign_transaction(transaction, sender_private_key)
        encrypted_transaction = self.encrypt_transaction(signed_transaction, sender_public_key)

        # Add the encrypted transaction to the current_transactions list
        self.current_transactions.append(encrypted_transaction)

        return encrypted_transaction

    def add_block(self, proof):
        previous_hash = self.hash(self.chain[-1]) if self.chain else None
        added_block = self.create_block(proof, previous_hash)
        return added_block

    def hash(self, data):
        data_string = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(data_string).hexdigest()

    def merkle_tree(self, transactions):
        if len(transactions) % 2 != 0:
            transactions.append(transactions[-1])

        merkle_tree = [self.hash(transaction) for transaction in transactions]

        while len(merkle_tree) > 1:
            merkle_tree = [self.hash(merkle_tree[i] + merkle_tree[i + 1]) for i in range(0, len(merkle_tree), 2)]

        return merkle_tree[0]

    def create_wallet(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        public_key = private_key.public_key()

        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        while True:
            wallet_address = f"Wallet_{len(self.wallets) + 1}"

            if wallet_address not in self.wallets:
                break

        self.wallets[wallet_address] = {
            'private_key': private_key,
            'public_key': pem.decode('utf-8'),
        }

        return wallet_address

    def get_balance(self, wallet_address):
        balance = 0
        for block in self.chain:
            for transaction in block['transactions']:
                if transaction['recipient'] == wallet_address:
                    balance += transaction['amount']
                if transaction['sender'] == wallet_address:
                    balance -= transaction['amount']
        return balance

    def sign_transaction(self, transaction, private_key):
        private_key = serialization.load_pem_private_key(
            private_key.encode(),
            password=None,
            backend=default_backend()
        )

        signature = private_key.sign(
            json.dumps(transaction, sort_keys=True).encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        return {
            'transaction': transaction,
            'signature': signature
        }

    def encrypt_transaction(self, signed_transaction, public_key):
        public_key = serialization.load_pem_public_key(
            public_key.encode(),
            backend=default_backend()
        )

        encrypted_transaction = {
            'encrypted_data': public_key.encrypt(
                json.dumps(signed_transaction, sort_keys=True).encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            ).hex()
        }

        return encrypted_transaction


class BlockchainCLI:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.parser = argparse.ArgumentParser(description="Blockchain Command-Line Interface")
        self.subparsers = self.parser.add_subparsers(dest="command", help="Available commands")

        self.parser_transaction = self.subparsers.add_parser("transaction", help="Create a new transaction")
        self.parser_transaction.add_argument("sender", type=str, help="Sender's wallet address")
        self.parser_transaction.add_argument("recipient", type=str, help="Recipient's wallet address")
        self.parser_transaction.add_argument("amount", type=float, help="Transaction amount")

        self.parser_add_block = self.subparsers.add_parser("add_block", help="Add a new block")

        self.parser_show = self.subparsers.add_parser("show", help="Show the current state of the blockchain")

        self.parser_create_wallet = self.subparsers.add_parser("create_wallet", help="Create a new wallet")

        self.parser_get_balance = self.subparsers.add_parser("get_balance", help="Get the balance of a wallet")
        self.parser_get_balance.add_argument("wallet_address", type=str, help="Wallet address")

    def run_command(self, args):
        if args.command == "transaction":
            transaction = self.blockchain.create_transaction(args.sender, args.recipient, args.amount)
            if transaction:
                print(f"Transaction added to Block {transaction['transaction']['block_index']}")
        elif args.command == "add_block":
            proof = int(input("Enter the proof for the new block: "))
            added_block = self.blockchain.add_block(proof)
            print(f"Block added: {added_block}")
        elif args.command == "show":
            self.display_blockchain()
        elif args.command == "create_wallet":
            wallet_address = self.blockchain.create_wallet()
            print(f"New wallet created: {wallet_address}")
        elif args.command == "get_balance":
            balance = self.blockchain.get_balance(args.wallet_address)
            print(f"Balance of wallet {args.wallet_address}: {balance}")
        else:
            print("Invalid command. Use 'transaction', 'add_block', 'show', 'create_wallet', or 'get_balance'.")

    def display_blockchain(self):
        print("Blockchain:")
        for block in self.blockchain.chain:
            print(json.dumps(block, indent=2))
            print("--------------------")


if __name__ == "__main__":
    # Instantiate the Blockchain class
    blockchain = Blockchain()

    # Instantiate the BlockchainCLI class with the blockchain instance
    blockchain_cli = BlockchainCLI(blockchain)

    # Parse command-line arguments
    args = blockchain_cli.parser.parse_args()

    # Run the corresponding command
    blockchain_cli.run_command(args)

