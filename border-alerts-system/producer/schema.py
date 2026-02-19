from pydantic import BaseModel,Field
from typing import Literal
from datetime import datetime
import pandas as pd

df = pd.Timestamp

class BorderAlerts(BaseModel):
    border: Literal["egypt" ,"lebanon" , "gaza" , "syria" ,"jordan"]
    zone: str
    timestamp: str = Field(df =df.isoformat)  # type: ignore do it later
    people_count: int
    weapons_count:int
    vehicle_type: Literal["motorcycle" , "jeep" , "truck" , "car" , "none"]
    distance_from_fence_m: int
    visibility_quality:float
    priority:Literal["URGENT","NORMAL"]