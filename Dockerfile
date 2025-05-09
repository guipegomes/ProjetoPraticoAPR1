FROM python:3 

WORKDIR /ProjetoPraticoAPR1

COPY . .

CMD ["python", "ProjetoPratico/index.py"]