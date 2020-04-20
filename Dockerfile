FROM python:3.6

RUN mkdir -p usr/src/file_service/

WORKDIR /usr/src/file_service/

COPY . /usr/src/file_service

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "run.py"]
