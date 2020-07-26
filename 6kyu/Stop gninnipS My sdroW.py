def spin_words(sentence:str):
    # Your code goes here
    ans = []
    for word in sentence.split(' '):
        if len(word) >= 5:
            ans.append(word[::-1])
        else:
            ans.append(word)
    return " ".join(ans)