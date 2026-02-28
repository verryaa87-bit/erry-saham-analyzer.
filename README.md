import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="CVMF Saham Checker - Verry", layout="wide")
st.title("Hybrid CAN-VCP Momentum Filter (CVMF) untuk Saham IDX/US")
st.markdown("**Input satu ticker** (contoh: BUMI.JK atau AAPL). Chart mungkin kosong karena yfinance issue .JK – cek manual di Yahoo/TradingView.")

ticker = st.text_input("Ticker Saham", "BUMI.JK").strip().upper()

if ticker:
    with st.spinner("Coba load data..."):
        try:
            data = yf.download(ticker, period="1y", progress=False)
            if data.empty:
                st.warning(f"Data kosong untuk {ticker}. Yahoo mungkin lagi rewel (khusus .JK sering).")
                st.info(f"Cek manual chart di: https://finance.yahoo.com/quote/{ticker}/chart")
                st.info("Coba ticker US seperti AAPL atau NVDA untuk test.")
            else:
                st.success(f"Data OK! {len(data)} hari tersedia.")
                st.subheader(f"Chart Harga & SMA - {ticker}")
                fig = go.Figure()
                fig.add_trace(go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'], name='Candlestick'))
                fig.add_trace(go.Scatter(x=data.index, y=data['Close'].rolling(10).mean(), name='10 SMA', line=dict(color='lime', width=2)))
                fig.add_trace(go.Scatter(x=data.index, y=data['Close'].rolling(20).mean(), name='20 SMA', line=dict(color='red', width=2)))
                st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Error: {e}. Coba refresh atau ticker lain. Issue yfinance umum untuk IDX.")

# Checklist tetap (kode slider & checkbox sama seperti sebelumnya, copy dari app lama kalau perlu)
st.subheader("Checklist CVMF (Manual)")
# ... paste kode checklist di sini dari versi sebelumnya ...
# Hitung score & tampil hasil
**Update Feb 2026**: yfinance sering gagal load data .JK (IDX) karena issue Yahoo API (data stuck atau empty). Ini umum, bukan bug app. Solusi: Cek chart manual di Yahoo Finance, TradingView, atau Stockbit. Ticker US (AAPL, NVDA) biasanya OK untuk test.
