def caesarCipher(s, k):
    result = []
    k = k % 26  
    for char in s:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr(base + (ord(char) - base + k) % 26))
        else:
            result.append(char)  
    return "".join(result)