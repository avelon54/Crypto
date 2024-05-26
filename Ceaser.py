def ceaser_decrypt(plain_text, key):
    turkish_alphabet_lower_case = 'abcçdefgğhıijklmnoöprsştuüvyz'
    turkish_alphabet_upper_case = 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
    decrypted_text = ''
    
    for char in plain_text:
        if char in turkish_alphabet_lower_case:
            position = turkish_alphabet_lower_case.find(char)
            new_position = (position - key) % 29
            decrypted_text += turkish_alphabet_lower_case[new_position]
        elif char in turkish_alphabet_upper_case:
            position = turkish_alphabet_upper_case.find(char)
            new_position = (position - key) % 29
            decrypted_text += turkish_alphabet_upper_case[new_position]
        else:
            decrypted_text += char
    
    return decrypted_text

def ceaser_encrypt(text, key):
    turkish_alphabet_lower_case = 'abcçdefgğhıijklmnoöprsştuüvyz'
    turkish_alphabet_upper_case = 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
    encrypted_text = ''
    
    for char in text:
        if char in turkish_alphabet_lower_case:
            position = turkish_alphabet_lower_case.find(char)
            new_position = (position + key) % 29
            encrypted_text += turkish_alphabet_lower_case[new_position]
        elif char in turkish_alphabet_upper_case:
            position = turkish_alphabet_upper_case.find(char)
            new_position = (position + key) % 29
            encrypted_text += turkish_alphabet_upper_case[new_position]
        else:
            encrypted_text += char
    
    return encrypted_text
encrypted_text = 'CEZES NĞNS LIÜ ES LIÜ ÇIÜHI'
original_text = 'MERHABA'
print("*****************************************************************")

keys = [5,3,4]
decrypted_text = ceaser_decrypt(encrypted_text, keys[0])
print('Encrypted text: ', encrypted_text)
print('Decrypted text: ', decrypted_text)

print("*****************************************************************")

encrypted_text = ceaser_encrypt(original_text, keys[1])
print('Decrypted text: ', original_text)
print('Encrypted text: ', encrypted_text)

print("*****************************************************************")



