if __name__ == "__main__":

    with open("txt.txt", "r", encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line: break
            print(line.strip())