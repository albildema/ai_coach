"""
╔══════════════════════════════════════════════════════════════╗
║  ENDURANCE DIGITAL TWIN — AI Coaching Platform              ║
║  Powered by Google Gemini · Built with Streamlit            ║
╚══════════════════════════════════════════════════════════════╝
"""

import streamlit as st
import time
import base64
from pathlib import Path

# ──────────────────────────────────────────────────────────────
# PAGE CONFIG
# ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Endurance Digital Twin",
    page_icon="🏊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────────────────────
# ELITE DARK MODE CSS — "MBH Bank" Aesthetic
# ──────────────────────────────────────────────────────────────
DARK_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

    :root {
        --bg-primary: #0A0A0F;
        --bg-secondary: #12121A;
        --bg-card: #16161F;
        --bg-hover: #1C1C28;
        --border: #1E1E2E;
        --border-glow: #00E5CC22;
        --accent: #00E5CC;
        --accent-dim: #00E5CC88;
        --accent-glow: #00E5CC33;
        --text-primary: #E8E8ED;
        --text-secondary: #8888A0;
        --text-muted: #55556A;
        --danger: #FF4D6A;
        --warning: #FFB84D;
        --success: #00E5CC;
        --gradient-1: linear-gradient(135deg, #00E5CC 0%, #007AFF 100%);
        --gradient-2: linear-gradient(135deg, #0A0A0F 0%, #16161F 100%);
        --radius: 16px;
        --radius-sm: 10px;
        --shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        --shadow-glow: 0 0 40px rgba(0, 229, 204, 0.08);
    }

    /* ── Global Reset ── */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"],
    [data-testid="stToolbar"], header, .main .block-container {
        background-color: var(--bg-primary) !important;
        color: var(--text-primary) !important;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        color: var(--text-primary) !important;
    }

    [data-testid="stHeader"] {
        background: transparent !important;
        backdrop-filter: blur(20px);
        border-bottom: 1px solid var(--border);
    }

    [data-testid="stToolbar"] { display: none !important; }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background: var(--bg-secondary) !important;
        border-right: 1px solid var(--border) !important;
    }

    [data-testid="stSidebar"] [data-testid="stMarkdown"] p,
    [data-testid="stSidebar"] [data-testid="stMarkdown"] h1,
    [data-testid="stSidebar"] [data-testid="stMarkdown"] h2,
    [data-testid="stSidebar"] [data-testid="stMarkdown"] h3,
    [data-testid="stSidebar"] label {
        color: var(--text-primary) !important;
    }

    [data-testid="stSidebar"] .stSelectbox > div > div,
    [data-testid="stSidebar"] .stTextInput > div > div > input {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
        color: var(--text-primary) !important;
        font-family: 'Inter', sans-serif !important;
    }

    [data-testid="stSidebar"] .stTextInput > div > div > input:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 2px var(--accent-glow) !important;
    }

    /* ── Chat Messages ── */
    [data-testid="stChatMessage"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius) !important;
        padding: 1.2rem 1.5rem !important;
        margin-bottom: 1rem !important;
        box-shadow: var(--shadow) !important;
        transition: all 0.3s ease !important;
    }

    [data-testid="stChatMessage"]:hover {
        border-color: var(--border-glow) !important;
        box-shadow: var(--shadow-glow) !important;
    }

    [data-testid="stChatMessage"] p,
    [data-testid="stChatMessage"] li,
    [data-testid="stChatMessage"] span {
        color: var(--text-primary) !important;
        font-size: 0.95rem !important;
        line-height: 1.7 !important;
    }

    [data-testid="stChatMessage"] strong {
        color: var(--accent) !important;
    }

    [data-testid="stChatMessage"] h1,
    [data-testid="stChatMessage"] h2,
    [data-testid="stChatMessage"] h3 {
        color: var(--accent) !important;
        font-weight: 600 !important;
    }

    [data-testid="stChatMessage"] code {
        background: var(--bg-primary) !important;
        color: var(--accent) !important;
        border: 1px solid var(--border) !important;
        border-radius: 6px !important;
        padding: 2px 8px !important;
        font-family: 'JetBrains Mono', monospace !important;
    }

    [data-testid="stChatMessage"] pre {
        background: var(--bg-primary) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
        padding: 1rem !important;
    }

    /* ── Chat Input & Bottom Area ── */
    [data-testid="stChatInput"],
    [data-testid="stBottom"],
    [data-testid="stBottomBlockContainer"],
    [data-testid="stChatFloatingInputContainer"],
    .stChatFloatingInputContainer,
    [class*="stBottom"],
    [class*="bottom-container"],
    .block-container,
    div[data-testid="stBottom"] > div,
    div[data-testid="stBottom"] > div > div,
    div[data-testid="stBottom"] > div > div > div,
    div[data-testid="stBottom"] > div > div > div > div,
    section[data-testid="stBottom"],
    footer,
    .appview-container > section,
    .stApp > div,
    .stApp > div > div,
    .main > div,
    .main > div > div,
    .main > div > div > div {
        background: var(--bg-primary) !important;
        background-color: var(--bg-primary) !important;
    }

    /* Remove all borders from the floating chat container */
    [data-testid="stBottom"] > div > div > div {
        border: none !important;
        background: var(--bg-primary) !important;
        padding: 0 !important;
    }

    [data-testid="stChatInput"] {
        border: none !important;
    }

    [data-testid="stChatInput"] textarea {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius) !important;
        color: var(--text-primary) !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.95rem !important;
        padding: 0.8rem 1.2rem !important;
    }

    [data-testid="stChatInput"] textarea:focus {
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 2px var(--accent-glow) !important;
    }

    [data-testid="stChatInput"] button {
        background: var(--accent) !important;
        border: none !important;
        border-radius: var(--radius-sm) !important;
        color: var(--bg-primary) !important;
    }

    [data-testid="stChatInput"] button:hover {
        opacity: 0.85 !important;
    }

    /* ── Nuclear: force ALL remaining elements dark ── */
    iframe, .stException, .stAlert,
    .element-container, .stMarkdown,
    div[data-testid] {
        background-color: transparent !important;
    }

    /* Explicit override for white bottom gap */
    .main .block-container {
        background: var(--bg-primary) !important;
        padding-bottom: 80px !important;
    }

    [data-testid="stAppViewContainer"] > div:last-child,
    [data-testid="stAppViewContainer"] > section {
        background: var(--bg-primary) !important;
        background-color: var(--bg-primary) !important;
    }

    /* ── Buttons ── */
    .stButton > button {
        background: var(--gradient-1) !important;
        color: var(--bg-primary) !important;
        border: none !important;
        border-radius: var(--radius-sm) !important;
        font-weight: 600 !important;
        font-family: 'Inter', sans-serif !important;
        padding: 0.6rem 1.5rem !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        font-size: 0.8rem !important;
    }

    .stButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 8px 25px var(--accent-glow) !important;
    }

    /* ── Dividers & Misc ── */
    hr {
        border-color: var(--border) !important;
        opacity: 0.5 !important;
    }

    [data-testid="stMarkdown"] a {
        color: var(--accent) !important;
    }

    /* ── Selectbox dropdown ── */
    [data-testid="stSidebar"] div[data-baseweb="select"] > div {
        background: var(--bg-card) !important;
        border-color: var(--border) !important;
    }

    div[data-baseweb="popover"] {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
    }

    div[data-baseweb="popover"] li {
        background: var(--bg-card) !important;
        color: var(--text-primary) !important;
    }

    div[data-baseweb="popover"] li:hover {
        background: var(--bg-hover) !important;
    }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: var(--bg-primary); }
    ::-webkit-scrollbar-thumb {
        background: var(--border);
        border-radius: 3px;
    }
    ::-webkit-scrollbar-thumb:hover { background: var(--accent-dim); }

    /* ── Hero Section ── */
    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: var(--accent-glow);
        border: 1px solid var(--accent-dim);
        border-radius: 100px;
        padding: 6px 18px;
        font-size: 0.75rem;
        font-weight: 600;
        color: var(--accent);
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 16px;
    }

    .hero-title {
        font-size: 2.4rem;
        font-weight: 700;
        line-height: 1.15;
        background: var(--gradient-1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 8px;
    }

    .hero-sub {
        font-size: 1rem;
        color: var(--text-secondary);
        line-height: 1.6;
        margin-bottom: 20px;
    }

    /* ── Status indicator ── */
    .status-dot {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: var(--success);
        margin-right: 8px;
        animation: pulse-dot 2s infinite;
    }

    @keyframes pulse-dot {
        0%, 100% { opacity: 1; box-shadow: 0 0 0 0 var(--accent-glow); }
        50% { opacity: 0.7; box-shadow: 0 0 0 6px transparent; }
    }

    /* ── Sidebar sport cards ── */
    .sport-indicator {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius-sm);
        padding: 12px 16px;
        margin: 8px 0;
        text-align: center;
        font-weight: 600;
        color: var(--accent);
        font-size: 0.9rem;
        letter-spacing: 0.5px;
    }

    /* ── Warning / Info boxes ── */
    .info-box {
        background: var(--bg-card);
        border-left: 3px solid var(--accent);
        border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
        padding: 12px 16px;
        margin: 12px 0;
        font-size: 0.85rem;
        color: var(--text-secondary);
        line-height: 1.6;
    }

    .warning-box {
        background: #1a1510;
        border-left: 3px solid var(--warning);
        border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
        padding: 12px 16px;
        margin: 12px 0;
        font-size: 0.85rem;
        color: var(--warning);
    }

    /* ── Footer ── */
    .footer {
        text-align: center;
        padding: 20px 0;
        color: var(--text-muted);
        font-size: 0.75rem;
        border-top: 1px solid var(--border);
        margin-top: 40px;
        letter-spacing: 0.5px;
    }
</style>
"""

st.markdown(DARK_CSS, unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────
# SYSTEM PROMPT — Digital Twin Filosofia Completa
# ──────────────────────────────────────────────────────────────
def get_system_prompt(sport: str) -> str:
    sport_context = {
        "Triathlon": "L'utente si sta allenando per il Triathlon (Nuoto + Bici + Corsa). Gestisci le tre discipline con le opportune transizioni e brick session.",
        "Corsa": "L'utente si concentra esclusivamente sulla Corsa. Elimina i riferimenti a nuoto e bici e rialloca il volume totale sulla corsa, mantenendo la filosofia 80/20 e LT1.",
        "Bici": "L'utente si concentra esclusivamente sul Ciclismo. Elimina i riferimenti a nuoto e corsa e rialloca il volume totale sulla bici, mantenendo la filosofia 80/20 e LT1.",
    }

    return f"""
Sei il "Digital Twin" di un atleta di Triathlon d'élite. Il tuo compito è tradurre una metodologia World-Tour in programmi sostenibili, sicuri e scientifici per amatori di ogni livello
