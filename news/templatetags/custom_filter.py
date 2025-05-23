from django import template
import re
from bs4 import BeautifulSoup, NavigableString

register = template.Library()

BAN_WORDS = ['редиска', 'дурак', 'грубиян']

@register.filter(name='censor')
def censor(value):
    if not isinstance(value, str):
        raise TypeError("Фильтр 'censor' можно применять только к строкам.")

    def replace_bad_word(match):
        word = match.group()
        return word[0] + '*' * (len(word) - 1)

    # функция для обработки текста без тегов
    def censor_text(text):
        for word in BAN_WORDS:
            pattern = rf'(?i)\b{re.escape(word)}\b'
            text = re.sub(pattern, replace_bad_word, text)
        return text

    soup = BeautifulSoup(value, 'html.parser')

    for elem in soup.find_all(text=True):
        if isinstance(elem, NavigableString):
            censored = censor_text(str(elem))
            elem.replace_with(censored)

    return str(soup)
