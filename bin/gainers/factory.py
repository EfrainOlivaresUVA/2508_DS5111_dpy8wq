import yahoo as yg
import wsj as wg


class GainerFactory:
    def __init__(self):
        pass

    def get_handler(self, fname):
        if fname.startswith('ygainer'):
            return yg.GainerYahoo()
        elif fname.startswith('wsjgainer'):
            return wg.GainerWSJ()
        else:
            raise Exception(f"Unrecognized file type {fname}")

