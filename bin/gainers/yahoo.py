from base import GainerBase

class GainerYahoo(GainerBase):
    def __init__(self):
        pass

    def download_html(self):
        print("Yahoo html download")

    def extract_csv(self):
        print("Yahoo csv create")

    def normalize_data(self):
        print("Yahoo normalize csv")


if __name__=="__main__":
    import sys
    assert len(sys.argv) == 2, "Please pass in one of 'html', 'csv', 'normalize'"
    function = sys.argv[1]
    valid_functions = ['html', 'csv', 'normalize']
    assert function in valid_functions, f"Expected one of {valid_functions} but got {function}"

    gainer = GainerYahoo()

    if function == 'html':
        gainer.download_html()
    elif function == 'csv':
        gainer.extract_csv()
    elif function == 'normalize':
        gainer.normalize_data()
