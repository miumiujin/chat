
def read_file(filename): # 將檔名變成一個參數 ，使用 function 的時候才去決定到底要讀取哪個檔案
	lines = []
	with open(filename, "r", encoding = "utf-8-sig") as f:
		for line in f: # 設一個for迴圈來讀取檔案 ， 然後每一行叫做一個 line
			lines.append(line.strip()) #為了把後面的換行符號在txt呈現時去掉
	return lines

def convert(lines):
	new = []
	person = None # 我們還不知道說話的人是誰 ，所以預設為 None ，但還是有再迴圈內先宣告這個變數
	for line in lines:
		if line == "Allen": # 如果 line 是 Allen 的話
			person = "Allen" # 就把 Allen 存在 person 這個變數當中
			continue # 跳到下一個迴圈
		elif line == "Tom":
			person = "Tom"
			continue
		if person: # 如果 person 有值 ，我們才執行下面這一行
		    new.append(person + ": " + line) # 一共有三個字串
	return new 

def write_file(filename, lines): # 寫入檔案
	with open(filename, "w") as f:
		for line in lines:
			f.write(line + "\n")


def main():
	lines = read_file("input.txt") # 在使用read_file()時 ，將"input.txt"放入filename這個參數 ，我們就可以在 with open 那行把它打開
	lines = convert(lines) # 觀察cmd的結果可以發現 ，lines 的結果是一個清單 ， 裝取我們 input.txt的所有內容
	write_file("output.txt", lines) # 第一個參數為輸出的檔名(產生出的檔案的名字)

main()