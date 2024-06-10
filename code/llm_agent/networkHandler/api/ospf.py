""" 
This module contains the OSPF API functions. 
"""

from llm_agent.networkHandler.connection_methods import (
    parse_connect,
)
from genie.metaparser.util.exceptions import SchemaEmptyParserError


def ospf_neighbors(device_name: str) -> dict:
    """
    Retrieves the OSPF neighbors for a given device. Neighbors down are not included.

    Args:
      device_name (str): Must come from the function get_devices_list_available

    Returns:
      dict: A dictionary containing the OSPF neighbors information.
    """
    try:
        r = parse_connect(
            device_name=device_name,
            string_to_parse='show ip ospf neighbor',
        )
        if type(r.get('parse')) is SchemaEmptyParserError:
            return {"error": f"NO_OSPF_NEIGHBORS_FOUND: {device_name}"}
        else:
            return r
    except Exception as err:
        return {"error": f"{err}"}


def ospf_running(device_name: str) -> dict:
    """
    Retrieves OSPF info for a given device usefull to verify if ospf is running or not.

    Args:
      device_name (str): Must come from the function get_devices_list_available

    Returns:
      dict: A dictionary containing the OSPF database.
    """
    try:
        return _extract_ospf_running(parse_connect(
            device_name=device_name,
            string_to_parse="show ip protocols",
        ))
    except SchemaEmptyParserError as e:
        return {"error": f"NO_OSPF_CONFIGURED_ON: {device_name}"}


def ospf_details(device_name: str,vrf_name: str = "default" ) -> dict:
    """
    Retrieves the OSPF process information for a given device.

    Args:
      device_name (str): Must come from the function get_devices_list_available
      vrf_name (str, optional): The name of the VRF. Defaults to "default".

    Returns:
      dict: Return informations about the OSPF processs .

    """
    try:
        r = parse_connect(
            device_name=device_name,
            string_to_parse="show ip ospf ",
        )
        if type(r.get('parse')) is SchemaEmptyParserError:
            raise Exception("NO_OSPF_CONFIGURED: SchemaEmptyParserError")
        return r
    except Exception:
        return [
            f"NO_OSPF_CONFIGURED: {vrf_name}, DEVICE: {device_name}"
        ]
def ospf_interfaces(device_name: str, vrf_name: str = "default") -> list:
    """
    Retrieves the OSPF interfaces for a given device and VRF.

    Args:
      device_name (str): Must come from the function get_devices_list_available
      vrf_name (str, optional): The name of the VRF. Defaults to "default".

    Returns:
      list: A list of OSPF interfaces.

    """
    try:
        r = parse_connect(
            device_name=device_name,
            string_to_parse="show ip ospf interface ",
        )
        if type(r.get('parse')) is SchemaEmptyParserError:
            raise Exception("NO_OSPF_NEIGHBORS_FOUND: SchemaEmptyParserError")
        return _extract_ospf_interface(data=r)
    except Exception:
        return [
            f"NO_OSPF_INTERFACES_FOUND VRF: {vrf_name}, DEVICE: {device_name}"
        ]


def _extract_ospf_running(data: dict) -> dict:
    ospf_data = data.get("protocols", {}).get("ospf", {}).get("vrf", {})
    result = {}
    for vrf, vrf_data in ospf_data.items():
        interfaces = (
            vrf_data.get("address_family", {})
            .get("ipv4", {})
            .get("instance", {})

        )
        if interfaces is not None:
            result[vrf] = interfaces

    if not result:
        return {"error": "NO_OSPF_CONFIGURED"}
    return result

# {'vrf': {'default': {'address_family': {'ipv4': {'instance': {'1': {'areas': # {'0.0.0.0': {'interfaces':


def _extract_ospf_interface(data: dict) -> dict:
    ospf_data = data.get("vrf", {})
    result = {}
    for vrf, vrf_data in ospf_data.items():
        ospf_process = (
            vrf_data.get("address_family", {})
            .get("ipv4", {})
            .get("instance", {})
        )
        for ospf_instance, instance_data in ospf_process.items():
            interf = instance_data.get("areas", {}).get(
                '0.0.0.0').get('interfaces')
            if interf is not None:
                result[vrf] = interf

    if not result:
        return {"error": "NO_OSPF_CONFIGURED"}
    return result
