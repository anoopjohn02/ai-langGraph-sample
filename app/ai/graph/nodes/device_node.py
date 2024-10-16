import logging, json
from typing import Any, Dict
from ..state import GraphState
from app.services.devices import get_user_devices

def devices_node(state: GraphState) -> Dict[str, Any]:
    user_id = state["user_id"]
    query = state["question"]
    logging.debug("devices_node: User with id %s", user_id)
    device_dicts = [device.to_dict() for device in get_user_devices(user_id)]
    documents = json.dumps(device_dicts)
    return {"documents": documents, "question": query}