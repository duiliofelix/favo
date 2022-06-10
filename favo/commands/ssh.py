import subprocess, json
from consolemenu import SelectionMenu
from favo.services.azure import choose_group, choose_vmss

def parse_instance_id(instance):
    buff = instance['id'].split('/')
    instance['id'] = buff[len(buff) - 1]
    return instance

def show_vm_menu(vms):
    if len(vms) == 1:
        return vms[0]['id']
            
    vm_list = []
    for vm in vms:
        vm_list.append('{} - {}'.format(vm['id'], vm['ip']))

    option = SelectionMenu.get_selection(vm_list)
    return vms[option]['id']

def ssh_cmd(args):
    group = args.group
    vmss = args.vmss
    instance = args.instance

    if not group:
        group = choose_group()
    
    if not vmss:
        vmss = choose_vmss(group)

    az_cmd = 'az vmss nic list -g {} --vmss-name {}'.format(group, vmss)
    jq_filter = 'jq "[.[] | {ip: .ipConfigurations[].privateIpAddress, id: .virtualMachine.id}]"'
    vms_str = subprocess.check_output('{} | {}'.format(az_cmd, jq_filter), shell=True, text=True)
    vms = list(map(parse_instance_id, json.loads(vms_str)))

    if not instance:
        instance = show_vm_menu(vms)

    for vm in vms:
        if vm['id'] == instance:
            subprocess.run("ssh {}".format(vm['ip']), shell=True)
            return

