from pydantic import BaseModel
from pydantic import confloat, conint


class GraphicMessage(BaseModel):
    aggressive_percent: confloat(ge=0, le=1)
    avg_speed: confloat(ge=0) | None


class LastMessage(BaseModel):
    drivers_count: conint(ge=0)
    aggressive_drivers_count: conint(ge=0)
    normal_drivers_count: conint(ge=0)
    abrupt_braking_count: conint(ge=0)
    abrupt_acceleration_count: conint(ge=0)
    max_speed: confloat(ge=0) | None
    min_speed: confloat(ge=0) | None
