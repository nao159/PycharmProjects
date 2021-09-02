def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'

    return wrapper


def make_emphasize(function):
    def wrapper():
        return f"<em>{function()}</em>"

    return wrapper


def green_text(function):
    def wrapper():
        return f'<h1 style=color: "green">{function}</h1>'

    return wrapper
