import pprint
from nemo_api.configuration import BaseConfiguration

class NemoIdAccount(object):
    """
    Attributes:
      api_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    api_types = {
        'sub': 'str',
        'email': 'str',
        'email_verified': 'bool',
        'name': 'str',
        'gender': 'str',
        'birthday': 'str',
        'profile_picture': 'str',
        'public_key': 'str',
        'redirect_uri': 'str',
        'client_id': 'str',
        'access_token': 'str',
        'expires_in': 'int',
        'id_token': 'str',
        'refresh_token': 'str',
        'token_type': 'str',
        'google_two_factor_authentication': 'bool',
        'fund_password': 'bool',
        'signature': 'dict(str, str)',
        'nemo_address': 'str',
        'wallet_address': 'list[str]'
    }
    attribute_map = {
        'sub': 'sub',
        'email': 'email',
        'email_verified':
        'email_verified',
        'name': 'name',
        'gender': 'gender',
        'birthday': 'birthday',
        'profile_picture': 'profile_picture',
        'public_key': 'public_key',
        'redirect_uri': 'redirect_uri',
        'client_id': 'client_id',
        'access_token': 'access_token',
        'expires_in': 'expires_in',
        'id_token': 'id_token',
        'refresh_token': 'refresh_token',
        'token_type': 'token_type',
        'google_two_factor_authentication': 'google_two_factor_authentication',
        'fund_password': 'fund_password',
        'signature': 'signature',
        'nemo_address': 'nemo_address',
        'wallet_address': 'wallet_address'
    }

    def __init__(
        self,
        sub=None,
        email=None,
        email_verified=None,
        name=None,
        gender=None,
        birthday=None,
        profile_picture=None,
        public_key=None,
        redirect_uri=None,
        client_id=None,
        access_token=None,
        expires_in=None,
        id_token=None,
        refresh_token=None,
        token_type=None,
        google_two_factor_authentication=None,
        fund_password=None,
        signature=None,
        nemo_address=None,
        wallet_address=None,
        local_vars_configuration=None
    ):  # noqa: E501
        # type: (str, str, bool, str, str, str, str, str, str, str, str, int, str, str, str, bool, bool, dict(str, str), str, list[str], BaseConfiguration) -> None
        if local_vars_configuration is None:
            local_vars_configuration = BaseConfiguration()
        self.local_vars_configuration = local_vars_configuration

        self._sub=None,
        self._email=None,
        self._email_verified=None,
        self._name=None,
        self._gender=None,
        self._birthday=None,
        self._profile_picture=None,
        self._public_key=None,
        self._redirect_uri=None,
        self._client_id=None,
        self._access_token=None,
        self._expires_in=None,
        self._id_token=None,
        self._refresh_token=None,
        self._token_type=None,
        self._google_two_factor_authentication=None,
        self._fund_password=None,
        self._signature=None,
        self._nemo_address=None,
        self._wallet_address=None,

        if sub is not None:
            self.sub = sub
        if email is not None:
            self.email = email
        if email_verified is not None:
            self.email_verified = email_verified
        if name is not None:
            self.name = name
        if gender is not None:
            self.gender = gender
        if birthday is not None:
            self.birthday = birthday
        if profile_picture is not None:
            self.profile_picture = profile_picture
        if public_key is not None:
            self.public_key = public_key
        if redirect_uri is not None:
            self.redirect_uri = redirect_uri
        if client_id is not None:
            self.client_id = client_id
        if access_token is not None:
            self.access_token = access_token
        if expires_in is not None:
            self.expires_in = expires_in
        if id_token is not None:
            self.id_token = id_token
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if token_type is not None:
            self.token_type = token_type
        if google_two_factor_authentication is not None:
            self.google_two_factor_authentication = google_two_factor_authentication
        if fund_password is not None:
            self.fund_password = fund_password
        if signature is not None:
            self.signature = signature
        if nemo_address is not None:
            self.nemo_address = nemo_address
        if wallet_address is not None:
            self.wallet_address = wallet_address

    @property
    def sub(self):
        return self._sub
    @sub.setter
    def sub(self, sub):
        self._sub = sub


    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email


    @property
    def email_verified(self):
        return self._email_verified
    @email_verified.setter
    def email_verified(self, email_verified):
        self._email_verified = email_verified


    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name


    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self, gender):self._gender = gender


    @property
    def birthday(self):
        return self._birthday
    @birthday.setter
    def birthday(self, birthday):
        self._birthday = birthday


    @property
    def profile_picture(self):
        return self._profile_picture
    @profile_picture.setter
    def profile_picture(self, profile_picture):
        self._profile_picture = profile_picture


    @property
    def public_key(self):
        return self._public_key
    @public_key.setter
    def public_key(self, public_key):
        self._public_key = public_key


    @property
    def redirect_uri(self):
        return self._redirect_uri
    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        self._redirect_uri = redirect_uri


    @property
    def client_id(self):
        return self._client_id
    @client_id.setter
    def client_id(self, client_id):
        self._client_id = client_id


    @property
    def access_token(self):
        return self._access_token
    @access_token.setter
    def access_token(self, access_token):
        self._access_token = access_token


    @property
    def expires_in(self):
        return self._expires_in
    @expires_in.setter
    def expires_in(self, expires_in):
        self._expires_in = expires_in


    @property
    def id_token(self):
        return self._id_token
    @id_token.setter
    def id_token(self, id_token):
        self._id_token = id_token



    @property
    def refresh_token(self):
        return self._refresh_token
    @refresh_token.setter
    def refresh_token(self, refresh_token):
        self._refresh_token = refresh_token


    @property
    def token_type(self):
        return self._token_type
    @token_type.setter
    def token_type(self, token_type):
        self._token_type = token_type


    @property
    def google_two_factor_authentication(self):
        return self._google_two_factor_authentication
    @google_two_factor_authentication.setter
    def google_two_factor_authentication(self, google_two_factor_authentication):
        self._google_two_factor_authentication = google_two_factor_authentication


    @property
    def fund_password(self):
        return self._fund_password
    @fund_password.setter
    def fund_password(self, fund_password):
        self._fund_password = fund_password


    @property
    def signature(self):
        return self._signature
    @signature.setter
    def signature(self, signature):
        self._signature = signature


    @property
    def nemo_address(self):
        return self._nemo_address
    @nemo_address.setter
    def nemo_address(self, nemo_address):
        self._nemo_address = nemo_address


    @property
    def wallet_address(self):
        return self._wallet_address
    @wallet_address.setter
    def wallet_address(self, wallet_address):
        self._wallet_address = wallet_address


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
        if not isinstance(other, NemoIdAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NemoIdAccount):
            return True

        return self.to_dict() != other.to_dict()