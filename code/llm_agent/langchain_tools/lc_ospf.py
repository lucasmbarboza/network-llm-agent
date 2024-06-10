"""
Wrapper functions to work with langchain tools and openAI
"""

from langchain.agents import tool

from llm_agent.utils.text_utils import output_to_json
from llm_agent.networkHandler.api.ospf import (
    ospf_neighbors,
    ospf_interfaces,
    ospf_running,
    ospf_details,
)


@tool
def verify_ospf_process(device_name: str) -> dict:
    """
    Retrieves the OSPF process information for a given device. 

    Args:
      device_name (str): Must come from the function get_devices_list_available

    Returns:
      dict: A dictionary containing the OSPF processs information.
    """
    return output_to_json(ospf_details(device_name))

@tool
def verify_active_ospf_neighbors(device_name: str) -> dict:
    """
    Retrieves the OSPF neighbors for a given device. Neighbors down are not included.

    Args:
      device_name (str): Must come from the function get_devices_list_available

    Returns:
      dict: A dictionary containing the OSPF neighbors information.
    """
    return output_to_json(ospf_neighbors(device_name))


@tool
def get_ospf_running(device_name: str) -> dict:
    """
    Retrieves ospf database for a given device.

    Args:
      device_name (str): Must come from the function get_devices_list_available

    Returns:
      dict: A dictionary containing the OSPF database.
    """
    return output_to_json(ospf_running(device_name))


@tool
def get_ospf_interface_information(
    device_name: str,
) -> list:
    """
    Retrieves the OSPF interfaces for a given device.

    Args:
      device_name (str): Must come from the function get_devices_list_available
      vrf_name (str, optional): The name of the VRF. Defaults to "default".

    Returns:
      list: A list of OSPF interfaces.

    """
    return output_to_json(ospf_interfaces(device_name, "default"))
    # return ospf_interfaces(device_name, "default")
