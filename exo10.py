word = input("Type a word: ")
its_palindrome = True

for i in range(len(word) // 2):
    if word[i] != word[-(i + 1)]:
        its_palindrome = False
        break

if its_palindrome:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")
