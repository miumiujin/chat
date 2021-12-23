
def read_file(filename): # 將檔名變成一個參數 ，使用 function 的時候才去決定到底要讀取哪個檔案
	lines = []
	with open(filename, "r", encoding = "utf-8-sig") as f:
		for line in f:
			lines.append(line.strip()) #為了把後面的換行符號在txt呈現時去掉
	return lines

def convert(lines):
	new = []
	person = None # 我們還不知道說話的人是誰 ，所以預設為 None ，但還是有宣告這個變數
	for line in lines:
		if line == "Allen":
			person = "Allen"
			continue
		elif line == "Tom":
			person = "Tom"
			continue

		if person: # 如果 person 有值 ，我們才執行下面這一行
		    new.append(person + ": " + line)
	return new 

def write_file(filename, lines):
	with open(filename, "w") as f:
		for line in lines:
			f.write(line + "\n")


def main():
	lines = read_file("input.txt") # 在使用read_file()時 ，將"input.txt"放入filename這個參數 ，我們就可以在 with open 那行把它打開
	lines = convert(lines)
	write_file("output.txt", lines)

main()