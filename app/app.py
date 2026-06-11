import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
# =========================
# LOAD MODEL
# =========================

model = joblib.load("../models/xgboost_ids.pkl")

label_encoder = joblib.load(
    "../models/label_encoder_xgb.pkl"
)

feature_columns = joblib.load(
    "../models/feature_columns_xgb.pkl"
)
feature_importance_df = pd.read_csv(
    "../reports/feature_importance.csv"
)
# =========================
# SESSION HISTORY
# =========================

if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# SIDEBAR
# =========================

st.sidebar.title("Project Information")

st.sidebar.info(
    """
    Intrusion Detection System

    Model: XGBoost

    Dataset: NSL-KDD

    Classes:
    - Normal
    - DoS
    - Probe
    - R2L
    - U2R
    """
)

# =========================
# PAGE
# =========================

st.title("🛡️ Intrusion Detection System")

st.write("XGBoost Based IDS")

# =========================
# MODEL STATS
# =========================

col1, col2, col3 = st.columns(3)

col1.metric(
    "Features",
    len(feature_columns)
)

col2.metric(
    "Classes",
    len(label_encoder.classes_)
)

col3.metric(
    "Model",
    "XGBoost"
)

st.divider()

# =========================
# INPUTS
# =========================

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

st.divider()

# =========================
# PREDICT
# =========================

if st.button("🔍 Predict Attack"):

    input_df = pd.DataFrame(
        0,
        index=[0],
        columns=feature_columns
    )

    if "src_bytes" in input_df.columns:
        input_df["src_bytes"] = src_bytes

    if "dst_bytes" in input_df.columns:
        input_df["dst_bytes"] = dst_bytes

    if "count" in input_df.columns:
        input_df["count"] = count

    if "same_srv_rate" in input_df.columns:
        input_df["same_srv_rate"] = same_srv_rate

    if "diff_srv_rate" in input_df.columns:
        input_df["diff_srv_rate"] = diff_srv_rate

    protocol_col = f"protocol_type_{protocol_type}"
    if protocol_col in input_df.columns:
        input_df[protocol_col] = 1

    service_col = f"service_{service}"
    if service_col in input_df.columns:
        input_df[service_col] = 1

    flag_col = f"flag_{flag}"
    if flag_col in input_df.columns:
        input_df[flag_col] = 1

    prediction = model.predict(input_df)

    attack = label_encoder.inverse_transform(prediction)

    try:
        confidence = (
            model.predict_proba(input_df).max()
            * 100
        )
    except:
        confidence = 0

    st.session_state.history.append(
        {
            "Prediction": attack[0],
            "Confidence (%)": round(confidence, 2)
        }
    )

    st.subheader("Prediction Result")

    if attack[0] == "Normal":
        st.success(
            f"✅ Predicted Attack Type: {attack[0]}"
        )
    else:
        st.error(
            f"⚠️ Predicted Attack Type: {attack[0]}"
        )

    st.info(
        f"📊 Confidence Score: {confidence:.2f}%"
    )

    st.progress(
        min(int(confidence), 100)
    )

    attack_info = {
        "Normal":
        "No threat detected.",

        "DoS":
        "Block suspicious IPs and monitor traffic spikes.",

        "Probe":
        "Monitor network scans and reconnaissance activity.",

        "R2L":
        "Review authentication logs and access control.",

        "U2R":
        "Immediately investigate privilege escalation attempts."
    }

    st.warning(
        attack_info.get(
            attack[0],
            "No recommendation available."
        )
    )

    st.subheader("Threat Severity")

    if attack[0] == "Normal":
        st.success("🟢 LOW RISK")

    elif attack[0] == "Probe":
        st.warning("🟡 MEDIUM RISK")

    elif attack[0] == "DoS":
        st.error("🔴 HIGH RISK")

    elif attack[0] == "R2L":
        st.error("🔴 HIGH RISK")

    elif attack[0] == "U2R":
        st.error("🚨 CRITICAL RISK")

st.divider()

# =========================
# HISTORY
# =========================

st.subheader("Prediction History")

if len(st.session_state.history) > 0:
    st.dataframe(
        pd.DataFrame(
            st.session_state.history
        )
    )
else:
    st.write(
        "No predictions made yet."
    )

st.divider()

st.subheader(
    "📈 Top Important Features"
)

top_features = (
    feature_importance_df
    .head(10)
)

fig = px.bar(
    top_features,
    x="Importance",
    y="Feature",
    orientation="h",
    title="Top 10 Important Features"
)

fig.update_layout(
    yaxis=dict(
        categoryorder="total ascending"
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.caption(
    "Built using XGBoost, Streamlit, and the NSL-KDD Dataset"
)