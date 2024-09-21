FROM python:3.12-slim

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

COPY dependencies.txt /usr/src/dependencies.txt
RUN pip install -r /usr/src/dependencies.txt

COPY stat_analysis.py /usr/src/stat_analysis.py
