import random



text_patterns = (

    #
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


    #
    'Orig. Inv. No.',
    'Repl. inv. No.',
    'Sheet 445',
    'Tag Number',
    'ketch',
    'Compeled by 123',

    # Только цифры
    '111',
    '222',
    '523525',
    '1234567',


    # =
    'L=124мм',
    'Ширина=123мм',
    'Длинна=1234мм',
    'Какой-то еще параметр=11111см',
    'Дом=344м.2',

    # присутствует тире
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

    new_text = text.translate({ord(i): '' for i in 'ABEKHMOPCTXaeopcxАВЕКНМОРСТХаеорсх..,1234567890 '})

    eng = [chr(i) for i in range(ord('A'), ord('Z'))] + [chr(i) for i in range(ord('a'), ord('z'))]

    if set(new_text).issubset(set(eng)):
        return 'eng_text'
    else:
        return 'ru_text'





def grouping(text: str) -> str:

    if '=' in text:
        return 'parameter'
    elif text.translate(('0','')).isdigit():
        return 'number'
    elif '-' in text:
        return 'id'
    else:
        return eng_or_rus(text)


def randomaizer() -> tuple:
    text = text_patterns[random.randint(0, 28)]
    axis_X = random.randrange(0, 100)
    axis_Y = random.randrange(0, 200)
    rotation = random.randrange(0, 359)
    font_size = random.randint(1, 20)
    font_type = font_types[random.randint(0, 4)]
    data_type = grouping(text)


    return text, axis_X, axis_Y, rotation, font_size, font_type, data_type


print(eng_or_rus('ABEHINV.'))

