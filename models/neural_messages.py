from pydantic import BaseModel, confloat, conint


class AnalystData(BaseModel):
    total_count: int
    aggressive_count: int
    acc_count: int 
    br_count: int
    lane_count: int
