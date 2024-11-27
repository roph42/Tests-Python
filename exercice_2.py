def are_anagrams(str1, str2):
    """
        Fonction vérifiant que deux chaînes de caractères sont des anagrammes
    """
    if(not isinstance(str1, str) or not isinstance(str2, str)):
        return f"Veuillez entrer des chaînes de caractères"
    
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False