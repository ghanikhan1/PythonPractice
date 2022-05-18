from cs50 import get_string

s = get_string("Text :")
num_letters, num_words, num_sentences = 0, 0, 0

for i in range(len(s)):
    num_words = len(s.split())
    if s[i].isalpha():
        num_letters += 1
    if s[i] == '.' or s[i] == '?' or s[i] == '!':
        num_sentences += 1
        
print(num_words)
print(num_letters)
print(num_sentences)

L = num_letters / num_words*100
S = num_sentences / num_words*100

index = 0.0588 * L - 0.296 * S - 15.8
if index >= 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(index)
    index = round(index)
    print("Grade ", index)
    