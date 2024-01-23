"""find all"""
"""name: Steve Martin"""
"""tag:life"""
"""tags:life,live"""
"""exit"""

from models import Author, Quote


def find_tag(tag):
    quote = Quote.objects(tags=tag)
    if quote:
        quotes = Quote.objects(tags=tag)
        list_quote = []
        for quote in quotes:
            list_quote.append(quote["quote"])
        return list_quote
    else:
        return None


def find_name(name):
    author = Author.objects(fullname=name).first()
    if author:
        quotes = Quote.objects(author=author)
        quote_list = []
        for quote in quotes:
            quote_list.append(quote["quote"])
        return quote_list

    else:
        return None


def find_all():
    quotes = Quote.objects()
    if quotes:
        for quote in quotes:
            print(quote.to_mongo().to_dict())
    else:
        print(f"Table is empty\n")


def main():
    while True:
        command = str(input("Enter command (name, tag, tags, exit): "))
        if command.strip().lower() == "exit":
            break
        if command.strip().lower() == "find all":
            find_all()
            continue

        try:
            command_key = command.split(":", maxsplit=1)[0].strip()
            command_value = command.split(":", maxsplit=1)[1].strip()
        except IndexError as err:
            print("Error:", err)
            print(
                "List of valid commands(examples):\
                    nname: Steve Martin\n\
                    tag:life\ntags:life,live\nexit"
            )
            continue

        if command_key == "name":
            res = find_name(command_value)

            if res is None:
                print(f"such a name: {command_value} does not exist\n")
                continue

            if len(res) == 1:
                res = "".join(res)
                print(f"Quote that said {command_value}:\n\t{res}\n")
                continue
            print(f"All quote that said {command_value}:\n")
            for _ in res:
                print(f"\t{quote}")

        elif command_key == "tag":
            res = find_tag(command_value)

            if res is None:
                print(f"this tag: {command_value} does not exist\n")
                continue

            if len(res) == 1:
                res = "".join(res)
                print(f"Quote with tag {command_value}:\n\t{res}\n")
                continue

            print(f"All quotes with tag {command_value}:\n")
            for _ in res:
                print(f"\t{quote}")

        elif command_key == "tags":
            value = [val.strip() for val in command_value.split(",")]

            res_list = []
            for tag in value:
                res = find_tag(tag)

                if res in res_list:
                    continue
                res_list.append(res)

                if res is None:
                    print(f"this tag: {tag} does not exist\n")
                    continue

            for quote in res_list:
                if quote is None:
                    continue
                print("\t", "\n\t".join(quote), "\n")


if __name__ == "__main__":
    try:
        main()

    except ConnectionError as ce:
        print(f"Error connecting to the database: {ce}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
