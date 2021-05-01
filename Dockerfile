FROM python:3

COPY requirements.txt requirements.txt
COPY models/ models/
COPY src/ src/

RUN pip install -r requirements.txt

CMD streamlit run src/app.py