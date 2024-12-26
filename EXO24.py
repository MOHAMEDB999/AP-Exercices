#I did not understand what was written in the exercise, so I used some help from ChatGPT (sorry).
#              (-_-)
def anagrams(S1, S2):
    # Remove spaces and convert to lowercase
    S1 = S1.replace(" ", "").lower()
    S2 = S2.replace(" ", "").lower()
    return sorted(S1) == sorted(S2)


print(anagrams("tame", "meta"))   # True
print(anagrams("tame", "mate"))   # True
print(anagrams("tame", "team"))   # True
print(anagrams("tabby", "batty")) # False
print(anagrams("python", "java")) # False
