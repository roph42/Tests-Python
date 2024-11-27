def find_missing_number(liste):
    """
        Fonction retournant un nombre manquant dans une liste de nombre
    """
    if not isinstance(liste, list):
        return f"Veuillez entrer une liste"
    
    ensemble = set(liste)
    min_val = min(liste)
    max_val = max(liste)
    
    for num in range(min_val, max_val + 1):
        if num not in ensemble:
            return num
        