FROM amancevice/superset:latest
USER root
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir -p /app/superset_home && chown -R superset:superset /app/superset_home
COPY superset_config.py /app/pythonpath/
ENV PYTHONPATH="/app/pythonpath:${PYTHONPATH}"
USER superset
EXPOSE 8088
CMD ["superset", "run", "-h", "0.0.0.0", "-p", "8088"]
