Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib2
>>> response=urllib2.open("http:://ggfw.wuxi.gov.cn/wx_portal/")

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    response=urllib2.open("http:://ggfw.wuxi.gov.cn/wx_portal/")
AttributeError: 'module' object has no attribute 'open'
>>> import urllib2
>>> response=urllib2.urlopen("http:://ggfw.wuxi.gov.cn/wx_portal/")

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    response=urllib2.urlopen("http:://ggfw.wuxi.gov.cn/wx_portal/")
  File "C:\Python27\lib\urllib2.py", line 154, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Python27\lib\urllib2.py", line 427, in open
    req = meth(req)
  File "C:\Python27\lib\urllib2.py", line 1126, in do_request_
    raise URLError('no host given')
URLError: <urlopen error no host given>
>>> reponse = urllib2.urlopen("http://ggfw.wuxi.gov.cn/wx_portal/")
>>> print response.read(3000)

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print response.read(3000)
NameError: name 'response' is not defined
>>> print response.read(3000)

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print response.read(3000)
NameError: name 'response' is not defined
>>> print reponse.read(3000)








<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<title>无锡市公共服务平台</title>



<link rel="stylesheet" type="text/css" href="/wx_portal/index/B1/css/base.css">

<link rel="stylesheet" type="text/css" href="/wx_portal/index/B1/css/header-wx.css">

<link rel="stylesheet" type="text/css" href="/wx_portal/index/B1/css/selectform.css">

<link rel="stylesheet" type="text/css" href="/wx_portal/index/B1/css/footer-wx.css">

<link type="text/css" rel="stylesheet" href="/wx_portal/index/B1/css/owl.carousel.css">

<link type="text/css" rel="stylesheet" href="/wx_portal/index/B1/css/owl.theme.css">

<link rel="stylesheet" type="text/css" href="/wx_portal/index/B1/css/peo_index.css">

<script src="/wx_portal/common/js/jquery-1.8.2.min.js"></script>

<!-- <script type="text/javascript" src="/wx_portal/index/B1/js/jquery.js"></script> -->

<script type="text/javascript">

		var indexUserId = 'null';

		var app_path='/wx_portal';

		var bx_myserver_catalogid = '1001';

// 		var mourl = "http://ggfw.wuxi.gov.cn/wx_mo";

// 		var imageurl = "http://ggfw.wuxi.gov.cn/image";

	</script>

<link rel="stylesheet" href="/wx_portal/common/css/bootstrap.min.css">

	<link rel="stylesheet" href="/wx_portal/common/css/local_base.css" type="text/css"/>

	<link rel="stylesheet" href="/wx_portal/frame/Bs1/css/local_common.css" />

	<!--page层-->

<!-- 	<link rel="stylesheet" href="/wx_portal/index/B1/css/city_index.css" type="text/css"/> -->

	<script src="/wx_portal/common/js/bootstrap.min.js"></script>

	<script src="/wx_portal/common/js/main.js"></script>	

	<!-- <script src="/wx_portal/common/js/plugins/jquery.slides.min.js"></script> -->

<!-- 	<script src="/wx_portal/common/js/plugins/jquery.nivo.slider.js"></script> -->

	<script src="/wx_portal/frame/Bs1/js/local_frame.js"></script>

	<script type="text/javascript" src="/wx_portal/common/js/common1.js"></script>

	<script type="text/javascript" src="/wx_portal/js/jquery.cookie.js"></script>

	<script type="text/javascript" src="/wx_portal/js/cookie.js"></script>

	<script type="text/javascript" src="/wx_portal/js/delcookie.js"></script>

	<script type="text/javascript" src="/wx_portal/index/B1/js/index.js"></script>

	<script type="text/javascript" src="/wx_portal/index/B1/js/owl.carousel.min.js"></script>

<script type="text/javascript">

		$(function(){

	//	    index.init();

			//index.showRecommend(0);

			index.getCatapplist(bx_myserver_catalogid);

			index.getSpecial('1005');

			$("#peoServiceBtn").addClass('selectedItem');

			// 重置

			$(".resetbtn").click(function(){

				$(this).parent().parent().find("input[type='text']").val("");

			});

			// 轮播 

	        $('#scroll').owlCarousel({

				items: 7,

				itemsDesktop:[2400,7],

				itemsDesktopSmall:[800,7],

				autoPlay: true,

				navigation: true,

				navigationText: ["",""],

				scrollPerPage: true

			});   

	  });

	</script>

	<style type="text/css">

	.ui_tumble_list a{

		margin-bottom: 5px;


>>> 
