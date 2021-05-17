# My Ethereum playground

The application creates a simple smart contract that keeps track of the user name and gender in the blockchain.

Inspired by this somewhat outdated guideline: [How to develop Ethereum contract using Python Flask](https://medium.com/coinmonks/how-to-develop-ethereum-contract-using-python-flask-9758fe65976e).

## Installation instructions

```
pip install -r requirements.txt
npm install
cp -a env.example .env
```

## Usage guideline

Run Ganache CLI

```
npx ganache-cli
```

Compile the contract

```
make
```

Activate the environment

```
source env/bin/activate
```

Deploy the contract. Copy the contact address somewhere.

```
flask root deploy_contract
```

Set the user name and gender.

```
flask root set_user -a 0xXXXXXX -n Roman -g male
```

Get back the information from the blockchain.

```
flask root get_user -a 0xXXXXXX
```

## Where is the web API?

Well, there's none.
