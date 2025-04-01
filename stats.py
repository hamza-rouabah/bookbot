def get_num_words(text):
    return len(text.split())

def get_char_num(text):
    num_dict = {}

    for char in text.lower():
        if char.isalpha():
            if char in num_dict:
                num_dict[char] +=1
            else:
                num_dict[char] = 1
    return num_dict