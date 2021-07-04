# pull official base image
FROM python:3.9.5

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV DB_BACKEND=django.db.backends.postgresql
ENV DB_HOST=127.0.0.1
ENV DB_PORT=5432
ENV DB_NAME=firebase_test
ENV DB_USER=admin
ENV DB_PASS=admin

RUN pip install --upgrade pip && pip install --upgrade setuptools

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

RUN chmod +x wait-for-it.sh

ENTRYPOINT ["./wait-for-it.sh", "-s" , "-t", "20", "database:5432", "--"]

CMD bash -c "python3 manage.py collectstatic --no-input && \
python3 manage.py makemigrations && \
python3 manage.py migrate && \
python3 manage.py runserver"
