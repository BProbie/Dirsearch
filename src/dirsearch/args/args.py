import argparse

"""
The Class of the Args
"""
class Args:

    argumentParser = argparse.ArgumentParser("Args")

    def getArgs(self) -> argparse.Namespace:
        self.argumentParser.add_argument("-uri", "-url", "-u", dest="uri", type=str, required=False, help="请求网址" + " " + "https://www.baidu.com/")

        args = self.argumentParser.parse_args()

        return args