[![pyversions](https://img.shields.io/badge/python%20-3.5%2B-blue.svg)]()
[![vueversions](https://img.shields.io/badge/vue.js-2.2.x-brightgreen.svg)]()
[![es2015](https://img.shields.io/badge/ECMAScript-6-green.svg)]()
[![ver](https://img.shields.io/badge/release-v0.1-red.svg)]()
[![MIT](https://img.shields.io/badge/license-MIT-ff69b4.svg)]()


<p align="center">
  <a href ="##"><img alt="sanic_vue" src="http://i2.muimg.com/536217/20f0cc743f009782.png"></a>

<h4 align="center" style="color:	#3399FF">
Convenient & efficient and better performance for new Python full stack.
</h4>

<p align="center" style="color: #FF66FF">Commemorate the 6 anniversary of enter the profession.</p>

<p align="center" style="color: #FF9933">Give beginner as a present.</p>

<p align="right" style="color: #3399FF">———————By Boyle Gu</p>

### [Chinese README[中文]](https://github.com/boylegu/SanicCRUD-vue/blob/master/README-CN.md)

## overview

This‘s a CRUD demo example base Sanic with Vue2 + webpack2. I hope pass thought this project for express new Python full stack base web practice.


## Why Sanic

After python3.4, Sanic is a Python web framework built on uvloop and designed for fast HTTP responses via asynchronous request handling. Compared with such as
Django, Flask and so these web framwork is much faster,and it's close affinity to Flask. 

what's uvloop?

uvloop is written in Cython and built on top of libuv. uvloop makes asyncio fast. In fact, it is at least 2x faster than nodejs, gevent, as well as any other Python asynchronous framework. The performance of uvloop-based asyncio is close to that of Go programs.

<p align="center">
  <a href ="##"><img style="box-shadow: 8px 8px 5px #888888;"alt="sanic_vue" src="http://i2.muimg.com/536217/d814cd60b591dc33.png"></a>

> Wow！What a striking similarity to Flask! Do you think？

## Why MVVM

Although it seems similar to MVC (except with a "view model" object in place of the controller), there's one major difference — the view owns the view model. Unlike a controller, a view model has no knowledge of the specific view that's using it.

This seemingly minor change offers huge benefits:

1. View models are testable. Since they don't need a view to do their work, presentation behavior can be tested without any UI automation or stubbing.

2. View models can be used like models. If desired, view models can be copied or serialized just like a domain model. This can be used to quickly implement UI restoration and similar behaviors.

3. View models are (mostly) platform-agnostic. Since the actual UI code lives in the view, well-designed view models can be used on the iPhone, iPad, and Mac, with only minor tweaking for each platform.

4. Views and view controllers are simpler. Once the important logic is moved elsewhere, views and VCs become dumb UI objects. This makes them easier to understand and redesign.
In short, replacing MVC with MVVM can lead to more versatile and rigorous UI code.

>  *In short, replacing MVC with MVVM can lead to more versatile and rigorous UI code.*

## Why to choose Vue.js

Vue.js is relatively new and is gaining lot of traction among the community of developers. VueJs works with MVVM design paradigm and has a very simple API. Vue is inspired by AngularJS, ReactiveJs and updates model and view via two way data binding.

Components are one of the most powerful features of Vue. They help you extend basic HTML elements to encapsulate reusable code. At a high level, components are custom elements that Vue’s compiler attaches behavior to. 

<p align="center">
  <a href ="##"><img style="box-shadow: 8px 8px 5px #888888;"alt="sanic_vue" src="http://i2.muimg.com/536217/5ae4b10becac44b0.png"></a>
  
## What's Webpack

Webpack is a powerful tool that bundles your app source code efficiently and loads that code from a server into a browser. It‘s excellent solution in frontend automation project

## What's Peewee

Sometimes a huge amount of write/reade as Database invite costly.So use orm is very importance. Such as Django-ORM、SQLAlchemy and so on. But I recommend that Peewee may be a better fit than others. Because some of the reasons:

1. A small, expressive ORM
2. Can be developed as reusable, encapsulated 
3. more friendly asynchronous support


## Demo


This's a sample ShangHai people information system as example demo.


[![demo-image](https://github.com/boylegu/SanicCRUD-vue/blob/master/image/demo_image.gif?raw=true)]()

## The project structure

     |
     |—— tests                            // unit test
     |
     |—— sanic_crudvue                    // main project
     |      |
     |      |—— config                    // base config in backend
     |      |
     |      |—— crud                      // core app in backend 
     |      |
     |      |—— frontend          
     |      |       |__ build             //  build static resource and webpack config
     |      |       |__ dist              // build target directory
     |      |       |__ src               // source code in frontend
     |      |       |    |   
     |      |       |    |__ components   // a vast variety of component 
     |      |       |    |
     |      |       |    |__ App.vue      // main web page
     |      |       |    |
     |      |       |    |__ eventBus.js  //  a central event bus for non Parent-Child Communication
     |      |       |    |
     |      |       |    |__ main.js      // webpack entry


### Feature (v0.1)

- Sanic (Back-end) 

  - How is start Sanic project and organization to base MVC layout with blueprint  
  
  - Build RestFul-API on Sanic and base CRUD logic implementation

  - Handle CORS(Cross-origin resource sharing) and resolve pre-flight request problem in Sanic
  
  - Simple encapsulated interface on peewee

  - Unit test on Sanic

  - Support hot reload in Sanic

  - Add interface documents about it's rest-api

  - Pagination implementation of RestFul-API with peewee and sanic

- VueJS & webpack (front-end)

  - Follow ECMAScript 6

  - What about coding by single file components in vueJS
  
  - Simple none parent-child communication and parent-child communication 

  - Interworking is between data and back-end
  
  - How grace import third JS package in vue
  
  - Handle format datetime
  
  - Pagination implementation
  
  - Reusable components
  
     - DbHeader.vue
     - DbFooter.vue  (sticky footer) 
     - DbFilterinput.vue
     - DbModal.vue
     - DbSidebar.vue
     - DbTable.vue

  - Config front-end env on webpack2 (include in vue2, handle static file, build different environment...... with webpack2)


### Main technology stack

- python 3
- sqlite (not recommend, only convenience example)
- vueJS 2.x
- webpack 2.x
- element ui
- axios

### Preparation

- Please must install Python 3.5， 3.6  or even higher version

- Install nodejs / npm

- Clone Repository

        git clone https://github.com/boylegu/SanicCRUD-vue.git
        
        cd SanicCRUD-vue

### Installation  

- Build back-end environment

        make install
        
- Build front-end environment

        cd sanic_crudvue/frontend

        npm install 

### Usage

- Run back-end server

        cd SanicCRUD-vue

        make dev

- Run Front-end Web Page

        cd sanic_crudvue/frontend

        npm run dev

- Unit test

        cd SanicCRUD-vue

        make test

> You can also run `cd sanic_crudvue/frontend;npm run build` and it's with Nginx in the production environment

## Future Plan

This project can be reference,study or teaching demonstration. After, I will update at every increme version in succession. In future,I have already some plan to below:

1. User Authentication
2. state manage with vuex
3. use vue-route
4. add docker deploy method
5. support yarn
... ...

## Support

1. Github Issue

2. To e-mail: gubaoer@hotmail.com

3. You can also join to QQ Group: 315308272

## Related projects

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

 
