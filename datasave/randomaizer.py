"""Этот файл отведен под рандомайзер, который создает данные для модели."""
import random


text_patterns = (

    'Абсцисса',
    'Габаритный чертеж',
    'Винтовые поверхности',
    'Горизонтальная прямая 1',
    'Горизонтальная плоскость проекций',
    'Исполнительный размер',
    'Комплекс',
    'Линейный размер1',
    'Масштаб',
    'Наружная резьба',

    'Orig. Inv. No.',
    'Repl. inv. No.',
    'Sheet 445',
    'Tag Number',
    'ketch',
    'Compeled by 123',

    '111',
    '222',
    '523525',
    '1234567',

    'L=124мм',
    'Ширина=123мм',
    'Длинна=1234мм',
    'Какой-то еще параметр=11111см',
    'Дом=344м.2',

    'К12-13',
    'А123-91',
    'КЗ12-12',
    'АБР93-94',
)


font_types = (
    'Adobe Jenson',
    'Алжирский',
    'Calisto MT',
    'Times New Roman',
    'Calibri'
)


def eng_or_rus(text: str) -> str:
    """

    Данная функция определяет к какому языку (Русский или Английский)
    относится текст.

    :param text: сгенерированный текст
    :return: тип текста

    """
    new_text = text.translate({ord(i): '' for i in 'ABEKHMOPCTXaeopcxАВЕКНМОРСТХаеорсх..,1234567890 '})

    eng = [chr(i) for i in range(ord('A'), ord('Z'))] + \
          [chr(i) for i in range(ord('a'), ord('z'))]

    ru = [chr(i) for i in range(ord('А'), ord('Я'))] + \
         [chr(i) for i in range(ord('а'), ord('я'))]

    if set(new_text).issubset(set(eng)):
        return 'eng_text'
    elif set(new_text).issubset(set(ru)):
        return 'ru_text'
    else:
        return 'multi_language_text'


def grouping(text: str) -> str:
    """

    Данная функция проверяет относится ли текст к следующим типам:
    параметр, номер, id.

    :param text: сгенерированный текст
    :return: либо один из перечисленных ранее типов, либо вызвает функцию
    eng_or_rus, которая определяет язык

    """
    if '=' in text:
        return 'parameter'
    elif text.translate(('0', '')).isdigit():
        return 'number'
    elif '-' in text:
        return 'id'
    else:
        return eng_or_rus(text)


def randomaizer() -> tuple:
    """

    Данная функция генерирует данные для модели.

    :return: возвращает кортеж из данных для модели

    """
    text = random.choice(text_patterns)
    axis_X = random.randint(0, 100)
    axis_Y = random.randint(0, 200)
    rotation = random.randint(0, 359)
    font_size = random.randint(1, 20)
    font_type = font_types[random.randint(0, 4)]
    data_type = grouping(text)

    return text, axis_X, axis_Y, rotation, font_size, font_type, data_type
