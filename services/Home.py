import streamlit as st


st.set_page_config(page_title="StoryVerse",
                   page_icon="📖",
                   layout="wide")

st.title("StoryVerse")
st.subheader("Narrative Planning System for Writers and Authors")
st.write(
        """
    Welcome to StoryVerse.

    Create stories, manage characters,
    organize scenes, and visualize timelines.
    """
)
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button(
        "Let's Get Started",
        use_container_width=True
    ):
        st.switch_page("pages/1_Stories.py")
