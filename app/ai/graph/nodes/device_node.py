import json
import logging
from typing import Any, Dict

from app.services.devices import get_user_devices
from ..state import GraphState


def user_devices_node(state: GraphState) -> Dict[str, Any]:
    user_id = state["user_id"]
    logging.debug("devices_node: User with id %s", user_id)
    documents = [json.dumps(device.to_dict()) for device in get_user_devices(user_id)]
    return {"documents": documents}