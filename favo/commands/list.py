import subprocess
from favo.services.azure import choose_group

def list_cmd(args):
    resource_group = choose_group()

    az_cmd = 'az vmss list -g %s | jq -r .[].name'%resource_group
    vmss_list = subprocess.check_output(az_cmd, shell=True, text=True)
    print(vmss_list)


