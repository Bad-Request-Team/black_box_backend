from pydantic import BaseModel, confloat, conint


class GraphicMessage(BaseModel):
    aggressive_percent: list[confloat(ge=0, le=1)]
    lane_percent: list[confloat(ge=0)]


class LastMessage(BaseModel):
    drivers_count: conint(ge=0)
    aggressive_drivers_count: conint(ge=0)
    normal_drivers_count: conint(ge=0)
    abrupt_braking_count: conint(ge=0)
    abrupt_acceleration_count: conint(ge=0)
    avg_speed: confloat(ge=0)
    avg_angle: confloat(ge=0)
    avg_acc: confloat(ge=0)
