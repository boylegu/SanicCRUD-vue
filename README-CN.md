## SanicCRUD-vue

Sanic ＋ 前端MVVM 一种新一代Python高性能全栈开发实践

<p align="center">
  <a href ="##"><img alt="sanic_vue" src="http://i2.muimg.com/536217/20f0cc743f009782.png"></a>

<h4 align="center" style="color:	#3399FF">
Convenient & efficient and better performance for new Python full stack.
</h4>

<p align="center" style="color: #FF66FF">Commemorate the 6 anniversary of enter the profession.</p>

<p align="center" style="color: #FF9933">献给所有坚守自己信念的朋友们</p>

<p align="right" style="color: #3399FF">———————By Boyle Gu</p>

## 背景
本项目将使用Sanic + Vue2 ＋ Webpack2 配合最简单CRUD的逻辑来展示一个基于Python的全新一代高性能全栈开发实践的Demo


### 为什么是Sanic
对于为何不是Flask、Django等著名框架，或许可能很多人会产生疑惑，Sanic本身和Flask非常的相似，而它的出现，不仅是大大改进过去WSGI时代性能低下通病，外加配合uvloop作为核心引擎，使Sanic在很多情况下单机并发甚至不亚于Golang，而且它更意味着Python在Web领域走进了全新的未来。

那么uvloop又是什么？简单的说，Python3.4之后作为最高效简单的协程并发库莫过于asyncio，而asyncio的出现仅仅只是为了提供更方便的异步编程及互操作的接口，其底层用的还是比较传统的event loop，而uvloop是在重新定制asyncio基础上引入了libuv，
其性能不仅超过了以往如gevent、tornado等Python异步框架，也同样以超过2倍多的性能领先于node.js。

<p align="center">
  <a href ="##"><img style="box-shadow: 8px 8px 5px #888888;"alt="sanic_vue" src="http://i2.muimg.com/536217/d814cd60b591dc33.png"></a>

> 是不是和Flask非常相似？


### 为什么是MVVM

那么在我继续之前，我也想和大家回顾一下Web开发的发展简史：

- 第一阶段: 网页三剑客，生猛的通过原生javascript直接操作Dom树;

- 第二阶段: JQuery诞生，配合前端MVC为代表的Backbone.js, 让我们可以优雅而简单的操作Dom树;

- 第三阶段: 后端架构升级为MVC，前后端分工更清晰，前端工程化、ECMAScript规范开始崭露头角;

- 第四阶段: 后端架构进入了微服务时代，前端架构不仅升级为MVVM，ES6更是成为目前事实上的标准;

在这里，我不想过于神化MVVM有多么的先进，JQuery为代表的MVC有多么的落后，但确实MVVM有着很多先进的特性:

- 低开销

- 易维护

- 可重用

### 为什么选择Vue.js

Vue.js是MVVM设计模式中目前最火热的一个前端框架之一，除了性能表现优异之外，与类似React相比，更轻量级、更容易上手。

通过Vue中的“单文件组件”特性，更灵活的定义组件，不仅使代码结构更清晰，而且能与任何其他组件进行随意组合，更具复用性。

<p align="center">
  <a href ="##"><img style="box-shadow: 8px 8px 5px #888888;"alt="sanic_vue" src="http://i2.muimg.com/536217/5ae4b10becac44b0.png"></a>

### Webpack是什么
Webpack提供了一整套前端工程自动化的解决方案

### peewee是什么

有了高性能的Sanic作为基石，或许还不够，最能成为后端性能瓶颈的更多的是在于数据库，因此挑选一个合适的ORM变的极为重要，目前python比较主流的ORM是Django-ORM、SQLAlchemy等，但为了配合Sanic这种性能卓越的框架，我更倾向于peewee，更轻量级、方便二次封装，更友好的支持异步。


## Demo

一个简单的“上海人员信息查询系统”作为例子


[![demo-image](https://github.com/boylegu/SanicCRUD-vue/blob/master/image/demo_image.gif?raw=true)]()

## 项目结构

     |
     |—— tests                            // 单元测试
     |
     |—— sanic_crudvue                    // 主项目
     |      |
     |      |—— config                    // 后端基本配置
     |      |
     |      |—— crud                      // 后端APP 
     |      |
     |      |—— frontend          
     |      |       |__ build             // webpack配置文件
     |      |       |__ dist              // 编译后的目标目录
     |      |       |__ src               // 前端源代码
     |      |       |    |   
     |      |       |    |__ components   // 本项目各种各样的核心组件 
     |      |       |    |
     |      |       |    |__ App.vue      // 主页
     |      |       |    |
     |      |       |    |__ eventBus.js  // 中央消息处理器，用于‘非父子组件’通信，下一个版本将会使用vuex
     |      |       |    |
     |      |       |    |__ main.js      // webpack入口



### 具备的功能(v0.1)

- Sanic (后端)

  - 如何开启一个基于Sanic的工程项目，并通过蓝本来组织基本的MVC模式
  
  - 通过在Sanic中建立基于RestFul-API并实现一个基本的CRUD逻辑
  
  - 处理CORS(跨域资源共享)以及解决在Sanic中“pre-flight”请求问题

  - 简单的在peewee上进行二次封装ORM
  
  - 演示在Sanic中进行单元测试

  - 支持热加载
  
  - 增加api接口文档 
  
  - 通过peewee和Sanic来实现RestFul-API的分页
   
- VueJS & webpack (前端)

  - 遵循ECMAScript 6 规范
  
  - 如何在vue中使用‘单文件组件’进行开发编码
  
  - 演示‘非父子组件’如何进行简单的通信以及‘父子组件’之间如何传递数据
  
  - 如何和后端进行数据交互

  - 如何在vue中优雅的引入第三方JS库

  - 格式化时间
  
  - 分页实现
  
  - 可复用组件
 
     - DbHeader.vue
     - DbFooter.vue  (sticky footer) 
     - DbFilterinput.vue
     - DbModal.vue
     - DbSidebar.vue
     - DbTable.vue 
     
     >> 得益于类似vue、react等MVVM模式，本项目的任何组件，只要您觉得合适，都可以复用在您的任何项目中，避免重复造轮子。
  
  - 如何通过webpack2配置来自动化构建前端环境(包括如何配置vue2、处理静态文件,构建不同环境等等)  

### 本项目主要技术栈

- python 3
- sqlite (not recommend, only convenience example)
- vueJS 2.x
- webpack 2.x
- element ui
- axios

### 准备工作

- 请必须安装 Python 3.5， 3.6 或以后更高的版本

- 安装 nodejs / npm

- 克隆仓库

        git clone https://github.com/boylegu/SanicCRUD-vue.git
        
        cd SanicCRUD-vue

### 安装

- 构建后端环境

        cd SanicCRUD-vue

        make install

- 构建前端环境

        cd sanic_crudvue/frontend

        npm install 

### 使用说明

- 运行后端服务

        make dev

- 运行前端服务

        cd sanic_crudvue/frontend

        npm run dev

- 运行单元测试

        cd SanicCRUD-vue

        make test
        
> 你也可以在生产环境中运行`cd sanic_crudvue/frontend;npm run build`进行编译并配合Nginx
        
## 未来计划

本项目可以作为工作参考、学习或者教学演示，之后将陆续以版本的形式，即每个版本都会新增不同的功能演示项，不定期进行发布更新，有以下功能已经在计划之中：

1. 用户认证
2. 引入更高级的vuex组件通信机制
3. 演示vue-route的使用
4. 加入docker部署环境
5. 新增针对yarn的支持
... ...

## 技术、教学支持

由于个人时间暂时有限，关于Sanic、Vue、webpack等所有的核心的议题内容非常庞大，因此我将以以下形式来回答和解释关于本项目Demo问题：

1. 以Github Issue的形式进行提问
2. 电子邮件的形式 gubaoer@hotmail.com
3. QQ群：315308272

## 相关项目
- [SpringBoot-vue for Java](https://github.com/boylegu/SpringBoot-vue)

## My Final Thoughts

```

                     ▄▄▄▄▄
            ▀▀▀██████▄▄▄       _______________
          ▄▄▄▄▄  █████████▄  /                 \
         ▀▀▀▀█████▌ ▀▐▄ ▀▐█ | Gotta go fast!   |
       ▀▀█████▄▄ ▀██████▄██ | _________________/
       ▀▄▄▄▄▄  ▀▀█▄▀█════█▀ |/
            ▀▀▀▄  ▀▀███ ▀       ▄▄
         ▄███▀▀██▄████████▄ ▄▀▀▀▀▀▀█▌   ______________________________ 
       ██▀▄▄▄██▀▄███▀ ▀▀████      ▄██  █                              \\ 
    ▄▀▀▀▄██▄▀▀▌████▒▒▒▒▒▒███     ▌▄▄▀▀▀▀█_____________________________ //
    ▌    ▐▀████▐███▒▒▒▒▒▐██▌
    ▀▄▄▄▄▀   ▀▀████▒▒▒▒▄██▀
              ▀▀█████████▀
            ▄▄██▀██████▀█
          ▄██▀     ▀▀▀  █
         ▄█             ▐▌
     ▄▄▄▄█▌              ▀█▄▄▄▄▀▀▄
    ▌     ▐                ▀▀▄▄▄▀
     ▀▀▄▄▀     ██   
 \  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ▀ 
 \- ▌          SanicCRUD-vue              ▀ ▀      
  - ▌                            (o)          ▀ 
 /- ▌            Go Go Go !               ▀ ▀           
 /  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ▀       
               ██

```

