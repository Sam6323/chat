
chat = []
chat_check = []

#讀檔案內容,去除\n
def read_file(filename):
	with open(filename, 'r', encoding='UTF-8') as f:
		for line in f:
			chat.append(line.strip())
	return chat
def check_chat(chat):
	for i in chat:
		if 'Allen' in i:
			who = i
			continue
		elif 'Tom' in i:
			who = i
			continue
		chat_check.append(who + ': ' + i + '\n')
	return chat_check
# 寫檔案
def write_file(write):
	with open(write, 'w', encoding='UTF-8') as keyin:
		for i in chat_check:
			keyin.write(i)
# main
def main():

	filename = ('input.txt')
	write = ('output_name.txt')
	read_file(filename)
	print(chat)
	check_chat(chat)
	write_file(write)
main()
