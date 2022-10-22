import telebot
from telebot import types




bot = telebot.TeleBot("5722841128:AAEEwD5T-qt_RPaN8zy8V_wYlNx1L5R1Zrk")
global points
global points1
global text
global text1
points=0
points1=0
text=""
text1=""
@bot.message_handler(commands=["start"])
def hello(message):

    markup = types.InlineKeyboardMarkup( row_width=2)
    documents=types.InlineKeyboardButton("Уроки 📖",callback_data="Уроки")
    test=types.InlineKeyboardButton("Тесты 📄",callback_data="Тесты")
    markup.add(documents,test)

    bot.send_message(message.chat.id,"👋👋👋 Приветствую тебя пользователь 👋👋👋")
    bot.send_message(message.chat.id,"👾 Я бот помощник 👾")
    bot.send_message(message.chat.id,"Со мной ты сможежь познать  Мир цифровой граммотности 😎 ")
    bot.send_message(message.chat.id,"Ты можешь выполнять уроки , а потом проходить тесты,\nчтобы узнать как ты усвоил материал",reply_markup=markup)

@bot.callback_query_handler(lambda call:True)

def document(call):




    if call.data == "На главную":
        markup = types.InlineKeyboardMarkup( row_width=2)
        documents = types.InlineKeyboardButton("Уроки 📖",callback_data="Уроки")
        test = types.InlineKeyboardButton("Тесты📄",callback_data="Тесты")
        markup.add(documents, test)
        bot.send_message(call.message.chat.id,"Вы в главном меню",reply_markup=markup)






    if call.data == "Уроки":
        markup=types.InlineKeyboardMarkup(row_width=2)
        lesson1=types.InlineKeyboardButton("📕 Урок №1",callback_data="l1")
        inf1=types.InlineKeyboardButton("ℹ Информация об уроке",callback_data="i1")
        lesson2=types.InlineKeyboardButton("📘 Урок №2",callback_data="l2")
        inf2=types.InlineKeyboardButton("ℹ Иформация об уроке",callback_data="i2")
        ng=types.InlineKeyboardButton("На главную",callback_data="На главную")
        markup.add(lesson1,inf1,lesson2,inf2,ng)
        bot.send_message(call.message.chat.id,"Какой урок вы хотите пройти?",reply_markup=markup)


    if call.data == "l1":

        markup = types.InlineKeyboardMarkup(row_width=2)
        lesson2 = types.InlineKeyboardButton("📘 Урок №2", callback_data="l2")
        inf2 = types.InlineKeyboardButton("ℹ Иформация об уроке", callback_data="i2")
        ng = types.InlineKeyboardButton("На главную", callback_data="На главную")
        markup.add( lesson2, inf2, ng)

        bot.send_message(call.message.chat.id, "📙 Никогда не давайте свои личные данные на подозрительных сайтах")
        bot.send_message(call.message.chat.id, "📘 Никогда не качайте файлы с непроверенных сайтов")
        bot.send_message(call.message.chat.id, "📗 Не ведитесь на различные подозрительне рекламы",reply_markup=markup)

    if call.data == "i1":
        markup = types.InlineKeyboardMarkup(row_width=2)
        lesson1 = types.InlineKeyboardButton("📕 Урок №1", callback_data="l1")
        inf1 = types.InlineKeyboardButton("ℹ Информация об уроке", callback_data="i1")
        lesson2 = types.InlineKeyboardButton("📘 Урок №2", callback_data="l2")
        inf2 = types.InlineKeyboardButton("ℹ Иформация об уроке", callback_data="i2")
        ng = types.InlineKeyboardButton("На главную", callback_data="На главную")
        markup.add(lesson1, inf1, lesson2, inf2, ng)
        bot.send_message(call.message.chat.id,"ℹ Этот урок научит вас правилам  ,которые нужно соблюдать в интернете, которые должен знать каждый пользователь",reply_markup=markup)


    if call.data == "l2":
        bot.send_message(call.message.chat.id,"📕 Цифровая грамотность – набор знаний и умений, которые необходимы \n для безопасного и эффективного использования цифровых технологий и ресурсов интернета")
        bot.send_message(call.message.chat.id, "📕 Включает в себя: цифровое потребление; цифровые компетенции; цифровую безопасность.")
        bot.send_message(call.message.chat.id, "📘 Цифровое потребление – использование интернет услуг для работы и жизни")
        bot.send_message(call.message.chat.id, "📘 Включает в себя: фиксированный интернет, мобильный интернет,\nцифровые устройства, интернет-СМИ, новости, социальные сети,\n Госуслуги,телемедицину, облачные технологии")
        bot.send_message(call.message.chat.id, "📙 Цифровые компетенции – навыки эффективного пользования технологиями.")
        bot.send_message(call.message.chat.id, "📙 Включают в себя: поиск информации, использование цифровых устройств, \nиспользование функционала социальных сетей, финансовые операции и т.д.")
        bot.send_message(call.message.chat.id, "📗 Оценка информации - этовынесение суждений о ее адекватности, актуальности, пользе,качестве, релевантности или эффективности")
        bot.send_message(call.message.chat.id, "👆 Выше представлена основная инфорация 👆")
        bot.send_message(call.message.chat.id,"Если вы хотите узнать больше нажмите на соответствующую конпку")
        markup=types.InlineKeyboardMarkup(row_width=1)
        y=types.InlineKeyboardButton("На главную",callback_data="На главную")
        info=types.InlineKeyboardButton("Дополнительная информация",callback_data="ди")
        markup.add(info,y)
        bot.send_message(call.message.chat.id,"Если вы завершили выполнение урока ,тогда выйдете в главное меню и пройдите тест 😀 ",reply_markup=markup)


    if call.data =="ди":
        bot.send_message(call.message.chat.id, "http://kiro46.ru/docs/Cifr_Gramot.pdf")
        markup=types.InlineKeyboardMarkup(row_width=1)
        e=types.InlineKeyboardButton("На главную",callback_data="На главную")
        markup.add(e)
        bot.send_message(call.message.chat.id,"Теперь вы знайте все!!! 🧐",reply_markup=markup)

    if call.data == "i2":
        markup = types.InlineKeyboardMarkup(row_width=2)
        lesson1 = types.InlineKeyboardButton("Урок №1", callback_data="l1")
        inf1 = types.InlineKeyboardButton("ℹ Информация об уроке", callback_data="i1")
        lesson2 = types.InlineKeyboardButton("Урок №2", callback_data="l2")
        inf2 = types.InlineKeyboardButton("ℹ Иформация об уроке", callback_data="i2")
        ng = types.InlineKeyboardButton("На главную", callback_data="На главную")
        markup.add(lesson1, inf1, lesson2, inf2, ng)
        bot.send_message(call.message.chat.id,"ℹ Этот урок научит вас осноным понятиям \n в сфере информационной грамотности",reply_markup=markup)

    # тест 1

    if call.data == "Тесты":
        markup = types.InlineKeyboardMarkup(row_width=2)
        test1 = types.InlineKeyboardButton("📃 Тест №1", callback_data="t1")
        testinf1 = types.InlineKeyboardButton("ℹ Информация о тесте", callback_data="it1")
        test2 = types.InlineKeyboardButton("📃 Тест №2", callback_data="t2")
        testinf2 = types.InlineKeyboardButton("ℹ Иформация о тесте", callback_data="it2")
        ng = types.InlineKeyboardButton("На главную", callback_data="На главную")
        markup.add(test1, testinf1, test2, testinf2, ng)
        bot.send_message(call.message.chat.id, "Какой тест вы хотите пройти?", reply_markup=markup)


    if call.data == "it1":

        markup = types.InlineKeyboardMarkup(row_width=2)
        test1 = types.InlineKeyboardButton("📃 Тест №1", callback_data="t1")
        testinf1 = types.InlineKeyboardButton("ℹ Информация о тесте", callback_data="it1")
        test2 = types.InlineKeyboardButton("📃 Тест №2", callback_data="t2")
        testinf2 = types.InlineKeyboardButton("ℹ Иформация о тесте", callback_data="it2")
        ng = types.InlineKeyboardButton("На главную", callback_data="На главную")
        markup.add(test1, testinf1, test2, testinf2, ng)
        bot.send_message(call.message.chat.id, "ℹ Этот тест на проверку самых базовых знаний,\n которыми должен владеть каждых пользователь", reply_markup=markup)

    if call.data == "it2":
        markup = types.InlineKeyboardMarkup(row_width=2)
        test1 = types.InlineKeyboardButton("📃 Тест №1", callback_data="t1")
        testinf1 = types.InlineKeyboardButton("ℹ Информация о тесте", callback_data="it1")
        test2 = types.InlineKeyboardButton("📃 Тест №2", callback_data="t2")
        testinf2 = types.InlineKeyboardButton("ℹ Иформация о тесте", callback_data="it2")
        ng = types.InlineKeyboardButton("На главную", callback_data="На главную")
        markup.add(test1, testinf1, test2, testinf2, ng)
        bot.send_message(call.message.chat.id,"ℹ Этот тест на проверку основных знаний по информационной грамотности",reply_markup=markup)

    if call.data == "it22":
        markup = types.InlineKeyboardMarkup(row_width=2)
        test2 = types.InlineKeyboardButton("📃 Тест №2", callback_data="t2")
        testinf2 = types.InlineKeyboardButton("ℹ Иформация о тесте", callback_data="it2")
        markup.add( test2, testinf2, )
        bot.send_message(call.message.chat.id,"ℹ Этот тест на проверку основных знаний по информационной грамотности",reply_markup=markup)

    if call.data == "t1":
        mark = types.InlineKeyboardMarkup(row_width=2)
        num_1 = types.InlineKeyboardButton("a", callback_data="a0")
        num_2 = types.InlineKeyboardButton("b", callback_data="b0")
        mark.add(num_1, num_2)
        bot.send_message(call.message.chat.id,
                         "Если бы вам поступило подозритеьное педложение, что бы вы сделали 🤔 ? :\n a)проигнорирую его\n b)отвечу на него",
                         reply_markup=mark)

    if call.data == "a0":
        bot.send_message(call.message.chat.id, "✅✅✅ Да,это правильный ответ! ✅✅✅")
        global points1
        points1 += 1
        mark = types.InlineKeyboardMarkup(row_width=2)
        num_1 = types.InlineKeyboardButton("a", callback_data="a01")
        num_2 = types.InlineKeyboardButton("b", callback_data="b01")
        mark.add(num_1, num_2)
        bot.send_message(call.message.chat.id,"Будете ли вы вводить свои данные на подозритеьных сайтах 🤔🤔 ? : \n a)да \n b)нет",reply_markup=mark)

    if call.data == "b0":
        bot.send_message(call.message.chat.id, "❌❌❌ Нет,это неправильный ответ ❌❌❌")
        mark = types.InlineKeyboardMarkup(row_width=2)
        num_1 = types.InlineKeyboardButton("a", callback_data="a01")
        num_2 = types.InlineKeyboardButton("b", callback_data="b01")
        mark.add(num_1, num_2)
        bot.send_message(call.message.chat.id,"Будете ли вы вводить свои данные на подозритеьных сайтах 🤔🤔 ? : \n a)да \n b)нет",reply_markup=mark)

    if call.data == "b01":
        bot.send_message(call.message.chat.id, "✅✅✅ Да,это правильный ответ! ✅✅✅")
        points1 += 1
        mark = types.InlineKeyboardMarkup(row_width=2)
        num_1 = types.InlineKeyboardButton("a", callback_data="a02")
        num_2 = types.InlineKeyboardButton("b", callback_data="b02")
        mark.add(num_1, num_2)
        bot.send_message(call.message.chat.id,"Будете ли вы скачивать файлы с подозрительных сайтов 🤔🤔🤔 ?: \n a)да \n b)нет",reply_markup=mark)

    if call.data == "a01":
        bot.send_message(call.message.chat.id, "❌❌❌ Нет,это неправильный ответ ❌❌❌")
        mark = types.InlineKeyboardMarkup(row_width=2)
        num_1 = types.InlineKeyboardButton("a", callback_data="a02")
        num_2 = types.InlineKeyboardButton("b", callback_data="b02")
        mark.add(num_1, num_2)
        bot.send_message(call.message.chat.id,"Будете ли вы скачивать файлы с подозрительных сайтов 🤔🤔🤔 ?: \n a)да \n b)нет",reply_markup=mark)

    if call.data == "b02":
        bot.send_message(call.message.chat.id, "✅✅✅ Да,это правильный ответ! ✅✅✅")
        points1 += 1
        mark = types.InlineKeyboardMarkup(row_width=2)
        num_1 = types.InlineKeyboardButton("a", callback_data="a03")
        num_2 = types.InlineKeyboardButton("b", callback_data="b03")
        mark.add(num_1, num_2)
        bot.send_message(call.message.chat.id,
                         "Будете ли вы открывать странные файлы 🤔🤔🤔🤔 ?: \n a)да \n b)нет",
                         reply_markup=mark)

    if call.data == "a02":
        bot.send_message(call.message.chat.id, "❌❌❌ Нет,это неправильный ответ ❌❌❌")
        mark = types.InlineKeyboardMarkup(row_width=2)
        num_1 = types.InlineKeyboardButton("a", callback_data="a03")
        num_2 = types.InlineKeyboardButton("b", callback_data="b03")
        mark.add(num_1, num_2)
        bot.send_message(call.message.chat.id,
                         "Будете ли вы открывать странные файлы 🤔🤔🤔🤔 ?: \n a)да \n b)нет",
                         reply_markup=mark)

    if call.data == "b03":
        bot.send_message(call.message.chat.id, "✅✅✅ Да,это правильный ответ! ✅✅✅")
        points1 += 1
        mark = types.InlineKeyboardMarkup(row_width=2)
        num_1 = types.InlineKeyboardButton("a", callback_data="a04")
        num_2 = types.InlineKeyboardButton("b", callback_data="b04")
        mark.add(num_1, num_2)
        bot.send_message(call.message.chat.id,
                         "Можно ли давать свои пароли незнакомым людям  🤔🤔🤔🤔🤔 ?: \n a)да \n b)нет",
                         reply_markup=mark)

    if call.data == "a03":
        bot.send_message(call.message.chat.id, "❌❌❌ Нет,это неправильный ответ ❌❌❌")
        mark = types.InlineKeyboardMarkup(row_width=2)
        num_1 = types.InlineKeyboardButton("a", callback_data="a04")
        num_2 = types.InlineKeyboardButton("b", callback_data="b04")
        mark.add(num_1, num_2)
        bot.send_message(call.message.chat.id,"Можно ли давать свои пароли незнакомым людям  🤔🤔🤔🤔🤔 ?: \n a)да \n b)нет",
                         reply_markup=mark)

    if call.data == "b04":
        bot.send_message(call.message.chat.id, "✅✅✅ Да,это правильный ответ! ✅✅✅")
        points1 += 1
        global text1

        if points1 <= 2:
            text1 = "Ты плохо усвоил материал 😭😭😭. Тебе надо получше все выучить"
        if points1 == 3:
            text1 = "Ты средне выучил материал 😐😐😐 . Тебе надо кое-что повторить"
        if points1 == 4:
            text1 = "Ты хорошо все усвоил 🙂🙂🙂 , но немного недоучил"
        if points1 == 5:
            text1 = "Отлично 😀 ! Ты идеально все выучил 😎😎😎 !!! 💯💯💯💯"

        mark = types.InlineKeyboardMarkup(row_width=2)
        button = types.InlineKeyboardButton("На главную", callback_data="На главную")
        nextt= types.InlineKeyboardButton("📃 Следующий тест",callback_data="t2")
        nextit=types.InlineKeyboardButton("Информация о следующем тесте",callback_data="it22")
        mark.add(nextt,nextit,button)

        bot.send_message(call.message.chat.id, "Ты получил " + str(points1) + " очков(а)")
        bot.send_message(call.message.chat.id, text1, reply_markup=mark)
        points1 =0

    if call.data == "a04":

        if points1 <= 2:
            text1 = "Ты плохо усвоил материал 😭😭😭. Тебе надо получше все выучить"
        if points1 == 3:
            text1 = "Ты средне выучил материал 😐😐😐 . Тебе надо кое-что повторить"
        if points1 == 4:
            text1 = "Ты хорошо все усвоил 🙂🙂🙂 , но немного недоучил"
        if points1 == 5:
            text1 = "Отлично 😀 ! Ты идеально все выучил 😎😎😎 !!! 💯💯💯💯"
        mark = types.InlineKeyboardMarkup(row_width=2)
        button = types.InlineKeyboardButton("На главную", callback_data="На главную")
        nextt = types.InlineKeyboardButton("📃 Следующий тест", callback_data="t2")
        nextit = types.InlineKeyboardButton("Информация о следующем тесте", callback_data="it22")
        mark.add(nextt, nextit, button)

        bot.send_message(call.message.chat.id, "❌❌❌ Нет,это неправильный ответ ❌❌❌")
        bot.send_message(call.message.chat.id, "Ты получил " + str(points1) + " очков(а)")
        bot.send_message(call.message.chat.id, text1, reply_markup=mark)
        points1= 0

    if call.data == "t2":
        mark = types.InlineKeyboardMarkup( row_width=2)
        num_1 = types.InlineKeyboardButton("a",callback_data="a")
        num_2 = types.InlineKeyboardButton("b",callback_data="b")
        mark.add(num_1, num_2)
        bot.send_message(call.message.chat.id, "Что такое цифровая гамотность 🤔 ? :\n a)набор знаний ,которые необходимы для безопасного и эффективного использования цифровых технологий и ресурсов интернета \n b)набор знаний ,которые необходимы для  эффективного использования приложений на различных цифровых устройствах", reply_markup=mark)


    if call.data == "a" :
        bot.send_message(call.message.chat.id, "✅✅✅ Да,это правильный ответ! ✅✅✅")
        global points
        points += 1
        mark = types.InlineKeyboardMarkup( row_width=2)
        num_1 = types.InlineKeyboardButton("a",callback_data="a1")
        num_2 = types.InlineKeyboardButton("b",callback_data="b1")
        mark.add(num_1, num_2)
        bot.send_message(call.message.chat.id, "Что такое цифровое потребление 🤔🤔 ? : \n a)использование интернет услуг для работы и жизни \n b)использование интернет услуг для развлечений", reply_markup=mark)

    if call.data == "b":
        bot.send_message(call.message.chat.id, "❌❌❌ Нет,это неправильный ответ ❌❌❌")
        mark = types.InlineKeyboardMarkup( row_width=2)
        num_1 = types.InlineKeyboardButton("a",callback_data="a1")
        num_2 = types.InlineKeyboardButton("b",callback_data="b1")
        mark.add(num_1, num_2)
        bot.send_message(call.message.chat.id, "Что такое цифровое потребление 🤔🤔 ? : \n a)использование интернет услуг для работы и жизни \n b)использование интернет услуг для развлечений", reply_markup=mark)



    if call.data == "a1" :
        bot.send_message(call.message.chat.id, "✅✅✅ Да,это правильный ответ! ✅✅✅")
        points += 1
        mark = types.InlineKeyboardMarkup(row_width=2)
        num_1 = types.InlineKeyboardButton("a",callback_data="a2")
        num_2 = types.InlineKeyboardButton("b",callback_data="b2")
        mark.add(num_1, num_2)
        bot.send_message(call.message.chat.id, "Что такое цифровые компетенции 🤔🤔🤔 ?: \n a)навыки эффективного пользования технологиями \n b)навыки эфектнивного создания технологий", reply_markup=mark)

    if call.data == "b1":
        bot.send_message(call.message.chat.id, "❌❌❌ Нет,это неправильный ответ ❌❌❌")
        mark = types.InlineKeyboardMarkup( row_width=2)
        num_1 = types.InlineKeyboardButton("a",callback_data="a2")
        num_2 = types.InlineKeyboardButton("b",callback_data="b2")
        mark.add(num_1, num_2)
        bot.send_message(call.message.chat.id,"Что такое цифровые компетенции 🤔🤔🤔 ?: \n a)навыки эффективного пользования технологиями \n b)навыки эфектнивного создания технологий", reply_markup=mark)



    if call.data == "a2" :
        bot.send_message(call.message.chat.id, "✅✅✅ Да,это правильный ответ! ✅✅✅")
        points += 1
        mark = types.InlineKeyboardMarkup( row_width=2)
        num_1 = types.InlineKeyboardButton("a",callback_data="a3")
        num_2 = types.InlineKeyboardButton("b",callback_data="b3")
        mark.add(num_1, num_2)
        bot.send_message(call.message.chat.id, "Что включают в себя цифровые компетенции 🤔🤔🤔🤔 ?: \n a)поиск информации \n b)поиск информации, использование цифровых устройств, использование функционала социальных сетей, финансовые операции, онлайн-покупки, критическое восприятие информации, производства мультимедийного контента, синхронизация устройств.", reply_markup=mark)

    if call.data == "b2":
        bot.send_message(call.message.chat.id, "❌❌❌ Нет,это неправильный ответ ❌❌❌")
        mark = types.InlineKeyboardMarkup( row_width=2)
        num_1 = types.InlineKeyboardButton("a",callback_data="a3")
        num_2 = types.InlineKeyboardButton("b",callback_data="b3")
        mark.add(num_1, num_2)
        bot.send_message(call.message.chat.id, "Что включают в себя цифровые компетенции 🤔🤔🤔🤔 ?: \n a)поиск информации \n b)поиск информации, использование цифровых устройств, использование функционала социальных сетей, финансовые операции, онлайн-покупки, критическое восприятие информации, производства мультимедийного контента, синхронизация устройств.", reply_markup=mark)


    if call.data == "b3" :
        bot.send_message(call.message.chat.id, "✅✅✅ Да,это правильный ответ! ✅✅✅")
        points += 1
        mark = types.InlineKeyboardMarkup( row_width=2)
        num_1 = types.InlineKeyboardButton("a",callback_data="a4")
        num_2 = types.InlineKeyboardButton("b",callback_data="a4")
        mark.add(num_1, num_2)
        bot.send_message(call.message.chat.id, "Что такое оценка информации 🤔🤔🤔🤔🤔 ?: \n a)вынесение суждений о ее адекватности,актуальности, пользе, качестве, релевантности или эффективности \n b)оценивание информации", reply_markup=mark)

    if call.data == "a3":
        bot.send_message(call.message.chat.id, "❌❌❌ Нет,это неправильный ответ ❌❌❌")
        mark = types.InlineKeyboardMarkup( row_width=2)
        num_1 = types.InlineKeyboardButton("a",callback_data="a4")
        num_2 = types.InlineKeyboardButton("b",callback_data="a4")
        mark.add(num_1, num_2)
        bot.send_message(call.message.chat.id, "Что такое оценка информации 🤔🤔🤔🤔🤔 ?: \n a)вынесение суждений о ее адекватности,актуальности, пользе, качестве, релевантности или эффективности \n b)оценивание информации", reply_markup=mark)



    if call.data == "a4" :
        bot.send_message(call.message.chat.id, "✅✅✅ Да,это правильный ответ! ✅✅✅")
        points += 1
        global text

        if points <= 2:
            text = "Ты плохо усвоил материал 😭😭😭. Тебе надо получше все выучить"
        if points == 3:
            text = "Ты средне выучил материал 😐😐😐 . Тебе надо кое-что повторить"
        if points == 4:
            text = "Ты хорошо все усвоил 🙂🙂🙂 , но немного недоучил"
        if points == 5:
            text = "Отлично 😀 ! Ты идеально все выучил 😎😎😎 !!! 💯💯💯💯"


        mark = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton("На главную",callback_data="На главную")
        mark.add(button)


        bot.send_message(call.message.chat.id ,"Ты получил "+str(points)+" очков(а)")
        bot.send_message(call.message.chat.id,text,reply_markup=mark)
        points = 0

    if call.data == "b4":

        if points <= 2:
            text = "Ты плохо усвоил материал 😭😭😭. Тебе надо получше все выучить"
        if points == 3:
            text = "Ты средне выучил материал 😐😐😐 . Тебе надо кое-что повторить"
        if points == 4:
            text = "Ты хорошо все усвоил 🙂🙂🙂 , но немного недоучил"


        mark = types.InlineKeyboardMarkup(row_width=1)
        button = types.InlineKeyboardButton("На главную",callback_data="На главную")
        mark.add(button)


        bot.send_message(call.message.chat.id, "❌❌❌ Нет,это неправильный ответ ❌❌❌")
        bot.send_message(call.message.chat.id,"Ты получил "+str(points)+" очков(а)")
        bot.send_message(call.message.chat.id,text,reply_markup=mark)
        points = 0

#end test1



bot.polling(none_stop=True)