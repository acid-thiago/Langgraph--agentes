# Imagem base Python
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia o requirements.txt
COPY requirements.txt .

# Atualiza pip e instala dependências
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia todo o código
COPY . .

# Expõe a porta 8000
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



