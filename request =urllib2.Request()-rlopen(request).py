Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib2
>>> request =urllib2.request("https://www.baidu.com/")

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    request =urllib2.request("https://www.baidu.com/")
AttributeError: 'module' object has no attribute 'request'
>>> request =urllib2.Request("https://www.baidu.com/")
>>> response=urllib2.urlopen(request)
>>> print response.read()
<html>
<head>
	<script>
		location.replace(location.href.replace("https://","http://"));
	</script>
</head>
<body>
	<noscript><meta http-equiv="refresh" content="0;url=http://www.baidu.com/"></noscript>
</body>
</html>
>>> print response.read(response)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print response.read(response)
  File "C:\Python27\lib\socket.py", line 377, in read
    left = size - buf_len
TypeError: unsupported operand type(s) for -: 'instance' and 'int'
>>>  print response.read(3000)
 
  File "<pyshell#6>", line 2
    print response.read(3000)
    ^
IndentationError: unexpected indent
>>> print response.read(3000)

>>> print response.read(3000)

>>> print response.read(3000)

>>> request =urllib2.Request("http://www.runoob.com/python/python-tutorial.html")
>>> response=urllib2.urlopen(request)
>>> print response.read(3000)
<!Doctype html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta property="qc:admins" content="465267610762567726375" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Python 基础教程 | 菜鸟教程</title>
<link rel='dns-prefetch' href='//s.w.org' />
<link rel="canonical" href="http://www.runoob.com/python/python-tutorial.html" />
<meta name="keywords" content="Python 基础教程,Python">
<meta name="description" content="Python 基础教程   Python是一种解释型、面向对象、动态数据类型的高级程序设计语言。 Python由Guido van Rossum于1989年底发明，第一个公开发行版发行于1991年。  像Perl语言一样, Python 源代码同样遵循 GPL(GNU General Public License)协议。 本教程主要针对Python 2.x版本的学习，如果你使用的是Python 3.x版本请移步至Python 3.X版本..">
<link rel="shortcut icon" href="//static.runoob.com/images/favicon.ico" mce_href="//static.runoob.com/images/favicon.ico" type="image/x-icon">
<link rel="stylesheet" href="/wp-content/themes/runoob/style.css?v=1.14" type="text/css" media="all" />
<link rel="stylesheet" href="//cdn.bootcss.com/font-awesome/4.7.0/css/font-awesome.min.css" media="all" />
<!--[if gte IE 9]><!-->
  <script src="//cdn.bootcss.com/jquery/2.0.3/jquery.min.js"></script>
  <!--<![endif]-->
<!--[if lt IE 9]>
     <script src="//cdn.bootcss.com/jquery/1.9.1/jquery.min.js"></script>
     <script src="//cdn.bootcss.com/html5shiv/r29/html5.min.js"></script>
  <![endif]-->
<link rel="apple-touch-icon" href="//static.runoob.com/images/icon/mobile-icon.png"/>
<meta name="apple-mobile-web-app-title" content="菜鸟教程">
</head>
<body>
<div class="container logo-search">
<div class="col search row-search-mobile">
<form action="index.php">
<input class="placeholder" value="搜索……" name="s" autocomplete="off">
</form>
</div>
<div class="row">
<div class="col logo">
<h1><a href="/">菜鸟教程 -- 学的不仅是技术，更是梦想！</a></h1>
</div>
<div class="col right-list">
<button class="btn btn-responsive-nav btn-inverse" data-toggle="collapse" data-target=".nav-main-collapse" id="pull" style=""> <i class="fa fa-navicon"></i> </button>
</div>
<div class="col search search-desktop last">
<form action="//www.runoob.com/" target="_blank">
<input class="placeholder" id="s" name="s" value="搜索……" autocomplete="off">
</form>
</div>
</div>
</div>
<div class="container navigation">
<div class="row">
<div class="col nav">
<ul class="pc-nav">
<li><a href="//www.runoob.com/">首页</a></li>
<li><a href="/html/html-tutorial.html">HTML</a></li>
<li><a href="/css/css-tutorial.html">CSS</a></li>
<li><a href="/js/js-tutorial.html">JavaScript</a></li>
<li><a href="/jquery/jquery-tutorial.html">jQuery</a></li>
<li><a href="/bootstrap/bootstrap-tutorial.html">Bootstrap</a></li>
<li><a href="/sql/sql-tutorial.html">SQL</a></li>
<li><a href="/mysql/mysql-tutorial.html">MySQL</a>
>>> 
