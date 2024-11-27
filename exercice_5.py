def custum_sort(liste):
    """
        Fonction triant les string dans une liste
    """
    if not isinstance(liste, list):
        return f"Veuillez entrer une liste"
    
    return sorted(liste, key=lambda x: (len(x), sorted(x)))
        