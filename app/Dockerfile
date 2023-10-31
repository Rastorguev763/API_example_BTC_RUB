# Используйте официальный образ Python в качестве базового образа
FROM python:3.12

# Установите рабочую директорию в контейнере
WORKDIR /app

# Копируйте зависимости проекта в контейнер
COPY /app/requirements.txt .

# Обновите pip до последней версии
RUN pip install --upgrade pip

# Установите зависимости
RUN pip install -r requirements.txt

# Копируйте остальные файлы проекта в контейнер
COPY . .

# Добавляем wait-for-it.sh
COPY wait-for-it.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/wait-for-it.sh

# Ожидание доступности базы данных
CMD ["wait-for-it.sh", "db:5432", "--", "python", "app/main.py"]