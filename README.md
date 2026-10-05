# 🤖 BONK Trading Agent

An experimental algorithmic trading agent for **BONK/USDT**, developed in Python and designed to run, among other environments, on **Android using Termux**.

> ⚠️ **Experimental project — simulation only**
>
> This project is not financial advice. Cryptocurrency trading involves a significant risk of capital loss. Public versions of this project are intended for experimentation, backtesting, and simulation.

---

## 🎯 Project Objective

The objective of **BONK Trading Agent** is to explore the possibility of automating a short-term trading strategy on the:

```text
BONK/USDT
```

The agent periodically retrieves market data, applies predefined trading strategies, and simulates trades in order to evaluate performance before any potential connection to a live trading account.

The project is progressively developed with a focus on:

* simulation;
* risk management;
* trade tracking;
* strategy comparison;
* simple operation on Android/Termux.

---

## 📱 Environment

The project can run in **Termux on Android**.

### Technologies

* Python 3
* Requests
* KuCoin public API
* CSV trade history
* Termux / Android
* Git / GitHub

---

## 📊 How It Works

The agent periodically queries the market to retrieve the BONK price.

Example public endpoint:

```text
/api/v1/market/orderbook/level1
```

for:

```text
BONK-USDT
```

The current simulation monitoring interval is:

```text
120 seconds
```

which means approximately one market analysis every **2 minutes**.

---

## 💰 Simulation Parameters

The parameters used in V6 are:

| Parameter                    |       Value |
| ---------------------------- | ----------: |
| Initial capital per strategy |    100 USDT |
| Simulated trade size         |     20 USDT |
| Simulated trading fee        |       0.10% |
| Entry threshold              |      +0.10% |
| Monitoring interval          | 120 seconds |
| Market                       |   BONK/USDT |

---

## 📈 Strategy Comparison

V6 compares several **Take Profit / Stop Loss** configurations.

### Strategy A

```text
Take Profit : +0.5%
Stop Loss   : -2%
```

### Strategy B

```text
Take Profit : +1%
Stop Loss   : -3%
```

### Strategy C

```text
Take Profit : +2%
Stop Loss   : -5%
```

The purpose is to compare different risk/reward configurations instead of relying on a single strategy.

---

## 🧪 Simulation Results

A recent simulation produced the following results:

| Strategy            | Trades | Wins | Losses | Win Rate |          P/L |
| ------------------- | -----: | ---: | -----: | -------: | -----------: |
| A — TP 0.5% / SL 2% |     43 |   34 |      9 |    79.1% | +1.6786 USDT |
| B — TP 1% / SL 3%   |     24 |   18 |      6 |    75.0% | +0.8735 USDT |
| C — TP 2% / SL 5%   |     10 |    8 |      2 |    80.0% | +2.0186 USDT |

### Simulated Final Capital

```text
A : 101.6786 USDT
B : 100.8735 USDT
C : 102.0186 USDT
```

> These results are based on simulation and do not guarantee future performance in live trading.

---

## 🗂️ Trade History

Simulated trades can be stored in a CSV file for further analysis.

Example:

```text
bonk_historique_v6.csv
```

The data can be used to analyze:

* number of trades;
* winning and losing trades;
* win rate;
* profit/loss;
* capital evolution;
* performance by time period;
* strategy comparison.

---

## 🔐 API Security

**Never publish API credentials on GitHub.**

Never include the following in the repository:

```text
API_KEY
API_SECRET
API_PASSPHRASE
TELEGRAM_TOKEN
```

Use environment variables instead:

```bash
export KUCOIN_API_KEY='...'
export KUCOIN_API_SECRET='...'
export KUCOIN_API_PASSPHRASE='...'
```

Sensitive files and credentials should be added to `.gitignore`.

---

## 📁 Recommended Project Structure

```text
bonk-trading-agent/
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── src/
│   └── bonk_agent.py
│
├── config/
│   └── config.example.py
│
├── data/
│   └── .gitkeep
│
└── docs/
    └── strategy.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/USERNAME/bonk-trading-agent.git
cd bonk-trading-agent
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the simulation:

```bash
python src/bonk_agent.py
```

---

## 🧪 Simulation Mode

The project should be tested in simulation before being used with a live trading account.

Simulation mode allows the agent to:

1. retrieve market data;
2. detect entry conditions;
3. simulate a buy;
4. monitor Take Profit / Stop Loss;
5. simulate a sell;
6. record the result;
7. update virtual capital.

---

## 🔮 Roadmap

Future versions may include:

* [ ] Improved signal detection
* [ ] Technical indicators
* [ ] Historical backtesting
* [ ] Dynamic risk management
* [ ] Automatic comparison of multiple strategies
* [ ] Performance dashboard
* [ ] Telegram notifications
* [ ] Improved logging
* [ ] Secure connection to the KuCoin private API
* [ ] Paper trading mode
* [ ] Optional live trading with explicit user confirmation

---

## ⚠️ Disclaimer

This software is provided for **educational and experimental purposes only**.

Simulation results do not guarantee future performance under real-market conditions.

Cryptocurrencies are highly volatile assets. A strategy that performs well during one market period may become unprofitable under different market conditions.

The user is solely responsible for their trading decisions and for how this software is used.

---

## 👨‍💻 Project

**BONK Trading Agent**

A personal research and experimentation project focused on algorithmic cryptocurrency trading.

Developed with:

```text
Python + Termux + KuCoin API
```

---

## 📜 License

This project may be distributed under the **MIT License**.

See the `LICENSE` file for the complete license terms.
