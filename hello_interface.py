import tkinter as tk


def main() -> None:
    janela = tk.Tk()
    janela.title("Hello World")
    janela.geometry("300x120")

    mensagem = tk.Label(janela, text="Hello World!", font=("Arial", 18))
    mensagem.pack(expand=True)

    janela.mainloop()


if __name__ == "__main__":
    main()
