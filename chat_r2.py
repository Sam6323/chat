# 讀檔案內容,去除\n
def read_file(filename):
	chat = []
	with open(filename, 'r', encoding='UTF-8-sig') as f:
		for line in f:
			chat.append(line.strip())
	return chat
def check_chat(chat):
	allen_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for i in chat:
		s = i.split(' ')
		time  = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for msg in s[2:]:
					allen_count += len(msg)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for msg in s[2:]:
					viki_count += len(msg)
			for msg in s[2:]:
				viki_count += len(msg)
	print('Allen說了: ', allen_count, '個字', ',傳了', allen_sticker_count, '貼圖', ',傳了', allen_image_count, '圖片')
	print('Viki說了: ', viki_count, '個字', ',傳了', viki_sticker_count, '貼圖', ',傳了', viki_image_count, '圖片')
	
# 寫檔案
def write_file(write, talking):
	with open(write, 'w', encoding='UTF-8') as keyin:
		for i in talking:
			keyin.write(i)
# main
def main():

	filename = ('-LINE-Viki.txt')
	write = ('output_name.txt')
	chat = read_file(filename)
	chat = check_chat(chat)
	#write_file(write, chat)
main()
