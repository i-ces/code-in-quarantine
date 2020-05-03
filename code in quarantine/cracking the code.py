def requred_word(sentence):
    words = sentence.split()

    for i in words:
        for x in i:
            if((x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z')):
                continue
            else:
                words.remove(i)

    max_len = len(max(words, key=len))

    return [word for word in words if len(word) == max_len]


sentence = input()
x = requred_word(sentence)
print(x[0])
