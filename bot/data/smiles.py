from emoji import emojize


class Emo:
	# коды эмодзи можно взять тут https://emojio.ru/smileys-emotion.html
	# или тут https://apps.timwhitlock.info/emoji/tables/unicode

	@staticmethod
	def emoj(smile):
		return emojize(smile, variant="emoji_type")

	ruble = emoj("₽")
	big_smile = emoj(":grinning_face_with_big_eyes:")
	hugs = emoj(":smiling_face_with_open_hands:")
	hand_over_mouth = emoj(":face_with_hand_over_mouth:")
	hundred = emoj(":hundred_points:")
	quiet = emoj(":shushing_face:")
	heart = emoj("❤️")
	omg_cat_face = emoj("🙀")
	red_exclamation = emoj("❗️")
	nerd_face = emoj(":nerd_face:")
	sunglasses = emoj("😎")
	explosive_head = emoj("🤯")
	hi = emoj("👋")
	just_smile = emoj("🙂")
	zero = emoj("0️⃣")
	one = emoj("1️⃣")
	two = emoj("2️⃣")
	three = emoj("3️⃣")
	four = emoj("4️⃣")
	five = emoj("5️⃣")
	six = emoj("6️⃣")
	seven = emoj("7️⃣")
	eight = emoj("8️⃣")
	nine = emoj("9️⃣")
	ten = emoj("🔟")
	hz = emoj("🤷‍♂️")
	please_eyes = emoj("🥺")
	plese = emoj("🙏")
	arrow_left = emoj("⬅️")
	arrow_right = emoj("➡️️")
	arrow_up = emoj("⬆️")
	arrow_down = emoj("⬇️")
	write = emoj('✍️')


class Texts:
	echo_text = (f'Такое я не знаю{Emo.hz}\nНа всякий случай сброшу всё до начального уровня\n'
				 f'Нажми /start, чтобы пройти опрос')


class Files:
	pass

