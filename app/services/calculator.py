from app.schemas import GenderEnum


def calculate_bmi(height: float, weight: float) -> float:
    bmi = weight / ((height/100) ** 2)
    return round(bmi, 1)

def calculate_bmr(gender: GenderEnum, height: float, weight: float, age: int) -> float:
    if gender == GenderEnum.male:
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    return round(bmr, 1)

def calculate_recommended_intake(bmr: float) -> float:
    activity_factor = 1.2
    return round(activity_factor * bmr)