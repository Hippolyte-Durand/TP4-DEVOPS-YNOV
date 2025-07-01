# Utilise une image Python officielle
FROM python:3.11-slim

# Définir le dossier de travail
WORKDIR /app

# Copier le code source dans l'image
COPY . .

# Installer pylint et unittest (via pip si besoin)
RUN pip install --no-cache-dir pylint

# Commande exécutée quand un conteneur est lancé
CMD ["python", "-m", "unittest", "SimpleMath.py"]