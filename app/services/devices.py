"""
Device service module
"""
import uuid
from typing import List

from app.data.sql.entities import Devices
from app.data.sql.repo import DeviceRepo
from app.models.device import DeviceDto
from app.models.user import LoggedInUser

repo = DeviceRepo()

def save_devices(devices: List[DeviceDto], user: LoggedInUser):
    """
    Method to save devices
    """
    for device in devices:
        entity = Devices()
        entity.id = uuid.uuid1()
        entity.name = device.name
        entity.description = device.description
        entity.type = device.type
        entity.user_id = user.id
        repo.save_device(entity)

def get_user_devices(user_id: uuid) -> List[DeviceDto]:
    """
    Method to get user devices
    """
    devices = repo.get_user_devices(user_id)
    return [DeviceDto(**device.__dict__) for device in devices]