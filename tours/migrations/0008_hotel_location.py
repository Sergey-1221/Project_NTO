# Generated by Django 4.0 on 2022-11-22 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0007_hotel_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='location',
            field=models.CharField(choices=[('Абакан', 'Абакан'), ('Азов', 'Азов'), ('Александров', 'Александров'), ('Алексин', 'Алексин'), ('Альметьевск', 'Альметьевск'), ('Анапа', 'Анапа'), ('Ангарск', 'Ангарск'), ('Анжеро-Судженск', 'Анжеро-Судженск'), ('Апатиты', 'Апатиты'), ('Арзамас', 'Арзамас'), ('Армавир', 'Армавир'), ('Арсеньев', 'Арсеньев'), ('Артем', 'Артем'), ('Архангельск', 'Архангельск'), ('Асбест', 'Асбест'), ('Астрахань', 'Астрахань'), ('Ачинск', 'Ачинск'), ('Балаково', 'Балаково'), ('Балахна', 'Балахна'), ('Балашиха', 'Балашиха'), ('Балашов', 'Балашов'), ('Барнаул', 'Барнаул'), ('Батайск', 'Батайск'), ('Белгород', 'Белгород'), ('Белебей', 'Белебей'), ('Белово', 'Белово'), ('Белогорск (Амурская область)', 'Белогорск (Амурская область)'), ('Белорецк', 'Белорецк'), ('Белореченск', 'Белореченск'), ('Бердск', 'Бердск'), ('Березники', 'Березники'), ('Березовский (Свердловская область)', 'Березовский (Свердловская область)'), ('Бийск', 'Бийск'), ('Биробиджан', 'Биробиджан'), ('Благовещенск (Амурская область)', 'Благовещенск (Амурская область)'), ('Бор', 'Бор'), ('Борисоглебск', 'Борисоглебск'), ('Боровичи', 'Боровичи'), ('Братск', 'Братск'), ('Брянск', 'Брянск'), ('Бугульма', 'Бугульма'), ('Буденновск', 'Буденновск'), ('Бузулук', 'Бузулук'), ('Буйнакск', 'Буйнакск'), ('Великие Луки', 'Великие Луки'), ('Великий Новгород', 'Великий Новгород'), ('Верхняя Пышма', 'Верхняя Пышма'), ('Видное', 'Видное'), ('Владивосток', 'Владивосток'), ('Владикавказ', 'Владикавказ'), ('Владимир', 'Владимир'), ('Волгоград', 'Волгоград'), ('Волгодонск', 'Волгодонск'), ('Волжск', 'Волжск'), ('Волжский', 'Волжский'), ('Вологда', 'Вологда'), ('Вольск', 'Вольск'), ('Воркута', 'Воркута'), ('Воронеж', 'Воронеж'), ('Воскресенск', 'Воскресенск'), ('Воткинск', 'Воткинск'), ('Всеволожск', 'Всеволожск'), ('Выборг', 'Выборг'), ('Выкса', 'Выкса'), ('Вязьма', 'Вязьма'), ('Гатчина', 'Гатчина'), ('Геленджик', 'Геленджик'), ('Георгиевск', 'Георгиевск'), ('Глазов', 'Глазов'), ('Горно-Алтайск', 'Горно-Алтайск'), ('Грозный', 'Грозный'), ('Губкин', 'Губкин'), ('Гудермес', 'Гудермес'), ('Гуково', 'Гуково'), ('Гусь-Хрустальный', 'Гусь-Хрустальный'), ('Дербент', 'Дербент'), ('Дзержинск', 'Дзержинск'), ('Димитровград', 'Димитровград'), ('Дмитров', 'Дмитров'), ('Долгопрудный', 'Долгопрудный'), ('Домодедово', 'Домодедово'), ('Донской', 'Донской'), ('Дубна', 'Дубна'), ('Евпатория', 'Евпатория'), ('Егорьевск', 'Егорьевск'), ('Ейск', 'Ейск'), ('Екатеринбург', 'Екатеринбург'), ('Елабуга', 'Елабуга'), ('Елец', 'Елец'), ('Ессентуки', 'Ессентуки'), ('Железногорск (Красноярский край)', 'Железногорск (Красноярский край)'), ('Железногорск (Курская область)', 'Железногорск (Курская область)'), ('Жигулевск', 'Жигулевск'), ('Жуковский', 'Жуковский'), ('Заречный', 'Заречный'), ('Зеленогорск', 'Зеленогорск'), ('Зеленодольск', 'Зеленодольск'), ('Златоуст', 'Златоуст'), ('Иваново', 'Иваново'), ('Ивантеевка', 'Ивантеевка'), ('Ижевск', 'Ижевск'), ('Избербаш', 'Избербаш'), ('Иркутск', 'Иркутск'), ('Искитим', 'Искитим'), ('Ишим', 'Ишим'), ('Ишимбай', 'Ишимбай'), ('Йошкар-Ола', 'Йошкар-Ола'), ('Казань', 'Казань'), ('Калининград', 'Калининград'), ('Калуга', 'Калуга'), ('Каменск-Уральский', 'Каменск-Уральский'), ('Каменск-Шахтинский', 'Каменск-Шахтинский'), ('Камышин', 'Камышин'), ('Канск', 'Канск'), ('Каспийск', 'Каспийск'), ('Кемерово', 'Кемерово'), ('Керчь', 'Керчь'), ('Кинешма', 'Кинешма'), ('Кириши', 'Кириши'), ('Киров (Кировская область)', 'Киров (Кировская область)'), ('Кирово-Чепецк', 'Кирово-Чепецк'), ('Киселевск', 'Киселевск'), ('Кисловодск', 'Кисловодск'), ('Клин', 'Клин'), ('Клинцы', 'Клинцы'), ('Ковров', 'Ковров'), ('Когалым', 'Когалым'), ('Коломна', 'Коломна'), ('Комсомольск-на-Амуре', 'Комсомольск-на-Амуре'), ('Копейск', 'Копейск'), ('Королев', 'Королев'), ('Кострома', 'Кострома'), ('Котлас', 'Котлас'), ('Красногорск', 'Красногорск'), ('Краснодар', 'Краснодар'), ('Краснокаменск', 'Краснокаменск'), ('Краснокамск', 'Краснокамск'), ('Краснотурьинск', 'Краснотурьинск'), ('Красноярск', 'Красноярск'), ('Кропоткин', 'Кропоткин'), ('Крымск', 'Крымск'), ('Кстово', 'Кстово'), ('Кузнецк', 'Кузнецк'), ('Кумертау', 'Кумертау'), ('Кунгур', 'Кунгур'), ('Курган', 'Курган'), ('Курск', 'Курск'), ('Кызыл', 'Кызыл'), ('Лабинск', 'Лабинск'), ('Лениногорск', 'Лениногорск'), ('Ленинск-Кузнецкий', 'Ленинск-Кузнецкий'), ('Лесосибирск', 'Лесосибирск'), ('Липецк', 'Липецк'), ('Лиски', 'Лиски'), ('Лобня', 'Лобня'), ('Лысьва', 'Лысьва'), ('Лыткарино', 'Лыткарино'), ('Люберцы', 'Люберцы'), ('Магадан', 'Магадан'), ('Магнитогорск', 'Магнитогорск'), ('Майкоп', 'Майкоп'), ('Махачкала', 'Махачкала'), ('Междуреченск', 'Междуреченск'), ('Мелеуз', 'Мелеуз'), ('Миасс', 'Миасс'), ('Минеральные Воды', 'Минеральные Воды'), ('Минусинск', 'Минусинск'), ('Михайловка', 'Михайловка'), ('Михайловск (Ставропольский край)', 'Михайловск (Ставропольский край)'), ('Мичуринск', 'Мичуринск'), ('Москва', 'Москва'), ('Мурманск', 'Мурманск'), ('Муром', 'Муром'), ('Мытищи', 'Мытищи'), ('Набережные Челны', 'Набережные Челны'), ('Назарово', 'Назарово'), ('Назрань', 'Назрань'), ('Нальчик', 'Нальчик'), ('Наро-Фоминск', 'Наро-Фоминск'), ('Находка', 'Находка'), ('Невинномысск', 'Невинномысск'), ('Нерюнгри', 'Нерюнгри'), ('Нефтекамск', 'Нефтекамск'), ('Нефтеюганск', 'Нефтеюганск'), ('Нижневартовск', 'Нижневартовск'), ('Нижнекамск', 'Нижнекамск'), ('Нижний Новгород', 'Нижний Новгород'), ('Нижний Тагил', 'Нижний Тагил'), ('Новоалтайск', 'Новоалтайск'), ('Новокузнецк', 'Новокузнецк'), ('Новокуйбышевск', 'Новокуйбышевск'), ('Новомосковск', 'Новомосковск'), ('Новороссийск', 'Новороссийск'), ('Новосибирск', 'Новосибирск'), ('Новотроицк', 'Новотроицк'), ('Новоуральск', 'Новоуральск'), ('Новочебоксарск', 'Новочебоксарск'), ('Новочеркасск', 'Новочеркасск'), ('Новошахтинск', 'Новошахтинск'), ('Новый Уренгой', 'Новый Уренгой'), ('Ногинск', 'Ногинск'), ('Норильск', 'Норильск'), ('Ноябрьск', 'Ноябрьск'), ('Нягань', 'Нягань'), ('Обнинск', 'Обнинск'), ('Одинцово', 'Одинцово'), ('Озерск (Челябинская область)', 'Озерск (Челябинская область)'), ('Октябрьский', 'Октябрьский'), ('Омск', 'Омск'), ('Орел', 'Орел'), ('Оренбург', 'Оренбург'), ('Орехово-Зуево', 'Орехово-Зуево'), ('Орск', 'Орск'), ('Павлово', 'Павлово'), ('Павловский Посад', 'Павловский Посад'), ('Пенза', 'Пенза'), ('Первоуральск', 'Первоуральск'), ('Пермь', 'Пермь'), ('Петрозаводск', 'Петрозаводск'), ('Петропавловск-Камчатский', 'Петропавловск-Камчатский'), ('Подольск', 'Подольск'), ('Полевской', 'Полевской'), ('Прокопьевск', 'Прокопьевск'), ('Прохладный', 'Прохладный'), ('Псков', 'Псков'), ('Пушкино', 'Пушкино'), ('Пятигорск', 'Пятигорск'), ('Раменское', 'Раменское'), ('Ревда', 'Ревда'), ('Реутов', 'Реутов'), ('Ржев', 'Ржев'), ('Рославль', 'Рославль'), ('Россошь', 'Россошь'), ('Ростов-на-Дону', 'Ростов-на-Дону'), ('Рубцовск', 'Рубцовск'), ('Рыбинск', 'Рыбинск'), ('Рязань', 'Рязань'), ('Салават', 'Салават'), ('Сальск', 'Сальск'), ('Самара', 'Самара'), ('Санкт-Петербург', 'Санкт-Петербург'), ('Саранск', 'Саранск'), ('Сарапул', 'Сарапул'), ('Саратов', 'Саратов'), ('Саров', 'Саров'), ('Свободный', 'Свободный'), ('Севастополь', 'Севастополь'), ('Северодвинск', 'Северодвинск'), ('Северск', 'Северск'), ('Сергиев Посад', 'Сергиев Посад'), ('Серов', 'Серов'), ('Серпухов', 'Серпухов'), ('Сертолово', 'Сертолово'), ('Сибай', 'Сибай'), ('Симферополь', 'Симферополь'), ('Славянск-на-Кубани', 'Славянск-на-Кубани'), ('Смоленск', 'Смоленск'), ('Соликамск', 'Соликамск'), ('Солнечногорск', 'Солнечногорск'), ('Сосновый Бор', 'Сосновый Бор'), ('Сочи', 'Сочи'), ('Ставрополь', 'Ставрополь'), ('Старый Оскол', 'Старый Оскол'), ('Стерлитамак', 'Стерлитамак'), ('Ступино', 'Ступино'), ('Сургут', 'Сургут'), ('Сызрань', 'Сызрань'), ('Сыктывкар', 'Сыктывкар'), ('Таганрог', 'Таганрог'), ('Тамбов', 'Тамбов'), ('Тверь', 'Тверь'), ('Тимашевск', 'Тимашевск'), ('Тихвин', 'Тихвин'), ('Тихорецк', 'Тихорецк'), ('Тобольск', 'Тобольск'), ('Тольятти', 'Тольятти'), ('Томск', 'Томск'), ('Троицк', 'Троицк'), ('Туапсе', 'Туапсе'), ('Туймазы', 'Туймазы'), ('Тула', 'Тула'), ('Тюмень', 'Тюмень'), ('Узловая', 'Узловая'), ('Улан-Удэ', 'Улан-Удэ'), ('Ульяновск', 'Ульяновск'), ('Урус-Мартан', 'Урус-Мартан'), ('Усолье-Сибирское', 'Усолье-Сибирское'), ('Уссурийск', 'Уссурийск'), ('Усть-Илимск', 'Усть-Илимск'), ('Уфа', 'Уфа'), ('Ухта', 'Ухта'), ('Феодосия', 'Феодосия'), ('Фрязино', 'Фрязино'), ('Хабаровск', 'Хабаровск'), ('Ханты-Мансийск', 'Ханты-Мансийск'), ('Хасавюрт', 'Хасавюрт'), ('Химки', 'Химки'), ('Чайковский', 'Чайковский'), ('Чапаевск', 'Чапаевск'), ('Чебоксары', 'Чебоксары'), ('Челябинск', 'Челябинск'), ('Черемхово', 'Черемхово'), ('Череповец', 'Череповец'), ('Черкесск', 'Черкесск'), ('Черногорск', 'Черногорск'), ('Чехов', 'Чехов'), ('Чистополь', 'Чистополь'), ('Чита', 'Чита'), ('Шадринск', 'Шадринск'), ('Шали', 'Шали'), ('Шахты', 'Шахты'), ('Шуя', 'Шуя'), ('Щекино', 'Щекино'), ('Щелково', 'Щелково'), ('Электросталь', 'Электросталь'), ('Элиста', 'Элиста'), ('Энгельс', 'Энгельс'), ('Южно-Сахалинск', 'Южно-Сахалинск'), ('Юрга', 'Юрга'), ('Якутск', 'Якутск'), ('Ялта', 'Ялта'), ('Ярославль', 'Ярославль')], default=123, max_length=200, verbose_name='Местоположение'),
            preserve_default=False,
        ),
    ]
