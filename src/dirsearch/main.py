from src.dirsearch.args.args import Args
from src.dirsearch.dirsearch.dirsearch import Dirsearch

"""The Entrance of the Main Program"""
if __name__ == "__main__": Dirsearch().main(Args().getArgs())