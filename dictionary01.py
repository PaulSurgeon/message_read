# 使用字典，做文字記數及查找功能。

drinks = {
	"coke" : "可樂",
	"tea" : "茶"
}

drinks["coffee"] = "咖啡"

print(drinks["coke"])
print(drinks["coffee"])
print("____________")
print(drinks)
print("____________")


foods = {
	"pasta": "義大利麵",
	"ramen": "拉麵"
}

print(foods["pasta"])
print("____________")

shop = [drinks, foods]

print(shop)

print(shop[0]["tea"])

# data = []
# with open("reviews.txt", "r") as f:
# 	for line in f:
# 		data.append(line)