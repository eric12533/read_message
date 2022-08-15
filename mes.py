data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

sum = 0
for d in data:
	sum += len(d)
print('留言的平均長度是',sum/len(data))

wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key進入字典
			
print('以下為出現超過100萬次的字')
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

#印出總共幾個單字
print('有紀錄的單字總共有', len(wc), '個')

#讓使用者查字
while True:
	word = input('請輸入您想搜尋的字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word], '次')
	else:
		print('這個字沒有出現過喔')

print('感謝使用本查詢功能')