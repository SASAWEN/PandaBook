# *PandaBook Note*

> https://github.com/MarkGao11520/python-flask-fisher-book

## 静态文件访问

flask访问静态文件

## 模版 html

### 模版语言 jinja2

#### 1. 语法

- 控制结构

  ```jinja2
  {% if data.food == 'pizza' %}
  	{{data.name}}
  {% elif data.food == 'cake'%}
  	do some thing
  {% else %}
  	{{ data.food }}
  {% endif %}
  
  
  ```

  

- 变量取值

  支持python中所有数据类型

  **字典、对象：**

  ```jinja2
  {{data.age}}
  {{data['age']}}
  ```

### 过滤器

变量可以通过“过滤器”进行修改。变量后面使用**管道(|)分割**，**多个过滤器可以链式调用**，前一个过滤器的输出会作为后一个过滤器的输入。

> safe:      渲染时值不转义
>
> capitialize:   把值的首字母转换成大写，其他子母转换为小写
>
> lower:    把值转换成小写形式
>
> upper:    把值转换成大写形式
>
> title:    把值中每个单词的首字母都转换成大写
>
> trim:      把值的首尾空格去掉
>
> striptags:    渲染之前把值中所有的HTML标签都删掉
>
> join:      拼接多个值为字符串
>
> replace:      替换字符串的值
>
> round:  默认对数字进行四舍五入，也可以用参数进行控制
>
> int:       把值转换成整型

### 模版继承



### flash 消息闪现

- **session 密钥配置：**



## 自定义校验

## redirect 重定向 & render_template 模版渲染

区别：

- 重定向把url换成重定向url
- 模版渲染不改变url，只使用模版来渲染请求的url

## cookie

服务器生成key：value，随resonse返回到浏览器 => cookie

cookie可以设置有效期，有效期内访问同一个网站，信息生效，过期失效。

广告精准投放：cookie存储喜好信息（购买记录等）

Login_user把用户信息写入到cookie（id）

## 获取当前访问网站用户信息

current_user：实质是实例化User模型。user.py定义get_user获取User的id号

## 反重定向攻击

next

## with & contextmanager

### collections.namedtuple

tuple各元素自定义命名

## yield生成器

## 可调用对象

判断python对象是否可调用：

- 使用内置callable函数
  - callable(func)
- 判断对象类型是否为FunctionType
  - type(func) is FunctionType
  - isinstance(func, FunctionType)
- 判断对象是否实现\__call__方法
  - hasattr(func, '\__call__')

## ajax

![Screen Shot 2019-11-04 at 4.52.29 PM](/Users/cala/Desktop/Screen Shot 2019-11-04 at 4.52.29 PM.png)

浏览器重新加载数据（服务器）刷新页面（模版渲染），消耗服务器性能。

解决：

- 页面缓存

- ajax：页面发送http请求，通过js把数据更新

## MVC模型

- **Model**：**有业务意义的业务逻辑** <==> 数据层（orm封装api）

  可进一步分层：

  - Service
  - Logic
  - Model   

- **View**：html页面

- **Controller**：**业务逻辑**




## http异常处理

### 1. flask提供的first_or_404

First_or_404执行流程：

首先检查是否有first元素，若无，则Aborter函数的__call__方法拿着封装好的self.mapping（实质是default_exceptions）通过参数传来的code去匹配相应的异常，并进行抛出。

视图函数在调用first_or_404()函数时，由于结果不存在，就抛出了上面的NotFound异常而**终止**了，后面的异常流程直到界面显示，都是由**HttpException**完成的。

异常页面由异常类的鸡肋HttpException定义 get_body()

### 2. 基于AOP面向切片编程

**作用：**实现自定义异常页面。

把所有处理的方法集中到一个函数中，使用flask的装饰器**app_errorhandler**实现，可以绑定异常代码。

## issue

1. **Q:** 假删除，所有类的基类包含status属性，表示数据是否生效。如果不指定status=1则filter_by结果包含无效对象，希望简化filter_by查询。

   **A:** 继承方式改写sqlalchemy.orm.filter_by，kwargs['status']默认值为1。
   
2. **Q:** 循环导入问题。在model层Gift模块需要查询想要该物品的用户数，因此需要导入wish模块，同理，wish模块需要导入gift模块，但是在模块头的位置导入会产生循环导入的问题。

   **A: **在需要用到wish模块的函数内部导入wish。

   > **全局导入 & 局部导入**
   >
   > 全局导入：对模块全局起作用
   >
   > 局部导入：对函数内部起作用
   >
   > **循环导入 & 覆盖导入**
   >
   > 循环导入解决办法：重构代码 or 使用局部导入
   >
   > 覆盖导入解决办法：重命名模块。因为Python解释器首先在当前运行脚本所处的的文件夹中查找名叫`math`的模块。
   
3. **Q:** [重置密码]发送确认邮件导致网页跳转存在小延迟。

   **A:** 使用异步邮件发送，简单来说，将发送邮件的动作另外开一个线程，但是又有另一个问题，无法将current_app传到另一个线程，因为flask的current_app每次取栈顶，因此需要使用current_app._get_current_object方法获取该线程下的对象。

   **current_app** 是LocalProxy类，是flask的app核心对象的代理，指向app和request请求类。

   flask在RequestContext入栈前会检查另外一个AppContext的栈的情况，如果栈顶元素为空或者不是当前对象，就会把AppContext推入栈中，然后RequestContext才进栈。

   **LocalStack：**线程隔离

   **LocalProxy：**根据线程/协程返回该线程对应的代理对象

   最终current_app获得的不是app上下文，而是flask实力化对象

   ![20180610215954276](/Users/cala/Grade4/Emergency/MyPanda/20180610215954276.png)

   也可手动app_context入栈：

   ```python
   # flask应用实例入栈
   ctx = app.app_context()
   ctx.push()
   a = current_app
   ctx.pop()
   ```

4. **Q:** 有记录意义的历史字段是否需要做模型关联？

   **A:** 不需要，应该无关联记录交易者用户名。交易者的用户名不必要动态改变，因为交易记录的意义在于记录交易当时的状态，犹如购物平台历史订单记录的价格是交易时的价格，而不因时间改变。**合理利用冗余，减少数据库查询时间。**