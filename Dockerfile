FROM python:3.13.5

WORKDIR /slotmachine

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

CMD  ["python3", "./main/slotmachine.py"]