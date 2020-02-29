import smtplib
import ssl

port = 465  # For SSL
password = ''  # Local password

# Create a secure SSL context
context = ssl.create_default_context()

# Сколько должно быть коробок в конкретном здании
enough_boxes = {1: 8,
                2: 7
                3: 6}
# По каким зданиям уже отправлено письмо
notified = {1: False,
            2: False,
            3: False}
# Костыль, чтобы знать, какое здание
buildings = {1: 'Кронверкский',
             2: 'Биржевая',
             3: 'Ломоносова'}
sender_email = ''
company_email = ''


def notify(boxes, building_id: int) -> None:
    building = buildings[building_id]
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        # Получить расположение всех полных коробок в текущем здании
        places = []
        for box in boxes:
            location = db.session.query(Place).filter(Place.place_id == box.place_id).first()
            places.append([location.floor, location.otdel])
        message = f'''
Subject: Контейнеры готовы к вывозу


В корпусе университета ИТМО по адресу {building} заполнено достаточно контейнеров.
Полные контейнеры располагаются в {places}.
        '''
        server.login(local_email, password)
        server.sendmail(sender_email, company_email, message)
    notified[building_id] = True
