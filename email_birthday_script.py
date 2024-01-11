from plyer import notification
import datetime as dt
import pandas as pd
import smtplib
import random


def _send_email(name, age, email, letter_id):
    sender_mail = 'EMAIL'
    password = 'PASSWORD'
    with open(f'resources/letter_{letter_id}.txt', encoding='UTF-8') as letter:
        letter = letter.read().replace('[NAME]',name).replace('[AGE]',age)
        with smtplib.SMTP("smtp.gmail.com") as smtp:
            smtp.starttls()
            smtp.login(user=sender_mail,
                       password=password)
            smtp.sendmail(from_addr=sender_mail,
                          to_addrs=email,
                          msg=f"Subject:Happy birthday\n\n{letter}".encode('UTF-8'))


def _get_letter_id(black_list):
    letter_id = random.randint(1, 5)
    while letter_id in black_list:
        letter_id = random.randint(1, 5)
        if len(black_list) >= 5:
            break
    return letter_id


def email_birthday_script():
    time = dt.datetime.now()
    current_date_segments = str(time.date()).split('-')
    current_date_segments = current_date_segments[::-1]

    data = pd.read_csv(f'resources\\birthdays.csv').copy()

    for date in data['Birthday date']:
        birthday_date_segments = date.split('-')
        if (current_date_segments[1] == birthday_date_segments[1]
                and current_date_segments[0] == birthday_date_segments[0]):
            row_data = data.loc[data['Birthday date'] == date].copy()
            age = str(int(current_date_segments[2]) - int(birthday_date_segments[2]))
            name = row_data['Name'].tolist()[0]
            email = row_data['Email'].tolist()[0]
            id_list = row_data['Letters sent(id)'].tolist()[0]
            mail_sent_today = row_data['Sent today'].tolist()[0]

            if pd.isna(id_list) or len(id_list) == 5:
                id_list = []
            else:
                id_list = [int(char) for char in id_list if char in range(1, 5)]
            letter_id = _get_letter_id(id_list)
            if mail_sent_today == 'N':
                _send_email(name=name,
                            age=age,
                            email=email,
                            letter_id=letter_id)
                id_list.append(letter_id)
                data.at[data.index[data['Birthday date'] == date][0], 'Letters sent(id)'] = id_list
                data.at[data.index[data['Birthday date'] == date][0], 'Sent today'] = 'Y'
                data.to_csv(path_or_buf='resources/birthdays.csv',
                            index=False)
                notification.notify(title='BirthdayPlanner',
                                    message=f'Email has been sent to {name}',
                                    app_icon=None,
                                    timeout=10)
            else:
                notification.notify(title='BirthdayPlanner',
                                    message=f'Email has been sent today already {name}',
                                    app_icon=None,
                                    timeout=10)
        else:
            data.at[data.index[data['Birthday date'] == date][0], 'Sent today'] = 'N'


if __name__ == '__main__':
    email_birthday_script()
