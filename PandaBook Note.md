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

