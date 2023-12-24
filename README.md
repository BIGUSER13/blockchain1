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
- [Contributing](#contributing)
- [License](#license)

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

Show examples and commands for creating wallets.

### Making Transactions

Provide examples and commands for making transactions between wallets.

### Adding Blocks

Explain how to add blocks to the blockchain.

### Displaying Blockchain

Show how to display the current state of the blockchain.

### Getting Wallet Balance

Explain how to check the balance of a wallet.

## Examples

Provide real-world examples or use cases of your blockchain project.

## Contributing

Explain how others can contribute to your project.

## License

Specify the license under which your project is distributed.

