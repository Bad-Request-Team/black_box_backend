from pydantic import BaseModel, confloat, conint


class AnalystData(BaseModel):
    avg_speed: confloat(ge=0)
    aggressive_percent: confloat(ge=0, le=1)
    drivers_count: conint(ge=0)
    aggressive_drivers_count: conint(ge=0)
    normal_drivers_count: conint(ge=0)
    abrupt_braking_count: conint(ge=0)
    abrupt_acceleration_count: conint(ge=0)
    max_speed: confloat(ge=0)
    min_speed: confloat(ge=0)
