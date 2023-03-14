def main():
    print("Welcome to an email slicer")
    print("")

    email_input = input("Enter your input:")
    (username, domain) = email_input.split("@")
    (domain, extention) = domain.split(".")
    print("USERNAME ", username)
    print("DOMAIN ", domain)
    print("EXTENTION", extention)


main()
