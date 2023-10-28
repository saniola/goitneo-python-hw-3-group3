def input_error(func):
    def inner(*args, **kwargs):
        print(args)
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__ == "add_contact":
                return "Error: Invalid number of arguments. Use 'add [name] [phone number]'."
            elif func.__name__ == "change_contact":
                return "Error: Invalid number of arguments. Use 'change [name] [old phone number] [new phone number]."
            elif func.__name__ == "show_phone":
                return "Error: Invalid number of arguments. Use 'phone [name]'."
            elif func.__name__ == "show_all":
                return "Error: Use 'all' without arguments."
        except KeyError:
            if func.__name__ == "show_phone":
                name = args[0]
                return f"Error: Contact with name {name} not found."
            if func.__name__ == "show_all":
                return "Error: The contacts list is empty."
            if func.__name__ == "change_contact":
                phone = args[1]
                return f"Error: Phone {phone} not found in the record."
        except TypeError:
            if func.__name__ == "change_contact" or func.__name__ == "add_contact":
                return "Error: The phone number must be 10 digits"
    return inner
