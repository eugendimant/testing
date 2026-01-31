"""UI helpers for the Streamlit game."""

from __future__ import annotations

import textwrap

import streamlit as st


def inject_css(ui_style: str) -> None:
    theme_bg = "#0b0b10" if ui_style == "arcade" else "#101018"
    st.markdown(
        f"""
        <style>
        html, body, [data-testid="stAppViewContainer"] {{
            background: radial-gradient(circle at top, #1b1b2f, {theme_bg} 60%);
            color: #f7f7fb;
        }}
        .game-title {{
            font-size: 2rem;
            letter-spacing: 0.08em;
            margin-bottom: 0.2rem;
        }}
        .hud-card {{
            background: rgba(21, 21, 34, 0.92);
            border-radius: 16px;
            padding: 1rem;
            border: 1px solid rgba(255,255,255,0.08);
            box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        }}
        .log-card {{
            background: rgba(10, 10, 20, 0.85);
            border-radius: 14px;
            padding: 0.8rem 1rem;
            margin-bottom: 0.5rem;
            border: 1px solid rgba(255,255,255,0.06);
        }}
        .scene-card {{
            background: rgba(18, 18, 30, 0.92);
            padding: 1rem 1.2rem;
            border-radius: 18px;
            border: 1px solid rgba(255,255,255,0.08);
        }}
        .glow-button button {{
            border-radius: 12px;
            padding: 0.6rem 1rem;
            font-weight: 600;
            background: linear-gradient(90deg, #e94560, #ff4d6d);
            color: #fff;
            border: none;
        }}
        .stat-pill {{
            display: inline-block;
            padding: 0.2rem 0.6rem;
            border-radius: 999px;
            background: rgba(255,255,255,0.08);
            font-size: 0.8rem;
        }}
        .hud-label {{
            font-weight: 600;
        }}
        .scene-title {{
            font-size: 1.4rem;
            margin-bottom: 0.2rem;
        }}
        .scene-subtitle {{
            color: #b2b2c2;
            margin-bottom: 0.6rem;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def stat_row(label: str, value: int) -> str:
    return f"<div><span class='hud-label'>{label}:</span> <span class='stat-pill'>{value}</span></div>"


def render_hud(gs: dict) -> None:
    stats = gs["stats"]
    with st.container():
        st.markdown(
            """
            <div class="hud-card">
                <div class="scene-title">Bojan Status</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="hud-card">
            """,
            unsafe_allow_html=True,
        )
        st.markdown(stat_row("Swagger", stats["swagger"]), unsafe_allow_html=True)
        st.markdown(stat_row("Respect", stats["respect"]), unsafe_allow_html=True)
        st.markdown(stat_row("Energy", stats["energy"]), unsafe_allow_html=True)
        st.markdown(stat_row("Cash", stats["cash"]), unsafe_allow_html=True)
        st.markdown(stat_row("Heat", stats["heat"]), unsafe_allow_html=True)
        st.markdown(stat_row("Suit", stats["suit"]), unsafe_allow_html=True)
        st.markdown(stat_row("Rage", stats["rage"]), unsafe_allow_html=True)
        st.markdown(stat_row("Viral", stats["viral"]), unsafe_allow_html=True)
        st.markdown(
            f"<div class='hud-label'>Door Stage: {gs['door']['stage']}/3</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<div class='hud-label'>Night: {gs['night_id']} · Turn: {gs['turn']}</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)


def render_log(gs: dict) -> None:
    st.markdown("### Night Feed")
    for entry in gs["log"][-6:][::-1]:
        st.markdown(
            f"<div class='log-card'>{textwrap.shorten(entry, 140)}</div>",
            unsafe_allow_html=True,
        )


def render_scene_card(title: str, subtitle: str, body: str) -> None:
    st.markdown(
        f"""
        <div class="scene-card">
            <div class="scene-title">{title}</div>
            <div class="scene-subtitle">{subtitle}</div>
            <div>{body}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
