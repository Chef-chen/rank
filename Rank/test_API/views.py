from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from test_API.models import Info
import json


# Create your views here.
def upload(request):
    # post请求上传分数
    if request.method == 'POST':
        # 获取客户端和分数
        client = request.POST.get('client')
        score = request.POST.get('score')
        # 数据库中查找该客户端并修改对应的分数
        try:
            client_obj = Info.objects.get(client=client)
        except:
            return HttpResponse('该客户端不存在')
        else:
            client_obj.score = score
            client_obj.save()
        return HttpResponse('分数上传成功')
    if request.method == 'GET':
        return render(request, 'test_API/test_upload.html')


def show(request):
    if request.method == 'GET':
        return render(request, 'test_API/test_display.html')
    # 获取客户端,获取搜索的范围
    a_json = request.body
    a_obj = json.loads(a_json)
    print(a_obj)
    start = int(a_obj['start'])
    end = int(a_obj['end'])
    myclient = a_obj['myclient']

    total = Info.objects.count()
    if start > total or start <= 0 or start > end or end > total:
        return JsonResponse({'code': 500, 'error': '查询范围有误'})

    rank = Info.objects.order_by('score')
    # 得到信息列表并按照分数降序
    info_list = [[info.client, info.score] for info in rank][::-1]
    print(info_list)

    # 根据信息列表得到排名列表
    rank_list = []
    for one in info_list:
        one.append(info_list.index(one) + 1)
        rank_list.append(one)
    print(rank_list)

    # 自己的排名
    count = 0
    for one in rank_list:
        if one[0] == myclient:
            break
        count += 1
    else:
        return JsonResponse({'code': 501, 'error': '您的客户端账号有误！'})
    client_self = rank_list[count]

    # 获取截取的排行榜
    rank_list = rank_list[start - 1:end]

    # 把搜索排名以及个人排名传到前端
    data_dict = {'rank_list': rank_list, 'client_self': client_self}

    return JsonResponse(data_dict)
