import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import Image
from data.database import db_insert, login_exist
import os


class NewAccount(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../images")
        self.img = ctk.CTkImage(Image.open(os.path.join(path, "reg.png")), size=(220, 220))
        self.label = ctk.CTkLabel(self, text="", image=self.img)
        self.label.pack()

        self.entry_1 = ctk.CTkEntry(self, width=220, height=50, corner_radius=25, border_width=2,
                                    fg_color="transparent",
                                    font=("Roboto", 17), placeholder_text="Имя пользователя", )
        self.entry_1.pack(padx=20, pady=10)

        self.entry_2 = ctk.CTkEntry(self, width=220, height=50, corner_radius=25, border_width=2,
                                    fg_color="transparent",
                                    font=("Roboto", 17), placeholder_text="Пароль", show="*")
        self.entry_2.pack(padx=20, pady=10)

        self.entry_3 = ctk.CTkEntry(self, width=220, height=50, corner_radius=25, border_width=2,
                                    fg_color="transparent",
                                    font=("Roboto", 17), placeholder_text="Подтвердите пароль", show="*")
        self.entry_3.pack(padx=20, pady=10)

        self.button = ctk.CTkButton(self, text="Регистрация", width=220, height=50, corner_radius=25, border_width=2,
                                    font=("Roboto", 17), fg_color="transparent", hover_color='#565B5E',
                                    command=self.register_func)
        self.button.pack(padx=20, pady=10)

    def register_func(self):
        if self.entry_1.get() == "" or self.entry_2.get() == "" or self.entry_3.get() == "":
            CTkMessagebox(title="Ошибка", message="Заполните все поля")
        elif len(self.entry_2.get()) < 6:
            CTkMessagebox(title="Ошибка", message="Пароль должен содержать не менее 6 символов")
        elif self.entry_2.get() != self.entry_3.get():
            CTkMessagebox(title="Ошибка", message="Пароли не совпадают")
        elif login_exist(self.entry_1.get()):
            CTkMessagebox(title="Ошибка", message="Такой логин уже существует")
        else:
            db_insert(self.entry_1.get(), self.entry_2.get())
            self.entry_1.delete(0, "end")
            self.entry_2.delete(0, "end")
            self.entry_3.delete(0, "end")
            self.button.focus()
            CTkMessagebox(title="Success", message="Регистрация прошла успешно")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.my_frame = NewAccount(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20)


if __name__ == '__main__':
    app = App()
    app.mainloop()