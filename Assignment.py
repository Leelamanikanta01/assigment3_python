def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    sentence = sentence.lower()
    return set(sentence) >= alphabet


input_sentence = "The quick brown fox jumps over the lazy dog"
if is_pangram(input_sentence):
    print("The input is a pangram.")
else:
    print("The input is not a pangram.")
