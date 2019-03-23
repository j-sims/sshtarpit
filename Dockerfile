FROM python:3.7.2-slim-stretch
ADD run.py /
EXPOSE 22
CMD ["python", "/run.py"]
