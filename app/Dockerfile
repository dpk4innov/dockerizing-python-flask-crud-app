FROM python:3.6
EXPOSE 5000
WORKDIR /app
COPY templates /app/templates
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY app.py /app
CMD python3 app.py
