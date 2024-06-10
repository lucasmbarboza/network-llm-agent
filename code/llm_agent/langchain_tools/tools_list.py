""" 
Import all the tools from the langchain_tools folder
"""

from llm_agent.langchain_tools.lc_inventory import get_devices_list_available
from llm_agent.langchain_tools.lc_device_health_state import (
    get_health_memory,
    get_health_cpu,
    get_health_logging,
)
from llm_agent.langchain_tools.lc_interface_config import (
    get_interface_running_config,
    get_interfaces_description,
)
from llm_agent.langchain_tools.lc_interface_operations import (
    action_shut_interface,
    action_unshut_interface,
)
from llm_agent.langchain_tools.lc_interface_state import (
    get_interfaces_status,
    get_single_interface_status,
    get_interface_information,
    get_interface_admin_status,
    verify_interface_state_up,
    get_interface_events,
)
from llm_agent.langchain_tools.lc_isis import (
    verify_active_isis_neighbors,
    get_isis_interface_events,
    get_isis_interface_information,
)
from llm_agent.langchain_tools.lc_routing import (
    get_vrf_present,
    get_interface_interfaces_under_vrf,
    get_routing_routes,
)

from llm_agent.langchain_tools.lc_ospf import (
    verify_active_ospf_neighbors,
    get_ospf_running,
    get_ospf_interface_information,
    verify_ospf_process,

)

from llm_agent.langchain_tools.lc_ping import ping_host_from_device

tools = [
    get_devices_list_available,
    get_health_memory,
    get_health_cpu,
    get_health_logging,
    get_interface_running_config,
    action_shut_interface,
    action_unshut_interface,
    get_interfaces_status,
    get_single_interface_status,
    get_interface_information,
    get_interfaces_description,
    get_interface_admin_status,
    verify_interface_state_up,
    get_interface_events,
    verify_active_isis_neighbors,
    get_isis_interface_events,
    get_isis_interface_information,
    get_vrf_present,
    get_interface_interfaces_under_vrf,
    get_routing_routes,
    verify_active_ospf_neighbors,
    verify_ospf_process,
    get_ospf_running,
    get_ospf_interface_information,
    ping_host_from_device
]
