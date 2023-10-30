import glob
import re

from docxtpl import DocxTemplate
from openpyxl import load_workbook


def read_context():
    wb = load_workbook('./context.xlsx')
    ws = wb['Sheet1']
    context = {}
    for row in ws.iter_rows(min_row=2, max_col=3):
        name = row[1].value
        data = row[2].value
        context[name] = data
    return context

def render_word_file(context):
    docs_files = glob.glob('*.docx') # Читаем все имена файлов *.docx
    for file_name in docs_files:
        if re.search(r'filled_', file_name) is None:
            print(f"<----------------------Делаем красиво с  {file_name}----------------------------------->")
            doc = DocxTemplate(file_name) # Читаем файл
            doc.render(context) # Производим замену name на data
            doc.save('filled_'+file_name) # Сохраняем файл с именем filled_{file_name}
            print(f"<----------------------Сделано красиво с  {file_name}---------------------------------->")


if __name__ == '__main__':
    print("<----------------------Погнали----------------------------------->")
    context = read_context()
    render_word_file(context)
    print("<----------------------Конец-------------------------------------->")