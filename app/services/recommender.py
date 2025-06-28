import json
from pathlib import Path
from typing import List

from app.schemas import MenuItem

menu_list = Path(__file__).parent.parent / "data" / "menus.json"

with open(menu_list, "r", encoding="UTF-8") as f:
    menus = json.load(f)

def recommend_menus_by_calories(recommended_intake: float) -> List[MenuItem]:
    meal_count = 2.3
    target_calories = recommended_intake / meal_count

    scored = [
        {
            "name": menu["name"],
            "calories": menu["calories"],
            "score": abs(menu["calories"] - target_calories),
        }
        for menu in menus
    ]

    scored.sort(key=lambda x: x["score"])
    top3 = scored[:3]

    return [MenuItem(name=menu["name"], calories=menu["calories"]) for menu in top3]