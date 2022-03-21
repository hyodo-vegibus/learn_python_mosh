while True:  # infinite Loop!!
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break  # <-- important
