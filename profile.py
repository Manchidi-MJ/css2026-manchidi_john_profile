import streamlit as st
from datetime import datetime

# ───────────────────────────────────────────────
# PAGE CONFIG
# ───────────────────────────────────────────────
st.set_page_config(
    page_title="Magaseng John Manchidi – MSc Cybersecurity",
    page_icon="🎓🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ───────────────────────────────────────────────
# CUSTOM CSS
# ───────────────────────────────────────────────
st.markdown("""
    <style>
    .main-header {
        font-size: 3.2rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #1e40af, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.3rem;
    }
    .sub-header {
        font-size: 1.8rem;
        color: #1e40af;
        border-bottom: 4px solid #60a5fa;
        padding-bottom: 0.5rem;
        margin: 2.2rem 0 1.2rem;
    }
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ───────────────────────────────────────────────
# SIDEBAR
# ───────────────────────────────────────────────
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/student-male.png", width=100)
    st.title("Magaseng John Manchidi")
    st.markdown("**MSc Cybersecurity Candidate**")

    st.divider()

    st.markdown("**Navigation**")
    page = st.radio(
        "Go to",
        ["🏠 Home", "🎓 Education", "🛠 Skills", "🔬 Research", "📂 Projects", "📬 Contact"],
        index=0
    )

    st.divider()
    st.caption("Polokwane, Limpopo • South Africa")
    st.caption(f"Local time: {datetime.now().strftime('%Y-%m-%d %H:%M SAST')}")
    st.caption("Profile last updated: Feb 2026")


# ───────────────────────────────────────────────
# HEADER
# ───────────────────────────────────────────────
st.markdown('<div class="main-header">Magaseng John Manchidi</div>', unsafe_allow_html=True)
st.markdown(
    '<p style="text-align:center; font-size:1.45rem; color:#64748b; margin-bottom:2rem;">'
    'MSc Cybersecurity Student  •  Researcher  •  Software Developer</p>',
    unsafe_allow_html=True
)


# ───────────────────────────────────────────────
# PAGES
# ───────────────────────────────────────────────
if page == "🏠 Home":
    col_left, col_right = st.columns([1, 3])

    with col_left:
        # Upload your photo to GitHub repo and update filename here
        st.image(
            "My Picture.jpg",
            caption="Magaseng John Manchidi",
            use_container_width=True
        )

    with col_right:
        st.markdown('<div class="sub-header">About Me</div>', unsafe_allow_html=True)
        st.markdown("""
        Master's student in **Cybersecurity** at the **University of Limpopo**  
        with strong interest in practical security solutions, defensive technologies  
        and protecting digital systems — especially in the South African context.

        Academic background:
        • BSc Computer Science and Statistics – University of Limpopo
        • BSc Honours in Computer Science – University of Limpopo

        Current focus:
        • Cybersecurity fundamentals & applied security
        • Threat detection & incident response
        • Secure software development practices
        • Interactive tools for security awareness and education
        """)

        st.info("Open to collaboration, internships, project ideas or discussions!")


elif page == "🎓 Education":
    st.markdown('<div class="sub-header">Education</div>', unsafe_allow_html=True)

    st.subheader("MSc Cybersecurity")
    st.caption("University of Limpopo • In progress • 2025 – present")
    st.markdown("Research direction under development – focus on applied cybersecurity")

    st.subheader("BSc Honours in Computer Science")
    st.caption("University of Limpopo • Completed")
    st.markdown("Advanced topics + mini-dissertation/project")

    st.subheader("BSc Computer Science and Statistics")
    st.caption("University of Limpopo • Completed")
    st.markdown("""
    Foundation in:
    • Programming & data structures
    • Databases & operating systems
    • Statistics, probability, data analysis
    """)


elif page == "🛠 Skills":
    st.markdown('<div class="sub-header">Technical Skills</div>', unsafe_allow_html=True)

    skills = [
        ("Python",               88, "scripting • security tools • automation"),
        ("Streamlit",            85, "interactive dashboards & security prototypes"),
        ("Pandas / NumPy",       82, "data manipulation & log analysis"),
        ("Git & GitHub",         78, "version control"),
        ("SQL",                  72, "database querying & security"),
        ("JavaScript / HTML/CSS", 60, "frontend basics"),
        ("Cybersecurity basics", 65, "networking, encryption, vulnerability scanning"),
        ("Linux / CLI",          75, "system hardening & forensics"),
    ]

    cols = st.columns(3)
    for i, (name, pct, desc) in enumerate(skills):
        with cols[i % 3]:
            st.markdown(f"**{name}**")
            st.progress(pct / 100)
            st.caption(desc)


elif page == "🔬 Research":
    st.markdown('<div class="sub-header">Cybersecurity Research Interests</div>', unsafe_allow_html=True)

    for item in [
        "Cyber threat detection and prevention in resource-constrained environments",
        "Secure software development lifecycle (SSDLC) practices",
        "Incident response and digital forensics tools",
        "Cybersecurity awareness & education platforms",
        "Network security & intrusion detection systems",
        "Privacy-preserving technologies & ethical hacking approaches",
        "Applications of machine learning in cybersecurity (anomaly detection, malware classification)",
    ]:
        st.markdown(f"• {item}")

    st.divider()
    st.subheader("Master's Research (in progress)")
    st.info("""
    Topic under discussion with supervisor at the University of Limpopo.

    Possible directions:
    • Lightweight security monitoring solutions for small organizations
    • User-centric cybersecurity awareness tools
    • Threat intelligence sharing mechanisms in African context
    • Applied cryptography or secure protocol implementations
    """)


elif page == "📂 Projects":
    st.markdown('<div class="sub-header">Selected Projects</div>', unsafe_allow_html=True)

    with st.expander("FinTrack SA – Personal Finance Tracker (ZAR)", expanded=True):
        st.markdown("""
        • Budgeting & expense tracking dashboard  
        • Features: transactions, budgets, accounts, savings goals  
        • Stack: Streamlit, Pandas, Plotly  
        • Security considerations: input validation, secure session handling
        """)
        if st.button("Show celebration", key="fintrack-celebration"):
            st.balloons()

    with st.expander("Other work / university projects"):
        st.markdown("""
        • Data analysis notebooks  
        • Command-line utilities  
        • Academic mini-projects & assignments  
        • Honours research component
        """)


elif page == "📬 Contact":
    st.markdown('<div class="sub-header">Get in Touch</div>', unsafe_allow_html=True)

    left, right = st.columns([3, 2])

    with left:
        with st.form("contact"):
            name    = st.text_input("Name")
            email   = st.text_input("Email")
            subject = st.text_input("Subject")
            msg     = st.text_area("Message", height=140)

            if st.form_submit_button("Send"):
                if not all([name, email, msg]):
                    st.warning("Please complete all required fields.")
                else:
                    st.success("Thank you! (Demo only – no email was sent)")
                    st.caption("In production this could send email or save to database")

    with right:
        st.markdown("**Connect**")
        st.markdown("• LinkedIn → [Magaseng John Manchidi](https://www.linkedin.com/in/magaseng-john-manchidi-920442255/)")
        st.markdown("• GitHub   → [Manchidi-MJ](https://github.com/Manchidi-MJ)")
        st.markdown("• Email    → johnmanchidi@gmail.com")
        st.markdown(" ")
        st.markdown("Polokwane, Limpopo • South Africa")


# Footer
st.markdown("---")
st.caption(f"© {datetime.now().year} Magaseng John Manchidi • Built with Streamlit")
