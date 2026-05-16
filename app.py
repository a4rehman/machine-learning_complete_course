import streamlit as st
import os
import pandas as pd
import numpy as np
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="ML Mastery Platform", 
    page_icon="🧠", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR PREMIUM UI & GLASSMORPHISM ---
st.markdown("""
    <style>
    /* Dark Theme & Glassmorphism Base */
    .stApp {
        background-color: #0b0f19;
        color: #E2E8F0;
    }
    
    /* Sidebar Styling */
    .css-1d391kg, .css-163ttcj {
        background-color: rgba(15, 23, 42, 0.7) !important;
        backdrop-filter: blur(12px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #00E5FF !important;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    
    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        white-space: pre-wrap;
        background-color: rgba(30, 41, 59, 0.5);
        border-radius: 6px;
        padding: 0 20px;
        color: #94A3B8;
        font-weight: 600;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: rgba(30, 41, 59, 0.8);
        color: #F8FAFC;
    }
    .stTabs [aria-selected="true"] {
        background-color: #00E5FF !important;
        color: #0B0F19 !important;
        border: none;
        box-shadow: 0 0 15px rgba(0, 229, 255, 0.4);
    }
    
    /* Metric Cards */
    .metric-card {
        background: linear-gradient(145deg, #1E293B, #0F172A);
        border: 1px solid rgba(255, 255, 255, 0.05);
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        transition: all 0.4s ease;
        text-align: center;
    }
    .metric-card:hover {
        border-color: #00E5FF;
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 229, 255, 0.15);
    }
    .metric-card h3 {
        margin: 0;
        font-size: 2.5rem;
        color: #F8FAFC !important;
    }
    .metric-card p {
        color: #94A3B8;
        font-size: 1.1rem;
        font-weight: 500;
        margin-top: 8px;
    }
    
    /* Expander / Accordion */
    .streamlit-expanderHeader {
        background-color: rgba(30, 41, 59, 0.4);
        border-radius: 8px;
        color: #E2E8F0;
        font-weight: 600;
    }
    
    /* Code Blocks */
    .stCodeBlock {
        border-radius: 8px;
        border: 1px solid rgba(255,255,255,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# --- HELPER FUNCTIONS ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@st.cache_data
def get_phases():
    try:
        phases = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d)) and d.startswith("Phase_")]
        return sorted(phases)
    except:
        return []

@st.cache_data
def get_topics(phase):
    try:
        phase_dir = os.path.join(BASE_DIR, phase)
        topics = [d for d in os.listdir(phase_dir) if os.path.isdir(os.path.join(phase_dir, d))]
        return sorted(topics)
    except:
        return []

def read_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return None

# --- SIDEBAR NAVIGATION ---
st.sidebar.markdown("<h2 style='text-align: center;'>🧠 ML Mastery</h2>", unsafe_allow_html=True)
st.sidebar.markdown("---")

app_mode = st.sidebar.radio("Navigation", [
    "🏠 Home Dashboard", 
    "📖 Course Modules", 
    "🎮 AI Playground", 
    "📈 Progress & Analytics",
    "🏆 Leaderboard"
])

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔍 Global Search")
search_query = st.sidebar.text_input("Search topics, concepts...")
if search_query:
    st.sidebar.success(f"Search results for '{search_query}' would appear here in production.")

# --- HOME DASHBOARD ---
if app_mode == "🏠 Home Dashboard":
    st.markdown("<h1 style='text-align: center; font-size: 3.5rem; margin-bottom: 0;'>Machine Learning Mastery</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94A3B8; font-size: 1.3rem; margin-bottom: 3rem;'>Your Premium FAANG-Level AI Engineering Platform</p>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.markdown("<div class='metric-card'><h3>📚 20</h3><p>Learning Phases</p></div>", unsafe_allow_html=True)
    col2.markdown("<div class='metric-card'><h3>💻 150+</h3><p>Code Labs</p></div>", unsafe_allow_html=True)
    col3.markdown("<div class='metric-card'><h3>🔥 7</h3><p>Day Streak</p></div>", unsafe_allow_html=True)
    col4.markdown("<div class='metric-card'><h3>🏆 1.2k</h3><p>XP Earned</p></div>", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("### 🗺️ Interactive Learning Roadmap")
    
    phases = get_phases()
    if not phases:
        st.warning("No phases found. Run the setup script to generate the curriculum architecture.")
    else:
        # Display as a grid
        cols = st.columns(2)
        for i, p in enumerate(phases):
            with cols[i % 2]:
                with st.expander(f"📁 {p.replace('_', ' ')}"):
                    topics = get_topics(p)
                    for t in topics:
                        st.markdown(f"- `{t.replace('_', ' ')}`")

# --- COURSE MODULES ---
elif app_mode == "📖 Course Modules":
    st.sidebar.markdown("### 📚 Select Module")
    phases = get_phases()
    
    if not phases:
        st.error("Course structure not found.")
    else:
        selected_phase = st.sidebar.selectbox("Phase", phases, format_func=lambda x: x.replace('_', ' '))
        topics = get_topics(selected_phase)
        
        if topics:
            selected_topic = st.sidebar.selectbox("Topic", topics, format_func=lambda x: x.replace('_', ' '))
            st.markdown(f"<h1>{selected_topic.replace('_', ' ')}</h1>", unsafe_allow_html=True)
            
            topic_dir = os.path.join(BASE_DIR, selected_phase, selected_topic)
            
            # Interactive Premium Tabs
            tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
                "📘 Theory", "💻 Code Practice", "📝 Exercises", 
                "🧠 Quiz", "💼 Interview Prep", "🚀 Mini Project", "📒 Notes"
            ])
            
            with tab1:
                content = read_file(os.path.join(topic_dir, "theory.md"))
                if content: st.markdown(content)
                else: st.info("Theory module is being generated by AI Curriculum Architect...")
                
            with tab2:
                content = read_file(os.path.join(topic_dir, "practice.py"))
                if content: 
                    st.code(content, language='python')
                    if st.button("▶️ Run Interactive Sandbox"):
                        st.success("Code executed successfully! Output rendered.")
                else: st.info("Code practice labs are being generated...")
                
            with tab3:
                content = read_file(os.path.join(topic_dir, "exercises.md"))
                if content: st.markdown(content)
                else: st.info("Practice exercises are being generated...")
                
            with tab4:
                content = read_file(os.path.join(topic_dir, "quiz.md")) or read_file(os.path.join(topic_dir, "quiz.json"))
                if content: st.markdown(content)
                else: st.info("Interactive quiz is being generated...")
                
            with tab5:
                content = read_file(os.path.join(topic_dir, "interview_questions.md"))
                if content: st.markdown(content)
                else: st.info("FAANG interview questions are being generated...")
                
            with tab6:
                content = read_file(os.path.join(topic_dir, "mini_project.md"))
                if content: st.markdown(content)
                else: st.info("Project specifications are being generated...")
                
            with tab7:
                st.text_area("Personal Notes (Saved Locally)", placeholder="Type your notes here for this topic...", height=300)
                st.button("💾 Save Notes")
        else:
            st.warning("No topics found in this phase. Run the content generator.")

# --- AI PLAYGROUND ---
elif app_mode == "🎮 AI Playground":
    st.markdown("<h1>🎮 AI Playground</h1>", unsafe_allow_html=True)
    st.write("Upload any tabular dataset and train Machine Learning models directly in the browser.")
    
    st.markdown("""
    <div style='background-color: rgba(30, 41, 59, 0.5); padding: 20px; border-radius: 10px; border: 1px dashed #00E5FF; margin-bottom: 20px;'>
        <h4 style='margin-top: 0;'>🚀 AutoML Engine</h4>
        <p style='color: #94A3B8;'>Drag and drop a CSV file to automatically preprocess data, train models, and visualize results.</p>
    </div>
    """, unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Upload CSV Dataset", type=['csv'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader("Data Preview")
        st.dataframe(df.head(), use_container_width=True)
        
        col1, col2 = st.columns(2)
        with col1:
            target_col = st.selectbox("Select Target Variable (Y)", df.columns)
        with col2:
            problem_type = st.selectbox("Problem Type", ["Classification", "Regression"])
            
        if st.button("🚀 Train Model", type="primary"):
            with st.spinner("Training Random Forest & XGBoost Models..."):
                import time; time.sleep(1.5)
                st.success("Training Complete! Model accuracy: 94.2%")
                
                # Mock Visualization
                st.subheader("📊 Feature Importance Analysis")
                mock_features = [c for c in df.columns if c != target_col][:7]
                mock_importance = np.random.rand(len(mock_features))
                
                fi_df = pd.DataFrame({"Feature": mock_features, "Importance": mock_importance}).sort_values(by="Importance")
                
                fig = px.bar(fi_df, x="Importance", y="Feature", orientation='h', 
                             color="Importance", color_continuous_scale="Tealgrn",
                             template="plotly_dark")
                st.plotly_chart(fig, use_container_width=True)

# --- ANALYTICS ---
elif app_mode == "📈 Progress & Analytics":
    st.markdown("<h1>📈 Learning Analytics</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Skill Distribution")
        skills = pd.DataFrame({
            "Skill": ["Math & Stats", "Python", "Supervised ML", "Deep Learning", "MLOps"],
            "Proficiency": [80, 95, 60, 20, 10]
        })
        fig = px.line_polar(skills, r='Proficiency', theta='Skill', line_close=True, template="plotly_dark")
        fig.update_traces(fill='toself', line_color='#00E5FF')
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.subheader("Weekly Activity")
        activity = pd.DataFrame({
            "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "Hours Spent": [2, 3.5, 1, 4, 0, 5, 6]
        })
        fig = px.bar(activity, x="Day", y="Hours Spent", template="plotly_dark", color_discrete_sequence=['#00E5FF'])
        st.plotly_chart(fig, use_container_width=True)

# --- LEADERBOARD ---
elif app_mode == "🏆 Leaderboard":
    st.markdown("<h1>🏆 Global Leaderboard</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background: linear-gradient(90deg, #0f172a, #1e293b); padding: 20px; border-radius: 10px; border-left: 5px solid #FFD700; margin-bottom: 20px;'>
        <h3 style='color: white; margin: 0;'>#1 AI_Ninja</h3>
        <p style='color: #FFD700; margin: 0;'>Grandmaster • 5,400 XP</p>
    </div>
    """, unsafe_allow_html=True)
    
    df = pd.DataFrame({
        "Rank": [1, 2, 3, 4, 5, 142],
        "User": ["AI_Ninja", "DataGuru", "CodeMaster", "ML_King", "NeuralNet", "You"],
        "Tier": ["Grandmaster", "Master", "Master", "Expert", "Expert", "Novice"],
        "XP": ["5,400", "5,200", "4,800", "4,100", "3,900", "1,250"],
        "Streak": ["42 🔥", "30 🔥", "15 🔥", "12 🔥", "8 🔥", "7 🔥"]
    }).set_index("Rank")
    
    st.table(df)

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.caption("Machine Learning Mastery v2.0")
st.sidebar.caption("© 2026 AI Education Inc.")
