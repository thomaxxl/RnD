from pyVmomi import vim
from samples.vsphere.common.service_manager import ServiceManager
from samples.vsphere.contentlibrary.lib.cls_api_client import ClsApiClient
from samples.vsphere.common.vim.helpers.vim_utils import get_obj
from com.vmware.content.library_client import Item
from com.vmware.vcenter.ovf_client import LibraryItem

vm_name = ''
rp_name = '' 
template_name = ''
esx_host = ''
api_host = ''
api_user = ''
api_pass = ''

service_manager = ServiceManager(api_host, api_user, api_pass, True)
service_manager.connect()
client = ClsApiClient(service_manager)
find_spec = Item.FindSpec(name = template_name)
ovf_template_id = client.library_item_service.find(find_spec)[0]
target = get_obj(service_manager.content, [vim.HostSystem], esx_host)
rp = get_obj(service_manager.content, [vim.ResourcePool], rp_name)
deployment_target = LibraryItem.DeploymentTarget(host_id=target._GetMoId(), resource_pool_id = rp._GetMoId())
deployment_spec = LibraryItem.ResourcePoolDeploymentSpec(name= template_name + '_deployed', accept_all_eula=True)
client.ovf_lib_item_service.deploy(ovf_template_id, deployment_target, deployment_spec)

