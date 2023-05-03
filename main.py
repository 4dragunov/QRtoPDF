import qrcode
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
import tempfile
import os

import config


def create_qr_code(url):
    # Создаем QR-код с заданными настройками
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=40,
        border=0,
    )
    qr.add_data(url)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white")


def create_qr_code_pdf_page(url, template_pdf_page):
    # Создаем QR-код для заданной ссылки
    qr_code_image = create_qr_code(url)

    # Сохраняем QR-код во временный файл
    temp_image_file = tempfile.NamedTemporaryFile(delete=False)
    temp_image_file_name = temp_image_file.name
    qr_code_image.save(temp_image_file_name)
    temp_image_file.close()

    # Создаем временный PDF-файл с QR-кодом
    temp_pdf_buffer = BytesIO()
    c = canvas.Canvas(temp_pdf_buffer, pagesize=letter)
    c.drawImage(temp_image_file_name, x=config.qr_position_x, y=config.qr_position_y, width=config.qr_width,
                height=config.qr_height)
    c.showPage()
    c.save()

    # Удаляем временный файл изображения
    os.unlink(temp_image_file_name)

    # Возвращаем страницу с QR-кодом из временного PDF-файла,
    # объединенную с макетом
    temp_pdf_buffer.seek(0)
    qr_code_page = PdfReader(temp_pdf_buffer).pages[0]
    template_pdf_page.merge_page(qr_code_page)

    return template_pdf_page


def insert_qr_codes_to_pdf(input_pdf_path, output_pdf_path, urls):
    # Читаем исходный PDF-файл с макетом
    pdf_reader = PdfReader(input_pdf_path)
    template_pdf_page = pdf_reader.pages[0]

    # Создаем объект PdfWriter для записи нового PDF-файла
    pdf_writer = PdfWriter()

    # Обходим список ссылок и создаем страницу с QR-кодом для каждой ссылки
    for url in urls:
        page_with_qr = create_qr_code_pdf_page(url, template_pdf_page)
        pdf_writer.add_page(page_with_qr)

    # Сохраняем новый PDF-файл с QR-кодами
    with open(output_pdf_path, "wb") as output_pdf_file:
        pdf_writer.write(output_pdf_file)


def read_urls_from_file(file_path):
    # Читаем список ссылок из файла
    with open(file_path, "r") as f:
        urls = [url.strip() for url in f.readlines()]
    return urls


if __name__ == "__main__":
    # Читаем список ссылок из файла url.txt
    urls = read_urls_from_file(config.urls_file_path)
    # Вставляем QR-коды в PDF-файл и сохраняем результат
    insert_qr_codes_to_pdf(config.input_pdf_path, config.output_pdf_path, urls)
