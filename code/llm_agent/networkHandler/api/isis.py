""" 
This module contains the ISIS API functions. 
"""

from llm_agent.networkHandler.connection_methods import (
    parse_connect,
)
from genie.metaparser.util.exceptions import SchemaEmptyParserError


def isis_neighbors(device_name: str) -> dict:
    """
    Retrieves the ISIS neighbors for a given device. Neighbors down are not included.

    Args:
      device_name (str): Must come from the function get_devices_list_available

    Returns:
      dict: A dictionary containing the ISIS neighbors information.
    """
    try:
        r = parse_connect(
            device_name=device_name,
            string_to_parse="show isis neighbors",
        )
        if type(r.parse) is SchemaEmptyParserError:
            raise Exception("NO_ISIS_NEIGHBORS_FOUND")
        else:
            return r
    except Exception:
        return {"error": f"NO_ISIS_NEIGHBORS_FOUND_ON: {device_name}"}


def isis_interface_events(device_name: str) -> dict:
    """
    Retrieves ISIS interface events for a given device.

    Args:
      device_name (str): Must come from the function get_devices_list_available

    Returns:
      dict: A dictionary containing the ISIS interface events.
    """
    try:
        r = parse_connect(
            device_name=device_name,
            string_to_parse="show isis lsp-log",
        )
        if type(r.parse) is SchemaEmptyParserError:
            raise Exception("NO_ISIS_EVENTS_FOUND")
        else:
            return r
    except Exception:
        return {"error": f"NO_ISIS_CONFIGURED_ON: {device_name}"}


def isis_interfaces(device_name: str, vrf_name: str = "default") -> list:
    """
    Retrieves the ISIS interfaces for a given device and VRF.

    Args:
      device_name (str): Must come from the function get_devices_list_available
      vrf_name (str, optional): The name of the VRF. Defaults to "default".

    Returns:
      list: A list of ISIS interfaces.

    """
    try:
        r = parse_connect(
            device_name=device_name,
            string_to_parse="show ip protocols",
        )
        if type(r.parse) is SchemaEmptyParserError:
            raise Exception("NO_ISIS_INTERFACES_FOUND")

    except Exception:
        return [
            f"NO_ISIS_INTERFACES_FOUND VRF: {vrf_name}, DEVICE: {device_name}"
        ]

    intf_isis = _extract_isis_interfaces(data=result)
    return intf_isis.get(
        vrf_name,
        f"NO_ISIS_INTERFACES_FOUND VRF: {vrf_name}, DEVICE: {device_name}",
    )


def _extract_isis_interfaces(data: dict) -> dict:
    isis_data = data.get("protocols", {}).get("isis", {}).get("vrf", {})
    result = {}
    for vrf, vrf_data in isis_data.items():
        interfaces = (
            vrf_data.get("address_family", {})
            .get("ipv4", {})
            .get("instance", {})
            .get("default", {})
            .get("configured_interfaces")
        )
        if interfaces is not None:
            result[vrf] = interfaces
    return result
