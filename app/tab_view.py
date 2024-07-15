import customtkinter as ctk
from app.new_accaunt import NewAccount
from app.login import Login

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class MyTabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # создание вкладок
        self.add("Вход в аккаунт")
        self.add("Регистрация")

        # добавление виджетов на вкладки
        tab_1_frame = Login(master=self.tab("Вход в аккаунт"))
        tab_1_frame.grid(row=0, column=0, padx=10, pady=10)

        tab_2_frame = NewAccount(master=self.tab("Регистрация"))
        tab_2_frame.grid(row=0, column=0, padx=10, pady=10)


class App(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

        self.geometry("+700+250")
        self.title("Вход в аккаунт")
        self.resizable(False, False)

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=(10, 20))


if __name__ == '__main__':
    app = App()
    app.mainloop()
