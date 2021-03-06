import sys
import argparse
from .commands import list_cmd, ssh_cmd

def run():
    parser = argparse.ArgumentParser(
        description='Azure auxiliary tool',
        prog='favo',
    )
    subparsers = parser.add_subparsers(
        metavar='command',
        dest='command',
    )
    
    list_parser = subparsers.add_parser('list', help='List all VMSS in a resource group')

    ssh_parser = subparsers.add_parser('ssh', help='Start ssh session on some VMSS Instance')
    ssh_parser.add_argument('-g', '--group', help='vmss resource group name')
    ssh_parser.add_argument('-v', '--vmss', help='vmss name')
    ssh_parser.add_argument('-i', '--instance', help='instance id')
    
    arguments = parser.parse_args(sys.argv[1:])
    if arguments.command == 'list':
        list_cmd(arguments)
    elif arguments.command == 'ssh':
        ssh_cmd(arguments)

