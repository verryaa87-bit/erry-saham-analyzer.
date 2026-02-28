import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="CVMF Saham Checker - Verry", layout="wide")
st.title("Hybrid CAN-VCP Momentum Filter (CVMF) untuk Saham IDX/US")
st.markdown("Masukkan ticker saham (contoh: BIPI.JK, MPIX.JK, BBCA.JK) lalu cek setup CAN SLIM + VCP/SMA.")

ticker = st.text_input("Ticker Saham (tambah .JK untuk IDX)", "BIPI.JK")

if ticker:
    with st.spinner("Loading data..."):
        data = yf.download(ticker, period="1y", progress=False)
    
    if data.empty:
        st.error("Data tidak ditemukan. Coba ticker lain atau cek koneksi.")
    else:
        st.subheader(f"Chart Harga & SMA - {ticker}")
        fig = go.Figure()
        fig.add_trace(go.Candlestick(x=data.index,
                                     open=data['Open'], high=data['High'],
                                     low=data['Low'], close=data['Close'],
                                     name='Candlestick'))
        fig.add_trace(go.Scatter(x=data.index, y=data['Close'].rolling(window=10).mean(),
                                 name='10 SMA', line=dict(color='lime', width=2)))
        fig.add_trace(go.Scatter(x=data.index, y=data['Close'].rolling(window=20).mean(),
                                 name='20 SMA', line=dict(color='red', width=2)))
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Checklist CVMF")
        col1, col2 = st.columns(2)
        with col1:
            eps_q = st.slider("EPS Growth Q/Q (%)", -100, 200, 25)
            eps_annual = st.slider("Annual EPS Growth (%)", 0, 100, 25)
            leader = st.slider("Relative Strength (%)", 0, 100, 80)
        with col2:
            market_up = st.checkbox("Pasar lagi Uptrend?", value=True)
            sma_respect = st.checkbox("Harga > 10 & 20 SMA?", value=True)
            vcp_yes = st.checkbox("Ada pola VCP?", value=False)
        
        score = 0
        if eps_q >= 25: score += 1
        if eps_annual >= 25: score += 1
        if leader >= 80: score += 1
        if market_up: score += 1
        if sma_respect: score += 1
        if vcp_yes: score += 1
        
        st.subheader("Hasil Akhir")
        if score >= 5:
            st.success(f"Score: {score}/6 → Strong Buy / Entry Ideal! 🚀")
        elif score >= 3:
            st.info(f"Score: {score}/6 → Watchlist / Potential")
        else:
            st.warning(f"Score: {score}/6 → Skip dulu")
