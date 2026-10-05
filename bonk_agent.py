import urllib.request,json,time,csv,os
from datetime import datetime

URL="https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BONK-USDT"
CAPITAL=100.0
TRADE=20.0
FEE=0.001
INTERVAL=120
ENTRY=0.001

S={
"A":{"tp":0.005,"sl":-0.02},
"B":{"tp":0.01,"sl":-0.03},
"C":{"tp":0.02,"sl":-0.05}
}

E={}
for k in S:
    E[k]={
        "cash":CAPITAL,
        "bonk":0,
        "buy":0,
        "cost":0,
        "trades":0,
        "wins":0,
        "losses":0,
        "real":0
    }

LOG=os.path.expanduser("~/bonk_historique_v6.csv")

if not os.path.exists(LOG):
    with open(LOG,"w",newline="") as f:
        csv.writer(f).writerow(
            ["date","strategy","action","price",
             "amount","cash","pnl","reason"]
        )

def price():
    with urllib.request.urlopen(URL,timeout=10) as r:
        d=json.loads(r.read().decode())
    return float(d["data"]["price"])

def log(k,action,p,q,cash,pnl,reason):
    with open(LOG,"a",newline="") as f:
        csv.writer(f).writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            k,action,f"{p:.10f}",f"{q:.2f}",
            f"{cash:.6f}",f"{pnl:.6f}",reason
        ])

print("="*60)
print("BONK AGENT V6 - COMPARAISON")
print("="*60)
print("A : TP +0.5% / SL -2%")
print("B : TP +1.0% / SL -3%")
print("C : TP +2.0% / SL -5%")
print("Capital : 100 USDT par strategie")
print("Trade   : 20 USDT")
print("Frais   : 0.10%")
print("Entree  : +0.10%")
print("Interval: 120 secondes")
print("MODE    : SIMULATION UNIQUEMENT")
print("="*60)

last=None
def run(k,p,old):
    e=E[k]
    cfg=S[k]

    if e["bonk"]==0:
        move=(p-old)/old

        if move>=ENTRY:
            fee=TRADE*FEE
            total=TRADE+fee

            if e["cash"]>=total:
                q=TRADE/p
                e["cash"]-=total
                e["bonk"]=q
                e["buy"]=p
                e["cost"]=total

                log(k,"BUY",p,q,e["cash"],0,"ENTRY")

                print(
                    f">>> {k} ACHAT | "
                    f"Prix {p:.10f} | "
                    f"BONK {q:.0f}"
                )
        return

    move=(p-e["buy"])/e["buy"]
    value=e["bonk"]*p

    reason=None

    if move>=cfg["tp"]:
        reason=f"TP +{cfg['tp']*100:.1f}%"

    elif move<=cfg["sl"]:
        reason=f"SL {cfg['sl']*100:.1f}%"

    if reason:

        sell_fee=value*FEE
        net=value-sell_fee
        pnl=net-e["cost"]

        e["cash"]+=net
        e["real"]+=pnl
        e["trades"]+=1

        if pnl>=0:
            e["wins"]+=1
        else:
            e["losses"]+=1

        log(
            k,"SELL",p,e["bonk"],
            e["cash"],pnl,reason
        )

        print()
        print(
            f">>> {k} VENTE | {reason} | "
            f"Variation {move*100:+.2f}% | "
            f"P/L {pnl:+.4f} USDT"
        )

        e["bonk"]=0
        e["buy"]=0
        e["cost"]=0


def summary(p):
    print()
    print("-"*78)
    print(f"BONK : {p:.10f} USDT")

    for k in S:
        e=E[k]
        value=e["cash"]+e["bonk"]*p
        pnl=value-CAPITAL

        if e["bonk"]:
            move=(p-e["buy"])/e["buy"]*100
            status=f"POSITION {move:+.2f}%"
        else:
            status="ATTENTE"

        print(
            f"{k} | "
            f"TP {S[k]['tp']*100:.1f}% "
            f"/ SL {abs(S[k]['sl'])*100:.1f}% | "
            f"Portefeuille {value:.3f} | "
            f"P/L {pnl:+.3f} | "
            f"Trades {e['trades']} | "
            f"{status}"
        )

    print("-"*78)


try:
    while True:

        try:
            p=price()

            if last is None:
                last=p
                print(
                    f"DEMARRAGE | BONK {p:.10f}"
                )
                time.sleep(INTERVAL)
                continue

            for k in S:
                run(k,p,last)

            summary(p)

            last=p
            time.sleep(INTERVAL)

        except Exception as err:
            print(f"Erreur : {err}")
            time.sleep(INTERVAL)

except KeyboardInterrupt:

    print()
    print("="*60)
    print("V6 ARRETEE")
    print("="*60)

    if last is not None:
        for k in S:
            e=E[k]
            value=e["cash"]+e["bonk"]*last
            pnl=value-CAPITAL

            if e["trades"]:
                winrate=e["wins"]/e["trades"]*100
            else:
                winrate=0

            print(
                f"{k} | "
                f"Portefeuille {value:.3f} | "
                f"P/L {pnl:+.3f} | "
                f"Trades {e['trades']} | "
                f"Gagnants {e['wins']} | "
                f"Perdants {e['losses']} | "
                f"Winrate {winrate:.1f}%"
            )

    print(f"Historique : {LOG}")

