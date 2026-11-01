# Actividad 7 Servicio de consulta bursátil

Estudiante: Julián Fernando Bravo Parra  
Código: 2503120

Servicio básico desarrollado con Python y Flask. La ruta `/` consulta datos de GOOGL desde el 1 de enero de 2020 mediante `yfinance` y devuelve una tabla HTML.

## Archivos

- `app.py`: servicio Flask que escucha en el puerto 5000.
- `read_value_yf.py`: consulta bursátil y ejecución por terminal, con GOOGL por defecto y cálculo del promedio de Close.
- `Dockerfile`: construcción de la imagen del servicio.
- `requirements.txt`: dependencias y versiones utilizadas.
- `.dockerignore`: exclusiones del contexto de construcción.

## Ejecutar con Docker

Desde la carpeta que contiene el Dockerfile:

```bash
docker build -t stock-market:2.0 .
docker run --rm -p 5000:5000 stock-market:2.0
```

Abrir `http://localhost:5000/` en el navegador.

## Despliegue realizado

La imagen `julianbravoparra/stock-market:2.0` se publicó en Docker Hub y se ejecutó en una instancia Ubuntu de AWS EC2 con el mapeo `80:5000`. El servicio se verificó mediante la IP y el DNS públicos. Las capturas de la demostración se presentan en el documento Word de la entrega.

La instancia se terminó después de guardar las evidencias, conforme al cierre del taller.
