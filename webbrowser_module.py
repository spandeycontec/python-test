import webbrowser
search = input("Enter keyword to search.: ").replace(" ", "+")
webbrowser.open("https://www.google.com/search?q="+search)