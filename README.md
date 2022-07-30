### pytest发现测试用例规则
```
1.模块名称必须是test_开头或_test结尾
2.类名必须是Test开头，并且不能有init方法
3.方法名称(用例名称)必须是test开头
```
--- 
### pytest执行测试用例
#### 1.命令行执行
```
pytest 参数
-v 输出更详细的信息
-s 输出调式信息
-n 2 多线程
--reruns 2 失败用例重跑2次
-x 出现一个错误终止测试
--maxfail=2 最大错误用例个数
--html=路径 生成测试报告
-k "" 执行用例名称包含字符串的用例
pytest "指定文件夹" 只会执行此文件夹下的用例
pytest "指定文件夹/文件::类名::方法" 只会执行此方法(node id指定特定测试用例)
```
#### 2.main方法主函数运行

```
pytest.main(["--reruns=2","-vs","--html=./reports/report.html",])
```
#### 3.pytest.ini文件执行
```
1.不管是命令行还是主函数运行都会去读取pytest.ini文件
2.pytest.ini文件必须放在项目的根目录
3.参数
    1)命令行参数
    addopts = -vs --html=./reports/report.html --reruns=2 -m "smoke or product_manage"
        --alluredir=./temps --clean-alluredir
    2)指定用例文件夹
    testpaths = ./testcases
    3)指定模块
    python_files = "test_*"
    4)指定类
    python_classes = "Test*"
    5)指定方法
    python_functions = "test_*"
    6)用例分组
    markers = 
        smoke:冒烟测试
        product_manager:商品管理
    7)基础路径,直接在方法名称里传参
    base_url = ""
    def test_(self,base_url):
        pass
```
---
### 改变用例执行顺序
```python
import pytest
@pytest.mark.run(order=1)
def test_api(self):
    pass
```
---
### pytest部分前置fixture
#### 1.定义fixture
```python
import pytest
@pytest.fixture(scope="function",autouse=False,params=["百里","北凡","星瑶"],ids=["baili","beifan","xingyao"],name="sql")
def execute_sql(request):
    print("前置执行")
    yield request.param
    print("后置执行")
```
#### 2.参数详解
##### 2.1 scope(当为module和session时autouse一般自动调用)
    1）function默认
        1)autouse=True,所有的方法自动使用
        2)autouse=False,需要在方法里添加fixture
            def test_(self,"fixture名称"):
                pass
    2）class
        1)autouse=True,所有类自动使用
        2)autouse=False,需要在类上添加装饰器@pytest.mark.usefixtures(fixture名称)
    3）module
    4）session，常用
---
### pytest执行过程
```
1.查找当前目录下的pytest.ini文件
2.根据pytest.ini文件里的testpaths找到用例目录
3.查找用例目录下的conftest.py文件
4.根据pytest.ini文件里的python_files查找用例module
5.查找用例module下的setup、teardown
6.根据pytest.ini文件里的python_classes、python_functions查找用例并执行
```
---
### allure报告
```
1.下载allure压缩文件后解压
2.配置环境变量
3.运行参数--alluredir=./temps --clean-alluredir
4.主函数os.system("allure generate ./temps -o ./reports --clean")
```
#### allure报告定制,logo
```
1.找到allure-2.13.3\config目录,打开allure.yaml文件
2.添加 - custom-logo-plugin
3.打开allure-2.13.3\plugins\custom-logo-plugin\static目录添加图片
4.更改样式，修改styles.css
.side-nav__brand {
  background: url('logo.png') no-repeat left center !important;
  margin-left: 10px;
  height: 90px;
  backgroung-size: contain !important;
}
.side-nav__brand-text {
  display: none;
}
```
#### allure报告定制，内容
```python
import allure
@allure.epic("项目名称")
@allure.feature("模块名称")
class TestProduct(object):
    @allure.story("接口名称")
    @allure.severity(allure.severity_level.NORMAL) #优先级别
    @allure.link("接口链接")
    @allure.issue("bug链接")
    @allure.testcase("测试用例链接")
    def test_(self):
        allure.dynamic.title("用例标题")
        allure.dynamic.description("用例描述")
        with allure.step("用例步骤描述"):
            pass
        allure.attach(body="截图内容",name="截图名称",attachment_type=allure.attachment_type.PNG)
        print("test")
```
#### allure报告网络访问
```
命令行输入allure open ./reports
```
---
### yaml详解
```
1.标量，基本类型
2.对象，dict，格式使用  key:(空格)value
3.数组，list，格式使用"-"
4.数据类型强转使用"!!数据类型"（!!binary）
5.引用(&设置锚点,*引用)
    mashang: &ms #锚点
      name: 百里
      age: 22
    job:
      job_nam: 老师
      msss: *ms
      <<: *ms #表示将引用合并到当前数据
```
---
### post请求中data和json传参区别
```
session.request(params=None,data=None,json=None,files=None)
文件上传：Content-Type:multipart/form-data               (files)
表单提交：Content-Type:application/x-www-form-urlencoded (data)纯键值对,不能嵌套
文本raw提交：
    json：Content-Type:application/json                  (json)可以嵌套dict
    text：Content-Type:text/plain                        (data)
    javascript：Content-Type:application/javascript      (data)
    xml：Content-Type:application/xml                    (data)   
    html：Content-Type:text/html                         (data)   
二进制提交：
    binary：Content-Type:application/octrent-stream      (data)  
```
---
### requests返回的response对象的属性很方法
```
res.text        返回字符串信息
res.content     返回二进制数据
res.json()      返回json数据
res.status_code 返回状态码
res.reason      返回响应信息
res.cookie      返回cookie信息
res.encoding    返回编码格式
res.headers     返回响应头
res.request.url 返回url
res.request.xxx 返回请求信息       
```
---
### cookie关联
```
cookie关联一般是通过session来实现，不需要手动设置cookie
1.手动设置cookie
    cookie = res.cookie
    request.get(cookie=cookie)
2.session自动关联cookie
    ression = requests.session
    session.request()
```
---