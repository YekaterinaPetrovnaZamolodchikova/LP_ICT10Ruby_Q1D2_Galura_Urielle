from pyscript import document

def generate_message(event):
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    document.getElementById("output").innerText = ""

    message = f"""Student Profile:\nName: \"{name}\"\nAge:\t{age}\nSchool: {school}\nWelcome to your profile showcase!"""
    document.getElementById("output").innerText = message
