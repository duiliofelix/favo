import subprocess
from consolemenu import SelectionMenu

def choose_group():
    groups = subprocess \
        .check_output('az group list | jq -r .[].name', shell=True, text=True) \
        .split()

    option = SelectionMenu.get_selection(groups)
    return groups[option]

def choose_vmss(group):
    az_cmd = 'az vmss list -g %s | jq -r .[].name'%group
    vmss_list = subprocess \
        .check_output(az_cmd, shell=True, text=True) \
        .split()

    option = SelectionMenu.get_selection(vmss_list)
    return vmss_list[option]
