from rest_framework.views import exception_handler
from rest_framework.exceptions import Throttled


def custom_exception_handler(exc, context):
    """自定义访问受限时返回消息
    """
    response = exception_handler(exc, context)

    if isinstance(exc, Throttled):
        custom_response_data = {
            'message': '请求受限，请勿频繁请求',
            'available_in': '%d 秒' % exc.wait,
            'error': True
        }
        response.data = custom_response_data

    return response
