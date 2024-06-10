import pyats
# from genie.testbed import load
from pyats.topology import loader
from pprint import pprint
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from llm_agent.networkHandler.api.ping import ping_device
from llm_agent.networkHandler.api.ospf import ospf_details
from langchain_core.utils.function_calling import convert_to_openai_function
from llm_agent.langchain_tools.lc_ping import ping_host_from_device
from llm_agent.langchain_tools.lc_interface_operations import action_shut_interface
import json



# Run project
# cd code
# uvicorn llm_agent.app:app --host 0.0.0.0 --port 5001&

# def ospf_database(device_name: str) -> dict:
#     """
#     Retrieves OSPF database for a given device.

#     Args:
#       device_name (str): Must come from the function get_devices_list_available

#     Returns:
#       dict: A dictionary containing the OSPF database.
#     """
#     try:
#         return parse_connect(
#             device_name=device_name,
#             string_to_parse="show ip ospf interface",
#         )
#     except Exception:
#         return {"error": f"NO_OSPF_CONFIGURED_ON: {device_name}"}

# testbed = loader.load('/code/testbed.yaml')

# dv = testbed.devices['Q-L-1']
# dv.connect(mit=True, via="cli",)


# def _extract_ospf_interface(data: dict) -> dict:
#     ospf_data = data.get("vrf", {})
#     result = {}
#     for vrf, vrf_data in ospf_data.items():
#         ospf_process = (
#             vrf_data.get("address_family", {})
#             .get("ipv4", {})
#             .get("instance", {})
#         )
#         for ospf_instance, instance_data in ospf_process.items():
#             interf = instance_data.get("areas", {}).get(
#                 '0.0.0.0').get('interfaces')
#             if interf is not None:
#                 result[vrf] = interf

#     if not result:
#         return {"error": "NO_OSPF_CONFIGURED"}
#     return result


# def ping_google(dv):
#     try:
#         p1 = dv.parse('ping google.com')
#         return p1

#     except SchemaEmptyParserError as e:
#         return {"Error": "NO_OSPF_CONFIGURED_ON: "}



print(convert_to_openai_function( ping_host_from_device))
pprint('\n ###################### \n')
print(convert_to_openai_function( action_shut_interface))

# def check_cdp_neighbors(dv):
#     try:
#         p1 = dv.parse('show cdp neighbors')
#         return p1

#     except SchemaEmptyParserError as e:
#         return {"Error": "NO_OSPF_CONFIGURED_ON: "}


# pprint(check_ospf(dv))

# pprint(ospf_neighbors('Q-L-1'))


{
  "name": "ping_host_from_device",
  "description": """Pings a destination from a device_name.
    Args:
      device_name (str): Must come from the function get_devices_list_available
      destination (str): The destination to ping.
      
    Returns:
        dict: with the result of the ping operation.""",
  "parameters": {
    "type": "object",
    "properties": {
      "device_name": {
        "type": "string"
      },
      "destination": {
        "type": "string"
      }
    },
    "required": [
      "device_name",
      "destination"
    ]
  }
}


{
  "name": "action_shut_interface",
  "description": """Shut down an interface on a device.
      Args:
        device_name (str): Must come from the function get_devices_list_available
        interface_name (str): The name of the interface to shut down.
              
      Returns:
           None""",
  "parameters": {
    "type": "object",
    "properties": {
      "device_name": {
        "type": "string"
      },
      "interface_name": {
        "type": "string"
      }
    },
    "required": [
      "device_name",
      "interface_name"
    ]
  }
}


