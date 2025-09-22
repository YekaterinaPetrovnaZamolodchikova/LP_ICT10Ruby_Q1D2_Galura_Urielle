from pyscript import when, display, document

@when("click", "#make-card")
def create_card(event):
    nickname = document.querySelector("#nickname").value
    hobby = document.querySelector("#hobby").value
    dream = document.querySelector("#dream").value

    document.querySelector("#output").innerText = ""

    card = f"""
    Personal Info 
    Nickname: {nickname}
    Hobby: {hobby}
    Dream Job: {dream}

    In Sentence:
    {nickname} loves spending their free time with {hobby}, and hopes to work someday as a/an {dream}.
    """

    display(card, target="output")
