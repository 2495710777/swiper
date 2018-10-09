from json import loads
from json import dumps
from json import JSONDecodeError

from common.errors import OK
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed


def is_json(test_str):
    '''检查字符串是否是 json'''
    if not isinstance(test_str, (str, bytes)):
        return False

    try:
        json.loads(test_str)
    except (TypeError, JSONDecodeError):
        return False
    else:
        return True


def render_json(data=None, error=OK) -> HttpResponse:
    '''将返回值渲染为 JSON 数据'''
    if data and is_json(data):
        result = data  # 如果传入的 data 本身就是 json 格式，则直接返回
    else:
        result = {
            'data': data or error.data,
            'sc': error.code  # 状态码 (status code)
        }

    if settings.DEBUG:
        # Debug 模式时，按规范格式输出 json
        json_str = dumps(result, ensure_ascii=False, indent=4, sort_keys=True)
    else:
        # 正式环境下，将返回数据压缩
        json_str = dumps(result, ensure_ascii=False, separators=[',', ':'])

    return HttpResponse(json_str)


def allow_http_methods(*methods):
    """检查允许的 HTTP 方法"""
    def decor(view_func):
        def wrap(request, *args, **kwargs):
            methods = [m.upper() for m in methods]
            if request.method not in methods:
                return HttpResponseNotAllowed(methods)
            return view_func(request, *args, **kwargs)
        return wrap
    return decor


require_post = allow_http_methods('post')
