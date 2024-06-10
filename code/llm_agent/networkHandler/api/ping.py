""" 
This module contains the ping API functions. 
"""
from llm_agent.networkHandler.connection_methods import (
    parse_connect,
)
from genie.metaparser.util.exceptions import SchemaEmptyParserError


def ping_device(device_name: str, destination: str) -> dict:
    """
    Pings a destination from a device.

    Args:
      device_name (str): The name of the device.
      destination (str): The destination to ping.

    Returns:
      dict: A dictionary containing the result of the ping operation.
    """
    try:
        r = parse_connect(
            device_name=device_name,
            string_to_parse=f"ping {destination}",
        )
        print(r)
        if type(r.get('parse')) is SchemaEmptyParserError:
            raise Exception("PING_FAILED")
        else:
            return r
    except Exception:
        return {"error": f"PING_FAILED_TO: {destination}"}