import click
from flask.cli import AppGroup

from playground.root import services

app_group = AppGroup("root")


@app_group.command("deploy_contract")
def deploy_contract():
    """Deploy a new contract and print the contract address"""
    print(services.deploy_contract())


@app_group.command("get_user")
@click.option("-a", "--address")
def get_user(address):
    """Print current user information"""
    print(services.get_user(address))


@app_group.command("set_user")
@click.option("-a", "--address")
@click.option("-n", "--name")
@click.option("-g", "--gender")
def set_user(address, name, gender):
    """Set current user information"""
    services.set_user(address, name, gender)
