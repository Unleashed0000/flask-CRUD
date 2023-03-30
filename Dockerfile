FROM python:3.10.9

WORKDIR /

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "flasky.py"]

EXPOSE 80