from model.model_group import Group
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of group", "file"])
except getopt.GetoptError as err:
    #getopt.usage()
    sys.exit(2)

n = 5
f = "data/group.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 #string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

test_data = [Group(name="Group name #2", header="Header", footer="footer")] + \
            [Group(name=random_string("name", 10), header=random_string("header", 20),
                   footer=random_string("footer", 20)) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))