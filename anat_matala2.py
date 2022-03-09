def reverse(sentence, reverse_word):
    sentence = sentence.split()
    bool = False
    if(type(reverse_word) != str):
        print("invalid input")
        return None
    for index, word in enumerate(sentence):
        if word == reverse_word:
            sentence[index] =  word[::-1]
            sent_str = ""
            for i in sentence:
                sent_str += str(i) + " "
            sent_str = sent_str[:-1]
            return(sent_str)
    print("The word was not found")
    return None
#print(reverse("I like apples and I also like bananas", "like"))
#reverse("I like apples and I also like bananas", "oranges")
#reverse("I like apples and I also like bananas", "Bananas")
#reverse("I like apples and I also like bananas", 3)
