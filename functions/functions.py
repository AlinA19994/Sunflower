import random
import string


class Functions:
    @staticmethod
    def random_number_between_range(Mylist):
        """
        Function Get list of elements and randon number between 0 and the length of the list
        :return: int between range
        """
        return random.randint(0, Mylist.count()-1)

    @staticmethod
    def random_name(length=6):
        """
        Function create random value from letters a-z ,A-Z and numbers 0-9
        Default length is: 6
        """
        characters = string.ascii_letters + string.digits
        random_name = ''.join(random.choices(characters, k=length))
        return random_name



