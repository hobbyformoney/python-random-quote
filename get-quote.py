import random

def random_quote():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)-1
  #for i in range(0,2):
  rnd = random.randint(0,last)
  #	print(quotes[rnd].replace("\n", " "))
  quote=quotes[rnd].replace("\n", " ")
  return quote

def save_quote(user_quote):
	f = open("quotes.txt", 'a')
	f.write(user_quote +'\n')
	return "ok"

def user_input():
	user_line = input("Введите текст: ")
	return user_line

def reply(text):
	print("Чего изволит хозяин: ", text)

def handle_command(command):
	command = command.lower()
	if command == "привет":
		reply('Привет-привет!')
	elif command == "пока":
		reply("Пока!")
		exit()
	elif command == "цитата":
		q = random_quote()
		reply(q)
	elif command == "сохрани цитату":
		user_quote = user_input()
		sq = save_quote(user_quote)
		reply(sq)

	else:
		reply("Не понятно, повторите")	

def start():
	while True:
		user_text = user_input()
		handle_command(user_text)	


if __name__== "__main__":
  start()
