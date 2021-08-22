import webbrowser

def review():
    review = input('ну как тебе?')
    positive_review = ['интересно', 'весело', 'смешно', 'мне очень понравилось', 'меня заинтересовало', 'увлекательно']
    negative_review = ['скучно', 'фигня']
    if review in positive_review:
        print('круто! мне тоже понравился новый выпуск!')
    elif review in negative_review:
        print('ты не шаришь....')

def new_video(link, name):
    video = input(f'Привет, ты видел новый выпуск {name}? (да,нет)')
    if video == 'да':
        review()
    elif video == 'нет':
        asd = input('Хочешь посмотреть?(да,нет?)')
        if asd == 'да':
            webbrowser.open(link)
            watch = input('Посмотрел? \n (да,нет)')
            if watch == 'да':
                review()

new_video(link='https://www.youtube.com/%27', name="хрень какая-то")


