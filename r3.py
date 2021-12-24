lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ') # 先把人名時間跟訊息以空格區隔開來
	time = s[0][:5] # s[0]的部分為時間跟人名連在一起，但時間永遠是s[0]的前五個值 ，現在我們想把人名跟時間進一步分割
	name = s[0][5:] # 重要觀念 : str(字串)可以當成清單(list)來看 
	print(name)
