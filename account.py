class Account:
    """
    A class representing an account object
    """

    def __init__(self, name: str) -> None:
        """
        Constructor that creates default values for each account object
        :param name: Account holder's first name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Method that increments the account balance by the specified amount
        :param amount: Amount for account balance to be incremented by
        :return: True or False if account balance was successfully incremented
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Method that decrements the account balance by the specified amount
        :param amount: Amount for account balance to be decremented by
        :return: True or False if account balance was successfully decremented
        """
        if amount <= 0 or self.__account_balance < amount:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Method that gets and returns the account balance
        :return: The account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method that gets and returns the account name
        :return: The account name
        """
        return self.__account_name
