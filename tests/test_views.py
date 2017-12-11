#coding=utf-8

from rmon.models.server import Server


class TestServer:
    """测试 Server 相关功能
    """

    def test_save(self, db):
        """测试 Server.save 保存服务器方法
        """
        # 初始状态下，数据库中没有保存任何 Redis，所以数量为 0
        assert Server.query.count() == 0
        server = Server(name="test", host='127.0.0.1')
        # 保存到数据库中
        server.save()
        # 现在数据库中数量变为 1
        assert  Server.query.count() == 1
        # 且数据库中的记录就是之前创建的记录
        assert Server.query.first() == server

    def test_delete(self, db, server):
        """测试 Server.delete 删除服务器方法
        """
        assert Server.query.count() == 1
        server.delete()
        assert Server.query.count() == 0

class TestServerDetail:
    """测试 Redis 服务器详情 API
    """

    endpoint = 'api.server_detail'

    def test_get_server_success(self, server, client):
        """测试获取 Redis 服务器详情
        """
        pass

    def test_get_server_failed(self, db, client):
        """获取不存在的 Redis 服务器详情失败
        """
        pass

    def test_update_server_success(self, server, client):
        """更新 Redis 服务器成功
        """
        pass


    def test_update_server_success_with_duplicate_server(self, server, client):
        """更新服务器名称为其他同名服务器名称时失败
        """
        pass

    def test_delete_success(self, server, client):
        """删除 Redis 服务器成功
        """
        pass

    def test_delete_failed_with_host_not_exist(self, db, client):
        """删除不存在的 Redis 服务器失败
        """
        pass