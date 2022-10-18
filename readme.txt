
二、插件的安装
pytest-html
pytest-xdist (多线程运行的插件)
pytest-ordering （改变用例的执行顺序的插件）
pytest-rerunfailures （失败用例重跑的插件）
allure-pytest （生成allue报告）
pyyaml （操作yaml文件的）
requests

Termal下明科执行 pip install -r requirements.txt

https://www.freesion.com/article/2061701921/ 改源


三、pytest默认测试用例的规则及基础应用
1. 模块名必须以test_开头或者_test结尾
2. 测试类必须以Test开头，并且不能带init方法
3. 测试用例必须以test_开头

执行： Alt+Enter自动导包
1.通过命令行执行 pytest
执行参数：
-vs -v输出详细信息 -s 输出调试信息

(venv) D:\PycharmProjects\pytestDemo>pytest -v -s
=============================================================== test session starts ===============================================================
platform win32 -- Python 3.9.13, pytest-7.1.3, pluggy-1.0.0 -- D:\dev_tool\Python\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.9.13', 'Platform': 'Windows-10-10.0.19042-SP0', 'Packages': {'pytest': '7.1.3', 'py': '1.11.0', 'pluggy': '1.0.0'}, 'Plugins
': {'allure-pytest': '2.11.0', 'forked': '1.4.0', 'html': '3.1.1', 'metadata': '2.0.2', 'ordering': '0.6', 'rerunfailures': '10.2', 'xdist': '2.5.0'
}, 'JAVA_HOME': 'D:\\dev_tool\\jdk11'}
rootdir: D:\PycharmProjects\pytestDemo
plugins: allure-pytest-2.11.0, forked-1.4.0, html-3.1.1, metadata-2.0.2, ordering-0.6, rerunfailures-10.2, xdist-2.5.0
collected 2 items

testcases/test_print.py::TestPrint::test_print1 测试打印功能
PASSED
testcases/test_print.py::TestPrint::test_print2 测试打印功能2
PASSED

-n 多线程运行 前提是安装了pytest-xdist 插件  -n=2
--reruns num 前提是安装插件   失败重跑     --reruns=2
-x 出现一个用例失败则停止测试
--maxfail 出现几个失败终止 --maxfail=2
--html 前提安装pytest-html 生成html报告
-k 运行测试用例中包含某个字符串的测试用例  -k "print or print1"

2.通过main函数   测试类中加main函数 pytest.main()


3.通过全局配置文件pytest.ini文件执行
注意：
一般放在根目录下 名称必须是pytest，ini
编码格式为ANSI
pytest，ini文件可以改变默认的测试用例规则
不管是命令行也好还是主函数运行。都会加载这个配置文件


4. pytest.ini文件有中文会有错 UnicodeDecodeError: 'gbk' codec can't decode byte 0xa1、
可以用utf-8

5.继续配置ini文件 测试用例分组执行 进行标记 然后测试用例添加装饰器（类似注解）
addopts = -vs -m "smoke"

markers =
    smoke:smoke test
    sanity:sanity test

@pytest.mark.smoke

四、pytest跳过测试用例
1. @pytest.mark.skip(reason = "no reason skip")
2. @pytest.mark.skipif(workage < 10, reason="work experience not long") 根据条件跳过

五、测试用例前后置
    def setup_class(self):
        print("beach class")

    def teardown_class(self):
        print("after class")

    def setup(self):
        print("before each test case")

    def teardown(self):
        print("after each test case")
对于每个测试类都定义这样的方法来实现前后置代码重复，考虑顶一个类封装这些方法，测试类
继承后可以稍微灵活些，但是对希望部分前后置的没办法解决

六、使用Fixture实现部分前后置
@pytest.fixture()
1. scope：作用域
    function:在函数之前和之后执行  yield后面的语句表示之后执行
    1. 手动调用的方式是在测试用例的参数里加入fixture的名称
    2.如果说fixture有通过return或yield返回值的话，那么可以把这个值传递到测试用例当中，值是通过
    固件的名字传递的

    class:在类之前和之后执行
    1.手动调用方式是在类的上面加上 @pytest.mark.usefixtures("exe_database_sql")装饰器调用

    package/session:在整个项目回话之前和之后执行 （1次）
    1.一版结合conftest.py文件来实现

2. autouse:自动执行 默认False 加此参数设置为true对当前类中的所有用例生效

如果希望在另一个py文件中调用需要结合conftest.py文件使用！

3. params: 实现参数化
    1.如何把值传到Fixture是通过fixture函数的参数里加入request来接收参数,然后通过request.param来取值
    （这里的param没有s）

4. ids: 不能单独使用，必须和params一起使用，左右是对参数起别名

5. name: 作用是给fixture起别名
特别注意：一旦使用了别名，namefixture的名称就不能再用了，只能用别名。

但是fixture只在一个模块使用，不合理，接下来引入下一个知识点

七、fixture结合conftest.py文件使用
1. conftest.py它是专门用于存放fixture的配置文件，名称是固定的，不能变
好处是各个模块可以复用固件配置

2. 在conftest.py文件里所有的方法在调用的时候不需要导包

3.contest.py文件可以有多个，并且多个conftest.py文件里面的多个fixture可以被一个用例调用

分层级管理 比如web系统的自动化，一个模块一个contest.py文件，定义的具体的fixture，公共的也可以定义contest.py作为共同的比如
登陆
(这里没有跟着视频敲 主要就是把.py文件分包，更有结构的组织，然后定义多个contest去管理不同的fixture 组合起来被测试用例组合起来
结构更清晰)
 print("test  multi fixtures " + um + db) 向这条语句 其实调了2个fixture

 八、 这些设置的优先级是怎么样？
 

