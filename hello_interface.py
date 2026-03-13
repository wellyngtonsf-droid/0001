"""Simple Hello World interface for Streamlit."""


def render_streamlit_app() -> None:
    """Render the Streamlit page content."""
    import streamlit as st

    st.set_page_config(page_title="Hello World", page_icon="👋", layout="centered")
    st.title("👋 Hello World")
    st.write("This is a simple Hello World interface built with Streamlit.")


def main() -> None:
    """Run the app in Streamlit, or print a fallback message if unavailable."""
    try:
        render_streamlit_app()
    except ModuleNotFoundError:
        print("Hello World!")


if __name__ == "__main__":
    main()
