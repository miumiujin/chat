
def read_file(filename): # 將檔名變成一個參數 ，使用 function 的時候才去決定到底要讀取哪個檔案
	lines = []
	with open(filename, "r", encoding = "utf-8-sig") as f:
		for line in f: # 設一個for迴圈來讀取檔案 ， 然後每一行叫做一個 line
			lines.append(line.strip()) #為了把後面的換行符號在txt呈現時去掉
	return lines

def convert(lines):
	
	person = None # 我們還不知道說話的人是誰 ，所以預設為 None ，但還是有再迴圈內先宣告這個變數
	ht_word_count = 0
	ht_sticker_count = 0
	ht_image_count = 0
	howard_word_count = 0
	howard_sticker_count = 0
	howard_image_count = 0
	for line in lines:
		s = line.split(" ") # 讀取每一行迴圈的時候 ，遇到空白鍵就切割 ，將結果儲存在 s 這個 list
		time = s[0]
		name = s[1]
		if name == "Hsuan":
			if s[3] == "貼圖":
				ht_sticker_count += 1
			elif s[3] == "圖片":
				ht_image_count += 1
			else:
			    for m in s[3:]: # 清單的分割
				    ht_word_count += len(m)
		elif name == "howard":
			if s[2] == "貼圖":
				howard_sticker_count += 1
			elif s[2] == "圖片":
				howard_image_count += 1
			else:
			    for m in s[2:]:
				    howard_word_count += len(m)
	print("Hsuan Ting 說了", ht_word_count, "個字", "傳了", ht_sticker_count, "個貼圖", ht_image_count, "張圖片")
	print("howard 說了", howard_word_count, "個字", "傳了", howard_sticker_count, "個貼圖", howard_image_count, "張圖片")
	

def write_file(filename, lines): # 寫入檔案
	with open(filename, "w") as f:
		for line in lines:
			s = line.split(" ") # 讀取每一行迴圈的時候 ，遇到空白鍵就切割 ，將結果儲存在 s 這個 list
			f.write(line + "\n")


def main():
	lines = read_file("line_input.txt") # 在使用read_file()時 ，將"input.txt"放入filename這個參數 ，我們就可以在 with open 那行把它打開
	lines = convert(lines) # 觀察cmd的結果可以發現 ，lines 的結果是一個清單 ， 裝取我們 input.txt的所有內容
	#write_file("output.txt", lines) # 第一個參數為輸出的檔名(產生出的檔案的名字)

main()