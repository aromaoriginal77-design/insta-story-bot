from telegram.ext import Updater, CommandHandler
import subprocess
import os

TOKEN = os.environ.get("BOT_TOKEN")

def start(update, context):
    update.message.reply_text(
        "یوزرنیم پیج پابلیک را بفرست:\n/ig nasa"
    )

def ig(update, context):
    if not context.args:
        update.message.reply_text("یوزرنیم وارد نشده")
        return

    username = context.args[0]
    update.message.reply_text("در حال دریافت استوری...")

    subprocess.run(["instaloader", "--stories", username])

    sent = False
    for root, dirs, files in os.walk("."):
        for f in files:
            if f.endswith(".mp4") or f.endswith(".jpg"):
                update.message.reply_video(
                    open(os.path.join(root, f), "rb")
                )
                sent = True

    if not sent:
        update.message.reply_text("استوری‌ای پیدا نشد")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("ig", ig))

updater.start_polling()
updater.idle()
