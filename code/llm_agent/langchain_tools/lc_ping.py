from langchain.agents import tool
from llm_agent.utils.text_utils import output_to_json

from llm_agent.networkHandler.api.ping import ping_device


@tool
def ping_host_from_device(device_name: str, destination: str) -> dict:
    """
    Pings a destination from a device_name.

    Args:
      device_name (str): Must come from the function get_devices_list_available
      destination (str): The destination to ping.

    Returns:
      dict: with the result of the ping operation.
    """
    return output_to_json(ping_device(device_name, destination))
