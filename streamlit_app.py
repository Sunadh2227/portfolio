from streamlit_lottie import st_lottie
import requests
import streamlit as st

st.set_page_config(page_title="Ganji Venkata Sunadh | Portfolio", layout="wide")

# Load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load your avatar animation
lottie_avatar = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_cg3v6a.json")

# --- Custom CSS ---
st.markdown("""
    <style>
    /* Sidebar background */
    [data-testid="stSidebar"] {
        background: linear-gradient(to right, #f7f8fc, #dde9f7);
        padding-top: 2rem;
    }

    /* Main background */
    .stApp {
        background: linear-gradient(to right, #f7f8fc, #dde9f7);
        color: #000000;
    }

    /* Custom radio buttons in sidebar */
    div[data-testid="stSidebar"] .stRadio > div {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    div[data-testid="stSidebar"] .stRadio > div > label {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 12px 20px;
        font-weight: 600;
        color: #000000;
        box-shadow: 0 4px 10px rgba(30, 60, 114, 0.1);
        transition: all 0.3s ease-in-out;
        cursor: pointer;
        border: 2px solid transparent;
    }

    div[data-testid="stSidebar"] .stRadio > div > label:hover {
        background-color: #e3f2fd;
        transform: scale(1.03);
        box-shadow: 0 6px 14px rgba(21, 101, 192, 0.2);
    }

    div[data-testid="stSidebar"] .stRadio > div > label[data-selected="true"] {
        background-color: #1e88e5;
        color: #f0f0f0;
        border: 2px solid #1565c0;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
with st.sidebar:
    if lottie_avatar:
        st_lottie(lottie_avatar, height=150, key="avatar")
    st.title("🚀 Navigation")
    selection = st.radio("Go to", ["🏠 About Me", "💼 Projects", "🛠️ Skills", "📬 Contact"])

# --- Main Page Content ---
if selection == "🏠 About Me":
    st.title("👋 About Me")
    st.markdown("""
    Hi, I'm **Ganji Venkata Sunadh**, a passionate **Data Scientist** with expertise in **Python** and **Machine Learning**.

    I specialize in extracting insights from data to support smarter decision-making and building predictive models that solve real-world problems.

    I’m currently seeking opportunities where I can contribute my technical skills and curiosity to build impactful solutions.
    """)
    st.markdown("📄 [Download My Resume](link_to_resume.pdf)")

elif selection == "💼 Projects":
    st.title("💼 Projects")
    st.subheader("⚡ Smart Energy Meter with IoT-Based Billing System")
    with st.expander("🎯 Objective"):
        st.write("To design a smart energy meter that measures electricity consumption in real-time and sends data to a cloud server.")
    with st.expander("🧠 Project Overview"):
        st.write("Microcontroller-based meter with IoT. Data sent to cloud for monitoring, billing, and alerts.")
    with st.expander("🔧 Key Components"):
        st.markdown("- ESP32 / Arduino\n- CT Sensor\n- ThingSpeak / Firebase\n- Cloud DB\n- LCD / OLED\n- Power Supply")
    with st.expander("📱 Features"):
        st.markdown("- Real-time monitoring\n- Billing\n- Alerts\n- Dashboard\n- Optional prepaid mode")
    with st.expander("✅ Skills Applied"):
        st.markdown("- Embedded C/Python\n- IoT integration\n- Cloud APIs\n- Data visualization")

elif selection == "🛠️ Skills":
    st.title("🛠️ Skills")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🧠 Programming")
        st.markdown("- Python\n- NumPy, pandas, matplotlib, sklearn")
        st.subheader("📊 Analysis")
        st.markdown("- Cleaning\n- EDA\n- Feature engineering")
        st.subheader("📈 ML")
        st.markdown("- Classification\n- Clustering\n- Model tuning")
    with col2:
        st.subheader("💻 Tools & DB")
        st.markdown("- SQL\n- Firebase\n- MySQL")
        st.subheader("☁️ Platforms")
        st.markdown("- Jupyter\n- GitHub\n- AWS")
        st.subheader("📂 Visualization")
        st.markdown("- seaborn\n- plotly\n- Tableau/Power BI")

elif selection == "📬 Contact":
    st.title("📬 Contact Me")
    st.markdown("""
    <div style='background-color:#f0f2f6;padding:20px;border-radius:10px'>
        <p><strong>📧 Email:</strong> sunadhganji22@gmail.com</p>
        <p><strong>👨‍💻 GitHub:</strong> <a href="https://github.com/Sunadh2227" target="_blank">Sunadh2227</a></p>
        <p><strong>🔗 LinkedIn:</strong> <a href="https://linkedin.com/in/sunadh-g-828378367" target="_blank">sunadh-g</a></p>
    </div>
    """, unsafe_allow_html=True)
