import requests
import json
import deepl 


def translate_yandex(rus_text):
    """Яндекс перевод"""
    if rus_text == '':
        return ''
    IAM_TOKEN = "t1.9euelZqLiseenJWRzMqKmMuXxpaPku3rnpWax56Qzc-Nx5ueksfHic2Ty53l9PdyA1VT-e8qXGGc3fT3MjJSU_nvKlxhnM3n9euelZqNi8mXj4-Rz52UyMiQm5TLiu_8xeuelZqNi8mXj4-Rz52UyMiQm5TLig.owRRfOfKJoLuLSF_XmhooIt_t26_cUjgA5IRX_qDI8LIS6hgiYe_2b7zBHFkRI9jt0R5l-1HEPTkiuKiyGL_Cg"
    folder_id = "b1gvu7iq6bjdf7jn5e6o"
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

