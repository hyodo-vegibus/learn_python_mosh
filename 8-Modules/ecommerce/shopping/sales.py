# from ecommerce.customer import contact
# from ..customer import contact


print("sales module is working!", __name__)


def calc_tax():
    print("Tax!")


def calc_shipping():
    pass


# contact.contactBook()

# The following works only in this file.
if __name__ == '__main__':
    print("sales started!")
