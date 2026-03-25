import random
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RecipeData:
    recept_name: str
    ingredient_name: str
    ingredient_amount_value: int
    cooking_time: int
    recept_description: str
    path_image: str


RECIPE_NAMES = [
    "Борщ украинский",
    "Картошечка со шкварками",
    "Греческий салат",
    "Тыквенный крем-суп",
    "Куриные котлеты по-киевски",
]

INGRIDIENTS_NAMES = [
    "молоко",
    "картофель",
    "сало",
    "подсолнечное масло",
    "свекла"
]

RECIPE_DESCRIPTIONS = [
    "Наваристый суп на говяжьем бульоне со свёклой, капустой и сметаной",
    "Шикарная жаренная картошечка со шкварками",
    "Свежий салат из огурцов, томатов, маслин и сыра фета с оливковым маслом",
    "Нежный крем-суп из запечённой тыквы со сливками и мускатным орехом",
    "Сочные куриные котлеты с хрустящей корочкой и сливочным маслом внутри",
]

BASE_DIR = Path(__file__).resolve().parent.parent.parent


def build_reciptt() -> RecipeData:
    return RecipeData(
        recept_name=random.choice(RECIPE_NAMES),
        ingredient_name=random.choice(INGRIDIENTS_NAMES),
        ingredient_amount_value=random.randint(100, 300),
        cooking_time=random.randint(15, 90),
        recept_description=random.choice(RECIPE_DESCRIPTIONS),
        path_image=str(BASE_DIR / "data" / "recipes" / "images" / "recept_image.png")
    )
