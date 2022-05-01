#計算留言平均長度

data = []
with open("reviews.txt", "r") as f:
	for line in f:
		data.append(line)

sum_len = 0
for line in data:
    sum_len = sum_len + len(line)

msg_avg = sum_len / len(data)
print(sum_len)
print(msg_avg)