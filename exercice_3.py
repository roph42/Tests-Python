def longest_unique_substring(s):
    """
        Fonction retournant la longueur de la plus longue sous-chaîne
        sans caractères répétés?
    """
    if not isinstance(s, str):
        return f"Veuillez entrer une chaîne de caractères"
    
    sub_s = ''

    for i in range(len(s)):
        if s[i] not in s[i:] or (s[i] in s[i:] and s[i] not in sub_s):
            sub_s += s[i]
    return len(sub_s)
        