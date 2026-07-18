import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

ABOUT_TEXT = (
    "🌤 Bu bot har kuni ertalab soat 07:00 da "
    "Samarqand ob-havosini taqdim etadi."
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Bot ishga tushirildi!\n\n"
        "🌤 Endi siz har kuni ertalab soat 07:00 da Samarqand ob-havosini avtomatik qabul qilasiz."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ABOUT_TEXT)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot ishga tushdi...")

    app.run_polling()

if __name__ == "__main__":
    main()
