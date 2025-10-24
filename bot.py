import telebot

bot = telebot.TeleBot('BOT_TOKEN')

@bot.message_handler(commands=['start'])

def greeting(message):
    bot.send_message(message.chat.id, "Привет! Я твой личный бот. Здесь можно вести заметки и получать напоминания. Чтобы узнать команды, напиши /help.")   

@bot.message_handler(commands=['help'])

def bot_help(message):
    bot.send_message(message.chat.id,"Вот что я умею:\n"
"/start — запуск бота и приветствие\n"
"/add — добавить новую заметку\n"
"/list — показать все заметки\n"
"/delete — удалить заметку по номеру\n"
"/help — показать этот текст снова")
notes = []
@bot.message_handler(commands=['list'])

def all_notes (message):
    if notes:
        bot.send_message(message.chat.id, f"Вот все твои заметки:\n" + "\n".join(notes)) 
    else:
        bot.send_message(message.chat.id, 'У тебя пока нет заметок!')

@bot.message_handler(commands=['add'])

def add_note(message):
    bot.send_message(message.chat.id, "Напишите заметку: ")
    bot.register_next_step_handler(message, save_note) 
def save_note(message):
    new_note = message.text
    notes.append(new_note)
    bot.send_message(message.chat.id, f"Заметка {new_note} успешно добавлена! 📝") 


@bot.message_handler(commands=['delete'])

def delete_note(message):
    bot.send_message(message.chat.id, f"Выберите заметку которую хотите удалить:\n " + "\n".joinnotes)
   
    message_text = ""
    for i, element in enumerate(notes, start=1):
        message_text += f'{i}. {element}\n'
    bot.send_message(message.chat.id, message_text)
    
    
    bot.register_next_step_handler(message, deleted_note)

    
    
def deleted_note(message):
    note_for_deleting = message.text
    if note_for_deleting.isdigit():
        note_for_deleting = int(note_for_deleting)
        index = note_for_deleting - 1
        if 0 <= index < len(notes):
            notes.pop(index)
            bot.send_message(message.chat.id, "Заметка удалена ✅")
        else:
            bot.send_message(message.chat.id, "Такой заметки нет")         
    else:
        bot.send_message(message.chat.id, "Введите номер заметки!")
        bot.register_next_step_handler(message, deleted_note)
      
        
bot.polling(none_stop=True)
