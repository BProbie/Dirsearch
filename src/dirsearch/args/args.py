import argparse
from pathlib import Path

"""
The Class of the Args
"""
class Args:

    argumentParser = argparse.ArgumentParser("Args")

    def getArgs(self) -> argparse.Namespace:
        self.argumentParser.add_argument(
            "-uri", "-url", "-u",
            dest="uri",
            type=str,
            required=False,
            help="请求网址 https://www.baidu.com/")
        self.argumentParser.add_argument(
            "-dictionary", "-d",
            dest="dictionary",
            type=str,
            nargs="+",
            required=False,
            help="字典路径 ./dictionary/default")

        args = self.argumentParser.parse_args()

        if args.dictionary is not None:
            args.dictionary = [str(Path(d).resolve()) for d in args.dictionary]
        else:
            args.dictionary = [str(Path("./dictionary/default").resolve())]

        return args