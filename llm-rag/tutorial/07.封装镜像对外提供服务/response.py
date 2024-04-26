"""基础返回结构"""


def base_response(code, msg, data=None):
    """基础返回格式"""
    if data is None:
        data = {}
    result = {
        "code": code,
        "message": msg,
        "data": data
    }
    return result


def success(data=None, msg='Success'):
    """成功返回格式"""
    return base_response(200, msg, data)


def fail(code=-1, msg='Fail', param=None):
    """失败返回格式""" 
    result = {
        "error": {
            "message": msg,
            "param": param,
            "code": code
        }
    }
    return result