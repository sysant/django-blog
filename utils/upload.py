import os
import uuid
from django.views.decorators.csrf import csrf_exempt   # 取消csrftoken验证
from django.http import JsonResponse   # 返回json数据格式
from django.conf import settings       # 获取settings.py文件中的配置信息


@csrf_exempt
def upload_file(request):
    # 获取表单上传的图片
    upload = request.FILES.get('upload')
    # 生成uid
    uid = ''.join(str(uuid.uuid4()).split('-'))
    # 修改图名称
    names = str(upload.name).split('.')
    names[0] = uid
    # 返回修改过的图片格式
    upload.name = '.'.join(names)
    new_path = os.path.join(settings.MEDIA_ROOT, 'upload/', upload.name)
    # 上传图片
    with open(new_path, 'wb+') as f:
        for chunk in upload.chunks():
            f.write(chunk)

    filename = upload.name
    url = '/media/upload/' + filename
    retdata = {
        'url': url,
        'uploaded': '1',
        'fileName': filename
    }
    return JsonResponse(retdata)