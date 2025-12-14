"""
Personal Finance Coach - Landing Page
Clean, professional landing page using Streamlit's native components.
No sidebar, just header, hero, features, and footer.
"""
import streamlit as st

# Configure page - MUST be first
st.set_page_config(
    page_title="Personal Finance Coach - Your Path to Financial Freedom",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"  # Hide sidebar on landing
)

# Initialize Session State (Prevent KeyErrors)
if "guest_data" not in st.session_state:
    st.session_state.guest_data = {
        "snapshot": {},
        "assets": [],
        "liabilities": [],
        "goals": [],
        "analysis": {}
    }

# Hide sidebar completely on landing page
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* Remove padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 0rem;
    }
    
    /* Header styling */
    .header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem 2rem;
        color: white;
        margin: -2rem -2rem 2rem -2rem;
    }
    
    /* Hero section */
    .hero {
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
        border-radius: 10px;
        margin: 2rem 0;
    }
    
    /* Feature card */
    .feature-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        height: 100%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Footer */
    .footer {
        background: #f5f5f5;
        padding: 2rem;
        margin: 3rem -2rem 0 -2rem;
        text-align: center;
        border-top: 1px solid #e0e0e0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header">
    <h2 style="margin: 0;">💰 Finance AI Coach</h2>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <h1 style="font-size: 3rem; margin-bottom: 1rem;">Your Path to Financial Freedom</h1>
    <p style="font-size: 1.3rem; color: #666; margin-bottom: 2rem;">
        Analyze your finances, identify problems, and get a personalized action plan
    </p>
</div>
""", unsafe_allow_html=True)

# CTA Buttons
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🚀 Get Started Free", type="primary", use_container_width=True):
        st.switch_page("pages/1_onboarding.py")
    
    st.markdown("""
    <p style="text-align: center; margin-top: 1rem; color: #888;">
        ✓ No signup required &nbsp;&nbsp; ✓ 100% Free &nbsp;&nbsp; ✓ Privacy first
    </p>
    """, unsafe_allow_html=True)

# Features Section
st.markdown("---")
st.markdown("## ✨ Everything You Need to Build Wealth")
st.markdown("")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🧮 Smart Analysis</h3>
        <p>Instant calculations of net worth, debt ratios, and emergency fund status</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("")
    
    st.markdown("""
    <div class="feature-card">
        <h3>📈 Progress Tracking</h3>
        <p>Simple monthly check-ins to track your financial progress</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🪣 Bucket System</h3>
        <p>Auto-organize money into Emergency, Debt, Short-term, and Long-term buckets</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("")
    
    st.markdown("""
    <div class="feature-card">
        <h3>🤖 AI Assistant</h3>
        <p>Ask "Why this?" on any recommendation for detailed explanations</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>🎯 Action Plan</h3>
        <p>Get top 3 priority actions with monthly targets</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("")
    
    st.markdown("""
    <div class="feature-card">
        <h3>🔐 Privacy First</h3>
        <p>Self-reported data, no bank access required</p>
    </div>
    """, unsafe_allow_html=True)

# How It Works
st.markdown("---")
st.markdown("## 🛣️ How It Works")
st.markdown("")

step_col1, step_col2, step_col3, step_col4 = st.columns(4)

with step_col1:
    st.markdown("### 1️⃣")
    st.markdown("**Share Finances**")
    st.caption("Income, expenses, assets, debts, goals")

with step_col2:
    st.markdown("### 2️⃣")
    st.markdown("**Get Analysis**")
    st.caption("Net worth, debt health, savings rate")

with step_col3:
    st.markdown("### 3️⃣")
    st.markdown("**Receive Plan**")
    st.caption("Top 3 actions + monthly targets")

with step_col4:
    st.markdown("### 4️⃣")
    st.markdown("**Track Progress**")
    st.caption("Monthly check-ins + nudges")

# Final CTA
st.markdown("---")
st.markdown("")

cta_col1, cta_col2, cta_col3 = st.columns([1, 2, 1])
with cta_col2:
    st.markdown("""
    <div style="background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; border-radius: 10px; text-align: center; color: white;">
        <h2>Ready to Take Control of Your Finances?</h2>
        <p style="font-size: 1.1rem; margin-bottom: 1.5rem;">
            Join thousands who have already started their journey
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    if st.button("🚀 Get Started - It's Free!", type="primary", use_container_width=True, key="cta_bottom"):
        st.switch_page("pages/1_onboarding.py")

# Footer
st.markdown("""
<div class="footer">
    <p><strong>Personal Finance Coach</strong></p>
    <p style="color: #888; margin-top: 0.5rem;">
        <a href="#" style="color: #667eea; text-decoration: none;">Features</a> • 
        <a href="#" style="color: #667eea; text-decoration: none;">Privacy Policy</a> • 
        <a href="#" style="color: #667eea; text-decoration: none;">Terms</a> • 
        <a href="#" style="color: #667eea; text-decoration: none;">Contact</a>
    </p>
    <p style="color: #999; margin-top: 1rem; font-size: 0.9rem;">
        © 2025 Personal Finance Coach. All rights reserved.
    </p>
</div>
""", unsafe_allow_html=True)
