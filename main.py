import glob
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
    print("<----------------------Погнали----------------------------------->")
    docs_files = glob.glob('*.docx')
    for file_name in docs_files:
        print(f"<----------------------Делаем красиво с  {file_name}----------------------------------->")
        doc = DocxTemplate(file_name)
        doc.render(context)
        doc.save('filled_'+file_name)
        print(f"<----------------------Сделано красиво с  {file_name}----------------------------------->")

    print("<----------------------Конец----------------------------------->")

if __name__ == '__main__':
    context = read_context()
    render_word_file(context)