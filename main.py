import streamlit as st
import datetime
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
from PIL import Image
import sqlite3
from datetime import date
from io import BytesIO
import fitz  # PyMuPDF for PDF processing
import base64
import matplotlib.dates as mdates

import FWG_manual
import inventory_management
import troubleshooting
import FWG_operations
import rag

# 사이드바에서 페이지 선택
page = st.sidebar.selectbox(
    "페이지 선택",
    ("조수기 메뉴얼", "재고관리", "Trouble Shooting", "조수기 작업", "RAG")
)



# 선택된 페이지에 따라 해당 모듈 실행
if page == "조수기 메뉴얼":
    FWG_manual.app()
elif page == "재고관리":
    inventory_management.app()
elif page == "Trouble Shooting":
    troubleshooting.app()
elif page == "조수기 작업":
    FWG_operations.app()
elif page == "RAG":
    rag.app()

# PDF 파일 표시 함수
def show_pdf(file_data):
    base64_pdf = base64.b64encode(file_data).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# PDF 파일을 데이터베이스에서 불러와 보여주는 함수
def load_and_display_pdf_from_db(database_path, file_id):
    conn = sqlite3.connect(database_path)
    c = conn.cursor()
    c.execute('SELECT file_data FROM pdf_files WHERE id = ?', (file_id,))
    pdf_data = c.fetchone()[0]
    conn.close()

    show_pdf(pdf_data)