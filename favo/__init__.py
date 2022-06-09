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
    
    list_parser = subparsers.add_parser('list', help='init help')

    ssh_parser = subparsers.add_parser('ssh', help='validate help')
    ssh_parser.add_argument('vmss', help='vmss name')
    ssh_parser.add_argument('instance', help='instance number')
    
    arguments = parser.parse_args(sys.argv[1:])
    if arguments.command == 'list':
        list_cmd(arguments)
    elif arguments.command == 'ssh':
        ssh_cmd(arguments)

