"""Simple Hello World interface compatible with Streamlit environments."""


def main() -> None:
    """Render a minimal Hello World interface."""
    try:
        import streamlit as st
    except Exception:
        print("Hello World!")
        return

    st.set_page_config(page_title="Hello World", page_icon="👋", layout="centered")
    st.title("👋 Hello World")
    st.write("Esta é uma interface simples em Python usando Streamlit.")


if __name__ == "__main__":
    main()
