import re
def decodeMorse(morse_code):
    return " ".join(["".join(map(lambda x: MORSE_CODE[x],val.split(' '))) for val in re.split('\s\s\s*', morse_code.strip())])



