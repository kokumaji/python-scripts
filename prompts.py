accepted_answers = ["1", "y", "yes", "0", "n", "no"]

def yesno(msg: str):
    response = input(f"{msg} [y/N] ")
    response = response.lower()

    if(response in accepted_answers):
        if(accepted_answers.index(response) < 3):
            return 1
        else:
            return 0
    else:
        print(f"Invalid Option '{response}'. Please try again.")
        yesno(msg)