import streamlit as st
from PIL import Image

# Import the AI function from ai.py
from ai import analyze_skin


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Skin IQ | Skin analysis",
    page_icon="✦",
    layout="centered"
)


# ============================================================
# DESIGN
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(
            145deg,
            #fffaf5 0%,
            #f3eee8 100%
        );
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
        color: #A67C00;
        font-size: 3.6rem;
        letter-spacing: -0.04em;
        margin: 0.35rem 0 0.75rem;
    }

    .hero p {
        color: #9A6F00;
        font-size: 1.08rem;
        margin: 0 auto;
        max-width: 34rem;
    }

    .upload-note {
        color: #766a62;
        font-size: 0.9rem;
        text-align: center;
        margin-bottom: 1rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">Personal skin insight</div>
        <h1>Skin IQ</h1>
        <p>
            Upload a clear photo of your face and discover
            a simpler way to understand your skin.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# UPLOAD
# ============================================================

st.subheader("Start your skin check")

uploaded_image = st.file_uploader(
    "Choose a face photo to analyse",
    type=[
        "jpg",
        "jpeg",
        "png",
        "webp"
    ],
    accept_multiple_files=False
)

st.markdown(
    """
    <div class="upload-note">
        Use a well-lit, front-facing image for the clearest results.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# ANALYSIS
# ============================================================

if uploaded_image is not None:

    try:

        # Open uploaded image
        image = Image.open(uploaded_image)

        # Display uploaded image
        st.image(
            image,
            caption="Your photo is ready for analysis.",
            use_container_width=True
        )

        st.success(
            "Photo uploaded successfully."
        )

        # ----------------------------------------------------
        # RUN AI
        # ----------------------------------------------------

        with st.spinner(
            "Analysing your skin..."
        ):

            results = analyze_skin(image)


        # ----------------------------------------------------
        # RESULTS
        # ----------------------------------------------------

        st.subheader(
            "Your skin analysis"
        )

        for label, score in results.items():

            st.write(
                f"**{label}:** {score:.4f}"
            )


        # ----------------------------------------------------
        # HIGHEST RESULT
        # ----------------------------------------------------

        highest_label = max(
            results,
            key=results.get
        )

        highest_score = results[
            highest_label
        ]

        st.info(
            f"Highest model result: "
            f"**{highest_label}** "
            f"({highest_score:.4f})"
        )


        # ----------------------------------------------------
        # DISCLAIMER
        # ----------------------------------------------------

        st.markdown(
            """
            <div class="upload-note">
                Skin IQ provides AI-generated skin insights
                and is not a medical diagnosis.
            </div>
            """,
            unsafe_allow_html=True
        )


    except Exception as e:

        st.error(
            "Skin IQ could not analyse the image."
        )

        st.write(
            "Error details:"
        )

        st.exception(e)