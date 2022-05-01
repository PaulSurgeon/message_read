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

#一共有多少留言小於150

data2 = []
with open("reviews.txt", "r") as f:
	for line in f:
		if len(line) < 150:
			data2.append(line)
print("一共有", len(data2), "筆留言長度小於150")
print(data2[1000])

#一共有多少筆留言提到shit

data3 = []
with open("reviews.txt", "r") as f:
	for line2 in f:
		if "shit" in line2:
			data3.append(line2)
print("一共有", len(data3), "筆留言提到shit")
print("這是第 10 筆留言:")
print(data3[9])