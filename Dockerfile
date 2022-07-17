FROM idock.daumkakao.io/chappie/python:3.10.4

ARG WORKERS=1
ARG THREADS=1

ENV APP_HOME=/app
WORKDIR $APP_HOME
RUN mkdir -p $APP_HOME

COPY . $APP_HOME

RUN pip install -r ./requirements.txt

## env
ENV PROFILE=dev
ENV WORKERS_NUM ${WORKERS}
ENV THREADS_NUM ${THREADS}
#ENV PYTHONPATH=$PYTHONPATH:.

EXPOSE 8080

RUN chmod +x docker-entry.sh
ENTRYPOINT ["./docker-entry.sh"]