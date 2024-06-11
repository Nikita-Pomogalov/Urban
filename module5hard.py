import time

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = time_now
        self.adult_mode = bool(adult_mode)

class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)

class UrTube:
    def __init__(self, users=[], videos=[], current_user=None):
        self.users = users
        self.videos = videos
        self.current = current_user

    def log_in(self, login, password):
        for user in self.users:
            if login == user[0]:
                if str(hash(password)) == hash(user[1]):
                    self.current = login
                print(f'Текущий пользователь {login}')

    def register(self, nickname, password, age):
        if self.users == []:
            self.users.append([nickname, password, age])
            self.current = nickname
            print('Поздравляем с регистрацией!')
        else:
            for user in self.users:
                if nickname == user[0]:
                    print(f'Пользователь {nickname} уже существует')
                    break
                else:
                    self.users.append([nickname, password, age])
                    print('Поздравляем с регистрацией!')
                    self.current = nickname
                    break
        # print(self.current)

    def log_out(self):
        self.current = None
        print('Выход... ')

    def add(self, *videos):
        for video in videos:
            if not any(existing_video.title == video.title for existing_video in self.videos):
                self.videos.append(video)
            else:
                print(f'Такое видео "{video.title}" уже есть')

    def get_videos(self, word):
        correct_videos = []
        for video in self.videos:
            if str(word.casefold()) in str(video.title.casefold()):
                correct_videos.append(video.title)
            else:
                continue
        return correct_videos

    def watch_video(self, film):
        if self.current == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for video in self.videos:
                if film == video.title:
                    for user in self.users:
                        if self.current == user[0]:
                            if video.adult_mode is True and user[2] < 18:
                                print("Вам нет 18 лет, пожалуйста покиньте страницу")
                            else:
                                timer = 0
                                while video.duration > video.time_now:
                                    timer += 1
                                    print(timer)
                                    time.sleep(1)
                                    video.duration -= 1
                                print('Конец видео')








ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
