# coding: utf-8
import six


class NemoverseApiException(Exception):
    """The base exception class for all NemoverseApiExceptions"""


class ApiTypeError(NemoverseApiException, TypeError):
    def __init__(self, msg, path_to_item=None, valid_classes=None, key_type=None):
        """Raises an exception for TypeErrors

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list): a list of keys an indices to get to the
                                 current_item
                                 None if unset
            valid_classes (tuple): the primitive classes that current item
                                   should be an instance of
                                   None if unset
            key_type (bool): False if our value is a value in a dict
                             True if it is a key in a dict
                             False if our item is an item in a list
                             None if unset
        """
        self.path_to_item = path_to_item
        self.valid_classes = valid_classes
        self.key_type = key_type
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiTypeError, self).__init__(full_msg)


class ApiValueError(NemoverseApiException, ValueError):
    def __init__(self, msg, path_to_item=None):
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list) the path to the exception in the
                received_data dict. None if unset
        """

        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiValueError, self).__init__(full_msg)


class ApiKeyError(NemoverseApiException, KeyError):
    def __init__(self, msg, path_to_item=None):
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiKeyError, self).__init__(full_msg)

class ApiReponseError(NemoverseApiException, KeyError):
    def __init__(self, resp):
        """
        Args:
            resp (str | dict): the api reponse
        """
        self.status = None
        self.reason = resp
        if isinstance(resp, dict):
            self.status = resp.get('status')
            self.reason = resp.get('params')
            if self.reason is not None:
                if self.reason.get('err'):
                    self.reason = self.reason.get('err')
                elif self.reason.get('error'):
                    self.reason = "{0} - {1}".format(self.reason.get('error'), self.reason.get('error_description'))
            
    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n" "Reason: {1}\n".format(self.status, self.reason)
        return error_message


class ApiException(NemoverseApiException):
    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n" "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message


# class GateApiException(ApiException):
#     def __init__(self, label=None, message=None, detail=None, exp=None):
#         """Init GateApiException from ApiException

#         :param str label: error label parsed
#         :param str message: error message parsed
#         :param str detail: possible error message parsed
#         :param ApiException exp: parent exception
#         """
#         self.label = label
#         self.message = detail if detail else message
#         self.status = exp.status
#         self.reason = exp.reason
#         self.body = exp.body
#         self.headers = exp.headers


def render_path(path_to_item):
    """Returns a string representation of a path"""
    result = ""
    for pth in path_to_item:
        if isinstance(pth, six.integer_types):
            result += "[{0}]".format(pth)
        else:
            result += "['{0}']".format(pth)
    return result

def raise_reponse_error(params=None, default=None):
    msg = default
    if params:
        if isinstance(params, dict):
            msg = params.get('err')
        if not msg:
            msg = params
    raise ApiReponseError(msg)