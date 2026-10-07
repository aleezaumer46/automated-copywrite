import base64
import streamlit as st
import streamlit.components.v1 as components
from groq import Groq
from dotenv import load_dotenv
import os
from fpdf import FPDF

st.set_page_config(
    page_title="AI Copywriter Pro",
    page_icon="✍️",
    layout="centered"
)


theme = st.toggle("🌙 Dark Mode")

if theme:
    st.markdown("""
    <style>

    /* Dark Theme */

    .stApp{
        background:#121212;
        color:white;
    }

    h1,h2,h3,h4,h5,h6,p,label,span,div{
        color:white !important;
    }

    .stTextInput input,
    .stTextArea textarea{
        background:#1E1E1E !important;
        color:white !important;
        border:1px solid #555 !important;
    }

    section[data-testid="stSidebar"]{
        background:#1A1A1A;
    }

    .stButton > button,
    .stDownloadButton > button{
        background:#2563EB !important;
        color:white !important;
        border:none !important;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover{
        background:#1D4ED8 !important;
        color:white !important;
    }

    </style>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
    <style>

    /* Light Theme */

    .stApp{
        background:#F8F9FA;
        color:#212529;
    }

    h1,h2,h3,h4,h5,h6,p,label,span,div{
        color:#212529 !important;
    }

    header[data-testid="stHeader"]{
        background:#F8F9FA !important;
    }

    header[data-testid="stHeader"] button,
    [data-testid="stToolbar"] button{
        color:#212529 !important;
    }

    div[data-baseweb="select"] > div{
        background:#FFFFFF !important;
        border-color:#CED4DA !important;
    }

    div[data-baseweb="select"] *,
    div[data-baseweb="popover"] [role="option"]{
        color:#212529 !important;
    }

    div[data-baseweb="popover"] [role="option"]{
        background:#FFFFFF !important;
    }

    div[data-baseweb="popover"] [role="option"]:hover{
        background:#E9ECEF !important;
    }

    .stTextInput input,
    .stTextArea textarea{
        background:white !important;
        color:#212529 !important;
        border:1px solid #CED4DA !important;
    }

    section[data-testid="stSidebar"]{
        background:#F1F3F5;
    }

    .stButton > button,
    .stDownloadButton > button{
        background:#0D6EFD !important;
        color:white !important;
        border:none !important;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover{
        background:#0B5ED7 !important;
        color:white !important;
    }

    </style>
    """, unsafe_allow_html=True)

# =====================================
# Page Configuration
# =====================================


# =====================================
# Load Environment Variables
# =====================================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("Groq API Key not found!")
    st.stop()


client = Groq(api_key=api_key)


# =====================================
# Session History
# =====================================

if "history" not in st.session_state:
    st.session_state.history = []


# =====================================
# Header
# =====================================

st.markdown("""
# ✍️ AI Copywriter Pro

### Create high-converting marketing copy for social media, emails, and ads using AI.
""")


st.info(
    "🚀 Generate professional marketing copy for LinkedIn, Instagram, and Email in seconds."
)


st.markdown("---")


# =====================================
# Inputs
# =====================================

product_name = st.text_input("Product Name")

product_description = st.text_area(
    "Product Description"
)



# =====================================
# Sidebar
# =====================================

with st.sidebar:

    st.header("⚙️ Settings")


    platform = st.selectbox(
        "Select Platform",
        ["LinkedIn","Instagram","Email"]
    )


    tone = st.selectbox(
        "Select Tone",
        [
            "Professional",
            "Friendly",
            "Casual",
            "Formal",
            "Persuasive",
            "Excited"
        ]
    )


    temperature = st.slider(
        "Temperature",
        0.0,
        1.0,
        0.7,
        0.1
    )


    top_p = st.slider(
        "Top P",
        0.0,
        1.0,
        0.9,
        0.1
    )


    st.divider()

    st.caption("🤖 Powered by Groq + Qwen 3.8 27B")


    st.divider()

    st.subheader("📜 Copy History")


    for i,item in enumerate(
        reversed(st.session_state.history),
        1
    ):

        with st.expander(f"Copy {i}"):

            st.write(item)



# =====================================
# Buttons
# =====================================

col1, col2 = st.columns(2)


with col1:

    generate = st.button(
        "🚀 Generate Marketing Copy",
        use_container_width=True
    )


with col2:

    regenerate = st.button(
        "🔄 Regenerate",
        use_container_width=True
    )



# =====================================
# AI Generation
# =====================================


if generate or regenerate:


    if not product_name or not product_description:

        st.warning(
            "Please enter Product Name and Product Description."
        )

        st.stop()



    prompt = f"""

You are an expert marketing copywriter.

Create 3 different high-quality marketing copy variations.

Variation 1:
Variation 2:
Variation 3:


Product Name:
{product_name}


Product Description:
{product_description}


Platform:
{platform}


Tone:
{tone}


Instructions:
- Match the platform style.
- Use selected tone.
- Keep content engaging.
- Create 3 unique variations.
- Add hashtags for LinkedIn and Instagram.
- For Email add Subject and Body.

"""


    with st.spinner(
        "🤖 AI is creating your marketing copy..."
    ):


        try:
            response = client.chat.completions.create(
                model="qwen/qwen3.8-27b",
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                top_p=top_p,
            )
        except Exception as error:
            st.error(f"Could not generate copy: {error}")
            st.stop()



    output=response.choices[0].message.content



    st.session_state.history.append(output)



    if len(st.session_state.history)>5:

        st.session_state.history.pop(0)



    st.success(
        "✅ Marketing copy generated successfully!"
    )

    st.subheader(f"{platform} Marketing Copy")

    st.write(output)

    encoded_output = base64.b64encode(output.encode("utf-8")).decode("ascii")

    components.html(
        f"""
        <button
        onclick="navigator.clipboard.writeText(new TextDecoder().decode(Uint8Array.from(atob('{encoded_output}'), c => c.charCodeAt(0))))"
        style="
            background-color:#4CAF50;
            color:white;
            border:none;
            padding:10px 18px;
            border-radius:8px;
            cursor:pointer;
            font-size:16px;
        ">
        📋 Copy Response
    </button>
    """,
    height=60,
)

    # =============================
    # Statistics
    # =============================

    st.divider()


    st.write(
        f"📝 Words: {len(output.split())}"
    )


    st.write(
        f"🔠 Characters: {len(output)}"
    )



    # =============================
    # Downloads
    # =============================

    st.divider()
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, output.encode("latin-1", "ignore").decode("latin-1"))
    pdf_bytes = bytes(pdf.output())

    st.download_button(
        "📥 Download TXT",
        data=output,
        file_name="marketing_copy.txt",
        mime="text/plain",
        use_container_width=True
        )
    
    st.download_button(
        "📄 Download PDF",
        data=pdf_bytes,
        file_name="marketing_copy.pdf",
        mime="application/pdf",
        use_container_width=True
        )