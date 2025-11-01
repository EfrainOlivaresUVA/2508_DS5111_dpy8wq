"""
Process gainers using two design patterns for a demo.

We'll use the Template pattern to ways processes.

We'll then use a factory method so we don't have to worry about the names of the files.
"""

from abc import ABCMeta, abstractmethod
import sys
sys.path.append('./bin/gainers')
import bin.gainers.factory as gf

class TemplateClass(metaclass=ABCMeta):
    def __init__(self, fname):
        pass

    @abstractmethod
    def create_csv(self):
        pass

    @abstractmethod
    def normalize(self):
        pass

    def template_method(self):
        print("Defining the Algorithm. Create the csv, then normalize it")
        self.create_csv()
        self.normalize()


class TwoStepClass(TemplateClass):
    def __init__(self, fname):
        self.fname = fname
        self.handler = gf.GainerFactory().get_handler(fname)

    def create_csv(self):
        self.handler.extract_csv()

    def normalize(self):
        self.handler.normalize_data()


class Client:
    def main(self, fname):
        self.concreate = TwoStepClass(fname)
        self.concreate.template_method()

if __name__=="__main__":
    import sys
    assert len(sys.argv) == 2
    fname = sys.argv[1]

    client = Client()
    client.main(fname)
