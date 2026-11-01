# Estudiante: Julián Fernando Bravo Parra
# Código: 2503120
# Fecha de elaboración: 28/10/2026

FROM python:3.11.3-bullseye
WORKDIR /work
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python3", "app.py"]
