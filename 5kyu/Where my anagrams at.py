def anagrams(word, words):
    target = sorted(word)
    return list(filter(lambda x:sorted(x) == target, words))
