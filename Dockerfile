# Use a Python base image
FROM python:3.12.1

# устанавливаем переменную окружения для Python, чтобы вывод был более читабельным
ENV PYTHONUNBUFFERED 1

# устанавливаем рабочую директорию в /app
WORKDIR /app

# копируем файл requirements.txt в рабочую директорию
COPY requirements.txt /app/

# устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# копируем текущий каталог в рабочую директорию
COPY . /app/

# опционально: выполняем миграции и собираем статику Django
# RUN python manage.py migrate
# RUN python manage.py collectstatic --noinput

# открываем порт 8000 для веб-сервера Django
EXPOSE 8000

# команда для запуска сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]