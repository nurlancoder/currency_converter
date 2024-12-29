import tkinter as tk
from tkinter import messagebox
import requests

def convert_currency():
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    amount = amount_var.get()

    if not amount.replace('.', '', 1).isdigit():
        messagebox.showerror("Hata", "Geçerli bir miktar girin.")
        return

    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)

    if response.status_code != 200:
        messagebox.showerror("Hata", "API bağlantısı başarısız!")
        return

    data = response.json()
    rate = data["rates"].get(to_currency, None)

    if rate:
        result = float(amount) * rate
        result_label.config(
            text=f"{amount} {from_currency} = {result:.2f} {to_currency}")
    else:
        messagebox.showerror("Hata", "Döviz kuru bulunamadı!")

window = tk.Tk()
window.title("Para Birimi Dönüştürücü")
window.geometry("500x400")
window.resizable(False, False)
window.configure(bg="#f0f0f5")

amount_var = tk.StringVar()
from_currency_var = tk.StringVar(value="USD")
to_currency_var = tk.StringVar(value="EUR")

tk.Label(window, text="Miktar:", font=("Arial", 12), bg="#f0f0f5").pack(pady=10)
tk.Entry(window, textvariable=amount_var, font=("Arial", 12), width=25).pack(pady=5)

tk.Label(window, text="Kaynak Para Birimi:", font=("Arial", 12), bg="#f0f0f5").pack(pady=10)
from_currency_menu = tk.OptionMenu(
    window, from_currency_var, "USD", "EUR", "TRY", "GBP", "JPY", "RUB", "AZN", "AED"
)
from_currency_menu.pack(pady=5)

tk.Label(window, text="Hedef Para Birimi:", font=("Arial", 12), bg="#f0f0f5").pack(pady=10)
to_currency_menu = tk.OptionMenu(
    window, to_currency_var, "USD", "EUR", "TRY", "GBP", "JPY", "RUB", "AZN", "AED"
)
to_currency_menu.pack(pady=5)

tk.Button(
    window, text="Dönüştür", command=convert_currency, font=("Arial", 12),
    bg="#007acc", fg="white", width=15, height=1
).pack(pady=20)

result_label = tk.Label(window, text="", font=("Arial", 16, "bold"), bg="#f0f0f5")
result_label.pack(pady=10)

window.mainloop()
