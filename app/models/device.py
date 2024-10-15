from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

class DeviceDto(BaseModel):
    """
    Device Dto
    """
    id: Optional[UUID] = None
    name: str
    description: str
    type: str
    created_on: Optional[datetime] = None

    def to_dict(self):
        return {
            'name': self.name,
            'type': self.type,
            'description': self.description,
        }
