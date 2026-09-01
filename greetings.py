def greet(name, greeting="Hello"):
    if not name:
        raise ValueError("name must not be empty")
    return f"{greeting}, {name}!"
