# Blockchain Project

This project implements a simple blockchain using Python. It includes functionalities for creating wallets, making transactions, and adding blocks to the blockchain.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Creating Wallets](#creating-wallets)
  - [Making Transactions](#making-transactions)
  - [Adding Blocks](#adding-blocks)
  - [Displaying Blockchain](#displaying-blockchain)
  - [Getting Wallet Balance](#getting-wallet-balance)
- [Examples](#examples)

## Introduction
The blockchain project is a simple implementation in Python that simulates a basic blockchain system with features such as creating wallets, making transactions, and adding blocks to the chain. The primary goal is to provide a hands-on understanding of how a blockchain works and its fundamental components.

Key Features:

Blockchain Implementation: The project establishes a basic blockchain structure consisting of blocks, each containing a list of transactions.
Wallet Functionality: Users can create wallets, initiate transactions between wallets, and check the balance of a wallet.
Cryptographic Security: Transactions are signed and encrypted using RSA cryptography, ensuring the security and integrity of the blockchain.
Problem Solving:

Educational Purpose: The project serves as an educational tool to help individuals understand the core concepts of blockchain technology.
Hands-On Learning: Users can experiment with creating wallets, making transactions, and observing how blocks are added to the blockchain.
Introduction to Cryptography: The project introduces basic cryptographic techniques such as digital signatures and encryption in the context of blockchain security.
Overall, this project provides a practical and simplified introduction to blockchain concepts, making it accessible for those looking to gain a foundational understanding of this innovative technology.

## Features

Key Features of the Blockchain Project:

Blockchain Implementation:

The project establishes a basic blockchain structure with a chain of blocks.
Each block contains information such as transactions, timestamps, and proof of work.
Transaction System:

Users can create transactions between wallets.
Transactions include sender, recipient, amount, and block index information.
Wallet Functionality:

Users can generate wallets with public and private key pairs.
Wallets are associated with unique wallet addresses.
Cryptographic Security:

Transactions are signed using private keys to ensure authenticity.
RSA cryptography is employed for digital signatures and encryption.
Balance Tracking:

The project tracks and calculates the balance of each wallet based on transactions.
Merkle Tree Implementation:

A Merkle tree is used to consolidate and hash transactions efficiently.
Command-Line Interface (CLI):

Interaction with the blockchain is facilitated through a command-line interface.
Commands include transaction creation, block addition, wallet creation, balance checking, and blockchain display.
Educational Purpose:

The project is designed for educational purposes to provide hands-on experience with blockchain concepts.
Security Measures:

Cryptographic techniques ensure the security and integrity of transactions.
The use of public and private keys enhances privacy and authentication.
User-Friendly CLI:

The command-line interface offers a user-friendly way to interact with and explore blockchain functionalities.
These features collectively create a comprehensive yet accessible blockchain simulation, allowing users to explore the core components and mechanisms of blockchain technology.


## Getting Started

Prerequisites:

Python:
Ensure that Python is installed on your system. You can download Python from python.org.

Virtual Environment (Optional but recommended):
It's good practice to create a virtual environment for the project to avoid conflicts with system-wide Python packages.
python -m venv venv

Dependencies:
Install the required dependencies using the following command:
pip install -r requirements.txt
Running the Blockchain Project:
Run the Main Script:

Execute the Main.py script to interact with the blockchain via the command-line interface.
python Main.py
This will display the available commands and options.

Create Wallet:
To create a new wallet, use the following command: 
python Main.py create_wallet


Perform Transactions:
Create transactions between wallets using the transaction command. For example: 
python Main.py transaction Wallet_1 Wallet_2 10.0

Add Blocks:
Add new blocks to the blockchain using the add_block command. You'll be prompted to enter the proof for the new block.
python Main.py add_block

Show Blockchain:
To display the current state of the blockchain, use the show command.
python Main.py show

Get Wallet Balance:
Check the balance of a wallet using the get_balance command. 
For example: 
python Main.py get_balance Wallet_1


Additional Notes:
The project uses a simple in-memory blockchain, so restarting the script will reset the blockchain.
Make sure to understand the commands and their options by referring to the help messages in the script.
Now you should have the blockchain project up and running! Feel free to experiment with different commands and explore the basic blockchain functionalities.

## Usage

Create a New Transaction:

Command: python Main.py transaction <sender_wallet> <recipient_wallet> <amount>
Example: python Main.py transaction Wallet_1 Wallet_2 10.0
Add a New Block:

Command: python Main.py add_block
Users will be prompted to enter the proof for the new block.
Show the Current State of the Blockchain:

Command: python Main.py show
Displays the details of all blocks in the blockchain.
Create a New Wallet:

Command: python Main.py create_wallet
Generates a new wallet with a unique address.
Get the Balance of a Wallet:

Command: python Main.py get_balance <wallet_address>
Example: python Main.py get_balance Wallet_1

### Creating Wallets

Create a New Wallet:
Command: python Main.py create_wallet
Example Output:
New wallet created: Wallet_1

Create Another Wallet:
Command: python Main.py create_wallet
Example Output:
New wallet created: Wallet_2
Now, you have created two wallets with unique addresses (Wallet_1 and Wallet_2). You can continue to create more wallets using the create_wallet command, and each wallet will be assigned a distinct address.

### Making Transactions

Create a Transaction:

Command: python Main.py transaction Wallet_1 Wallet_2 10.0
Example Output:
Transaction added to Block 2

Create Another Transaction:
Command: python Main.py transaction Wallet_2 Wallet_1 5.0
Example Output:
Transaction added to Block 3
Now, you have initiated two transactions between Wallet_1 and Wallet_2. The specified amounts have been transferred, and these transactions are added to their respective blocks in the blockchain.

### Adding Blocks

Mine a New Block:

Command: python Main.py add_block

Example Output:
Enter the proof for the new block: 324567
Block added: {'index': 4, 'timestamp': 1643529812.123456, 'transactions': [...], 'proof': 324567, 'previous_hash': 'c3b42d7eab7e1a37f4b3f9c2c73de342b3d25c4975d2c5472542278f79b3780f'}
In this example, you are prompted to enter the proof for the new block. The proof is a value that, when hashed with the previous block's hash, satisfies a specific condition (e.g., having a certain number of leading zeros). The provided proof is used to create a new block, and the block is added to the blockchain.

Verify the Updated Blockchain:
Command: python Main.py show
Example Output:

Blockchain:
{
  "index": 1,
  "timestamp": 1643529637.123456,
  "transactions": [...],
  "proof": 100,
  "previous_hash": null
}
{
  "index": 2,
  "timestamp": 1643529642.123456,
  "transactions": [...],
  "proof": 12345,
  "previous_hash": "68f0f6b3033da05e033c2b03c4911d93a1e2bba28a0e1cfd4b0a32f06dbd7b48"
}
{
  "index": 3,
  "timestamp": 1643529650.123456,
  "transactions": [...],
  "proof": 67890,
  "previous_hash": "ed746f2519d0d1236e2f877e193c1f1a39f6f1587d55dd4c74d61b1f7d41df75"
}
{
  "index": 4,
  "timestamp": 1643529812.123456,
  "transactions": [...],
  "proof": 324567,
  "previous_hash": "c3b42d7eab7e1a37f4b3f9c2c73de342b3d25c4975d2c5472542278f79b3780f"
}
The updated blockchain includes the newly mined block (Index 4) with the specified proof and previous hash. Each block is linked to the previous one through its hash, ensuring the integrity and immutability of the blockchain.
### Displaying Blockchain

Show how to display the current state of the blockchain.

### Getting Wallet Balance

To check the balance of a wallet in the blockchain project, you can use the following command:
python Main.py get_balance <wallet_address>

Replace <wallet_address> with the actual wallet address you want to check. Here's an example:
python Main.py get_balance Wallet_2
This command will output the balance of the specified wallet address. The balance is calculated based on the transactions associated with the wallet in the blockchain.

Example Output:
Balance of wallet Wallet_2: 25.0

## Examples

Cryptocurrency Transactions:

Users can create wallets, make secure and transparent transactions with a cryptocurrency, and view their transaction history.
Example command: python Main.py create_wallet
Supply Chain Management:

The blockchain can be used to track the movement of goods in a supply chain, ensuring transparency and preventing fraud.
Example command: python Main.py transaction SenderWallet RecipientWallet Amount
Smart Contracts:

Implement smart contracts on the blockchain for self-executing contracts with predefined rules.
Example command: python Main.py add_block


