def join_words(words, separator):
    return separator.join(words)


name = ["a", "b", "c", "d"]
sep = "_"
result = join_words(name, sep)
print(result)
