FROM python:3.7
RUN pip install kubernetes
RUN pip install flask
COPY scheduler.py /scheduler.py
CMD python /scheduler.py
EXPOSE 3000
