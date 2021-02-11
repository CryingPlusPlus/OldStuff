import pyperclip, re

emailRegex = re.compile(r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+\.[a-zA-Z]{2,3})", re.VERBOSE)
end = '\n'.join(emailRegex.findall(pyperclip.paste()))
pyperclip.copy(end)
