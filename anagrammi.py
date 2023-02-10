# problema di decisione: le due stringhe s1 e s2 sono anagrammi?

def is_anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        print("Sono anagrammi.")
    else:
        print("Non sono anagrammi.")

s1 ="mario rossi"
s2 ="orso rimasi"

print ( is_anagram(s1, s2) )
