from django.http import JsonResponse, HttpResponse
import datetime
import platform
from demo.settings import env
import os
def index(request):
    return HttpResponse("Hello, World!")

# 健康检查接口
def healthz(request):
    """
    返回应用的健康状态
    """
    return JsonResponse({
        'status': 'ok',
        'timestamp': datetime.datetime.now().isoformat(),
    })

# 信息接口
def info(request):
    """
    返回应用和环境的基本信息
    """
    branch = os.environ.get('GIT_BRANCH', 'unknown')
    commit_id = os.environ.get('GIT_COMMIT_ID', 'unknown')
    app = os.environ.get('APP', 'unknown')

    return JsonResponse({
        'app': app,
        'version': '1.0.0',
        'environment': env,
        'branch': branch,
        'commit_id': commit_id,
        'python_version': platform.python_version(),
        'os': platform.system(),
        'timestamp': datetime.datetime.now().isoformat(),
    })
