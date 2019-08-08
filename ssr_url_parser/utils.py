"""
@Project   : ssr_url_parser
@Module    : utils.py
@Author    : tyong920 [tyong920@gmail.com]
@Created   : 2018/6/22 16:36
@Desc      :
"""
import base64
import re

from .exceptions import ParseError

PTN_IPV4 = re.compile(
    r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')


def _fill_missing(string: str):
    """Fill base64 decoded string with ="""
    missing_padding = 4 - len(string) % 4
    if missing_padding:
        return string + '=' * missing_padding
    return string


def check_ipv4(ip: str):
    """Check if the ip is valid IPV4 format"""
    if PTN_IPV4.match(ip):
        return True
    else:
        return False


def parse_ssr_url(ssr_url: str):
    """Parse the ssr_url into dict"""
    result = {}
    try:
        _, url_body = ssr_url.split('://')
        url_body = _fill_missing(url_body)
        url_body = base64.urlsafe_b64decode(url_body).decode('utf8')

        config = re.split(r'[:/?&]', url_body)

        ip = config[0]
        port = config[1]
        protocol = config[2]
        method = config[3]
        obfs = config[4]
        password_raw = config[5]
        password_corrected = _fill_missing(password_raw)
        password_decoded = base64.urlsafe_b64decode(
            password_corrected).decode('utf8')

        # get extra param in ssr string params
        for param in config:
            matches = re.match(r"^(\w+)=(.+)$", param)
            if matches:
                key, value = matches[1],  matches[2]

                if key == "obfsparam":
                    value_decoded = base64.urlsafe_b64decode(
                        _fill_missing(value)).decode('utf8')
                    result['obfs_param'] = value_decoded
                elif key == "protoparam":
                    value_decoded = base64.urlsafe_b64decode(
                        _fill_missing(value)).decode('utf8')
                    result['protocol_param'] = value_decoded
                else:
                    result[key] = value

    except Exception as err:
        raise ParseError from err
    else:
        result.update({'server': ip,
                       'method': method,
                       'obfs': obfs,
                       'password': password_decoded,
                       'server_port': port,
                       'protocol': protocol,
                       })
        return result
