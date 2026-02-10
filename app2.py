"""
ЕДИНАЯ ПЛАТФОРМА SMART GOVERNANCE
Республика Казахстан
Цветовая схема: Stormy Morning
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta

# ============== КОНФИГУРАЦИЯ ==============
st.set_page_config(
    page_title="Единая платформа Smart Governance",
    page_icon="🇰🇿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============== STORMY MORNING PALETTE ==============
COLORS = {
    'dark': '#384959',
    'muted': '#6A89A7',
    'medium': '#88BDF2',
    'light': '#BDDDFC',
    'bg': '#F4F8FC',
    'white': '#FFFFFF',
    'success': '#4A9079',
    'warning': '#C4956A',
    'danger': '#A76A6A',
    'text': '#2D3748',
    'text_secondary': '#5A6B7D',
}

# ============== СТИЛИ ==============
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * {{
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }}
    
    .stApp {{
        background: {COLORS['bg']};
    }}
    
    .block-container {{
        padding: 1rem 2rem 2rem 2rem;
        max-width: 1400px;
    }}
    
    /* Скрыть стандартные элементы */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    .stDeployButton {{display: none;}}
    
    /* ===== SIDEBAR ===== */
    [data-testid="stSidebar"] {{
        background: {COLORS['dark']};
        border-right: 1px solid {COLORS['light']};
    }}
    
    [data-testid="stSidebar"] > div:first-child {{
        padding-top: 1rem;
    }}
    
    .sidebar-header {{
        text-align: center;
        padding: 1.5rem 1rem;
        border-bottom: 1px solid {COLORS['light']};
        margin-bottom: 1rem;
    }}
    
    .sidebar-logo {{
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }}
    
    .sidebar-title {{
        color: {COLORS['light']};
        font-size: 1rem;
        font-weight: 700;
        margin: 0;
        line-height: 1.3;
    }}
    
    .sidebar-subtitle {{
        color: {COLORS['muted']};
        font-size: 0.8rem;
        margin-top: 0.3rem;
    }}
    
    /* Sidebar radio */
    [data-testid="stSidebar"] .stRadio > div {{
        gap: 0.25rem;
    }}
    
    [data-testid="stSidebar"] .stRadio label {{
        background: transparent;
        padding: 0.75rem 1rem;
        border-radius: 8px;
        margin: 0.15rem 0;
        transition: all 0.2s ease;
        cursor: pointer;
        color: {COLORS['text']};
        font-weight: 500;
    }}
    
    [data-testid="stSidebar"] .stRadio label:hover {{
        background: {COLORS['light']};
    }}
    
    [data-testid="stSidebar"] .stRadio label[data-checked="true"] {{
        background: linear-gradient(135deg, {COLORS['medium']}, {COLORS['muted']});
        color: white;
    }}
    
    /* ===== PAGE HEADER ===== */
    .page-header {{
        background: linear-gradient(135deg, {COLORS['dark']} 0%, {COLORS['muted']} 100%);
        color: white;
        padding: 1.75rem 2rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 20px rgba(56, 73, 89, 0.2);
    }}
    
    .page-header h1 {{
        margin: 0;
        font-size: 1.5rem;
        font-weight: 700;
        letter-spacing: -0.3px;
    }}
    
    .page-header p {{
        margin: 0.4rem 0 0 0;
        opacity: 0.9;
        font-size: 0.9rem;
    }}
    
    /* ===== SECTION TITLE ===== */
    .section-title {{
        color: {COLORS['dark']};
        font-size: 1.1rem;
        font-weight: 600;
        margin: 1.5rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid {COLORS['light']};
    }}
    
    /* ===== CARDS ===== */
    .card {{
        background: {COLORS['white']};
        border-radius: 12px;
        padding: 1.25rem;
        box-shadow: 0 2px 8px rgba(56, 73, 89, 0.06);
        border: 1px solid {COLORS['light']};
        margin-bottom: 1rem;
        transition: all 0.2s ease;
    }}
    
    .card:hover {{
        box-shadow: 0 4px 16px rgba(56, 73, 89, 0.1);
        border-color: {COLORS['medium']};
    }}
    
    .card-header {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 0.75rem;
    }}
    
    .card-title {{
        color: {COLORS['dark']};
        font-size: 1rem;
        font-weight: 600;
        margin: 0;
    }}
    
    .card-subtitle {{
        color: {COLORS['muted']};
        font-size: 0.85rem;
        margin-top: 0.25rem;
    }}
    
    /* ===== METRICS ===== */
    .metric {{
        background: {COLORS['white']};
        border-radius: 10px;
        padding: 1rem 1.25rem;
        border: 1px solid {COLORS['light']};
        height: 100%;
    }}
    
    .metric-label {{
        color: {COLORS['muted']};
        font-size: 0.8rem;
        font-weight: 500;
        margin-bottom: 0.3rem;
        text-transform: uppercase;
        letter-spacing: 0.3px;
    }}
    
    .metric-value {{
        color: {COLORS['dark']};
        font-size: 1.5rem;
        font-weight: 700;
        line-height: 1.2;
    }}
    
    .metric-delta {{
        font-size: 0.8rem;
        font-weight: 600;
        margin-top: 0.3rem;
    }}
    
    .metric-delta.positive {{ color: {COLORS['success']}; }}
    .metric-delta.negative {{ color: {COLORS['danger']}; }}
    .metric-delta.neutral {{ color: {COLORS['muted']}; }}
    
    /* ===== HIGHLIGHT METRIC ===== */
    .metric-highlight {{
        background: linear-gradient(135deg, {COLORS['dark']} 0%, {COLORS['muted']} 100%);
        color: white;
        border-radius: 12px;
        padding: 1.25rem;
        box-shadow: 0 4px 16px rgba(56, 73, 89, 0.25);
    }}
    
    .metric-highlight .metric-label {{
        color: rgba(255,255,255,0.8);
    }}
    
    .metric-highlight .metric-value {{
        color: white;
        font-size: 1.75rem;
    }}
    
    .metric-highlight .metric-delta {{
        color: rgba(255,255,255,0.9);
    }}
    
    /* ===== ALERTS ===== */
    .alert {{
        padding: 1rem 1.25rem;
        border-radius: 8px;
        margin: 0.75rem 0;
        border-left: 4px solid;
    }}
    
    .alert-success {{
        background: #EBF5F1;
        border-color: {COLORS['success']};
    }}
    .alert-success .alert-title {{ color: #2D5A4A; }}
    .alert-success .alert-text {{ color: #3D7A62; }}
    
    .alert-warning {{
        background: #FDF6EE;
        border-color: {COLORS['warning']};
    }}
    .alert-warning .alert-title {{ color: #8B5A2B; }}
    .alert-warning .alert-text {{ color: #A67344; }}
    
    .alert-danger {{
        background: #F9EEEE;
        border-color: {COLORS['danger']};
    }}
    .alert-danger .alert-title {{ color: #6B3A3A; }}
    .alert-danger .alert-text {{ color: #8B4A4A; }}
    
    .alert-info {{
        background: #EDF4FC;
        border-color: {COLORS['medium']};
    }}
    .alert-info .alert-title {{ color: {COLORS['dark']}; }}
    .alert-info .alert-text {{ color: {COLORS['muted']}; }}
    
    .alert-title {{
        font-weight: 600;
        font-size: 0.9rem;
        margin-bottom: 0.3rem;
    }}
    
    .alert-text {{
        font-size: 0.85rem;
        line-height: 1.5;
    }}
    
    /* ===== AI BOX ===== */
    .ai-box {{
        background: linear-gradient(135deg, #E8F4FD 0%, {COLORS['light']} 100%);
        border-left: 4px solid {COLORS['medium']};
        border-radius: 0 10px 10px 0;
        padding: 1rem 1.25rem;
        margin: 1rem 0;
    }}
    
    .ai-box-title {{
        color: {COLORS['dark']};
        font-weight: 600;
        font-size: 0.85rem;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }}
    
    .ai-box-text {{
        color: {COLORS['text_secondary']};
        font-size: 0.9rem;
        line-height: 1.6;
    }}
    
    /* ===== BADGES ===== */
    .badge {{
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
    }}
    
    .badge-primary {{ background: {COLORS['light']}; color: {COLORS['dark']}; }}
    .badge-success {{ background: #D4ECE3; color: #2D5A4A; }}
    .badge-warning {{ background: #F9E8D6; color: #8B5A2B; }}
    .badge-danger {{ background: #F2DADA; color: #6B3A3A; }}
    
    /* ===== PROGRESS ===== */
    .progress-container {{
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-top: 0.5rem;
    }}
    
    .progress-bar {{
        flex: 1;
        height: 6px;
        background: {COLORS['light']};
        border-radius: 3px;
        overflow: hidden;
    }}
    
    .progress-fill {{
        height: 100%;
        border-radius: 3px;
        background: linear-gradient(90deg, {COLORS['medium']}, {COLORS['muted']});
    }}
    
    .progress-fill.success {{ background: linear-gradient(90deg, {COLORS['success']}, #5AA88F); }}
    .progress-fill.warning {{ background: linear-gradient(90deg, {COLORS['warning']}, #D4A57A); }}
    .progress-fill.danger {{ background: linear-gradient(90deg, {COLORS['danger']}, #B87A7A); }}
    
    .progress-text {{
        color: {COLORS['muted']};
        font-size: 0.8rem;
        font-weight: 600;
        min-width: 40px;
        text-align: right;
    }}
    
    /* ===== TABLE STYLES ===== */
    .data-table {{
        width: 100%;
        border-collapse: collapse;
        font-size: 0.85rem;
    }}
    
    .data-table th {{
        background: {COLORS['light']};
        color: {COLORS['dark']};
        font-weight: 600;
        padding: 0.75rem 1rem;
        text-align: left;
        border-bottom: 2px solid {COLORS['medium']};
    }}
    
    .data-table td {{
        padding: 0.75rem 1rem;
        border-bottom: 1px solid {COLORS['light']};
        color: {COLORS['text']};
    }}
    
    .data-table tr:hover td {{
        background: {COLORS['bg']};
    }}
    
    /* ===== SYNC BANNER ===== */
    .sync-banner {{
        background: #EDF4FC;
        border: 1px solid {COLORS['medium']};
        border-radius: 8px;
        padding: 0.75rem 1rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin: 1rem 0;
    }}
    
    .sync-icon {{
        width: 8px;
        height: 8px;
        background: {COLORS['success']};
        border-radius: 50%;
        animation: pulse 2s ease-in-out infinite;
    }}
    
    @keyframes pulse {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.5; transform: scale(1.2); }}
    }}
    
    .sync-text {{
        color: {COLORS['dark']};
        font-weight: 500;
        font-size: 0.85rem;
    }}
    
    /* ===== TABS ===== */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 4px;
        background: {COLORS['white']};
        padding: 4px;
        border-radius: 8px;
        border: 1px solid {COLORS['light']};
    }}
    
    .stTabs [data-baseweb="tab"] {{
        background: transparent;
        border-radius: 6px;
        padding: 8px 16px;
        font-weight: 500;
        color: {COLORS['muted']};
        font-size: 0.85rem;
    }}
    
    .stTabs [aria-selected="true"] {{
        background: {COLORS['dark']};
        color: white;
    }}
    
    /* ===== BUTTONS ===== */
    .stButton > button {{
        background: linear-gradient(135deg, {COLORS['medium']} 0%, {COLORS['muted']} 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.25rem;
        font-weight: 600;
        font-size: 0.85rem;
        transition: all 0.2s ease;
        box-shadow: 0 2px 8px rgba(136, 189, 242, 0.3);
    }}
    
    .stButton > button:hover {{
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(136, 189, 242, 0.4);
    }}
    
    /* Secondary button */
    .stButton > button[kind="secondary"] {{
        background: {COLORS['white']};
        color: {COLORS['dark']};
        border: 1px solid {COLORS['light']};
        box-shadow: none;
    }}
    
    /* ===== FOOTER ===== */
    .footer {{
        background: {COLORS['dark']};
        color: white;
        padding: 1.25rem 1.5rem;
        border-radius: 10px;
        margin-top: 2rem;
        text-align: center;
    }}
    
    .footer-title {{
        font-weight: 600;
        font-size: 0.9rem;
        margin-bottom: 0.25rem;
    }}
    
    .footer-subtitle {{
        color: rgba(255,255,255,0.6);
        font-size: 0.8rem;
    }}
    
    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {{
        .block-container {{
            padding: 1rem;
        }}
        
        .page-header {{
            padding: 1.25rem 1.5rem;
        }}
        
        .page-header h1 {{
            font-size: 1.25rem;
        }}
        
        .metric-value {{
            font-size: 1.25rem;
        }}
        
        [data-testid="stSidebar"] {{
            min-width: 200px;
        }}
    }}
    
    /* ===== PLOTLY OVERRIDES ===== */
    .js-plotly-plot .plotly .modebar {{
        display: none !important;
    }}
</style>
""", unsafe_allow_html=True)

# ============== КОМПОНЕНТЫ ==============

def render_page_header(title, subtitle):
    st.markdown(f"""
    <div class="page-header">
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

def render_section_title(title):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)

def render_metric(label, value, delta=None, delta_type="neutral", highlight=False):
    delta_html = ""
    if delta:
        delta_html = f'<div class="metric-delta {delta_type}">{delta}</div>'
    
    card_class = "metric-highlight" if highlight else "metric"
    st.markdown(f"""
    <div class="{card_class}">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        {delta_html}
    </div>
    """, unsafe_allow_html=True)

def render_alert(alert_type, title, text):
    st.markdown(f"""
    <div class="alert alert-{alert_type}">
        <div class="alert-title">{title}</div>
        <div class="alert-text">{text}</div>
    </div>
    """, unsafe_allow_html=True)

def render_ai_box(title, text):
    st.markdown(f"""
    <div class="ai-box">
        <div class="ai-box-title">ИИ-рекомендация: {title}</div>
        <div class="ai-box-text">{text}</div>
    </div>
    """, unsafe_allow_html=True)

def render_sync_banner(text):
    st.markdown(f"""
    <div class="sync-banner">
        <div class="sync-icon"></div>
        <div class="sync-text">{text}</div>
    </div>
    """, unsafe_allow_html=True)

def render_task_card(ministry, task, status, progress, critical):
    critical_class = "danger" if critical == "Критическая" else "warning"
    status_class = "primary" if status == "В работе" else "warning" if status == "Ожидает" else "primary"
    progress_class = "danger" if progress < 40 else "warning" if progress < 70 else "success"
    
    st.markdown(f"""
    <div class="card">
        <div class="card-header">
            <div>
                <span class="badge badge-{critical_class}">{critical}</span>
                <div class="card-title" style="margin-top:0.5rem;">{ministry}</div>
            </div>
            <span class="badge badge-{status_class}">{status}</span>
        </div>
        <div class="card-subtitle">{task}</div>
        <div class="progress-container">
            <div class="progress-bar">
                <div class="progress-fill {progress_class}" style="width:{progress}%;"></div>
            </div>
            <span class="progress-text">{progress}%</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_subsidy_card(name, amount, deadline, status, requires_local=False):
    local_badge = '<span class="badge badge-success" style="margin-left:8px;">Переработка</span>' if requires_local else ""
    st.markdown(f"""
    <div class="card">
        <div class="card-header">
            <div>
                <div class="card-title">{name}{local_badge}</div>
                <div class="card-subtitle">Макс: {amount} | Срок: {deadline}</div>
            </div>
            <span class="badge badge-success">{status}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_order_card(buyer, product, volume, price, status):
    status_class = "primary" if status == "Новый" else "success"
    st.markdown(f"""
    <div class="card">
        <div class="card-header">
            <div>
                <div class="card-title">{buyer}</div>
                <div class="card-subtitle">{product} | {volume}</div>
                <div style="color:{COLORS['success']};font-weight:700;font-size:1.1rem;margin-top:0.5rem;">{price}</div>
            </div>
            <span class="badge badge-{status_class}">{status}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_producer_card(name, product, volume, rating, contact):
    st.markdown(f"""
    <div class="card">
        <div class="card-header">
            <div>
                <div class="card-title">{name}</div>
                <div class="card-subtitle">{product} | {volume}</div>
            </div>
            <span class="badge badge-primary">{rating}</span>
        </div>
        <div style="color:{COLORS['muted']};font-size:0.85rem;">{contact}</div>
    </div>
    """, unsafe_allow_html=True)

def render_footer():
    st.markdown("""
    <div class="footer">
        <div class="footer-title">V поток «Талдау мектебі» | Сенат Парламента РК</div>
        <div class="footer-subtitle">Smart Governance: данные, аналитика и ИИ для эффективного управления</div>
    </div>
    """, unsafe_allow_html=True)

# ============== ДАННЫЕ ==============

@st.cache_data
def load_price_data():
    dates = pd.date_range(start='2026-01-01', periods=40, freq='D')
    np.random.seed(42)
    base_astana = 90000
    base_export = 96000
    
    astana_prices = [base_astana]
    export_prices = [base_export]
    
    for i in range(1, 40):
        astana_prices.append(astana_prices[-1] + np.random.randint(-500, 800))
        export_prices.append(export_prices[-1] + np.random.randint(-400, 900))
    
    return pd.DataFrame({
        'Дата': dates,
        'Астана': astana_prices,
        'Экспорт': export_prices,
        'Ячмень': [p * 0.75 for p in astana_prices],
    })

@st.cache_data
def load_localization_data():
    return pd.DataFrame({
        'Год': ['2024', '2025', '2026', '2027', '2028', '2029', '2030'],
        'Факт': [15, 18, 25, 35, 42, 48, 55],
        'Цель': [50, 50, 50, 50, 50, 50, 50]
    })

@st.cache_data
def load_radar_data():
    return pd.DataFrame({
        'Показатель': ['АПК', 'Образование', 'Здравоохранение', 'Безопасность', 'Инфраструктура', 'Финансы'],
        'Значение': [78, 72, 65, 85, 67, 70],
        'Целевое': [85, 80, 80, 90, 80, 80]
    })

@st.cache_data
def load_budget_data():
    return pd.DataFrame({
        'Категория': ['Налоговые поступления', 'Трансферты', 'Неналоговые доходы', 'Прочие'],
        'Сумма': [1850, 1680, 520, 200]
    })

@st.cache_data
def load_expense_data():
    return pd.DataFrame({
        'Категория': ['Образование', 'Здравоохранение', 'Инфраструктура', 'Соц. защита', 'АПК', 'Прочие'],
        'Сумма': [980, 720, 650, 580, 420, 900]
    })

@st.cache_data
def load_region_comparison():
    return pd.DataFrame({
        'Область': ['Акмолинская', 'Костанайская', 'СКО', 'Павлодарская', 'Карагандинская'],
        'Урожай_план': [4500, 5200, 3800, 2100, 1800],
        'Урожай_факт': [4200, 5500, 3600, 2300, 1700],
        'Локализация': [18, 22, 15, 28, 35],
        'Субсидии': [12.5, 15.2, 9.8, 8.4, 7.1]
    })

@st.cache_data
def load_harvest_forecast():
    return pd.DataFrame({
        'Культура': ['Пшеница', 'Ячмень', 'Масличные', 'Кукуруза'],
        'Прогноз': [22.5, 3.2, 1.8, 0.8],
        'Факт_2025': [18.5, 2.8, 1.5, 0.7],
        'Рост': [21.6, 14.3, 20.0, 14.3]
    })

# ============== СТРАНИЦЫ ==============

def page_home():
    render_page_header(
        "Единая платформа Smart Governance",
        "Консолидация данных | Анализ | Прогноз | Решение"
    )
    
    # Ключевые метрики
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_metric("Прогноз урожая 2026", "28 млн т", "+22% к среднему", "positive", highlight=True)
    with col2:
        render_metric("Локализация АПК", "18%", "Цель: 50%", "negative")
    with col3:
        render_metric("Субсидии выплачено", "285 млрд", "+12% к плану", "positive")
    with col4:
        render_metric("Активных СХТП", "142 500", "+8.5% г/г", "positive")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Описание модулей
    render_section_title("Модули платформы")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="card" style="border-top: 3px solid {COLORS['success']};">
            <div class="card-title">Модуль Производители</div>
            <div class="card-subtitle">Сельхозтоваропроизводители</div>
            <ul style="color:{COLORS['text_secondary']};font-size:0.85rem;padding-left:1.2rem;margin-top:1rem;">
                <li>Каталог мер господдержки</li>
                <li>Карта производителей сырья</li>
                <li>Рыночная аналитика</li>
                <li>Маркетплейс прямых продаж</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="card" style="border-top: 3px solid {COLORS['medium']};">
            <div class="card-title">Модуль Акимат</div>
            <div class="card-subtitle">Местные исполнительные органы</div>
            <ul style="color:{COLORS['text_secondary']};font-size:0.85rem;padding-left:1.2rem;margin-top:1rem;">
                <li>Сводный дашборд района</li>
                <li>Социальные показатели</li>
                <li>Бюджет и инвестиции</li>
                <li>ИИ-прогнозы развития</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="card" style="border-top: 3px solid {COLORS['dark']};">
            <div class="card-title">Модуль Госорганы</div>
            <div class="card-subtitle">Министерства и ведомства</div>
            <ul style="color:{COLORS['text_secondary']};font-size:0.85rem;padding-left:1.2rem;margin-top:1rem;">
                <li>Космомониторинг и прогнозы</li>
                <li>Синхронизация задач</li>
                <li>Региональный анализ</li>
                <li>KPI и исполнение</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    render_alert("info", "Принцип синхронного управления",
                "Прогноз урожая → Все министерства получают задачи одновременно → Скоординированное исполнение за дни вместо месяцев")
    
    # График локализации
    render_section_title("Динамика локализации добавленной стоимости")
    
    data = load_localization_data()
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Год'], y=data['Цель'],
        mode='lines', name='Цель',
        line=dict(color=COLORS['warning'], width=2, dash='dash'),
    ))
    
    fig.add_trace(go.Scatter(
        x=data['Год'], y=data['Факт'],
        mode='lines+markers', name='Факт/Прогноз',
        line=dict(color=COLORS['medium'], width=3),
        marker=dict(size=8),
        fill='tozeroy',
        fillcolor='rgba(136, 189, 242, 0.2)'
    ))
    
    fig.update_layout(
        height=320,
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5,
                   font=dict(color=COLORS['dark'], size=12)),
        yaxis=dict(gridcolor='rgba(106, 137, 167, 0.2)', range=[0, 60],
                  tickfont=dict(color=COLORS['muted']), title='%'),
        xaxis=dict(gridcolor='rgba(106, 137, 167, 0.2)',
                  tickfont=dict(color=COLORS['muted']))
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    render_footer()

def page_schtp():
    render_page_header(
        "Модуль Производители",
        "КХ «Арай» | Аршалынский район | БИН: 123456789012"
    )
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Дашборд", "Господдержка", "Карта сырья", "Рынок", "Маркетплейс"
    ])
    
    # ===== TAB 1: ДАШБОРД =====
    with tab1:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            render_metric("Урожай 2025", "5 200 т", "+12%", "positive")
        with col2:
            render_metric("Выручка", "485 млн", "+18%", "positive")
        with col3:
            render_metric("Средняя цена", "93 200 ₸/т", "+3 500", "positive")
        with col4:
            render_metric("Субсидии", "41.7 млн", "Получено", "neutral")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            render_section_title("Динамика цен")
            
            price_data = load_price_data()
            fig = go.Figure()
            
            fig.add_trace(go.Scatter(
                x=price_data['Дата'], y=price_data['Астана'],
                mode='lines', name='Астана',
                line=dict(color=COLORS['muted'], width=2)
            ))
            fig.add_trace(go.Scatter(
                x=price_data['Дата'], y=price_data['Экспорт'],
                mode='lines', name='Экспорт',
                line=dict(color=COLORS['medium'], width=2)
            ))
            
            fig.update_layout(
                height=280,
                margin=dict(l=20, r=20, t=10, b=20),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                legend=dict(orientation="h", yanchor="bottom", y=1.02,
                           font=dict(color=COLORS['dark'], size=11)),
                yaxis=dict(gridcolor='rgba(106, 137, 167, 0.2)',
                          tickfont=dict(color=COLORS['muted'], size=10),
                          title='₸/тонна'),
                xaxis=dict(gridcolor='rgba(106, 137, 167, 0.2)',
                          tickfont=dict(color=COLORS['muted'], size=10))
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            render_ai_box(
                "Оптимальное время продажи",
                "Рекомендуем реализовать <b>60% урожая</b> в период <b>15-25 марта</b>. "
                "Ожидаемый рост цен: +5-7%. Забронируйте вагоны заранее."
            )
            
            render_section_title("Активные заказы")
            render_order_card("Ресторан «Алтын Орда»", "Пшеница 3 кл.", "50 т", "96 000 ₸/т", "Новый")
    
    # ===== TAB 2: ГОСПОДДЕРЖКА =====
    with tab2:
        render_section_title("Доступные меры государственной поддержки")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            subsidies = [
                {"name": "Инвестиционные субсидии", "amount": "до 50 млн ₸", "deadline": "15.03.2026", "status": "Открыт", "local": False},
                {"name": "Субсидии на семена", "amount": "до 5 млн ₸", "deadline": "01.04.2026", "status": "Открыт", "local": False},
                {"name": "Субсидии на удобрения", "amount": "до 8 млн ₸", "deadline": "01.04.2026", "status": "Открыт", "local": False},
                {"name": "Субсидии на переработку", "amount": "до 80 млн ₸", "deadline": "01.06.2026", "status": "Открыт", "local": True},
                {"name": "Субсидии на технику", "amount": "до 25 млн ₸", "deadline": "30.06.2026", "status": "Открыт", "local": True},
                {"name": "Льготное кредитование", "amount": "до 500 млн ₸", "deadline": "Постоянно", "status": "Открыт", "local": False},
                {"name": "Страхование посевов", "amount": "50% премии", "deadline": "15.05.2026", "status": "Открыт", "local": False},
                {"name": "Экспортная поддержка", "amount": "до 15 млн ₸", "deadline": "Постоянно", "status": "Открыт", "local": False},
            ]
            
            for sub in subsidies:
                render_subsidy_card(sub["name"], sub["amount"], sub["deadline"], sub["status"], sub["local"])
        
        with col2:
            render_ai_box(
                "Персональная рекомендация",
                "На основе вашего профиля (зерновые, 5 200 т, Аршалынский район) рекомендуем подать на "
                "<b>«Субсидии на семена»</b> — потенциальная выгода до 5 млн ₸. Срок подачи: до 01.04.2026."
            )
            
            render_alert("info", "Условия локализации",
                        "Субсидии с пометкой «Переработка» требуют обязательной переработки продукции на территории Казахстана.")
    
    # ===== TAB 3: КАРТА СЫРЬЯ =====
    with tab3:
        render_section_title("Производители сырья в регионе")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            producers = [
                {"name": "КХ «Зерно Астаны»", "product": "Пшеница 3 кл.", "volume": "8 500 т", "rating": "4.8", "contact": "+7 701 123 4567"},
                {"name": "ТОО «Агро-Акмола»", "product": "Пшеница, Ячмень", "volume": "12 000 т", "rating": "4.6", "contact": "+7 702 234 5678"},
                {"name": "КХ «Нива»", "product": "Масличные", "volume": "3 200 т", "rating": "4.9", "contact": "+7 705 345 6789"},
                {"name": "ТОО «Степь»", "product": "Пшеница 4 кл.", "volume": "6 800 т", "rating": "4.5", "contact": "+7 707 456 7890"},
                {"name": "КХ «Береке»", "product": "Ячмень", "volume": "4 100 т", "rating": "4.7", "contact": "+7 700 567 8901"},
            ]
            
            for prod in producers:
                render_producer_card(prod["name"], prod["product"], prod["volume"], prod["rating"], prod["contact"])
        
        with col2:
            render_ai_box(
                "Поиск сырья",
                "Для вашего перерабатывающего предприятия найдено <b>5 поставщиков</b> в радиусе 100 км. "
                "Общий доступный объём: <b>34 600 тонн</b>."
            )
            
            # Мини-карта (заглушка)
            st.markdown(f"""
            <div class="card" style="text-align:center;padding:2rem;">
                <div style="color:{COLORS['muted']};font-size:0.9rem;">Интерактивная карта</div>
                <div style="color:{COLORS['dark']};font-size:1.1rem;font-weight:600;margin-top:0.5rem;">Аршалынский район</div>
                <div style="color:{COLORS['muted']};font-size:0.85rem;margin-top:0.25rem;">5 производителей | 34 600 т</div>
            </div>
            """, unsafe_allow_html=True)
    
    # ===== TAB 4: РЫНОК =====
    with tab4:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            render_metric("Пшеница (Астана)", "95 800 ₸", "+2.1%", "positive")
        with col2:
            render_metric("Пшеница (Экспорт)", "102 500 ₸", "+1.8%", "positive")
        with col3:
            render_metric("Ячмень", "72 400 ₸", "+0.9%", "positive")
        with col4:
            render_metric("Масличные", "185 000 ₸", "-0.5%", "negative")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        render_section_title("Динамика цен за 40 дней")
        
        price_data = load_price_data()
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=price_data['Дата'], y=price_data['Астана'],
            mode='lines', name='Пшеница (Астана)',
            line=dict(color=COLORS['dark'], width=2)
        ))
        fig.add_trace(go.Scatter(
            x=price_data['Дата'], y=price_data['Экспорт'],
            mode='lines', name='Пшеница (Экспорт)',
            line=dict(color=COLORS['medium'], width=2)
        ))
        fig.add_trace(go.Scatter(
            x=price_data['Дата'], y=price_data['Ячмень'],
            mode='lines', name='Ячмень',
            line=dict(color=COLORS['muted'], width=2)
        ))
        
        fig.update_layout(
            height=350,
            margin=dict(l=20, r=20, t=20, b=20),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            legend=dict(orientation="h", yanchor="bottom", y=1.02,
                       font=dict(color=COLORS['dark'], size=11)),
            yaxis=dict(gridcolor='rgba(106, 137, 167, 0.2)',
                      tickfont=dict(color=COLORS['muted']), title='₸/тонна'),
            xaxis=dict(gridcolor='rgba(106, 137, 167, 0.2)',
                      tickfont=dict(color=COLORS['muted']))
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        render_ai_box(
            "Рыночный прогноз",
            "Ожидается рост цен на пшеницу на <b>5-7%</b> в марте-апреле в связи с сезонным спросом. "
            "Рекомендуем зафиксировать контракты на экспорт до конца февраля."
        )
    
    # ===== TAB 5: МАРКЕТПЛЕЙС =====
    with tab5:
        render_alert("success", "Преимущество прямых продаж",
                    "Средняя цена на маркетплейсе на 15-20% выше, чем у перекупщиков. Вы экономите на посредниках.")
        
        render_section_title("Актуальные заказы")
        
        col1, col2 = st.columns(2)
        
        with col1:
            orders = [
                {"buyer": "Ресторан «Алтын Орда»", "product": "Пшеница 3 кл.", "volume": "50 т", "price": "96 000 ₸/т", "status": "Новый"},
                {"buyer": "Сеть «Магнум»", "product": "Мука в/с", "volume": "20 т", "price": "185 000 ₸/т", "status": "Активный"},
                {"buyer": "ТОО «Хлебозавод»", "product": "Пшеница 2 кл.", "volume": "200 т", "price": "98 000 ₸/т", "status": "Новый"},
            ]
            
            for order in orders:
                render_order_card(order["buyer"], order["product"], order["volume"], order["price"], order["status"])
        
        with col2:
            orders = [
                {"buyer": "Экспорт — Узбекистан", "product": "Пшеница 3 кл.", "volume": "2 000 т", "price": "102 000 ₸/т", "status": "Новый"},
                {"buyer": "Экспорт — Китай", "product": "Масличные", "volume": "500 т", "price": "188 000 ₸/т", "status": "Активный"},
                {"buyer": "ТОО «Макфа-KZ»", "product": "Пшеница твёрдая", "volume": "1 000 т", "price": "105 000 ₸/т", "status": "Новый"},
            ]
            
            for order in orders:
                render_order_card(order["buyer"], order["product"], order["volume"], order["price"], order["status"])
    
    render_footer()

def page_mio():
    render_page_header(
        "Модуль Акимат",
        f"Аршалынский район | Акмолинская область | {datetime.now().strftime('%d.%m.%Y')}"
    )
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Сводка", "Сельское хозяйство", "Социальная сфера", "Бюджет", "Прогноз"
    ])
    
    # ===== TAB 1: СВОДКА =====
    with tab1:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            render_metric("Население", "33 363", "-0.8%", "negative")
        with col2:
            render_metric("Занятость", "18 106", "Безр. 4.2%", "neutral")
        with col3:
            render_metric("Посевы", "191 868 га", "+10.7%", "positive")
        with col4:
            render_metric("Бюджет", "4 250 млн", "+70 млн", "positive")
        with col5:
            render_metric("Локализация", "15%", "Цель: 50%", "negative")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            render_section_title("Индекс развития района")
            
            radar_data = load_radar_data()
            fig = go.Figure()
            
            fig.add_trace(go.Scatterpolar(
                r=radar_data['Целевое'].tolist() + [radar_data['Целевое'].iloc[0]],
                theta=radar_data['Показатель'].tolist() + [radar_data['Показатель'].iloc[0]],
                fill='toself',
                fillcolor='rgba(196, 149, 106, 0.2)',
                line=dict(color=COLORS['warning'], width=1, dash='dash'),
                name='Цель'
            ))
            
            fig.add_trace(go.Scatterpolar(
                r=radar_data['Значение'].tolist() + [radar_data['Значение'].iloc[0]],
                theta=radar_data['Показатель'].tolist() + [radar_data['Показатель'].iloc[0]],
                fill='toself',
                fillcolor='rgba(136, 189, 242, 0.4)',
                line=dict(color=COLORS['medium'], width=2),
                name='Факт'
            ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(visible=True, range=[0, 100],
                                   gridcolor='rgba(106, 137, 167, 0.2)',
                                   tickfont=dict(color=COLORS['muted'], size=10)),
                    angularaxis=dict(gridcolor='rgba(106, 137, 167, 0.2)',
                                    tickfont=dict(color=COLORS['dark'], size=11))
                ),
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="center", x=0.5,
                           font=dict(size=11)),
                height=350,
                margin=dict(l=60, r=60, t=40, b=60),
                paper_bgcolor='rgba(0,0,0,0)',
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            render_section_title("Требуют внимания")
            render_alert("danger", "Отток населения",
                        "За год: -0.8% (-267 чел). Прогноз на 2026: -2.1% без принятия мер.")
            render_alert("warning", "Низкая локализация АПК",
                        "Только 15% продукции перерабатывается в районе. 85% добавленной стоимости уходит.")
            render_alert("info", "Рост инвестиций",
                        "Инвестиции: 2 850 млн (+23%). Новый проект: элеватор на 50 000 тонн.")
    
    # ===== TAB 2: СЕЛЬСКОЕ ХОЗЯЙСТВО =====
    with tab2:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            render_metric("Посевные площади", "191 868 га", "+10.7%", "positive")
        with col2:
            render_metric("Урожайность", "14.2 ц/га", "+8%", "positive")
        with col3:
            render_metric("Валовый сбор", "272 500 т", "+19%", "positive")
        with col4:
            render_metric("Поголовье КРС", "45 200", "+3.2%", "positive")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            render_section_title("Структура посевов")
            
            crop_data = pd.DataFrame({
                'Культура': ['Пшеница', 'Ячмень', 'Масличные', 'Кормовые', 'Прочие'],
                'Площадь': [125000, 32000, 18000, 12000, 4868]
            })
            
            fig = px.pie(crop_data, values='Площадь', names='Культура',
                        color_discrete_sequence=[COLORS['dark'], COLORS['muted'], 
                                                 COLORS['medium'], COLORS['light'], '#9CA3AF'])
            fig.update_layout(
                height=280,
                margin=dict(l=20, r=20, t=20, b=20),
                paper_bgcolor='rgba(0,0,0,0)',
                legend=dict(font=dict(size=11, color = COLORS['dark'])), 
            )
            fig.update_traces(textposition='inside', textinfo='percent+label',
                            textfont=dict(size=11))
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            render_section_title("Субсидии по категориям")
            
            subsidy_data = pd.DataFrame({
                'Категория': ['ТОО', 'КХ', 'ПК', 'ИП'],
                'Сумма': [280, 120, 40, 20]
            })
            
            fig = px.bar(subsidy_data, x='Категория', y='Сумма',
                        color_discrete_sequence=[COLORS['medium']])
            fig.update_layout(
                height=280,
                margin=dict(l=20, r=20, t=20, b=20),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                yaxis=dict(gridcolor='rgba(106, 137, 167, 0.2)',
                          tickfont=dict(color=COLORS['muted']), 
                          title=dict(
                              text='млн ₸',
                              font=dict(color=COLORS['dark']))),
                xaxis=dict(tickfont=dict(color=COLORS['dark']),
                           title=dict(
                              text='Категория',
                              font=dict(color=COLORS['dark'])))
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    # ===== TAB 3: СОЦИАЛЬНАЯ СФЕРА =====
    with tab3:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            render_metric("Школы", "24", "5 788 учащихся", "neutral")
        with col2:
            render_metric("Больницы/ФАП", "12", "28 врачей/10к", "neutral")
        with col3:
            render_metric("Преступность", "12.5/10к", "-8%", "positive")
        with col4:
            render_metric("Дороги", "342 км", "67% в норме", "neutral")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            render_section_title("Качество услуг")
            
            services = [
                {"name": "Образование", "value": 72},
                {"name": "Здравоохранение", "value": 65},
                {"name": "Безопасность", "value": 85},
                {"name": "Инфраструктура", "value": 67},
                {"name": "Коммунальные услуги", "value": 58},
            ]
            
            for svc in services:
                progress_class = "success" if svc["value"] >= 75 else "warning" if svc["value"] >= 60 else "danger"
                st.markdown(f"""
                <div style="margin-bottom:0.75rem;">
                    <div style="display:flex;justify-content:space-between;margin-bottom:0.25rem;">
                        <span style="color:{COLORS['dark']};font-size:0.85rem;font-weight:500;">{svc["name"]}</span>
                        <span style="color:{COLORS['muted']};font-size:0.85rem;">{svc["value"]}%</span>
                    </div>
                    <div class="progress-bar">
                        <div class="progress-fill {progress_class}" style="width:{svc["value"]}%;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            render_section_title("Миграция населения")
            
            migration_data = pd.DataFrame({
                'Год': ['2021', '2022', '2023', '2024', '2025'],
                'Прибыло': [450, 420, 380, 350, 320],
                'Убыло': [520, 580, 620, 590, 587]
            })
            
            fig = go.Figure()
            fig.add_trace(go.Bar(x=migration_data['Год'], y=migration_data['Прибыло'],
                                name='Прибыло', marker_color=COLORS['success']))
            fig.add_trace(go.Bar(x=migration_data['Год'], y=migration_data['Убыло'],
                                name='Убыло', marker_color=COLORS['danger']))
            
            fig.update_layout(
                height=250,
                barmode='group',
                margin=dict(l=20, r=20, t=20, b=20),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                legend=dict(orientation="h", yanchor="bottom", y=1.02, font=dict(size=11, color = COLORS['dark'])),
                yaxis=dict(gridcolor='rgba(106, 137, 167, 0.2)',
                          tickfont=dict(color=COLORS['muted']), title='чел.'),
                xaxis=dict(tickfont=dict(color=COLORS['dark']))
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    # ===== TAB 4: БЮДЖЕТ =====
    with tab4:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            render_metric("Доходы", "4 250 млн", "+1.7%", "positive")
        with col2:
            render_metric("Расходы", "4 180 млн", "+2.1%", "neutral")
        with col3:
            render_metric("Инвестиции", "2 850 млн", "+23%", "positive")
        with col4:
            render_metric("Налоги", "1 850 млн", "+5.2%", "positive")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            render_section_title("Структура доходов")
            
            budget_data = load_budget_data()
            fig = px.pie(budget_data, values='Сумма', names='Категория',
                        color_discrete_sequence=[COLORS['dark'], COLORS['muted'], 
                                                 COLORS['medium'], COLORS['light']])
            fig.update_layout(
                height=280,
                margin=dict(l=20, r=20, t=20, b=20),
                paper_bgcolor='rgba(0,0,0,0)',
                legend=dict(font=dict(size=11, color = COLORS['dark'])),
            )
            fig.update_traces(textposition='inside', textinfo='percent',
                            textfont=dict(size=11))
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            render_section_title("Структура расходов")
            
            expense_data = load_expense_data()
            fig = px.pie(expense_data, values='Сумма', names='Категория',
                        color_discrete_sequence=[COLORS['success'], COLORS['medium'], 
                                                 COLORS['muted'], COLORS['warning'],
                                                 COLORS['dark'], COLORS['light']])
            fig.update_layout(
                height=280,
                margin=dict(l=20, r=20, t=20, b=20),
                paper_bgcolor='rgba(0,0,0,0)',
                legend=dict(font=dict(size=11, color = COLORS['dark'])),
            )
            fig.update_traces(textposition='inside', textinfo='percent',
                            textfont=dict(size=11))
            
            st.plotly_chart(fig, use_container_width=True)
    
    # ===== TAB 5: ПРОГНОЗ =====
    with tab5:
        render_section_title("Сценарии развития до 2030 года")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="card" style="border-top: 3px solid {COLORS['muted']};">
                <div class="card-title">Базовый сценарий</div>
                <div class="card-subtitle">Без дополнительных мер</div>
                <div style="margin-top:1rem;">
                    <div style="display:flex;justify-content:space-between;padding:0.5rem 0;border-bottom:1px solid {COLORS['light']};">
                        <span style="color:{COLORS['text_secondary']};">Население</span>
                        <span style="color:{COLORS['danger']};font-weight:600;">-8% (30 694)</span>
                    </div>
                    <div style="display:flex;justify-content:space-between;padding:0.5rem 0;border-bottom:1px solid {COLORS['light']};">
                        <span style="color:{COLORS['text_secondary']};">Локализация</span>
                        <span style="color:{COLORS['warning']};font-weight:600;">21%</span>
                    </div>
                    <div style="display:flex;justify-content:space-between;padding:0.5rem 0;border-bottom:1px solid {COLORS['light']};">
                        <span style="color:{COLORS['text_secondary']};">Рабочие места</span>
                        <span style="color:{COLORS['danger']};font-weight:600;">-5%</span>
                    </div>
                    <div style="display:flex;justify-content:space-between;padding:0.5rem 0;">
                        <span style="color:{COLORS['text_secondary']};">Бюджет</span>
                        <span style="color:{COLORS['muted']};font-weight:600;">+8%</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="card" style="border-top: 3px solid {COLORS['success']};">
                <div class="card-title">Оптимистичный сценарий</div>
                <div class="card-subtitle">С реализацией рекомендаций</div>
                <div style="margin-top:1rem;">
                    <div style="display:flex;justify-content:space-between;padding:0.5rem 0;border-bottom:1px solid {COLORS['light']};">
                        <span style="color:{COLORS['text_secondary']};">Население</span>
                        <span style="color:{COLORS['success']};font-weight:600;">+6% (35 365)</span>
                    </div>
                    <div style="display:flex;justify-content:space-between;padding:0.5rem 0;border-bottom:1px solid {COLORS['light']};">
                        <span style="color:{COLORS['text_secondary']};">Локализация</span>
                        <span style="color:{COLORS['success']};font-weight:600;">55%</span>
                    </div>
                    <div style="display:flex;justify-content:space-between;padding:0.5rem 0;border-bottom:1px solid {COLORS['light']};">
                        <span style="color:{COLORS['text_secondary']};">Рабочие места</span>
                        <span style="color:{COLORS['success']};font-weight:600;">+180</span>
                    </div>
                    <div style="display:flex;justify-content:space-between;padding:0.5rem 0;">
                        <span style="color:{COLORS['text_secondary']};">Бюджет</span>
                        <span style="color:{COLORS['success']};font-weight:600;">+35%</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        render_ai_box(
            "Рекомендации для оптимистичного сценария",
            "1. <b>Мини-элеватор</b> (инвестиции 450 млн) → +45 рабочих мест, +120 млн налогов/год<br>"
            "2. <b>Кооператив фермеров</b> (инвестиции 80 млн) → +20% цена для фермеров<br>"
            "3. <b>Платформа прямых продаж</b> (инвестиции 25 млн) → +15% доход СХТП"
        )
    
    render_footer()

def page_gov():
    render_page_header(
        "Модуль Госорганы",
        "Межведомственная координация | Синхронное управление"
    )
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "Мониторинг", "Синхронизация", "Регионы", "KPI"
    ])
    
    # ===== TAB 1: МОНИТОРИНГ =====
    with tab1:
        render_alert("success", "Прогноз урожая 2026",
                    "На основе NDVI-индекса и метеоданных: зерновые — 28 млн тонн (+22% к среднему). Уверенность прогноза: 87%.")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            render_metric("Пшеница", "22.5 млн т", "+21.6%", "positive", highlight=True)
        with col2:
            render_metric("Ячмень", "3.2 млн т", "+14.3%", "positive")
        with col3:
            render_metric("Масличные", "1.8 млн т", "+20.0%", "positive")
        with col4:
            render_metric("Кукуруза", "0.8 млн т", "+14.3%", "positive")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            render_section_title("NDVI по регионам")
            
            region_data = load_region_comparison()
            
            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=region_data['Область'],
                y=region_data['Урожай_план'],
                name='План',
                marker_color=COLORS['light']
            ))
            fig.add_trace(go.Bar(
                x=region_data['Область'],
                y=region_data['Урожай_факт'],
                name='Прогноз',
                marker_color=COLORS['medium']
            ))
            
            fig.update_layout(
                height=300,
                barmode='group',
                margin=dict(l=20, r=20, t=20, b=20),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                legend=dict(orientation="h", yanchor="bottom", y=1.02, font=dict(size=11)),
                yaxis=dict(gridcolor='rgba(106, 137, 167, 0.2)',
                          tickfont=dict(color=COLORS['muted']), title='тыс. тонн'),
                xaxis=dict(tickfont=dict(color=COLORS['dark'], size=10))
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            render_section_title("Метеопрогноз")
            
            weather = [
                {"period": "Июнь", "status": "Благоприятно", "class": "success"},
                {"period": "Июль", "status": "Благоприятно", "class": "success"},
                {"period": "Август", "status": "Умеренный риск", "class": "warning"},
                {"period": "Сентябрь", "status": "Благоприятно", "class": "success"},
            ]
            
            for w in weather:
                st.markdown(f"""
                <div style="display:flex;justify-content:space-between;align-items:center;padding:0.6rem 0;border-bottom:1px solid {COLORS['light']};">
                    <span style="color:{COLORS['dark']};font-weight:500;">{w["period"]}</span>
                    <span class="badge badge-{w["class"]}">{w["status"]}</span>
                </div>
                """, unsafe_allow_html=True)
    
    # ===== TAB 2: СИНХРОНИЗАЦИЯ =====
    with tab2:
        render_sync_banner("Режим синхронизации активен | Все министерства получили задачи | Срок: 15.05.2026")
        
        render_section_title("Задачи министерств")
        
        tasks = [
            {"ministry": "МСХ РК", "task": "Расчёт лимитов закупа Продкорпорации: 3.5 млн тонн. Субсидии: +45 млрд ₸", 
             "status": "В работе", "progress": 65, "critical": "Высокая"},
            {"ministry": "КТЖ / Минтранс", "task": "Обеспечить 12 000 вагонов. Приоритетные направления: Достык, Хоргос, Актау", 
             "status": "Ожидает", "progress": 30, "critical": "Критическая"},
            {"ministry": "МИД / Минторговли", "task": "Переговоры по экспортным контрактам: Китай (+2 млн т), Узбекистан, Иран", 
             "status": "В работе", "progress": 45, "critical": "Высокая"},
            {"ministry": "Минфин / МНЭ", "task": "Резервирование бюджета: +85 млрд ₸. Источники: НФ, перераспределение", 
             "status": "На согласовании", "progress": 50, "critical": "Высокая"},
            {"ministry": "МИО (Акиматы)", "task": "Подготовка элеваторов и ХПП. Проверка весового оборудования", 
             "status": "В работе", "progress": 40, "critical": "Высокая"},
        ]
        
        col1, col2 = st.columns(2)
        
        for i, task in enumerate(tasks):
            with col1 if i % 2 == 0 else col2:
                render_task_card(task["ministry"], task["task"], task["status"], task["progress"], task["critical"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        render_ai_box(
            "Межведомственная рекомендация",
            "При текущих темпах <b>КТЖ не успеет</b> подготовить вагоны к уборочной. "
            "Рекомендуем провести <b>экстренное совещание</b> с участием Минтранс и Минфин для ускорения финансирования."
        )
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Отправить напоминания", use_container_width=True):
                st.success("Напоминания отправлены ответственным")
        with col2:
            if st.button("Созвать совещание", use_container_width=True):
                st.info("Приглашения отправлены на 12.02.2026 10:00")
        with col3:
            if st.button("Сформировать отчёт", use_container_width=True):
                st.success("Отчёт сформирован и направлен в АП")
    
    # ===== TAB 3: РЕГИОНЫ =====
    with tab3:
        render_section_title("Сравнительный анализ областей")
        
        region_data = load_region_comparison()
        
        # Собираем строки таблицы
        table_rows = ""
        for _, row in region_data.iterrows():
            diff = row['Урожай_факт'] - row['Урожай_план']
            diff_color = COLORS['success'] if diff >= 0 else COLORS['danger']
            local_color = COLORS['success'] if row['Локализация'] >= 25 else COLORS['warning'] if row['Локализация'] >= 18 else COLORS['danger']
            
            table_rows += f"""
                <tr>
                    <td><strong>{row['Область']}</strong></td>
                    <td>{row['Урожай_план']:,}</td>
                    <td style="color:{diff_color}">{row['Урожай_факт']:,} ({'+' if diff >= 0 else ''}{diff:,})</td>
                    <td style="color:{local_color}">{row['Локализация']}%</td>
                    <td>{row['Субсидии']} млрд</td>
                </tr>"""
        
        # Полная таблица в одной строке
        full_table = f"""
        <table class="data-table">
            <thead>
                <tr>
                    <th>Область</th>
                    <th>План (тыс. т)</th>
                    <th>Прогноз (тыс. т)</th>
                    <th>Локализация</th>
                    <th>Субсидии (млрд)</th>
                </tr>
            </thead>
            <tbody>{table_rows}
            </tbody>
        </table>
        """
        
        # Один вызов st.markdown
        st.markdown(full_table, unsafe_allow_html=True)



 
        
        render_section_title("Субсидии vs Локализация")
        
        fig = px.scatter(region_data, x='Субсидии', y='Локализация',
                        size='Урожай_факт', color='Область',
                        color_discrete_sequence=[COLORS['dark'], COLORS['muted'], 
                                                 COLORS['medium'], COLORS['warning'], COLORS['success']])
        
        fig.update_layout(
            height=350,
            margin=dict(l=20, r=20, t=20, b=20),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            legend=dict(font=dict(size=11, color=COLORS['dark'])),
            yaxis=dict(gridcolor='rgba(106, 137, 167, 0.2)',
                      tickfont=dict(color=COLORS['muted']), title='Локализация, %', title_font=dict(color=COLORS['dark'])),
            xaxis=dict(gridcolor='rgba(106, 137, 167, 0.2)',
                      tickfont=dict(color=COLORS['muted']), title='Субсидии, млрд ₸', title_font=dict(color=COLORS['dark']))
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # ===== TAB 4: KPI =====
    with tab4:
        render_section_title("Ключевые показатели эффективности")
        
        col1, col2, col3, col4 = st.columns(4)
        
        kpis = [
            {"name": "Урожай", "value": 28, "target": 35, "unit": "млн т"},
            {"name": "Экспорт", "value": 72, "target": 100, "unit": "%"},
            {"name": "Локализация", "value": 18, "target": 50, "unit": "%"},
            {"name": "Продбезопасность", "value": 85, "target": 100, "unit": "%"},
        ]
        
        for i, kpi in enumerate(kpis):
            with [col1, col2, col3, col4][i]:
                pct = int((kpi["value"] / kpi["target"]) * 100)
                color = COLORS['success'] if pct >= 80 else COLORS['warning'] if pct >= 60 else COLORS['danger']
                
                fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=kpi["value"],
                    title={'text': kpi["name"], 'font': {'size': 14, 'color': COLORS['dark']}},
                    number={'suffix': f' {kpi["unit"]}', 'font': {'size': 20, 'color': COLORS['dark']}},
                    gauge={
                        'axis': {'range': [0, kpi["target"]], 'tickfont': {'size': 10, 'color': COLORS['dark']}},
                        'bar': {'color': color},
                        'bgcolor': COLORS['dark'],
                        'borderwidth': 0,
                        'steps': [
                            {'range': [0, kpi["target"] * 0.6], 'color': 'rgba(167, 106, 106, 0.2)'},
                            {'range': [kpi["target"] * 0.6, kpi["target"] * 0.8], 'color': 'rgba(196, 149, 106, 0.2)'},
                            {'range': [kpi["target"] * 0.8, kpi["target"]], 'color': 'rgba(74, 144, 121, 0.2)'},
                        ],
                        'threshold': {
                            'line': {'color': COLORS['dark'], 'width': 2},
                            'thickness': 0.75,
                            'value': kpi["target"]
                        }
                    }
                ))
                
                fig.update_layout(
                    height=200,
                    margin=dict(l=20, r=20, t=40, b=20),
                    paper_bgcolor='rgba(0,0,0,0)',
                )
                
                st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        render_section_title("Динамика выполнения")
        
        years = ['2020', '2021', '2022', '2023', '2024', '2025', '2026']
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=years, y=[15, 16, 17, 18, 20, 22, 28],
                                mode='lines+markers', name='Урожай (млн т)',
                                line=dict(color=COLORS['dark'], width=2)))
        fig.add_trace(go.Scatter(x=years, y=[12, 13, 14, 15, 16, 17, 18],
                                mode='lines+markers', name='Локализация (%)',
                                line=dict(color=COLORS['medium'], width=2)))
        
        fig.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=20, b=20),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            legend=dict(orientation="h", yanchor="bottom", y=1.02, font=dict(size=11, color = COLORS["dark"])),
            yaxis=dict(gridcolor='rgba(106, 137, 167, 0.2)', tickfont=dict(color=COLORS['muted'])),
            xaxis=dict(gridcolor='rgba(106, 137, 167, 0.2)', tickfont=dict(color=COLORS['dark']))
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    render_footer()

# ============== SIDEBAR & NAVIGATION ==============

def main():
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-header">
            <div class="sidebar-logo">🇰🇿</div>
            <div class="sidebar-title">Единая платформа<br>Smart Governance</div>
            <div class="sidebar-subtitle">Республика Казахстан</div>
        </div>
        """, unsafe_allow_html=True)
        
        page = st.radio(
            "Навигация",
            ["Главная", "Производители", "Акимат", "Госорганы"],
            label_visibility="collapsed"
        )
        
        st.divider()
        
        st.markdown(f"""
        <div style="padding:1rem;background:{COLORS['light']};border-radius:8px;font-size:0.8rem;">
            <div style="color:{COLORS['dark']};font-weight:600;margin-bottom:0.5rem;">V поток «Талдау мектебі»</div>
            <div style="color:{COLORS['muted']};">Сенат Парламента РК</div>
            <div style="color:{COLORS['muted']};margin-top:0.5rem;">Кейс: Аршалынский район</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="margin-top:1rem;padding:0.75rem;font-size:0.75rem;color:{COLORS['muted']};">
            Обновлено: {datetime.now().strftime('%d.%m.%Y %H:%M')}
        </div>
        """, unsafe_allow_html=True)
    
    # Роутинг
    if page == "Главная":
        page_home()
    elif page == "Производители":
        page_schtp()
    elif page == "Акимат":
        page_mio()
    elif page == "Госорганы":
        page_gov()

if __name__ == "__main__":
    main()
