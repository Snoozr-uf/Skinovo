import streamlit as st

st.set_page_config(page_title="Skinovo | Skin analysis", page_icon="✦", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(145deg, #fffaf5 0%, #f3eee8 100%);
    }
    .hero {
        padding: 3.5rem 0 1.5rem;
        text-align: center;
    }
    .eyebrow {
        color: #9b6246;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.16em;
        text-transform: uppercase;
    }
    .hero h1 {
        color: #2f2925;
        font-size: 3.6rem;
        letter-spacing: -0.04em;
        margin: 0.35rem 0 0.75rem;
    }
    .hero p {
        color: #6f625a;
        font-size: 1.08rem;
        margin: 0 auto;
        max-width: 34rem;
    }
    .upload-note {
        color: #766a62;
        font-size: 0.9rem;
        text-align: center;
    }
    </style>
    <div class="hero">
        <div class="eyebrow">Personal skin insight</div>
        <h1>Skinovo</h1>
        <p>Upload a clear photo of your face and discover a simpler way to understand your skin.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.subheader("Start your skin check")
uploaded_image = st.file_uploader(
    "Choose a face photo to analyse",
    type=["jpg", "jpeg", "png", "webp"],
    accept_multiple_files=False,
)
st.markdown(
    '<div class="upload-note">Use a well-lit, front-facing image for the clearest results.</div>',
    unsafe_allow_html=True,
)

if uploaded_image is not None:
    st.image(uploaded_image, caption="Your photo is ready for analysis.", use_container_width=True)
    st.success("Photo uploaded successfully. Skin analysis will appear here next.")
