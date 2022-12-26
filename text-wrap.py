import textwrap

def wrap(string, max_width):
    wraped = textwrap.fill(string,max_width)
    return wraped

if __name__ == '__main__':