from fastapi import APIRouter

from app.schemas import RecommendResponse, RecommendRequest
from app.services.calculator import calculate_bmi, calculate_recommended_intake, calculate_bmr
from app.services.recommender import recommend_menus_by_calories

router = APIRouter()

@router.post("/recommend", response_model=RecommendResponse)
def recommend(data: RecommendRequest):
    bmi = calculate_bmi(data.weight, data.height)
    bmr = calculate_bmr(data.gender, data.weight, data.height, data.age)
    recommended_intake = calculate_recommended_intake(bmr)

    recommended_menu = recommend_menus_by_calories(recommended_intake)

    return RecommendResponse(
        bmi=bmi,
        bmr=bmr,
        recommended_intake=recommended_intake,
        recommended_menu=recommended_menu
    )