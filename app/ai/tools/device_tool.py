
import logging, json
from langchain_core.tools import Tool
from app.services.devices import get_user_devices


def devices_tool(user_id: str, *args) -> str:
    logging.debug("devices_query: User with id %s", user_id)
    device_dicts = [device.to_dict() for device in get_user_devices(user_id)]
    return json.dumps(device_dicts)

def define_devices_tool(user_id: str):
    def devices_tool_wrapper(*args) -> str:
        logging.debug("Given: %s", args)
        return devices_tool(user_id, args)

    return Tool.from_function(
        name="devices_tool",
        description="This tool provides the list of devices for the user. The devices can be anything like"
                    "- Sensor"
                    "- Electronics"
                    "Use this tool when query contains the questions about the user devices. For example:"
                    "- How many devices do I have?"
                    "- Which are the devices with type spare parts?",
        func=devices_tool_wrapper
    )