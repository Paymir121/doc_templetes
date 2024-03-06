import requests
import json
import deepl
import os
from dotenv import load_dotenv

load_dotenv()


def translate_yandex(rus_text):
    """Яндекс перевод"""
    if rus_text == '':
        return ''
    IAM_TOKEN = os.getenv('IAM_TOKEN')
    folder_id = os.getenv('folder_id')
    target_language = 'en'
    texts = [rus_text]

    body = {
        "targetLanguageCode": target_language,
        "texts": texts,
        "folderId": folder_id,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(IAM_TOKEN)
    }

    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                             json=body,
                             headers=headers
                             )
    data = json.loads(response.text)
    # print(data)
    print(data["translations"][0]["text"])
    return data["translations"][0]["text"]


def translate_deeple(rus_text):
    """Перевод Deeple"""
    auth_key = 'kek'
    target_language = 'RU-EN'
    text = [rus_text]
    translator = deepl.Translator(auth_key)
    result = translator.translate_text(text, target_lang=target_language) 
    print(result.text)


def translate(rus_text):
    translate = 'yandex'
    # translate = 'deeple'

    if translate == 'deeple':   
        return translate_deeple(rus_text)
    
    if translate == 'yandex':
        return translate_yandex(rus_text)

### Для Теста
translate("первый человек")
