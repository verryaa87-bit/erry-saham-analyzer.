
# CVMF Saham Checker - Hybrid CAN SLIM + VCP Analyzer

App web sederhana untuk analisis saham IDX/US pakai strategi hybrid **CAN SLIM** (William O'Neil) + **VCP/SMA Trend Filter** (Mark Minervini style).  
Cocok buat swing/position trading di bull market, fokus momentum growth stocks.

![App Screenshot](https://via.placeholder.com/800x400?text=App+Screenshot+Contoh)  
*(Ganti link gambar ini nanti kalau kamu upload screenshot app ke repo)*

## Fitur Utama
- Chart candlestick + 10 SMA (hijau) & 20 SMA (merah) dari yfinance.
- Checklist manual CVMF: EPS growth, Annual growth, Relative Strength, Market uptrend, Harga respect SMA, Pola VCP.
- Score otomatis: Strong Buy (5-6/6), Watchlist (3-4/6), Skip (<3/6).
- Timeframe: Daily (1 tahun data).

## Cara Pakai
1. Buka app live: [Link App Kamu](https://erry-saham-analyzer-jabntzeeuwfruakacrez.streamlit.app) *(ganti dengan link real app kamu)*
2. Masukkan ticker (contoh: `BUMI.JK` untuk IDX, atau `AAPL` untuk US).
3. Lihat chart (kalau load, kalau kosong cek Yahoo Finance manual karena yfinance kadang delay).
4. Geser slider & centang checklist sesuai data real saham (dari Stockbit/Investing.com/Yahoo).
5. Lihat hasil score & keputusan trading.

**Catatan**: Chart mungkin kosong karena issue yfinance untuk .JK stocks (umum di 2025-2026). Cek manual chart di https://finance.yahoo.com/quote/[TICKER]/chart atau TradingView.

## Cara Install/Run Lokal (Opsional)
```bash
git clone https://github.com/verryaa87-bit/er ry-saham-analyzer.git
cd er ry-saham-analyzer
pip install -r requirements.txt
streamlit run app.py
