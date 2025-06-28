from enum import Enum

from pydantic import BaseModel, Field
from typing import List

class GenderEnum(str, Enum):
    male = "male"
    female = "female"

class GoalEnum(str, Enum):
    lean_bulking = "lean-bulking"
    bulking = "bulking"
    weight_loss = "weight-loss"

class RecommendRequest(BaseModel):
    gender: GenderEnum = Field(..., description="gender (male/female)")
    height: float = Field(..., gt=0, description="height (cm)")
    weight: float = Field(..., gt=0, description="weight (kg)")
    age: int = Field(..., gt=0, description="age (years)")
    goal: GoalEnum = Field(..., description="diet goal (lean-bulking, bulking, weight-loss)")

class MenuItem(BaseModel):
    name: str
    calories: float

class RecommendResponse(BaseModel):
    bmi: float
    bmr: float
    recommended_intake: float
    recommended_menu: List[MenuItem]