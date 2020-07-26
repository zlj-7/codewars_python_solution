def my_first_interpreter(code):
    # Make your esolang interpreter here
    new_code = ""
    for char in code:
        if char == '+' or char == '.':
            new_code += char
    words = new_code.strip().split('.')
    ans = ""
    print(words)
    length = 0
    for word in words[:-1]:
        length += len(word)
        ans += chr(length % 256)
    return ans