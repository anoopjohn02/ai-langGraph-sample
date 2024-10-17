import json
import logging
import uuid
from typing import Any, Dict

from app.services.devices import get_user_devices
from ..state import GraphState


def user_devices_node(state: GraphState) -> Dict[str, Any]:
    user_id = uuid.UUID(state["user_id"]).hex
    query = state["question"]
    logging.debug("devices_node: User with id %s", user_id)
    device_dicts = [device.to_dict() for device in get_user_devices(user_id)]
    documents = json.dumps(device_dicts)
    return {"documents": documents, "question": query}