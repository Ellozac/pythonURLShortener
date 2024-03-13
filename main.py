import customtkinter
import requests
import pyperclip


class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")
        # Makes Floating Window for WM
        self.attributes('-type', 'dialog')
        self.textBox = customtkinter.CTkEntry(
            self, width=200, height=10)
        self.confirmButton = customtkinter.CTkButton(
            self, text="Copy and Shorten!", command=lambda: self.getShortUrl(self.textBox.get().strip()))

        self.shortened = customtkinter.CTkLabel(self, text="")
        self.textBox.pack(pady=10)
        self.confirmButton.pack(pady=20)
        self.shortened.pack()

    def getShortUrl(self, urlToShort: str) -> str:
        if urlToShort.startswith("https://") or urlToShort.startswith("http://"):
            pass
        else:
            urlToShort = "https://" + urlToShort
        ApiUrl = "https://cleanuri.com/api/v1/shorten"
        data = {
            "url": urlToShort
        }

        res = requests.post(ApiUrl, data=data)

        try:
            if res.json()["result_url"]:
                pyperclip.copy(res.json()["result_url"])
                self.shortened.configure(text=res.json()["result_url"])
                return res.json()["result_url"]
        except KeyError:
            self.shortened.configure(text="Please only enter VALID urls!")
            return "KeyError"


app = Main()
app.mainloop()
