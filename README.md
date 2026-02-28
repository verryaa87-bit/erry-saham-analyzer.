# CVMF Saham Analyzer

App sederhana untuk analisis saham IDX/US pakai hybrid strategi **CAN SLIM** (William O'Neil) + **VCP + SMA** (Mark Minervini style).

Nama lengkap: **Hybrid CAN-VCP Momentum Filter (CVMF)**

## Fitur Utama
- Chart candlestick + 10 SMA (hijau) & 20 SMA (merah) dari yfinance
- Checklist manual untuk 6 kriteria CVMF (EPS growth, RS, market trend, VCP, dll.)
- Hitung score otomatis → Strong Buy / Watch / Skip
- Cocok untuk swing/position trading growth stocks

## Cara Pakai
1. Buka app live: [https://erry-saham-analyzer-xxx.streamlit.app](https://erry-saham-analyzer-jabntzeeuwfruakacrez.streamlit.app)  
   (ganti link dengan URL asli app kamu setelah deploy)
2. Masukkan **satu ticker** (contoh: `BUMI.JK`, `BBCA.JK`, `AAPL`)
3. Lihat chart (kalau load) + geser slider & centang checklist sesuai data real saham
4. Lihat hasil score di bawah → kalau 5-6/6 → setup kuat!

**Catatan**: Chart kadang kosong karena issue yfinance untuk ticker .JK (IDX). Cek manual di Yahoo Finance atau TradingView.

## Kriteria CVMF (Ringkasan)
| No | Kriteria              | Target Ideal          | Bobot |
|----|-----------------------|-----------------------|-------|
| 1  | EPS Growth Q/Q        | ≥25%                  | 1     |
| 2  | Annual EPS Growth     | ≥25%                  | 1     |
| 3  | Relative Strength     | ≥80%                  | 1     |
| 4  | Market Uptrend        | Ya                    | 1     |
| 5  | Harga > 10 & 20 SMA   | Ya                    | 1     |
| 6  | Ada Pola VCP          | Ya (kontraksi ketat)  | 1     |

Score 5-6 → **Strong Buy** 🚀  
Score 3-4 → **Watchlist**  
<3 → **Skip**
**Catatan Penting (Feb 2026)**  
- Chart harga & SMA kadang kosong / stuck karena library yfinance sedang bermasalah dengan ticker .JK (IDX). Ini issue umum, bukan bug app.  
- Solusi: Cek chart manual di Yahoo Finance, TradingView, atau Stockbit.  
- Ticker US (AAPL, NVDA, dll.) biasanya load normal untuk test.  
- Update app nanti kalau yfinance fix atau ganti library alternatif.
## Dibuat Dengan
- Python + Streamlit
- yfinance (data saham)
- Plotly (chart interaktif)

Dibuat oleh verry (Surabaya, Feb 2026) – untuk pribadi & eksperimen trading.

Happy analyzing saham, brow! 📈
