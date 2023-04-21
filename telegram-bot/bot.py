import logging
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (Application, ApplicationBuilder, Updater,
                          CommandHandler, MessageHandler, CallbackContext,
                          filters, ConversationHandler, CallbackQueryHandler)
import os
import requests
from io import BytesIO
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.environ.get("API_URL")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        'Welcome to the Food Tracker Bot! To log a symptom, simply type the symptom name and any additional information (e.g. severity or notes).'
        ' To upload an image, use the paperclip icon and select the image you want to send.')


async def handle_text(update: Update, context: CallbackContext):
    text = update.message.text
    # Parse the message text to extract symptom name, severity, and notes
    # Then, call your API to log the symptom for the user
    # For example:
    # symptom_name, severity, notes = parse_symptom_info(text)
    # log_symptom(symptom_name, severity, notes, update.message.from_user.id)
    await update.message.reply_text(f"Logged symptom: {text}")


async def handle_image(update: Update, context: CallbackContext):
    file_id = update.message.photo[-1].file_id
    file = await context.bot.getFile(file_id)
    image = await file.download_as_bytearray()
    image = Image.open(BytesIO(image))
    image.show()

    await update.message.reply_text("Image uploaded successfully.")


# Define states for ConversationHandler
LOG_SYMPTOM, SELECT_SYMPTOM, INPUT_SEVERITY, INPUT_NOTES = range(4)


async def log_symptom(update: Update, context):
    await update.message.reply_text("Please, send me the name of the symptom you want to log.")
    return SELECT_SYMPTOM


async def select_symptom(update: Update, context):
    symptom_name = update.message.text
    # Search for the symptom using the API
    response = requests.get(f"{API_BASE_URL}/symptoms?search={symptom_name}")
    symptoms = response.json()
    print(symptoms)
    if len(symptoms) == 0:
        await update.message.reply_text("No symptom found. Please try again.")
        return SELECT_SYMPTOM

    keyboard = [[InlineKeyboardButton(s["name"], callback_data=f"{s['id']}")] for s in symptoms]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Select the symptom you want to log:", reply_markup=reply_markup)
    return INPUT_SEVERITY


async def input_severity(update: Update, context):
    query = update.callback_query
    await query.answer()

    context.user_data["symptom_id"] = query.data
    await query.edit_message_text("Please enter the severity of the symptom on a scale of 1 to 10.")
    return INPUT_NOTES


async def input_notes(update: Update, context):
    severity = int(update.message.text)
    context.user_data["severity"] = severity
    await update.message.reply_text(
        "Please enter any additional notes about the symptom (or type /skip if you don't want to add notes).")
    return LOG_SYMPTOM


async def log_symptom_done(update: Update, context):
    notes = update.message.text
    if notes == "/skip":
        notes = ""

    # Log the symptom using the API
    user_id = update.message.from_user.id
    symptom_data = {
        "user_id": user_id,
        "symptom_id": context.user_data["symptom_id"],
        "severity": context.user_data["severity"],
        "notes": notes
    }

    response = requests.post(f"{API_BASE_URL}/users/{user_id}/symptoms", json=symptom_data)

    if response.status_code == 200:
        await update.message.reply_text("Symptom logged successfully!")
    else:
        await update.message.reply_text("An error occurred while logging the symptom. Please try again.")

    return ConversationHandler.END


async def cancel(update: Update, context):
    await update.message.reply_text("Operation cancelled.")
    return ConversationHandler.END


def main() -> None:
    TOKEN = os.environ.get('TELEGRAM_TOKEN')
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        ConversationHandler(
            entry_points=[CommandHandler("log_symptom", log_symptom)],
            states={SELECT_SYMPTOM: [MessageHandler(filters.TEXT, select_symptom)],
                    INPUT_SEVERITY: [CallbackQueryHandler(input_severity)],
                    INPUT_NOTES: [MessageHandler(filters.TEXT, input_notes)],
                    },
            fallbacks=[CommandHandler("cancel", cancel)],

        )
    )
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    application.add_handler(MessageHandler(filters.PHOTO, handle_image))

    application.run_polling()


if __name__ == "__main__":
    main()
