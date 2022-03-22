def index():
    with open('templates/index.html') as template:
        return template.read()


def test():
    with open('templates/test.html') as template:
        return template.read()
