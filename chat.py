



#讀檔案內容,去除\n
def read_file(filename):
	chat = []
	with open(filename, 'r', encoding='UTF-8-sig') as f:
		for line in f:
			chat.append(line.strip())
	return chat
def check_chat(chat):
	recheck = []
	for i in chat:
		if 'Allen' in i:
			who = i
			continue
		elif 'Tom' in i:
			who = i
			continue
		recheck.append(who + ': ' + i + '\n')
	return recheck
# 寫檔案
def write_file(write, talking):
	with open(write, 'w', encoding='UTF-8') as keyin:
		for i in talking:
			keyin.write(i)
# main
def main():

	filename = ('input.txt')
	write = ('output_name.txt')
	chat = read_file(filename)
	chat = check_chat(chat)
	write_file(write, chat)
main()
