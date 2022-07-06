from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import config

app = ApplicationBuilder().token(config.TOKEN).build()



async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}!\nБот по ведению списка дел активирован!!!\nВведи команду /help для просмотра доступных команд')

async def help_message(update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
    await update.message.reply_text(f'Вот список команд для взаимодействия со мной:\n/todo - выводит актуальный список дел.\n/add <задача> - добавит новую задачу в список.\n')

async def add_task(update, context) -> None:
    text = update.message.text
    with open('task.txt', "a", encoding = 'utf8') as file:
        file.write(f"{text}\n")

async def todo_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    read_sprv = open('task.txt', 'r', encoding = 'utf8')
    for i, line in enumerate(read_sprv, 1):
        await update.message.reply_text(f'{i} - {line}')
    read_sprv.close()

app.add_handler(CommandHandler("start", hello))
app.add_handler(CommandHandler("help", help_message))
app.add_handler(CommandHandler("add", add_task))
app.add_handler(CommandHandler("todo", todo_message))

app.run_polling()