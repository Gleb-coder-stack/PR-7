def process_input():
    global unique_words
    unique_words = set()

    for _ in range(3):
        line = input("Введите строку: ")
        words = line.split()
        unique_words.update(words)


def longest_word():
    longest_word = ""
    for word in unique_words:
        if (len(word) > len(longest_word)) or (len(word) == len(longest_word) and word < longest_word):
            longest_word = word
    return longest_word


process_input()
print("+".join(unique_words))
print(longest_word())
