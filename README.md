# django使用DBUtils实现连接池

#### 由于django没有连接池的功能，当并发量大时可能造成数据库连接超限。

#### DBUtils 是一套用于管理数据库连接池的Python包，为高频度高并发的数据库访问提供更好的性能，可以自动管理连接对象的创建和释放。并允许对非线程安全的数据库接口进行线程安全包装。

#### django结合DBUtils使用，数据库连接管理完全交给DBUtils处理，平滑切换db backends。

### django使用连接的过程：
* 请求开始： 新建连接（从DBUtils管理的连接池中获取连接）
* 请求结束： 关闭连接（实际由DBUtils将连接返还连接池）

## DBUtils
DBUtils提供两种外部接口：

* PersistentDB ：提供线程专用的数据库连接，并自动管理连接。
* PooledDB ：提供线程间可共享的数据库连接，并自动管理连接。

实测证明 PersistentDB 的速度是最高的，但是在某些特殊情况下，数据库的连接过程可能异常缓慢，而此时的PooledDB则可以提供相对来说平均连接时间比较短的管理方式。

## django settings
```
DATABASES = {
    "default": {
        "ENGINE": "db_pool.db.backends.mysql",
        "NAME": "xxx",
        "USER": "xxx",
        "PASSWORD": "xxx",
        "HOST": "mysql",
        "PORT": "3306",
        "ATOMIC_REQUESTS": True,
        "CHARSET": "utf8",
        "COLLATION": "utf8_bin",
        "POOL": {
            "mincached": 5,
            "maxcached ": 500,
        }
    }
}
```
