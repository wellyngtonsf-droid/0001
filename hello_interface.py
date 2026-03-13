"""Simple Hello World interface for Streamlit."""


def render_streamlit_app() -> None:
    """Render the Streamlit page content."""
    import streamlit as st

    st.set_page_config(page_title="Seja Bem-Vindo Mundo", page_icon="👋", layout="centered")
    st.markdown(
        "<h1 style='color: black; font-weight: 700;'>seja bem vindo mundo</h1>",
        unsafe_allow_html=True,
    )


def main() -> None:
    """Run the app in Streamlit, or print a fallback message if unavailable."""
    try:
        render_streamlit_app()
    except ModuleNotFoundError:
        print("seja bem vindo mundo")


if __name__ == "__main__":
    main()
