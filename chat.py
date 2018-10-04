
chat = []
chat_check = []

#讀檔案內容,去除\n
def read_file(filename):
	with open(filename, 'r', encoding='UTF-8') as f:
		for line in f:
			chat.append(line.strip())
	return chat
# def check_chat(chat):
# 	for i in chat:
# 		if i == 'Allen':
# 			who = i
# 			continue
# 		elif i == 'Tom':
# 			who = i
# 			continue
# 		chat_check.append(who + ': ' + i + '\n')


	return chat_check

# main
def main():

	filename = ('input.txt')
	read_file(filename)
	print(chat)
	# check_chat(chat)

	with open('test.txt', 'w', encoding='UTF-8') as keyin:
		for i in chat_check:
			keyin.write(i)
main()
