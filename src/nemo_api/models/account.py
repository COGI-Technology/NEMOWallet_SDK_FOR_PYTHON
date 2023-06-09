import pprint
from decimal import Decimal
from nemo_api.configuration import BaseConfiguration
from eth_utils import is_address
from nemo_api.function import parse_decimal

class AccountBalance(object):
    """
    Attributes:
      api_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    api_types = {
        'account': 'str',
        'balance': 'str',
        'available_balance': 'str',
        'pending_balance': 'str',
        'pending_claim': 'str'
    }
    attribute_map = {
        'account': 'account',
        'balance': 'balance',
        'available_balance': 'available_balance',
        'pending_balance': 'pending_balance',
        'pending_claim': 'pending_claim'
    }

    def __init__(
        self,
        account=None,
        balance=None,
        available_balance=None,
        pending_balance=None,
        pending_claim=None,
        local_vars_configuration=None
    ):  # noqa: E501
        # type: (str, Decimal, Decimal, Decimal, Decimal, BaseConfiguration) -> None
        if local_vars_configuration is None:
            local_vars_configuration = BaseConfiguration()
        self.local_vars_configuration = local_vars_configuration

        self._account = None
        self._balance = None
        self._available_balance = None
        self._pending_balance = None
        self._pending_claim = None

        if account is not None:
            self.account = account
        if balance is not None:
            self.balance = balance
        if available_balance is not None:
            self.available_balance = available_balance
        if pending_balance is not None:
            self.pending_balance = pending_balance
        if pending_claim is not None:
            self.pending_claim = pending_claim

    @property
    def account(self):
        """Gets the account of this AccountBalance.  # noqa: E501

        Account is an Ethereum address  # noqa: E501

        :return: The Ethereum address of this AccountBalance.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this AccountBalance.

        Account is an Ethereum address  # noqa: E501

        :param account: The Ethereum address of this AccountBalance.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and not is_address(account):
            raise ValueError("Not an Ethereum address: {0}".format(account))
        self._account = account

    @property
    def balance(self):
        """Gets the balance of this AccountBalance.  # noqa: E501

        Balance  # noqa: E501

        :return: The balance of this AccountBalance.  # noqa: E501
        :rtype: str
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this AccountBalance.

        Balance  # noqa: E501

        :param balance: The balance of this AccountBalance.  # noqa: E501
        :type: str
        """
        self._balance = parse_decimal(balance) if self.local_vars_configuration.client_side_validation else balance

    @property
    def available_balance(self):
        """Gets the available balance of this AccountBalance.  # noqa: E501

        Available balance  # noqa: E501

        :return: The Available balance of this AccountBalance.  # noqa: E501
        :rtype: str
        """
        return self._available_balance

    @available_balance.setter
    def available_balance(self, available_balance):
        """Sets the available balance of this AccountBalance.

        Available balance  # noqa: E501

        :param available_balance: The available balance of this AccountBalance.  # noqa: E501
        :type: str
        """
        self._available_balance = parse_decimal(available_balance) if self.local_vars_configuration.client_side_validation else available_balance

    @property
    def pending_balance(self):
        """Gets the pending balance of this AccountBalance.  # noqa: E501

        Pending balance  # noqa: E501

        :return: The Pending balance of this AccountBalance.  # noqa: E501
        :rtype: str
        """
        return self._pending_balance

    @pending_balance.setter
    def pending_balance(self, pending_balance):
        """Sets the pending balance of this AccountBalance.

        Pending balance  # noqa: E501

        :param pending_balance: The pending balance of this AccountBalance.  # noqa: E501
        :type: str
        """
        self._pending_balance = parse_decimal(pending_balance) if self.local_vars_configuration.client_side_validation else pending_balance

    @property
    def pending_claim(self):
        """Gets the pending claim of this AccountBalance.  # noqa: E501

        Pending claim  # noqa: E501

        :return: The Pending claim of this AccountBalance.  # noqa: E501
        :rtype: str
        """
        return self._pending_claim

    @pending_claim.setter
    def pending_claim(self, pending_claim):
        """Sets the pending claim of this AccountBalance.

        Pending claim  # noqa: E501

        :param pending_claim: The Pending claim of this AccountBalance.  # noqa: E501
        :type: str
        """
        self._pending_claim = parse_decimal(pending_claim) if self.local_vars_configuration.client_side_validation else pending_claim


    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.api_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AccountBalance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountBalance):
            return True

        return self.to_dict() != other.to_dict()