FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY req.txt /app/
RUN pip install --upgrade pip && \
    pip install -r req.txt

COPY nginx/nginx.conf /etc/nginx/conf.d/

COPY . /app/


EXPOSE 8003

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8003", "my_site.wsgi:application"]