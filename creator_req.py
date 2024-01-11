import subprocess
import re

def create_requirements():
    word = str(subprocess.check_output(["pip", "freeze"]))
    pattern = r"(?:b')*(.*?)==(?:.*?)\\r\\n"
    res = re.findall(pattern=pattern, string=word)

    strres = '\n'.join(res)

    with open('requirements.txt', 'w') as f:
        f.write(strres)


if __name__=='__main__':
    create_requirements()


