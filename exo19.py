def pf_word():
    return input("Enter a word: ").strip().lower()


def save_to_file(words):
    filename = input("Enter a filename to save the unique words: ").strip()
    try:
        with open(filename, 'w') as file:
            file.write('\n'.join(sorted(words)))
        print(f"Unique words saved to {filename}.")
    except IOError:
        print("Error: Unable to save the file.")


def main():
    uniquewords = set()  
    tword = []  

    print("Enter words. The program will stop when you enter a duplicate word.")

    while True:
        word = pf_word()

        if word in uniquewords:
            print("\nDuplicate detected!")
            print(f"You typed in {len(uniquewords)} unique words.")
            print(f"Total words entered: {len(tword)}")
            print(f"Unique words (alphabetically): {sorted(uniquewords)}")

            if input("Would you like to save the unique words to a file? (yes/no): ").strip().lower() == "yes":
                save_to_file(uniquewords)
            break

        uniquewords.add(word)
        tword.append(word)

        print(f"Current unique word count: {len(uniquewords)}")


if __name__ == "__main__":
    main()
