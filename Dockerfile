FROM python:3

RUN pip3 install flask
RUN pip3 install redis
RUN pip3 install pymongo

COPY *.py /

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

#EXPOSE 8080

ENTRYPOINT ["python3", "controller.py"]
