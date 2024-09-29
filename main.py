from get_urls import get_urls
from get_contents import get_contents

clh_home = "https://www.redhat.com/en/command-line-heroes"

if __name__ == '__main__':
    get_urls(clh_home)
    get_contents()
