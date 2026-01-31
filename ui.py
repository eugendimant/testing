import streamlit as st


def inject_styles():
    st.markdown(
        """
        <style>
            :root {
                color-scheme: dark;
            }
            body {
                background: radial-gradient(circle at top, #1b1b2f, #0b0b10 60%);
            }
            .main {
                background: radial-gradient(circle at top, #1b1b2f, #0b0b10 60%);
            }
            .neon-card {
                background: rgba(20, 20, 34, 0.9);
                padding: 1.2rem;
                border-radius: 16px;
                border: 1px solid rgba(255,255,255,0.08);
                box-shadow: 0 12px 30px rgba(0,0,0,0.45);
            }
            .hud {
                display: grid;
                grid-template-columns: repeat(2, minmax(0, 1fr));
                gap: 0.6rem;
                font-size: 0.85rem;
                color: #e6e6f2;
            }
            .hud span { color: #b9b9c8; }
            .log {
                background: rgba(10, 10, 18, 0.65);
                border-radius: 12px;
                padding: 0.8rem;
                max-height: 220px;
                overflow-y: auto;
                font-size: 0.85rem;
            }
            .log p {
                margin: 0 0 0.5rem 0;
            }
            .glow-button > button {
                background: linear-gradient(90deg, #e94560, #ff4d6d);
                border: none;
                color: white;
                font-weight: 600;
                border-radius: 10px;
            }
            .tone-pill {
                display: inline-block;
                background: rgba(255,255,255,0.08);
                border-radius: 999px;
                padding: 0.2rem 0.7rem;
                margin-right: 0.3rem;
                font-size: 0.75rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header(title, subtitle):
    st.markdown(
        f"""
        <div class="neon-card">
            <h1 style="margin:0; letter-spacing:0.08em;">{title}</h1>
            <p style="margin:0.4rem 0 0; color:#b9b9c8;">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_hud(gs):
    stats = gs["stats"]
    st.markdown(
        f"""
        <div class="neon-card hud">
            <div><strong>Swagger</strong><br><span>{stats['swagger']}</span></div>
            <div><strong>Respect</strong><br><span>{stats['respect']}</span></div>
            <div><strong>Energy</strong><br><span>{stats['energy']}</span></div>
            <div><strong>Cash</strong><br><span>{stats['cash']}</span></div>
            <div><strong>Heat</strong><br><span>{stats['heat']}</span></div>
            <div><strong>Suit</strong><br><span>{stats['suit']}</span></div>
            <div><strong>Rage</strong><br><span>{stats['rage']}</span></div>
            <div><strong>Viral</strong><br><span>{stats['viral']}</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_log(gs):
    if not gs["log"]:
        return
    entries = "".join(f"<p>• {line}</p>" for line in gs["log"][-10:])
    st.markdown(f"<div class='log'>{entries}</div>", unsafe_allow_html=True)


def render_scene_title(text):
    st.markdown(f"<div class='neon-card'><h2 style='margin:0'>{text}</h2></div>", unsafe_allow_html=True)
