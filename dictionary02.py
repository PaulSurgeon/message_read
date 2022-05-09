# 使用字典，做文字記數及查找功能。

data = []
with open("reviews.txt", "r") as f:
    for line in f:
        data.append(line)

word_count = {}
words = []
for msg in data:
    words = msg.split()
    for word in words:
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1

for word in word_count:
    if word_count[word] > 10000:
        print(word, word_count[word])