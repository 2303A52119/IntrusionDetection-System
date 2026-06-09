import streamlit as st
import pandas as pd
import pickle

# Load model
with open("../models/random_forest.pkl", "rb") as f:
    model = pickle.load(f)

# Load label encoder
with open("../models/label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

# Load feature columns
with open("../models/feature_columns.pkl", "rb") as f:
    feature_columns = pickle.load(f)

st.title("Intrusion Detection System")

st.write("Random Forest Based IDS")

protocol_type = st.selectbox(
    "Protocol Type",
    ["tcp", "udp", "icmp"]
)

service = st.selectbox(
    "Service",
    [
        "http",
        "ftp_data",
        "private",
        "smtp",
        "telnet",
        "other"
    ]
)

flag = st.selectbox(
    "Flag",
    ["SF", "S0", "REJ", "RSTO"]
)

src_bytes = st.number_input(
    "Source Bytes",
    min_value=0
)

dst_bytes = st.number_input(
    "Destination Bytes",
    min_value=0
)

count = st.number_input(
    "Count",
    min_value=0
)

same_srv_rate = st.slider(
    "Same Service Rate",
    0.0,
    1.0,
    0.5
)

diff_srv_rate = st.slider(
    "Different Service Rate",
    0.0,
    1.0,
    0.5
)

if st.button("Predict"):

    input_df = pd.DataFrame(
        0,
        index=[0],
        columns=feature_columns
    )

    input_df["src_bytes"] = src_bytes
    input_df["dst_bytes"] = dst_bytes
    input_df["count"] = count
    input_df["same_srv_rate"] = same_srv_rate
    input_df["diff_srv_rate"] = diff_srv_rate

    input_df[f"protocol_type_{protocol_type}"] = 1

    if f"service_{service}" in input_df.columns:
        input_df[f"service_{service}"] = 1

    if f"flag_{flag}" in input_df.columns:
        input_df[f"flag_{flag}"] = 1

    prediction = model.predict(input_df)

    attack = label_encoder.inverse_transform(prediction)

    st.success(
        f"Predicted Attack Type: {attack[0]}"
    )