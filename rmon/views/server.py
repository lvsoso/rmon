#coding=utf-8

from flask import request, g

from rmon.common.rest import RestView
from rmon.common.decorators import ObjectMustBeExist, TokenAuthenticate
from rmon.models import Server, ServerSchema


class ServerList(RestView):
    """Redis 服务器列表
    """

    method_decorators = (TokenAuthenticate(),)

    def get(self):
        """获取 Redis 列表
        """
        servers = Server.query.all()
        return ServerSchema().dump(servers, many=True).data

    def post(self):
        """创建 Redis 服务器
        """
        data = request.get_json()
        server, errors = ServerSchema().load(data)
        if errors:
            return errors, 400
        server.ping()
        server.save()
        return {'ok': True}, 201


class ServerDetail(RestView):

    method_decorators = (TokenAuthenticate(), ObjectMustBeExist(Server))

    def get(self, object_id):
        data, _ = ServerSchema().dump(g.instance)
        return data

    def put(self, object_id):
        schema = ServerSchema(context={"instance":g.instance})
        data = request.get_json()
        server, errors = schema.load(data, partial=True)
        if errors:
            return errors, 400
        server.save()
        return {'ok': True}

    def delete(self, object_id):
        g.instance.delete()
        return {'ok': True}, 204

class ServerMetrics(RestView):
    method_decorators = (TokenAuthenticate(), ObjectMustBeExist(Server))

    def get(self, object_id):
        """获取监控信息
        TODO 如何限制访问频率
        """
        return g.instance.get_metrics()


class ServerCommand(RestView):

    method_decorators = (TokenAuthenticate(), ObjectMustBeExist(Server))

    def post(self, object_id):
        """执行 Redis 命令
        TODO 命令参数如何解析
        """
        pass