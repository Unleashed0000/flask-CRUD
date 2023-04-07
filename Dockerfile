FROM python:3.10.9

WORKDIR /

COPY . .

RUN pip install --no-cache-dir -r requirements_all.txt

CMD ["python", "flasky.py"]

EXPOSE 80