

def reader_func(txt_file):

        try:
            with open(txt_file, "r", encoding="utf-8") as file:
                lines = file.readlines()
            print(f"სტრიქონები: {len(lines)}")

            words = 0
            for line in lines:
                words += len(line.split())
            print(f"სიტყვები: {words}")

            symbols = 0
            for line in lines:
                symbols += len(line)
            print(f"სიმბოლოები: {symbols}")

        except FileNotFoundError:
            print("File not found")


reader_func("data.txt")



















































































