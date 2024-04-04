FROM python:3.12.2
LABEL author="Andrii Semekha"

WORKDIR = /usr/andrii_semekha/bdd_web_chrome

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements/common.txt

CMD ["pytest", "tests/"]
