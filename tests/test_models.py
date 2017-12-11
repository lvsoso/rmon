#coding=utf-8

from rmon.models.server import Server
from rmon.common.errors import RestError

class TestServer:

    def test_save(self, db):
        assert Server.query.count() == 0
        server = Server(name="test", host="127.0.0.1")
        server.save()
        assert Server.query.count() == 1
        assert Server.query.first() == server

    def test_delete(self, db, server):
        assert Server.query.count() == 1
        server.delete()
        assert Server.query.count() == 0

    def test_ping_success(self, db, server):
        """测试 Server.ping 方法执行成功

        需要保证 Redis 服务器监听在 127.0.0.1:6379 地址
        """
        assert server.ping() is True

    def test_ping_failed(self, db):
        """测试 Server.ping 方法执行失败

        Server.ping 方法执行失败时，会抛出 RestException 异常
        """

        # 没有 Redis 服务器监听在 127.0.0.1:6399 地址, 所以将访问失败
        server = Server(name='test', host='127.0.0.1', port=6399)

        try:
            server.ping()
        except RestError as e:
            assert e.code == 400
            assert e.message == 'redis server %s can not connected' % server.host

    def test_create_server_success(self, db, client):
        """测试创建 Redis 服务器成功
        """
        # TODO 自行补充
        pass

    def test_create_server_failed_with_invalid_host(self, db, client):
        """无效的服务器地址导致创建 Redis 服务器失败
        """
        # TODO 自行补充
        pass

    def test_create_server_failed_with_duplciate_server(self, server, client):
        """创建重复的服务器时将失败
        """
        # TODO 自行补充
        pass
