# Utiliser une image Python minimale
FROM python:3.11-slim

# Installer Flask
RUN pip install flask

# Copier le fichier app.py dans l'image
COPY app.py /app/app.py
WORKDIR /app

# Expose le port 3000 pour Flask
EXPOSE 3000

# Commande par dfaut
CMD ["python", "app.py"]

