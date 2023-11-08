def my_title(text):
    words = text.split()
    modified_words = [word[0].upper() + word[1:].lower() for word in words]
    modified_text = " ".join(modified_words)
    return modified_text


text = "orlov Ilya evgenyevich"
modified_text = my_title(text)
print(modified_text)
