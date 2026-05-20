from . import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spellbook.light_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()
    is_valid = any(item.lower() in ingredients_lower for item in allowed)
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} {status}"
