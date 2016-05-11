import subprocess
import os
import uuid
from time import sleep


def open_writer(new_screen_name):
    with open("entry_template.html", "r") as tmpl:
        tmpl_text = tmpl.read()

        name = "entry_" + str(uuid.uuid4())
        entry_name = "entries/" + name + ".html"
        text_name = "texts/" + name

        new_text = tmpl_text\
            .replace("{{screen}}", new_screen_name)\
            .replace("{{text}}", text_name)\

        with open(entry_name, "w+") as new_entry:
            new_entry.write(new_text)
        with open(text_name, "w+") as new_text:
            new_text.write("")

    subprocess.Popen(["chromium-browser", entry_name])


if __name__ == "__main__":
    screens = os.listdir("screens")
    while True:
        current_screens = os.listdir("screens")
        current_screens.sort()
        if screens != current_screens:
            screens = current_screens
            open_writer(screens[-1])
        sleep(1)
