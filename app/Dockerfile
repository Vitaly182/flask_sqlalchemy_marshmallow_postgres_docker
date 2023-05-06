FROM python:3.9

WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip && python -m pip install -r requirements.txt

COPY . /app

EXPOSE 5000

COPY ./entrypoint.sh /app

RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]