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

    /* ── Sidebar toggle button (collapse/expand arrow) ── */
    [data-testid="stSidebar"] button[kind="header"],
    [data-testid="collapsedControl"],
    [data-testid="stSidebarCollapsedControl"],
    button[data-testid="stSidebarCollapsedControl"],
    .stSidebar button,
    [data-testid="stSidebar"] [data-testid="stBaseButton-header"],
    [data-testid="collapsedControl"] > div,
    [data-testid="collapsedControl"] svg {
        color: var(--accent) !important;
        fill: var(--accent) !important;
        background: var(--bg-secondary) !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
        opacity: 1 !important;
        visibility: visible !important;
    }

    [data-testid="collapsedControl"] {
        background: var(--bg-secondary) !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
    }

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
Sei il "Digital Twin" di un atleta di Triathlon d'élite. Il tuo compito è tradurre una metodologia World-Tour in programmi sostenibili, sicuri e scientifici per amatori di ogni livello.

CONTESTO SPORT ATTIVO: {sport_context.get(sport, sport_context["Triathlon"])}

═══════════════════════════════════════════════
1. FILOSOFIA TECNICA (Core d'Élite)
═══════════════════════════════════════════════
• Distribuzione Intensità: 80% Bassa Intensità (Z1/Z2), 20% Alta Qualità.
• Soglia Aerobica (LT1): Pilastro fondamentale per l'efficienza. Utilizza intervalli lunghi (15'-20') a intensità moderata.
• Periodizzazione: Cicli 3:1 (Carico/Scarico). Se l'utente è un "Master" (>45 anni), valuta autonomamente il passaggio a un ciclo 2:1 se segnala recupero lento.

═══════════════════════════════════════════════
2. SEGMENTAZIONE UTENTE (Archetipi)
═══════════════════════════════════════════════
• Performance: Punta al PB o alla qualifica (Kona/70.3 Worlds). Volume 10-15h. Accetta carichi densi.
• Finisher: Obiettivo completare la gara con piacere. Volume 7-10h. Priorità assoluta alla costanza e alla prevenzione infortuni.
• Soglia Minima: Se l'utente ha <7h/settimana, avvisalo che il metodo verrà semplificato per mantenere almeno la salute cardiovascolare, ma le prestazioni d'élite richiedono più tempo.

═══════════════════════════════════════════════
3. TECNOLOGIA E INPUT (Agnoticismo dei Dati)
═══════════════════════════════════════════════
• Dual-Coding: Scrivi sempre i lavori con due parametri (es: Watt e RPE, o Passo e Frequenza Cardiaca). Se l'utente non ha sensori, usa solo la scala RPE (1-10).
• Zwift/Rulli: Per ogni sessione bici, fornisci una descrizione testuale chiara per il "Build Workouts" di Zwift (es: 10' Warm-up @50% FTP, 3x15' @80% FTP).

═══════════════════════════════════════════════
4. LOGICA DI ADATTAMENTO "VITA REALE"
═══════════════════════════════════════════════
• Stress-Sync: Chiedi sempre il livello di stress lavorativo. Se Stress > 8/10, trasforma la sessione "Soglia" in "Z2 Easy".
• Missed Session: Se l'utente salta un allenamento, NON raddoppiare mai il giorno dopo. Elimina la sessione persa e riparti dal programma originale.
• Injury Prevention: Se l'utente segnala fastidi a tendini o articolazioni, blocca la corsa per 48h e sostituiscila con nuoto o bici agile (senza carico).

═══════════════════════════════════════════════
5. TONO E OUTPUT
═══════════════════════════════════════════════
• Stile: Professionale, diretto, da atleta professionista che parla a un pari-grado amatore. No fronzoli, molta sostanza.
• Struttura Risposta:
  **🎯 Focus del giorno:** (es. "Oggi costruiamo la tua base aerobica").
  **🏋️ Allenamento:** (Dettagliato con Zone, Watt/Pace e RPE).
  **💡 Il Consiglio del Pro:** (Un trucco tecnico su nutrizione, idrodinamica o posizione in sella).
  **📋 Check-out:** "Com'è andata? Fammi sapere le tue sensazioni e il tuo battito a riposo domani mattina."

═══════════════════════════════════════════════
6. GESTIONE PSICOLOGICA ED EGODYNAMICS
═══════════════════════════════════════════════
• Trattamento "Pro-Am": Rivolgiti all'utente con il rispetto che si deve a un atleta dedicato. Non sminuire mai i suoi obiettivi, ma usa la tua autorità tecnica per proteggerlo dal sovrallenamento.
• La Scienza come Freno: Quando l'utente vuole spingere più del previsto, non dire solo "no". Spiega la fisiologia: "Spingere oggi interferirebbe con l'adattamento mitocondriale cercato nella sessione di ieri". Gli amatori rispettano la scienza.
• Validazione Post-Sessione: Dopo ogni allenamento di qualità, fornisci un feedback che celebri la disciplina, non solo la velocità.
• Gestione del "Senso di Colpa": Se l'atleta salta una sessione, usa un tono rassicurante ma razionale. Spiega che la consistenza a lungo termine batte la singola sessione perfetta.
• Monitoraggio dei Segnali Deboli: Se l'utente usa parole come "frustrato", "stanco morto" o "deluso", attiva immediatamente il protocollo di scarico preventivo, anche se i dati numerici sembrano ancora buoni.

═══════════════════════════════════════════════
7. GESTIONE EDUCATIVA E TUTORING
═══════════════════════════════════════════════
• Fase di Onboarding (Livello di Conoscenza): Al primo contatto assoluto, prima di generare tabelle, chiedi all'utente: "Per assicurarmi di parlare la tua stessa lingua, quanto ti senti esperto di metrica dell'allenamento? (A. Principiante: spiegami tutto / B. Intermedio: conosco le basi / C. Avanzato: vai dritto al punto tecnico)".
• Spiegazioni "Just-in-Time": Se l'utente è A o B, ogni volta che introduci termini come FTP, RPE, Z2 o VO2 Max, aggiungi una brevissima spiegazione tra parentesi o un'analogia.
• Trigger Video "Elite Insights": Quando il piano prevede lavori tecnici, cita sempre l'esistenza di un supporto video.
• Verifica Costante: Al termine di ogni spiegazione complessa, chiedi: "È tutto chiaro su come impostare il tuo orologio/ciclocomputer per questo lavoro o vuoi che ti aiuti a farlo?".
• Focus sulle Sensazioni: Ricorda all'amatore che i numeri sono importanti, ma imparare ad ascoltare il proprio corpo (RPE) è ciò che lo renderà un atleta migliore nel lungo periodo.

═══════════════════════════════════════════════
8. COERENZA HARDWARE E TARGETING
═══════════════════════════════════════════════
• Priorità Metriche: Se l'utente dichiara di NON avere un misuratore di potenza, NON fornire riferimenti primari in Watt/FTP. Fornisci i target in Frequenza Cardiaca (BPM) e RPE.
• Reality Check Obiettivi: Se un utente principiante dichiara obiettivi estremi con poco tempo, intervieni con autorità tecnica.
• Formattazione Garmin/Training: Presenta sempre il cuore della sessione in un blocco pulito chiamato "SCHEMA PER OROLOGIO", strutturato per fasi (Riscaldamento, Lavoro, Defaticamento).
• Universalità Endurance: Il focus attuale è {sport}.

═══════════════════════════════════════════════
ONBOARDING AUTOMATICO
═══════════════════════════════════════════════
Se questa è la PRIMA interazione in assoluto con l'utente (cioè l'utente manda il suo PRIMO messaggio), IGNORA qualsiasi richiesta specifica e procedi ESCLUSIVAMENTE con le domande di profilazione seguenti, in un unico messaggio strutturato e accogliente:

1. "Benvenuto, atleta. Sono il tuo Digital Twin — il tuo coach personale basato su metodologia World-Tour. Prima di iniziare, ho bisogno di conoscerti."
2. "**Livello di conoscenza tecnica:** A) Principiante, B) Intermedio, C) Avanzato"
3. "**Qual è il tuo obiettivo principale?** (es. prima gara, migliorare il PB, completare un Ironman...)"
4. "**Quante ore settimanali puoi dedicare all'allenamento?**"
5. "**Livello di stress lavorativo attuale (1-10)?**"
6. "**Hardware disponibile:** Hai un misuratore di potenza? Un cardiofrequenzimetro? Quale orologio/ciclocomputer usi?"
7. "**Età e anni di esperienza nello sport?**"
8. "**Hai infortuni o fastidi cronici attuali?**"

Chiudi con: "Rispondi pure in un unico messaggio o punto per punto — costruiremo il tuo piano su queste fondamenta."

DOPO l'onboarding, nelle interazioni successive, rispondi normalmente seguendo tutte le regole sopra.
"""


# ──────────────────────────────────────────────────────────────
# SESSION STATE INITIALIZATION
# ──────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "api_key_set" not in st.session_state:
    st.session_state.api_key_set = False
if "model" not in st.session_state:
    st.session_state.model = None
if "sport" not in st.session_state:
    st.session_state.sport = "Triathlon"
if "onboarding_done" not in st.session_state:
    st.session_state.onboarding_done = False


# ──────────────────────────────────────────────────────────────
# SIDEBAR
# ──────────────────────────────────────────────────────────────
with st.sidebar:
    # Logo
    logo_path = Path(__file__).parent / "assets" / "logo.png"
    if logo_path.exists():
        logo_data = base64.b64encode(logo_path.read_bytes()).decode()
        st.markdown(
            f"""
            <div style="text-align:center; padding: 20px 0 10px 0;">
                <img src="data:image/png;base64,{logo_data}"
                     style="width:120px; border-radius:20px; box-shadow: 0 0 40px rgba(0,229,204,0.15);" />
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div style="text-align:center; margin-bottom:24px;">
            <div class="hero-badge">⚡ AI COACHING</div>
            <h2 style="margin:0; font-size:1.3rem; font-weight:700; color:#E8E8ED;">
                Endurance Digital Twin
            </h2>
            <p style="margin:4px 0 0 0; font-size:0.78rem; color:#8888A0;">
                Metodologia World-Tour per Amatori
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # ── API Key ──
    st.markdown(
        '<p style="font-size:0.8rem; font-weight:600; color:#8888A0; letter-spacing:1px; text-transform:uppercase; margin-bottom:4px;">🔑 Google API Key</p>',
        unsafe_allow_html=True,
    )
    api_key = st.text_input(
        "API Key",
        type="password",
        placeholder="Inserisci la tua Google API Key...",
        label_visibility="collapsed",
        key="api_key_input",
    )

    if api_key:
        try:
            import google.generativeai as genai

            # Only reconfigure if key changed
            if st.session_state.get("_last_api_key") != api_key:
                genai.configure(api_key=api_key)
                st.session_state._last_api_key = api_key
                st.session_state.model = genai.GenerativeModel(
                    "gemini-1.5-flash",
                    system_instruction=get_system_prompt(st.session_state.sport),
                )
                st.session_state.chat_session = st.session_state.model.start_chat(history=[])

            st.session_state.api_key_set = True
            st.markdown(
                '<div class="info-box"><span class="status-dot"></span> API connessa con successo</div>',
                unsafe_allow_html=True,
            )
        except Exception as e:
            st.session_state.api_key_set = False
            st.markdown(
                f'<div class="warning-box">⚠️ Errore API: {str(e)[:80]}</div>',
                unsafe_allow_html=True,
            )
    else:
        st.markdown(
            '<div class="info-box">Inserisci la tua Google API Key per iniziare.<br><a href="https://aistudio.google.com/apikey" target="_blank" style="color:#00E5CC;">Ottieni una chiave gratuita →</a></div>',
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # ── Sport Selector ──
    st.markdown(
        '<p style="font-size:0.8rem; font-weight:600; color:#8888A0; letter-spacing:1px; text-transform:uppercase; margin-bottom:4px;">🏆 Disciplina</p>',
        unsafe_allow_html=True,
    )

    sport_icons = {"Triathlon": "🏊🚴🏃", "Corsa": "🏃", "Bici": "🚴"}

    sport = st.selectbox(
        "Sport",
        ["Triathlon", "Corsa", "Bici"],
        label_visibility="collapsed",
        key="sport_selector",
    )

    if sport != st.session_state.sport:
        st.session_state.sport = sport
        # Rebuild model with new sport context
        if st.session_state.api_key_set and api_key:
            try:
                import google.generativeai as genai

                genai.configure(api_key=api_key)
                st.session_state.model = genai.GenerativeModel(
                    "gemini-1.5-flash",
                    system_instruction=get_system_prompt(sport),
                )
                st.session_state.chat_session = st.session_state.model.start_chat(history=[])
                st.session_state._last_api_key = api_key
            except Exception:
                pass

    st.markdown(
        f'<div class="sport-indicator">{sport_icons.get(sport, "🏊")} {sport.upper()}</div>',
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # ── Session Stats ──
    n_msgs = len(
        [m for m in st.session_state.messages if m["role"] == "user"]
    )
    st.markdown(
        f"""
        <div style="padding:12px; background:#16161F; border-radius:10px; border:1px solid #1E1E2E;">
            <p style="font-size:0.7rem; color:#8888A0; text-transform:uppercase; letter-spacing:1px; margin:0 0 8px 0;">📊 Sessione Attuale</p>
            <p style="font-size:0.85rem; color:#E8E8ED; margin:4px 0;">Messaggi: <strong style="color:#00E5CC;">{n_msgs}</strong></p>
            <p style="font-size:0.85rem; color:#E8E8ED; margin:4px 0;">Sport: <strong style="color:#00E5CC;">{sport}</strong></p>
            <p style="font-size:0.85rem; color:#E8E8ED; margin:4px 0;">Onboarding: <strong style="color:{'#00E5CC' if st.session_state.onboarding_done else '#FFB84D'};">{'✓ Completo' if st.session_state.onboarding_done else '⏳ In attesa'}</strong></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # ── Reset Button ──
    if st.button("🔄  Nuova Sessione", use_container_width=True):
        st.session_state.messages = []
        st.session_state.onboarding_done = False
        st.rerun()

    # ── Footer ──
    st.markdown(
        """
        <div class="footer">
            ENDURANCE DIGITAL TWIN v1.0<br>
            Powered by Google Gemini AI<br>
            © 2026 — All rights reserved
        </div>
        """,
        unsafe_allow_html=True,
    )


# ──────────────────────────────────────────────────────────────
# MAIN AREA — HEADER
# ──────────────────────────────────────────────────────────────
if not st.session_state.messages:
    st.markdown(
        """
        <div style="text-align:center; padding:60px 0 30px 0;">
            <div class="hero-badge">⚡ DIGITAL TWIN ENGINE</div>
            <div class="hero-title">Il Tuo Coach d'Élite.<br>Sempre con Te.</div>
            <p class="hero-sub">
                Metodologia World-Tour adattata al tuo stile di vita.<br>
                Allenamenti scientifici, adattamento in tempo reale, zero compromessi.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Feature cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div style="background:#16161F; border:1px solid #1E1E2E; border-radius:16px; padding:24px; text-align:center; min-height:180px;">
                <div style="font-size:2rem; margin-bottom:12px;">🧬</div>
                <h4 style="color:#00E5CC; margin:0 0 8px 0; font-size:0.95rem;">Periodizzazione Adattiva</h4>
                <p style="color:#8888A0; font-size:0.82rem; line-height:1.5; margin:0;">
                    Cicli 3:1 intelligenti con auto-regolazione per età e recupero. Il piano si adatta a te, non il contrario.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div style="background:#16161F; border:1px solid #1E1E2E; border-radius:16px; padding:24px; text-align:center; min-height:180px;">
                <div style="font-size:2rem; margin-bottom:12px;">🎯</div>
                <h4 style="color:#00E5CC; margin:0 0 8px 0; font-size:0.95rem;">Dual-Coding</h4>
                <p style="color:#8888A0; font-size:0.82rem; line-height:1.5; margin:0;">
                    Ogni sessione con doppio parametro: Watt+RPE o Passo+FC. Compatibile con qualsiasi hardware.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """
            <div style="background:#16161F; border:1px solid #1E1E2E; border-radius:16px; padding:24px; text-align:center; min-height:180px;">
                <div style="font-size:2rem; margin-bottom:12px;">🧠</div>
                <h4 style="color:#00E5CC; margin:0 0 8px 0; font-size:0.95rem;">Stress-Sync</h4>
                <p style="color:#8888A0; font-size:0.82rem; line-height:1.5; margin:0;">
                    Il coach monitora il tuo stress e adatta l'intensità. La vita reale viene prima dell'allenamento.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────
# CHAT DISPLAY — Render Existing Messages
# ──────────────────────────────────────────────────────────────
for message in st.session_state.messages:
    avatar = "🏊" if message["role"] == "assistant" else "🧑‍💻"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])


# ──────────────────────────────────────────────────────────────
# STREAMING HELPER
# ──────────────────────────────────────────────────────────────
def stream_response(text: str, speed: float = 0.008):
    """Simulate streaming by yielding characters progressively."""
    buffer = ""
    for char in text:
        buffer += char
        yield buffer
        time.sleep(speed)


# ──────────────────────────────────────────────────────────────
# CHAT INPUT & AI RESPONSE
# ──────────────────────────────────────────────────────────────
if prompt := st.chat_input(
    "Scrivi un messaggio al tuo coach...",
    key="chat_input",
):
    # ── Guard: API key check ──
    if not st.session_state.api_key_set:
        st.error(
            "⚠️ **Configura la tua Google API Key nella sidebar** per iniziare a parlare con il tuo Digital Twin."
        )
        st.stop()

    # ── Add user message ──
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(prompt)

    # ── Generate AI response ──
    with st.chat_message("assistant", avatar="🏊"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            # Build conversation history for context
            chat = st.session_state.chat_session

            # Check if this is the first user message (trigger onboarding)
            is_first_message = len([m for m in st.session_state.messages if m["role"] == "user"]) == 1

            if is_first_message and not st.session_state.onboarding_done:
                # Force onboarding regardless of what user says
                onboarding_trigger = (
                    f"[SISTEMA: Questo è il PRIMO messaggio dell'utente. "
                    f"DEVI procedere con l'onboarding completo come da istruzioni, "
                    f"ignorando la richiesta specifica. Il messaggio dell'utente era: \"{prompt}\"]"
                )
                response = chat.send_message(onboarding_trigger)
                st.session_state.onboarding_done = True
            else:
                response = chat.send_message(prompt)

            full_response = response.text

            # Streaming effect
            displayed = ""
            for i, char in enumerate(full_response):
                displayed += char
                # Update every N chars for performance
                if i % 3 == 0 or i == len(full_response) - 1:
                    message_placeholder.markdown(displayed + "▌")
                    time.sleep(0.005)

            message_placeholder.markdown(full_response)

        except Exception as e:
            error_msg = str(e)

            if "quota" in error_msg.lower() or "429" in error_msg:
                full_response = (
                    "⚠️ **Limite API raggiunto**\n\n"
                    "Hai superato la quota di richieste per la tua API Key. "
                    "Attendi qualche minuto o verifica il tuo piano su "
                    "[Google AI Studio](https://aistudio.google.com/)."
                )
            elif "invalid" in error_msg.lower() or "401" in error_msg:
                full_response = (
                    "🔐 **API Key non valida**\n\n"
                    "La chiave inserita non è riconosciuta. Verifica di aver copiato "
                    "correttamente la tua Google API Key dalla "
                    "[console Google AI](https://aistudio.google.com/apikey)."
                )
            elif "safety" in error_msg.lower():
                full_response = (
                    "🛡️ **Filtro di sicurezza attivato**\n\n"
                    "La risposta è stata bloccata dai filtri di sicurezza di Google. "
                    "Prova a riformulare la tua domanda."
                )
            else:
                full_response = (
                    "❌ **Errore di comunicazione**\n\n"
                    "Non sono riuscito a contattare il servizio AI. "
                    "Verifica la tua connessione internet e riprova.\n\n"
                    f"*Dettaglio tecnico: `{error_msg[:120]}`*"
                )

            message_placeholder.markdown(full_response)

        # Save assistant response
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )
