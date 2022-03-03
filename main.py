import imaplib
import email
import smtplib

print("Cinar Sehreman")
print("Mail gonderme ve Gmail inbox kontrol")


while True:
    print(
        "---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("lutfen gmail hesabinizdan asagidaki linkteki daha az guvenli uygulama erisimini aciniz")
    print(
        "https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OQWUSa8LE4ina7cO2HSkmmw2BspYrX6I-LT_hkFhjtpIdTjHNUpc9py5TDlOFjfMRjioLIatn_MSlF3dkutNFeaXmYWg")
    print(
        "---------------------------------------------------------------------------------------------------------------------------------------------------------")
    host = 'imap.gmail.com'
    print("lutfen giris yapiniz")
    username = input("gmail hesabinizi yaziniz:")
    password = input("gmail hesabinizin sifresini yazin:")

    veri = input("mail gondermek icin 1 gelen kutunuza bakmak icin 2 yaziniz:")
    if veri == "1":
        print(
        "---------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("mail gondermeyi sectiniz")
        print(
        "---------------------------------------------------------------------------------------------------------------------------------------------------------")
        alici = input("mesaj gondermek istediginiz maili yazin:")

        mesaj = input("gondermek istediginiz mesaji yazin:")

        server = smtplib.SMTP("smtp.gmail.com", '587')
        server.ehlo()
        server.starttls()

        server.login(username, password)
        print("giriş başarılı")

        server.sendmail(username, alici, mesaj)
        print("gönderim tamamlandı")

    elif veri == "2":
        print(
        "---------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("gelen kutusuna bakmayi sectiniz")
        print(
        "---------------------------------------------------------------------------------------------------------------------------------------------------------")


        def get_inbox():
            mail = imaplib.IMAP4_SSL(host)
            mail.login(username, password)
            mail.select("inbox")
            _, search_data = mail.search(None, 'UNSEEN')
            my_message = []
            for num in search_data[0].split():
                email_data = {}
                _, data = mail.fetch(num, '(RFC822)')
                # print(data[0])
                _, b = data[0]
                email_message = email.message_from_bytes(b)
                for header in ['subject', 'to', 'from', 'date']:
                    print("{}: {}".format(header, email_message[header]))
                    email_data[header] = email_message[header]
                for part in email_message.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True)
                        email_data['body'] = body.decode()
                        print(body)
                        print('----------------------------------------------------------------------')
                    elif part.get_content_type() == "text/html":
                        html_body = part.get_payload(decode=True)
                        email_data['html_body'] = html_body.decode()
                my_message.append(email_data)
            return my_message


        if __name__ == "__main__":
            my_inbox = get_inbox()


