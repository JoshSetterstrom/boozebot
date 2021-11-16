import yagmail, json

##Sends email to desired recipient
def send_email(site, elements):
    with open("./data/sensitive.json", "r") as file:
        data = json.load(file)

    contents = [(f"""
        <html>
            <body>
                <div style="display:block;max-width:50vw">
                    {elements}
                </div>
            </body>
        </html>
        """)
    ]

    yagmail.SMTP(f"{data['bot']['user']}", f"{data['bot']['pass']}").send(
        to=f"{data['recipient']}",
        subject=f"{site} has updated their stock.",
        contents=contents)