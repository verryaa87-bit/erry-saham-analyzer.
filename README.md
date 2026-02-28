import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

st.title("Hybrid CAN-VCP Stock Checker (IDX/US)")

ticker = st.text_input("Masukkan Ticker (contoh: BIPI.JK atau MPIX.JK)", "BIPI.JK")

if ticker:
    data = yf.download(ticker, period="1y")
    if data.empty:
        st.error("Data tidak ditemukan. Coba ticker lain (tambah .JK untuk IDX).")
    else:
        st.subheader("Harga & Chart")
        fig = go.Figure()
        fig.add_trace(go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'], name='Price'))
        fig.add_trace(go.Scatter(x=data.index, y=data['Close'].rolling(10).mean(), name='10 SMA', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=data.index, y=data['Close'].rolling(20).mean(), name='20 SMA', line=dict(color='red')))
        st.plotly_chart(fig)

        # Simple CAN SLIM check (manual input atau approx)
        st.subheader("Checklist Sederhana CAN-VCP")
        col1, col2 = st.columns(2)
        with col1:
            eps_growth = st.slider("EPS Growth Q/Q (%)", -50, 100, 25)
            annual_growth = st.slider("Annual EPS Growth (%)", 0, 100, 25)
        with col2:
            sma_respect = st.checkbox("Harga > 10 & 20 SMA?")
            vcp_tight = st.checkbox("Ada pola VCP (kontraksi pullback makin kecil)?")
        
        score = 0
        if eps_growth >= 25: score += 1
        if annual_growth >= 25: score += 1
        if sma_respect: score += 1
        if vcp_tight: score += 1
        
        if score >= 3:
            st.success(f"Score: {score}/4 → Potential Buy! (Watch breakout)")
        else:
            st.warning(f"Score: {score}/4 → Watch dulu atau skip")
