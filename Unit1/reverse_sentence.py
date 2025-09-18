def reverse_sentence(sentence):
    lst = sentence.split(" ")
    lst = lst[::-1]
    for i in lst:
        print(i, end=" ")
    print()

# Example Usage
sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)

sentence = "Pooh"
reverse_sentence(sentence) 