import smtplib
import re
from openpyxl import load_workbook
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from NaverNewsCrawler import NaverNewsCrawler

keyword = input("Set the keyword: ")
crawler = NaverNewsCrawler(keyword)

fileName = input("Type the file name to save data: ")
crawler.get_news(fileName)

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
SMTP_USER = 'wjss5115@gmail.com'
SMTP_PASSWORD = 'secret-password-test-result-successful'

def send_mail(name, address, subject, contents, attachment=None):
    if not re.match('(^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', address):
        print('Wrong email')
        return

    message = MIMEMultipart('alternative')
    if attachment:
        message = MIMEMultipart('mixed')

    message['From'] = SMTP_USER
    message['To'] = address
    message['Subject'] = name + '님, ' + subject

    text = MIMEText(contents, _charset='utf-8')
    message.attach(text)

    if attachment:
        from email.mime.base import MIMEBase
        from email import encoders

        file_data = MIMEBase('application', 'octect-stream')
        file_data.set_payload(open(attachment, 'rb').read())
        encoders.encode_base64(file_data)

        import os
        filename = os.path.basename(attachment)
        file_data.add_header('Content-Disposition', 'attachment; filename="'+filename+'"')
        message.attach(file_data)
    
    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    smtp.sendmail(SMTP_USER, address,  message.as_string())
    smtp.close()

wb = load_workbook('email_list.xlsx')
data = wb.active

lineNum = 2
while (data['B' + str(lineNum)].value):
    send_mail(data['B' + str(lineNum)].value, data['C' + str(lineNum)].value, keyword + "에 관한 네이버 기사목록 엑셀 파일입니다.", "첨부파일을 참조해주세요", fileName)
    lineNum += 1
