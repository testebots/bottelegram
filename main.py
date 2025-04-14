from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters

TOKEN = "7296549910:AAGuv0PW4RhV1Rehh_ame_Y0dDtGNt2zoYg"

# Função que envia a mensagem de introdução com botões
async def enviar_mensagem_introducao(chat_id, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Conteúdo", callback_data='conteudo'),
            InlineKeyboardButton("Avaliações", callback_data='avaliacoes'),
            InlineKeyboardButton("Personalizados", callback_data='personalizados')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_photo(
        chat_id=chat_id,
        photo="https://i.ibb.co/7xGYBBFb/photo-2025-04-14-11-37-59.jpg",  # substitua por sua imagem
        caption="🌸 Saudações MIUDINHOS: 🌸",
        reply_markup=reply_markup
    )
    print("Nova introdução")

# Handler para o comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await enviar_mensagem_introducao(update.effective_chat.id, context)

# Handler para qualquer outra mensagem
async def qualquer_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await enviar_mensagem_introducao(update.effective_chat.id, context)

# Handler para clique nos botões
async def responder_botao(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [[InlineKeyboardButton("🌸 Entrar em Contato 🌸", callback_data='contato')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if query.data == 'conteudo':
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text="💰 𝑽𝑨𝑳𝑶𝑹𝑬𝑺:\n\n🌸 10 𝑭𝑶𝑻𝑶𝑺 𝑺𝑬𝑴𝑰 𝑵𝑼𝑫𝑬𝑺 - R$ 45\n\n🌸 10 𝑭𝑶𝑻𝑶𝑺 𝑵𝑼𝑫𝑬𝑺 𝑬𝑿𝑷𝑳𝑰́𝑪𝑰𝑻𝑶𝑺 - R$ 95\n\n🌸 3 𝑽𝑰́𝑫𝑬𝑶𝑺 𝑺𝑬𝑿𝑶  - R$ 250\n\n🌸 3 𝑽𝑰́𝑫𝑬𝑶𝑺 𝑴𝑨𝑺𝑻𝑼𝑹𝑩𝑨𝑪̧𝑨̃𝑶 𝑨𝑻𝑬́ 𝑮𝑶𝒁𝑨𝑹 - R$195\n\n🌸 3 - 𝑽𝑰́𝑫𝑬𝑶𝑺 𝑬𝑿𝑷𝑳𝑰́𝑪𝑰𝑻𝑶𝑺 𝑬𝑿𝑰𝑩𝑰𝑵𝑫𝑶 𝑶 𝑪𝑶𝑹𝑷𝑶 - R$ 165",
            reply_markup=reply_markup
        )
    elif query.data == 'avaliacoes':
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text="💰 𝑨𝑽𝑨𝑳𝑰𝑨𝑪‌𝑶‌𝑬𝑺:\n\n🎀 𝑨‌𝑼𝑫𝑰𝑶: R$ 25\n\n🎀 𝑻𝑬𝑿𝑻𝑶: R$ 15\n\n🎀 𝑯𝑼𝑴𝑰𝑳𝑯𝑨𝑪‌𝑨‌𝑶 𝑨‌𝑼𝑫𝑰𝑶: R$ 35\n\n🎀 𝑨𝑽𝑨𝑳𝑰𝑨𝑪‌𝑨‌𝑶 𝑨‌𝑼𝑫𝑰𝑶 + 𝑪𝑶𝑵𝑺𝑬𝑳𝑯𝑶 𝑵𝑶 𝑸𝑼𝑬 𝑷𝑶𝑫𝑬 𝑴𝑬𝑳𝑯𝑶𝑹𝑨𝑹: R$ 45",
            reply_markup=reply_markup
        )
    elif query.data == 'personalizados':
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text="🌸 𝗦𝗘𝗥𝗩𝗜𝗖̧𝗢𝗦 𝗘𝗫𝗧𝗥𝗔 (𝗖𝗢𝗡𝗦𝗨𝗟𝗧𝗔𝗥 𝗗𝗜𝗦𝗣𝗢𝗡𝗜𝗕𝗜𝗟𝗜𝗗𝗔𝗗𝗘)\n\n\n👩🏽‍❤️‍💋‍👨🏽 𝑾𝑬𝑩 𝑵𝑨𝑴𝑶𝑹𝑶 𝟭𝟱 DIAS - COM DIREITO A 𝟯 FOTOS E 𝟯 VÍDEOS POR DIA, LIGAÇÃO DE VOZ E VÍDEO: R$ 𝟰𝟱𝟬\n\n\n🎥 𝑽𝑰́𝑫𝑬𝑶𝑺 𝑷𝑬𝑹𝑺𝑶𝑵𝑨𝑳𝑰𝒁𝑨𝑫𝑶𝑺 𝑫𝑬 𝑨𝑻𝑬́ 𝟭𝟬 MINUTOS: R$ 𝟮𝟰𝟱  REAIS\n\n\n𝙊𝙐𝙏𝙍𝙊𝙎 𝙎𝙀𝙍𝙑𝙄𝘾̧𝙊𝙎 𝙊𝙐 𝙎𝙐𝙂𝙀𝙎𝙏𝙊̃𝙀𝙎 𝙁𝘼𝙑𝙊𝙍 𝙀𝙉𝙏𝙍𝘼𝙍 𝙀𝙈 𝘾𝙊𝙉𝙏𝘼𝙏𝙊",
            reply_markup=reply_markup
        )
    elif query.data == 'contato':
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text="🌸 Só mandar mensagem pelo telegram: 🌸 \n\n @lylixc"
        )

# Inicialização do app
app = ApplicationBuilder().token(TOKEN).build()

# Adiciona os handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, qualquer_mensagem))
app.add_handler(CallbackQueryHandler(responder_botao))

print("Bot rodando...")
app.run_polling()
