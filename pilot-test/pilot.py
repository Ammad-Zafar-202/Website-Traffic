import streamlit as st
import requests
import random
import pandas as pd

ips = ["24.48.0.1", "8.8.8.8", "132.239.1.5", "128.101.101.101", "1.1.1.1"]

def estimate_age(ip):
    return random.choice(["18‑25","26‑35","36‑50","50+"])

def get_geo(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        return r.json()
    except:
        return {}

data = []
for ip in ips:
    geo = get_geo(ip)
    data.append({
        "ip": ip,
        "country": geo.get("country", "Unknown"),
        "region": geo.get("regionName", "Unknown"),
        "age": estimate_age(ip)
    })

df = pd.DataFrame(data)
st.title("Website Traffic Pilot Dashboard")
st.write(df)

st.bar_chart(df['country'].value_counts())
st.bar_chart(df['age'].value_counts())
