"""
	功能：
        1. 多条记录分析与获取
        2. 将内容保存到csv文件
    问题：
	    下载网页部分存在问题，不能正常下载到需要的数据
"""

import re
import time
import csv
from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException


def download(url, headers=None, num_retries=3):
    print('Downloading:', url)
    try:
        response = requests.get(url)
        print(response.status_code)
        if response.status_code == 200:
            return response.content
        return None
    except RequestException as e:
        print('error:', e.response)
        html = ''
        if hasattr(e.response, 'status_code'):
            code = e.response.status_code
            print('error code:', code)
            if num_retries > 0 and 500 <= code < 600:
                # 遇到5XX 的错误就重试
                html = download(url, headers, num_retries - 1)
        else:
            code = None
    return html


page = """
<html class="">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="renderer" content="webkit">
    <meta http-equiv="Cache-Control" content="max-age=300">
    <link rel="dns-prefetch" href="//search.jd.com">
    <link rel="dns-prefetch" href="//item.jd.com">
    <link rel="dns-prefetch" href="//list.jd.com">
    <link rel="dns-prefetch" href="//p.3.cn">
    <link rel="dns-prefetch" href="//misc.360buyimg.com">
    <link rel="dns-prefetch" href="//nfa.jd.com">
    <link rel="dns-prefetch" href="//d.jd.com">
    <link rel="dns-prefetch" href="//img12.360buyimg.com">
    <link rel="dns-prefetch" href="//img13.360buyimg.com">
    <link rel="dns-prefetch" href="//static.360buyimg.com">
    <link rel="dns-prefetch" href="//csc.jd.com">
    <link rel="dns-prefetch" href="//mercury.jd.com">
    <link rel="dns-prefetch" href="//x.jd.com">
    <link rel="dns-prefetch" href="//wl.jd.com">
    <title>手机 - 商品搜索 - 京东</title>
    <meta name="Keywords" content="手机,京东手机">
    <meta name="description" content="在京东找到了5787件手机的类似商品，其中包含了“手机”等类型的手机的商品。">
    <script type="text/javascript" async="" src="https://wlssl.jd.com/wl.js"></script>
    <script>
        window.loadFa_toJson_data = {
            query: '%E6%89%8B%E6%9C%BA'
        };
        window.jdpts = {};
        jdpts._st = new Date().getTime();
        window.pageConfig = {
            closeJpg: 1,
            compatible: false,
            searchType: 0,
            jdfVersion: '2.0.0',
            floatnav: 1,
            price_pdos_off: 0,
            actName: '',
            pSource: 'search_pc',
            queryParam: {
                c1: 0,
                c2: 653,
                c3: 655,
                brand: '',
                price: '',
                keyword: '手机',
                page: '1'
            }
        };
        window.searchUnit = {
            resizeOnebox: function (g, f, j) {
                var g = parseInt(g),
                    i = typeof f,
                    h = typeof j;
                if (!isNaN(g)) {
                    if ("string" == i && f != "" && g > 0) {
                        $("#J_oneBoxFrame_" + f).css("height", g + 10);
                        h == "function" && j()
                    } else {
                        if (i == "undefined" || i == "function") {
                            $("#virtualWareIFrame").css("height", g > 0 ? g + 10 : 0);
                            i == "function" && f()
                        }
                    }
                }
            },
            resizeShopbox: function (e, d) {
                var f = 0;
                switch (e) {
                    case 1:
                    case 2:
                        f = 145;
                        break;
                    case 3:
                        f = 75;
                        break;
                    case 4:
                        f = 80;
                        break;
                    default:
                        break
                }
                f && $("#shopboxIFrame").css("height", f).show();
                typeof (d) == "string" && (new Image().src = d)
            },
            coupon: {}
        };
        window.QUERY_KEYWORD = '手机';
        window.REAL_KEYWORD = '手机';
    </script>
    <link type="text/css" rel="stylesheet"
        href="//misc.360buyimg.com/??jdf/1.0.0/unit/ui-base/5.0.0/ui-base.css,jdf/1.0.0/unit/shortcut/5.0.0/shortcut.css,jdf/1.0.0/unit/global-header/5.0.0/global-header.css,jdf/1.0.0/unit/myjd/5.0.0/myjd.css,jdf/1.0.0/unit/nav/5.0.0/nav.css,jdf/1.0.0/unit/shoppingcart/5.0.0/shoppingcart.css,jdf/1.0.0/unit/global-footer/5.0.0/global-footer.css,jdf/1.0.0/unit/service/5.0.0/service.css,jdf/1.0.0/unit/global-header-photo/5.0.0/global-header-photo.css,jdf/1.0.0/ui/area/1.0.0/area.css">
    <link type="text/css" rel="stylesheet" href="//misc.360buyimg.com/product/search/1.0.7/css/search.css">
    <script type="text/javascript"
        src="//misc.360buyimg.com/??jdf/1.0.0/unit/base/5.0.0/base.js,jdf/lib/jquery-1.6.4.js,product/module/es5-shim.js">
    </script>
    <script>
        window.SEARCH = {
            cid: 655,
            ui_ver: '1.0.7',
            c_category: 655,
            p_category: 653,
            enable_adv: 1,
            enable_prom_adwords: 1,
            enable_prom_flag: 1,
            enable_price: 1,
            enable_stock: 2,
            enable_yyk: 0,
            lottery_code: '',
            is_correct_hash: function (e) {
                var a = ["keyword", "brand_id", "activity_id", "coupon_batch", "ecard_id"];
                for (var c = 0, b = a.length; c < b; c++) {
                    var d = new RegExp("(^|\\?|&)" + a[c] + "=([^&]*)(\\s|&|$)");
                    if (d.test(e)) {
                        return true
                    }
                }
                return false
            },
            get_real_hash: function () {
                var a = window.location.hash.substr(1);
                if (a && $.browser.mozilla) {
                    return location.href.substr(location.href.indexOf("#") + 1)
                } else {
                    return a
                }
            }
        };
        (function (a, b) {
            var c = b.get_real_hash();
            if (b.is_correct_hash(c)) {
                a.location.href = a.location.pathname + "?" + c;
                return false
            } else {
                if (a.self != a.top || $.browser.msie && $.browser.version <= 9) {
                    var f = null,
                        e = function () {
                            var d = $(a).width();
                            return 1210 > d ? $("html").removeClass() : $("html").removeClass().addClass(d >=
                                1210 && 1390 > d ? "resp01" : "resp02"), true
                        };
                    e();
                    $(a).resize(function () {
                        clearTimeout(f), f = setTimeout(e, 20)
                    })
                }
            }
        })(window, SEARCH);
    </script>
    <script async="" src="//h5.360buyimg.com/ws_js/gatherInfo.js"></script>
    <link charset="utf-8" rel="stylesheet"
        href="https://static.360buyimg.com/devfe/toolbar/1.0.0/??widget/common/common.css">
    <link charset="utf-8" rel="stylesheet" href="https://misc.360buyimg.com/jdf/1.0.0/ui/tips/1.0.0/tips.css">
</head>

<body>
    <!--shortcut start-->
    <div id="shortcut-2014">
        <div class="w">
            <ul class="fl">
                <li id="ttbar-home"><i class="iconfont"></i><a href="//www.jd.com/" target="_blank">京东首页</a></li>
                <li class="dorpdown" id="ttbar-mycity">
                    <div class="dt cw-icon ui-areamini-text-wrap" style=""> <i class="iconfont"></i> <span
                            class="ui-areamini-text" data-id="13" title="山东">山东</span> </div>
                    <div class="dd dorpdown-layer">
                        <div class="dd-spacer"></div>
                        <div class="ui-areamini-content-wrap">
                            <div class="ui-areamini-content">
                                <div class="ui-areamini-content-list clearfix">
                                    <div class="item"><a data-id="1" href="javascript:void(0)">北京</a></div>
                                    <div class="item"><a data-id="2" href="javascript:void(0)">上海</a></div>
                                    <div class="item"><a data-id="3" href="javascript:void(0)">天津</a></div>
                                    <div class="item"><a data-id="4" href="javascript:void(0)">重庆</a></div>
                                    <div class="item"><a data-id="5" href="javascript:void(0)">河北</a></div>
                                    <div class="item"><a data-id="6" href="javascript:void(0)">山西</a></div>
                                    <div class="item"><a data-id="7" href="javascript:void(0)">河南</a></div>
                                    <div class="item"><a data-id="8" href="javascript:void(0)">辽宁</a></div>
                                    <div class="item"><a data-id="9" href="javascript:void(0)">吉林</a></div>
                                    <div class="item"><a data-id="10" href="javascript:void(0)">黑龙江</a></div>
                                    <div class="item"><a data-id="11" href="javascript:void(0)">内蒙古</a></div>
                                    <div class="item"><a data-id="12" href="javascript:void(0)">江苏</a></div>
                                    <div class="item"><a data-id="13" href="javascript:void(0)" class="selected">山东</a>
                                    </div>
                                    <div class="item"><a data-id="14" href="javascript:void(0)">安徽</a></div>
                                    <div class="item"><a data-id="15" href="javascript:void(0)">浙江</a></div>
                                    <div class="item"><a data-id="16" href="javascript:void(0)">福建</a></div>
                                    <div class="item"><a data-id="17" href="javascript:void(0)">湖北</a></div>
                                    <div class="item"><a data-id="18" href="javascript:void(0)">湖南</a></div>
                                    <div class="item"><a data-id="19" href="javascript:void(0)">广东</a></div>
                                    <div class="item"><a data-id="20" href="javascript:void(0)">广西</a></div>
                                    <div class="item"><a data-id="21" href="javascript:void(0)">江西</a></div>
                                    <div class="item"><a data-id="22" href="javascript:void(0)">四川</a></div>
                                    <div class="item"><a data-id="23" href="javascript:void(0)">海南</a></div>
                                    <div class="item"><a data-id="24" href="javascript:void(0)">贵州</a></div>
                                    <div class="item"><a data-id="25" href="javascript:void(0)">云南</a></div>
                                    <div class="item"><a data-id="26" href="javascript:void(0)">西藏</a></div>
                                    <div class="item"><a data-id="27" href="javascript:void(0)">陕西</a></div>
                                    <div class="item"><a data-id="28" href="javascript:void(0)">甘肃</a></div>
                                    <div class="item"><a data-id="29" href="javascript:void(0)">青海</a></div>
                                    <div class="item"><a data-id="30" href="javascript:void(0)">宁夏</a></div>
                                    <div class="item"><a data-id="31" href="javascript:void(0)">新疆</a></div>
                                    <div class="item"><a data-id="52993" href="javascript:void(0)">港澳</a></div>
                                    <div class="item"><a data-id="32" href="javascript:void(0)">台湾</a></div>
                                    <div class="item"><a data-id="84" href="javascript:void(0)">钓鱼岛</a></div>
                                    <div class="item"><a data-id="53283" href="javascript:void(0)">海外</a></div>
                                </div>
                            </div>
                        </div>
                        <div class="areamini_inter">
                            <div class="areamini_inter_split"></div>
                            <p class="areamini_inter_desc">Available Sites</p>
                            <ul class="areamini_inter_list">
                                <li class="areamini_inter_item"> <a class="areamini_inter_lk"
                                        href="//www.joybuy.com/?source=1&amp;visitor_from=2" target="_blank"
                                        clstag="h|keycount|head|topbar_0101">
                                        <div class="areamini_inter_ico areamini_inter_ico_global"></div>
                                        <div class="areamini_inter_name">Global Site</div>
                                    </a> </li>
                                <li class="areamini_inter_item"> <a class="areamini_inter_lk"
                                        href="//www.jd.ru/?source=1&amp;visitor_from=2" target="_blank"
                                        clstag="h|keycount|head|topbar_0102">
                                        <div class="areamini_inter_ico areamini_inter_ico_russia"></div>
                                        <div class="areamini_inter_name">Сайт России</div>
                                    </a> </li>
                                <li class="areamini_inter_item"> <a class="areamini_inter_lk"
                                        href="//www.jd.id/?source=1&amp;visitor_from=2" target="_blank"
                                        clstag="h|keycount|head|topbar_0103">
                                        <div class="areamini_inter_ico areamini_inter_ico_indonesia"></div>
                                        <div class="areamini_inter_name">Situs Indonesia</div>
                                    </a> </li>
                                <li class="areamini_inter_item"> <a class="areamini_inter_lk"
                                        href="//www.joybuy.es/?source=1&amp;visitor_from=2" target="_blank"
                                        clstag="h|keycount|head|topbar_0103">
                                        <div class="areamini_inter_ico areamini_inter_ico_spain"></div>
                                        <div class="areamini_inter_name">Sitio de España</div>
                                    </a> </li>
                                <li class="areamini_inter_item"> <a class="areamini_inter_lk"
                                        href="//www.jd.co.th/?source=1&amp;visitor_from=2" target="_blank"
                                        clstag="h|keycount|head|topbar_0105">
                                        <div class="areamini_inter_ico areamini_inter_ico_thailand"></div>
                                        <div class="areamini_inter_name">เว็บไซต์ประเทศไทย</div>
                                    </a> </li>
                            </ul>
                        </div>
                    </div>
                </li>
            </ul>
            <ul class="fr">
                <li class="fore1" id="ttbar-login"><a href="javascript:login();"
                        class="link-login">你好，请登录</a>&nbsp;&nbsp;<a href="javascript:regist();"
                        class="link-regist style-red">免费注册</a></li>
                <li class="spacer"></li>
                <li class="fore2">
                    <div class="dt">
                        <a target="_blank" href="//order.jd.com/center/list.action">我的订单</a>
                    </div>
                </li>
                <li class="spacer"></li>
                <li class="fore3 dorpdown" id="ttbar-myjd">
                    <div class="dt cw-icon">
                        <!-- <i class="ci-right"><s>◇</s></i> -->
                        <a target="_blank" href="//home.jd.com/">我的京东</a><i class="iconfont"></i>
                    </div>
                    <div class="dd dorpdown-layer">
                        <div class="dd-spacer"></div>
                        <div class="dd-inner"><span class="loading"></span></div>
                    </div>
                </li>
                <li class="spacer"></li>
                <li class="fore4" id="ttbar-member">
                    <div class="dt">
                        <a target="_blank" href="//vip.jd.com/">京东会员</a>
                    </div>
                </li>
                <li class="spacer"></li>
                <li class="fore5 dorpdown" id="ttbar-ent">
                    <div class="dt cw-icon"> <a target="_blank" href="//b.jd.com/">企业采购</a><i class="iconfont"></i>
                    </div>
                    <div class="dd dorpdown-layer">
                        <div class="dd-spacer"></div>
                        <div class="dd-inner" id="ttbar-ent-main">
                            <div class="dd-spacer"></div>
                            <div class="dd-inner"><span class="loading"></span></div>
                        </div>
                    </div>
                </li>
                <li class="spacer"></li>
                <li class="fore6 dorpdown" id="ttbar-serv">
                    <div class="dt cw-icon">
                        <!-- <i class="ci-right"><s>◇</s></i> -->
                        客户服务<i class="iconfont"></i>
                    </div>
                    <div class="dd dorpdown-layer">
                        <div class="dd-spacer"></div>
                        <div class="dd-inner"><span class="loading"></span></div>
                    </div>
                </li>
                <li class="spacer"></li>
                <li class="fore7 dorpdown" id="ttbar-navs">
                    <div class="dt cw-icon">
                        <!-- <i class="ci-right"><s>◇</s></i> -->
                        网站导航<i class="iconfont"></i>
                    </div>
                    <div class="dd dorpdown-layer">
                        <div class="dd-spacer"></div>
                        <div class="dd-inner"><span class="loading"></span></div>
                    </div>
                </li>
                <li class="spacer"></li>
                <li class="fore8 dorpdown" id="ttbar-apps">
                    <div class="dt cw-icon">
                        <!-- <i class="ci-left"></i> -->
                        <!-- <i class="ci-right"><s>◇</s></i> -->
                        <a target="_blank" href="//app.jd.com/">手机京东</a>
                    </div>
                    <div class="dd dorpdown-layer">
                        <div class="dd-spacer"></div>
                        <div class="dd-inner" id="ttbar-apps-main">
                            <div class="dd-spacer"></div>
                            <div class="dd-inner"><span class="loading"></span></div>
                        </div>
                    </div>
                </li>
            </ul>
            <span class="clr"></span>
        </div>
    </div>
    <div id="o-header-2013">
        <div id="header-2013" style="display:none;"></div>
    </div>
    <!--shortcut end-->
    <div class="w">
        <div id="logo-2014">
            <a href="//www.jd.com/" class="logo">京东</a>
        </div>
        <div id="search-2014">
            <ul id="shelper" class="hide" style="display: none;"></ul>
            <div class="form">
                <input type="text" onkeydown="javascript:if(event.keyCode==13) search('key');" autocomplete="off"
                    id="key" accesskey="s" class="text blurcolor"><span class="photo-search-btn">
                    <form id="search-img-upload" clstag="h|keycount|2016|03d" method="post"
                        action="//search.jd.com/image?op=upload" enctype="multipart/form-data" target="search_upload">
                        <span class="upload-bg"></span><input type="file" name="file" class="upload-trigger"
                            accept="image/png,image/jpeg,image/jpg"></form>
                </span>
                <button onclick="search('key');return false;" class="button cw-icon"><i></i>搜索</button>
            </div>
        </div>
        <div id="settleup-2014" class="dorpdown">
            <div class="cw-icon">
                <i class="iconfont"></i>
                <i class="iconfont arrow"></i><i class="ci-count" id="shopping-amount">0</i>
                <a target="_blank" href="//cart.jd.com/cart.action">我的购物车</a>
            </div>
            <div class="dorpdown-layer">
                <div class="spacer"></div>
                <div id="settleup-content"><span class="loading"></span></div>
            </div>
        </div>
        <div id="hotwords" class="haveline"><a onclick="searchlog(1,0,0,52,'华为')"
                href="Search?keyword=%E5%8D%8E%E4%B8%BA&amp;enc=utf-8&amp;spm=2.1.0" class="fore">华为</a><b>|</b><a
                onclick="searchlog(1,0,1,52,'华为手机')"
                href="Search?keyword=%E5%8D%8E%E4%B8%BA%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;spm=2.1.1">华为手机</a><b>|</b><a
                onclick="searchlog(1,0,2,52,'手机自营')"
                href="Search?keyword=%E6%89%8B%E6%9C%BA%E8%87%AA%E8%90%A5&amp;enc=utf-8&amp;spm=2.1.2">手机自营</a><b>|</b><a
                onclick="searchlog(1,0,3,52,'小米')"
                href="Search?keyword=%E5%B0%8F%E7%B1%B3&amp;enc=utf-8&amp;spm=2.1.3">小米</a><b>|</b><a
                onclick="searchlog(1,0,4,52,'二手手机')"
                href="Search?keyword=%E4%BA%8C%E6%89%8B%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;spm=2.1.4">二手手机</a><b>|</b><a
                onclick="searchlog(1,0,5,52,'手机5g手机')"
                href="Search?keyword=%E6%89%8B%E6%9C%BA5g%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;spm=2.1.5">手机5g手机</a><b>|</b><a
                onclick="searchlog(1,0,6,52,'荣耀')"
                href="Search?keyword=%E8%8D%A3%E8%80%80&amp;enc=utf-8&amp;spm=2.1.6">荣耀</a><b>|</b><a
                onclick="searchlog(1,0,7,52,'苹果')"
                href="Search?keyword=%E8%8B%B9%E6%9E%9C&amp;enc=utf-8&amp;spm=2.1.7">苹果</a><b>|</b><a
                onclick="searchlog(1,0,8,52,'苹果手机')"
                href="Search?keyword=%E8%8B%B9%E6%9E%9C%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;spm=2.1.8">苹果手机</a><b>|</b><a
                onclick="searchlog(1,0,9,52,'oppo')"
                href="Search?keyword=oppo&amp;enc=utf-8&amp;spm=2.1.9">oppo</a><b>|</b><a
                onclick="searchlog(1,0,10,52,'vivo')"
                href="Search?keyword=vivo&amp;enc=utf-8&amp;spm=2.1.10">vivo</a><b>|</b><a
                onclick="searchlog(1,0,11,52,'小米9')"
                href="Search?keyword=%E5%B0%8F%E7%B1%B39&amp;enc=utf-8&amp;spm=2.1.11">小米9</a><b>|</b><a
                onclick="searchlog(1,0,12,52,'华为p30')"
                href="Search?keyword=%E5%8D%8E%E4%B8%BAp30&amp;enc=utf-8&amp;spm=2.1.12">华为p30</a><b>|</b><a
                onclick="searchlog(1,0,13,52,'小米手机')"
                href="Search?keyword=%E5%B0%8F%E7%B1%B3%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;spm=2.1.13">小米手机</a></div>
        <span class="clr"></span>
    </div>
    <!--nav start-->
    <div id="nav-2014">
        <div class="w">
            <div class="w-spacer"></div>
            <div id="categorys-2014" class="dorpdown" data-type="default"
                style="height: auto; left: 0px; position: absolute;">
                <div class="dt">
                    <a target="_blank" href="//www.jd.com/allSort.aspx">全部商品分类</a>
                </div>
                <div class="dd" style="display:none;"></div>
            </div>
            <div id="navitems-2014" style="padding-left: 190px;">
                <ul id="navitems-group1">
                    <li clstag="" id="nav-fashion" class="fore1">
                        <a class="b" target="_blank" href="//channel.jd.com/fashion.html">京东时尚</a>
                    </li>
                    <li clstag="" id="nav-beauty" class="fore2">
                        <a class="b" target="_blank" href="//channel.jd.com/beautysale.html">美妆馆</a>
                    </li>
                    <li clstag="" id="nav-chaoshi" class="fore3">
                        <a class="b" target="_blank" href="//channel.jd.com/chaoshi.html">超市</a>
                    </li>
                    <li clstag="" id="nav-fresh" class="fore4">
                        <a class="b" target="_blank" href="//fresh.jd.com">生鲜</a>
                    </li>
                </ul>
                <div class="spacer"></div>
                <ul id="navitems-group2">
                    <li clstag="" id="nav-jdww" class="fore1">
                        <a class="b" target="_blank" href="//www.jd.hk/">海囤全球</a>
                    </li>
                    <li clstag="" id="nav-red" class="fore2">
                        <a class="b" target="_blank" href="//red.jd.com/">闪购</a>
                    </li>
                    <li clstag="" id="nav-auction" class="fore3">
                        <a class="b" target="_blank" href="//paimai.jd.com/">拍卖</a>
                    </li>
                </ul>
                <div class="spacer"></div>
                <ul id="navitems-group3">
                    <li clstag="" id="nav-jdjr" class="fore1">
                        <a class="b" target="_blank" href="//jr.jd.com/">金融</a>
                    </li>
                </ul>
            </div>
            <div id="treasure"></div>
            <span class="clr"></span>
        </div>
    </div>
    <!--nav end-->
    <div style="display:none"><a href="//club.jd.com/rank/655/e69c8de58aa1e68081e5baa6e5a5bd_2.html">服务态度好</a><a
            href="//club.jd.com/rank/655/e59381e8b4a8e580bce5be97e4bfa1e8b596_2.html">品质值得信赖</a><a
            href="//club.jd.com/rank/655/e789a9e6b581e9809fe5baa6e5bfab_2.html">物流速度快</a><a
            href="//club.jd.com/rank/655/e6ada3e59381e4bf9de99a9c_2.html">正品保障</a><a
            href="//club.jd.com/rank/655/e789a9e7be8ee4bbb7e5bb89_2.html">物美价廉</a><a
            href="//club.jd.com/rank/655/e680a7e4bbb7e6af94e8be83e9ab98_2.html">性价比较高</a><a
            href="//club.jd.com/rank/655.html">好评度</a><a
            href="//club.jd.com/koubei/e9ad85e6978fe6898be69cba.html">魅族手机</a><a
            href="//club.jd.com/koubei/e7b4a2e5b0bce6898be69cba.html">索尼手机</a><a
            href="//club.jd.com/koubei/31e6898be69cba.html">1手机</a><a
            href="//club.jd.com/koubei/e58d8ee4b8bae88da3e8808038e6898be69cba.html">华为荣耀8手机</a><a
            href="//club.jd.com/koubei/e5beaee8bdafe6898be69cba.html">微软手机</a><a
            href="//club.jd.com/koubei/e8afbae59fbae4ba9ae6898be69cba.html">诺基亚手机</a><a
            href="//club.jd.com/koubei/e4b8ade585b4e6898be69cba.html">中兴手机</a><a
            href="//club.jd.com/koubei/e88bb9e69e9c6970686f6e65e6898be69cba.html">苹果iphone手机</a><a
            href="//club.jd.com/koubei/e88da3e88080e696b0e6acbee6898be69cba.html">荣耀新款手机</a><a
            href="//club.jd.com/koubei/e6ada5e6ada5e9ab98e6898be69cba.html">步步高手机</a><a
            href="https://www.jd.com/pinpai/25591.html">vivo</a><a href="https://www.jd.com/pinpai/63032.html">一加</a><a
            href="https://www.jd.com/pinpai/655-212527.html">惠族（HUIZUU）</a><a
            href="https://www.jd.com/pinpai/655-205278.html">COTTEE</a><a
            href="https://www.jd.com/pinpai/655-38605.html">MANN</a><a
            href="https://www.jd.com/jiage/9987966d01887f957937.html">wa wa mi yu</a><a
            href="https://www.jd.com/jiage/9987e0ca018f808d3dee.html">一加一支持联通4g</a><a
            href="https://www.jd.com/tupian/9987e57e983103208b06.html">中兴520b</a><a
            href="https://www.jd.com/tupian/9987cd40656ba6e4d1ff.html">6以上手机</a><a
            href="https://www.jd.com/xinkuan/9987bbc4ec94276fe486.html">正品大显</a><a
            href="https://www.jd.com/xinkuan/99871a6b97ec7041e5dc.html">小米i5</a><a
            href="https://www.jd.com/sptopic/6705e45a38098f335eb.html">联想K320t</a><a
            href="https://www.jd.com/sptopic/6706edbb8ba5ee16c6b.html">诺基亚（NOKIA）E63</a><a
            href="https://www.jd.com/sptopic/9987f001012d9b1d37c3.html">卡特红色手机</a><a
            href="https://www.jd.com/hotitem/998754408da4a046ecc8.html">copitel老人机</a><a
            href="https://www.jd.com/hotitem/998785a0746a8a2c7065.html">新款ios手机价位</a><a
            href="https://www.jd.com/hotitem/652c83c818ef3c93651.html">华为（HUAWEI）畅玩7X </a><a
            href="https://www.jd.com/jxinfo/d68990f72978b024.html">电信4寸排行榜，电信4寸十大排名推荐</a><a
            href="https://www.jd.com/jxinfo/e6f52f3f26463e10.html">Apple iPhone 6s Plus 手机 灰色</a><a
            href="https://www.jd.com/jxinfo/0da409e008b6212e.html">守护宝 L105 手机 金色</a><a
            href="https://yp.jd.com/9987619247247bf7074f.html">朵唯500-999手机</a><a
            href="https://yp.jd.com/99872d1f94cac1be2b43.html">恒波双卡双4G手机</a><a
            href="https://www.jd.com/phb/9987e1553a714b99cd7d.html">3C老人机</a><a
            href="https://www.jd.com/phb/99871c2aa34f9caf18c8.html">翻盖大屏手机</a><a
            href="https://www.jd.com/phb/key_998726722f82d5644d70.html">三防手机双卡双待</a><a
            href="https://www.jd.com/phb/key_9987d318186d62708f83.html">3C小米黑色分期</a><a
            href="https://www.jd.com/phb/key_998761c2772371a9da4d.html">哈尔滨七星手机</a><a
            href="https://www.jd.com/phb/zhishi/ff3637ad933b03c5.html">声卡麦克风手机排行榜，声卡麦克风手机十大排名推荐</a><a
            href="https://www.jd.com/phb/zhishi/255b00b626984019.html">狗狗中暑的解决办法</a><a
            href="https://www.jd.com/phb/zhishi/f94fba8be8225729.html">利用4种海绵时间 强健自己身体</a><a
            href="https://www.jd.com/brand/998703b921256c902e87.html">oppo充值中心</a><a
            href="https://www.jd.com/brand/99870a706d48e343307d.html">vivo手机751a</a><a
            href="https://www.jd.com/xinghao/9987751582afc599339f.html">nubia与中兴</a><a
            href="https://www.jd.com/xinghao/9987ef6ca5199c6251f9.html">中国移动商城手机</a><a
            href="https://www.jd.com/cppf/9987f4c0b3cf50626421.html">荣耀8x性价比</a><a
            href="https://www.jd.com/cppf/9987a9a9de0f8543b2ff.html">小米4cmcv</a><a
            href="https://www.jd.com/cppf/9987c4380dd663d6dce3.html">小米cp0027</a><a
            href="https://www.jd.com/nrjs/ee1046a021e5bcc4.html">智能手机解锁哪款好？智能手机解锁怎么样好用吗？</a><a
            href="https://www.jd.com/nrjs/0719c55414c47402.html">高端大屏手机哪款好？高端大屏手机怎么样好用吗？</a><a
            href="https://www.jd.com/nrjs/ab4932400530af51.html">tl10华为哪款好？tl10华为怎么样好用吗？</a><a
            href="https://www.jd.com/book/99874d55213a81dc3f3a.html">海信手机h10</a><a
            href="https://www.jd.com/book/998756dabf95bea499ce.html">金立v7000手机</a><a
            href="https://www.jd.com/zuozhe/998712f2e3f667db36f6.html">联想手机售价</a><a
            href="https://www.jd.com/zuozhe/99870fb247e6f066aa84.html">华为tl10a价钱</a><a
            href="https://www.jd.com/hprm/670b1ce3d0accfd4159.html">华为Mate10</a><a
            href="https://www.jd.com/hprm/9987f04396fab9dc55f8.html">酷和黑色手机</a><a
            href="https://www.jd.com/hprm/998774d83d5a67fbf961.html">魅族PRO6新机</a><a
            href="https://www.jd.com/zxnews/0adec67cf75860da.html">支持联通手机哪款好？支持联通手机怎么样好用吗？</a><a
            href="https://www.jd.com/zxnews/31ca84b763327aa4.html">四核智能手机电信哪款好？四核智能手机电信怎么样好用吗？</a><a
            href="https://www.jd.com/zxnews/f045d41096e4233b.html">八合手机哪款好？八合手机怎么样好用吗？</a></div>
    <div id="J_searchWrap" class="w">
        <div id="J_crumbsBar" class="crumbs-bar">
            <div class="crumbs-nav">
                <div class="crumbs-nav-main clearfix">
                    <div class="crumbs-nav-item">
                        <div class="crumbs-first"><a
                                href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA">全部结果</a>
                        </div>
                    </div>
                    <i class="crumbs-arrow">&gt;</i>
                    <div class="crumbs-nav-item">

                        <div class="menu-drop">
                            <div class="trigger"><a class="curr"
                                    href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653#J_searchWrap">手机</a><i
                                    class="menu-drop-arrow"></i></div>
                            <div class="menu-drop-main">
                                <ul class="menu-drop-list" data-level="p">
                                    <li class="first"><span>手机</span></li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=13767#J_searchWrap"
                                            title="二手手机通讯" onclick="searchlog(1,13767,0,51)">二手手机通讯</a></li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=6880#J_searchWrap"
                                            title="运营商" onclick="searchlog(1,6880,1,51)">运营商</a></li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=830#J_searchWrap"
                                            title="手机配件" onclick="searchlog(1,830,2,51)">手机配件</a></li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=828#J_searchWrap"
                                            title="影音娱乐" onclick="searchlog(1,828,3,51)">影音娱乐</a></li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=6745#J_searchWrap"
                                            title="汽车装饰" onclick="searchlog(1,6745,4,51)">汽车装饰</a></li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=12345#J_searchWrap"
                                            title="智能设备" onclick="searchlog(1,12345,5,51)">智能设备</a></li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=671#J_searchWrap"
                                            title="电脑整机" onclick="searchlog(1,671,6,51)">电脑整机</a></li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=1462#J_searchWrap"
                                            title="户外装备" onclick="searchlog(1,1462,7,51)">户外装备</a></li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=829#J_searchWrap"
                                            title="数码配件" onclick="searchlog(1,829,8,51)">数码配件</a></li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=3287#J_searchWrap"
                                            title="计算机与互联网" onclick="searchlog(1,3287,9,51)">计算机与互联网</a></li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=13780#J_searchWrap"
                                            title="收纳用品" onclick="searchlog(1,13780,10,51)">收纳用品</a></li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=17407#J_searchWrap"
                                            title="视听影音" onclick="searchlog(1,17407,11,51)">视听影音</a></li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=686#J_searchWrap"
                                            title="外设产品" onclick="searchlog(1,686,12,51)">外设产品</a></li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=12800#J_searchWrap"
                                            title="游戏设备" onclick="searchlog(1,12800,13,51)">游戏设备</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <i class="crumbs-arrow">&gt;</i>
                    <div class="crumbs-nav-item">

                        <div class="menu-drop">
                            <div class="trigger"><a class="curr"
                                    href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid3=655#J_searchWrap">手机</a><i
                                    class="menu-drop-arrow"></i></div>
                            <div class="menu-drop-main">
                                <ul class="menu-drop-list clearfix" data-level="c">
                                    <li class="first"><span>手机</span></li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid3=13271#J_searchWrap"
                                            title="特殊商品" onclick="searchlog(1,13271,0,51)">特殊商品</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <i class="crumbs-arrow">&gt;</i>
                    <div class="crumbs-nav-item">
                        <strong class="search-key">"手机"</strong>
                    </div>
                </div>
            </div>
        </div>
        <div id="J_container" class="container">
            <div id="J_selector" class="selector">
                <div class="J_selectorLine s-brand">
                    <div class="sl-wrap">
                        <div class="sl-key"><strong>品牌：</strong></div>
                        <div class="sl-value">
                            <ul class="sl-b-letter J_brandLetter" onclick="searchlog(1,0,0,48)">
                                <li data-initial="0" class="curr">所有品牌</li>
                                <li data-initial="A">A</li>
                                <li data-initial="B">B</li>
                                <li data-initial="C">C</li>
                                <li data-initial="D">D</li>
                                <li data-initial="F">F</li>
                                <li data-initial="H">H</li>
                                <li data-initial="K">K</li>
                                <li data-initial="L">L</li>
                                <li data-initial="M">M</li>
                                <li data-initial="N">N</li>
                                <li data-initial="O">O</li>
                                <li data-initial="R">R</li>
                                <li data-initial="S">S</li>
                                <li data-initial="T">T</li>
                                <li data-initial="V">V</li>
                                <li data-initial="X">X</li>
                                <li data-initial="Y">Y</li>
                                <li data-initial="Z">Z</li>
                            </ul>
                            <div class="clr"></div>
                            <div class="sl-v-logos">
                                <ul class="J_valueList v-fixed">
                                    <li id="brand-8557" data-initial="H" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,0,71,'品牌::华为（HUAWEI）')"
                                            title="华为（HUAWEI）">
                                            <i></i><img
                                                src="//img30.360buyimg.com/popshop/jfs/t1/21713/1/5027/5175/5c38740eE4ccfc381/0bedaba1e05119ac.jpg"
                                                width="102" height="36">华为（HUAWEI） </a>
                                    </li>
                                    <li id="brand-14026" data-initial="A" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_Apple%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,1,71,'品牌::Apple')" title="Apple">
                                            <i></i><img
                                                src="//img30.360buyimg.com/popshop/jfs/t2989/240/151377693/3895/30ad9044/574d36dbN262ef26d.jpg"
                                                width="102" height="36">Apple </a>
                                    </li>
                                    <li id="brand-18374" data-initial="X" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E5%B0%8F%E7%B1%B3%EF%BC%88MI%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,2,71,'品牌::小米（MI）')" title="小米（MI）">
                                            <i></i><img
                                                src="//img20.360buyimg.com/popshop/jfs/t1/906/28/10166/2645/5bc93b63Eb0813c2e/600c61f344607414.jpg"
                                                width="102" height="36">小米（MI） </a>
                                    </li>
                                    <li id="brand-2032" data-initial="O" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_OPPO%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,3,71,'品牌::OPPO')" title="OPPO">
                                            <i></i><img
                                                src="//img20.360buyimg.com/popshop/jfs/t1/22465/2/10288/3283/5c860ac9E1bbb5da9/33ffbca794e7b965.jpg"
                                                width="102" height="36">OPPO </a>
                                    </li>
                                    <li id="brand-63032" data-initial="Y" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E4%B8%80%E5%8A%A0%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,4,71,'品牌::一加')" title="一加">
                                            <i></i><img
                                                src="//img30.360buyimg.com/popshop/jfs/t2398/233/975959106/6263/a786f5b8/563b33ffN9c288c6c.jpg"
                                                width="102" height="36">一加 </a>
                                    </li>
                                    <li id="brand-25591" data-initial="V" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_vivo%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,5,71,'品牌::vivo')" title="vivo">
                                            <i></i><img
                                                src="//img20.360buyimg.com/popshop/jfs/t1/29511/37/10225/4458/5c860fb4E13b3c8bb/38a9e351637f92f9.jpg"
                                                width="102" height="36">vivo </a>
                                    </li>
                                    <li id="brand-240039" data-initial="M" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E9%AD%85%E6%97%8F%EF%BC%88MEIZU%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,6,71,'品牌::魅族（MEIZU）')"
                                            title="魅族（MEIZU）">
                                            <i></i><img
                                                src="//img30.360buyimg.com/popshop/jfs/t23308/338/2405488313/4879/86ef646d/5b7e7f1fNddb8e4ff.jpg"
                                                width="102" height="36">魅族（MEIZU） </a>
                                    </li>
                                    <li id="brand-15127" data-initial="S" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E4%B8%89%E6%98%9F%EF%BC%88SAMSUNG%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,7,71,'品牌::三星（SAMSUNG）')"
                                            title="三星（SAMSUNG）">
                                            <i></i><img
                                                src="//img20.360buyimg.com/popshop/jfs/t1/1534/38/9873/3556/5bc93df2E73c40121/74dc92d16e483509.jpg"
                                                width="102" height="36">三星（SAMSUNG） </a>
                                    </li>
                                    <li id="brand-13539" data-initial="N" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E8%AF%BA%E5%9F%BA%E4%BA%9A%EF%BC%88NOKIA%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,8,71,'品牌::诺基亚（NOKIA）')"
                                            title="诺基亚（NOKIA）">
                                            <i></i><img
                                                src="//img20.360buyimg.com/popshop/jfs/t1/1035/26/11181/2858/5bce7321E51f2c59e/0c685f39d86436dd.jpg"
                                                width="102" height="36">诺基亚（NOKIA） </a>
                                    </li>
                                    <li id="brand-298340" data-initial="H" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E9%BB%91%E9%B2%A8%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,9,71,'品牌::黑鲨')" title="黑鲨">
                                            <i></i><img
                                                src="//img20.360buyimg.com/popshop/jfs/t1/9366/31/13399/5823/5c41d14fEfc04192d/283a213db9eb9735.jpg"
                                                width="102" height="36">黑鲨 </a>
                                    </li>
                                    <li id="brand-215243" data-initial="F" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E9%A3%9E%E5%88%A9%E6%B5%A6%EF%BC%88PHILIPS%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,10,71,'品牌::飞利浦（PHILIPS）')"
                                            title="飞利浦（PHILIPS）">
                                            <i></i><img
                                                src="//img20.360buyimg.com/popshop/jfs/t1/5932/28/11176/6002/5bce822bE4be57b0c/162d6a5b24eb2ab7.jpg"
                                                width="102" height="36">飞利浦（PHILIPS） </a>
                                    </li>
                                    <li id="brand-27094" data-initial="N" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E5%8A%AA%E6%AF%94%E4%BA%9A%EF%BC%88nubia%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,11,71,'品牌::努比亚（nubia）')"
                                            title="努比亚（nubia）">
                                            <i></i><img
                                                src="//img20.360buyimg.com/popshop/jfs/t2101/155/882410684/3730/b24b14db/5631cd12N7548352d.jpg"
                                                width="102" height="36">努比亚（nubia） </a>
                                    </li>
                                    <li id="brand-438621" data-initial="R" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_realme%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,12,71,'品牌::realme')" title="realme">
                                            <i></i><img
                                                src="//img30.360buyimg.com/popshop/jfs/t1/48763/28/366/4349/5cd4d321E3de63480/bb6bd8cb1169483f.jpg"
                                                width="102" height="36">realme </a>
                                    </li>
                                    <li id="brand-38126" data-initial="M" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E7%BE%8E%E5%9B%BE%EF%BC%88meitu%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,13,71,'品牌::美图（meitu）')"
                                            title="美图（meitu）">
                                            <i></i><img
                                                src="//img20.360buyimg.com/popshop/jfs/t1/16499/6/14897/3459/5cac7aaaEa660b929/87a13d76760b2ebf.jpg"
                                                width="102" height="36">美图（meitu） </a>
                                    </li>
                                    <li id="brand-2266" data-initial="R" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_ROG%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,14,71,'品牌::ROG')" title="ROG">
                                            <i></i><img
                                                src="//img30.360buyimg.com/popshop/jfs/t25714/151/2114096477/2971/2c57ec07/5bc467c2Ned5a3c61.jpg"
                                                width="102" height="36">ROG </a>
                                    </li>
                                    <li id="brand-91515" data-initial="C" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E9%94%A4%E5%AD%90%EF%BC%88smartisan%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,15,71,'品牌::锤子（smartisan）')"
                                            title="锤子（smartisan）">
                                            <i></i><img
                                                src="//img20.360buyimg.com/popshop/jfs/t1954/102/907711365/5487/9f26868f/5631ccdeNe8df5efb.jpg"
                                                width="102" height="36">锤子（smartisan） </a>
                                    </li>
                                    <li id="brand-210131" data-initial="L" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E8%81%94%E6%83%B3%EF%BC%88Lenovo%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,16,71,'品牌::联想（Lenovo）')"
                                            title="联想（Lenovo）">
                                            <i></i><img
                                                src="//img30.360buyimg.com/popshop/jfs/t1/7730/1/1440/6292/5bce7447E8c0dc0cf/15668b30fabe0850.jpg"
                                                width="102" height="36">联想（Lenovo） </a>
                                    </li>
                                    <li id="brand-16975" data-initial="T" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E5%A4%A9%E8%AF%AD%EF%BC%88K-Touch%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,17,71,'品牌::天语（K-Touch）')"
                                            title="天语（K-Touch）">
                                            <i></i><img
                                                src="//img20.360buyimg.com/popshop/jfs/t1/14033/34/5735/3344/5c41d0f9Eb0710525/2e7c09aba0e52cc5.jpg"
                                                width="102" height="36">天语（K-Touch） </a>
                                    </li>
                                    <li id="brand-21011" data-initial="Z" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E4%B8%AD%E5%85%B4%EF%BC%88ZTE%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,18,71,'品牌::中兴（ZTE）')" title="中兴（ZTE）">
                                            <i></i><img
                                                src="//img30.360buyimg.com/popshop/jfs/t1/1509/30/11025/1890/5bcda60dEe221df01/b9ea1c771f750731.png"
                                                width="102" height="36">中兴（ZTE） </a>
                                    </li>
                                    <li id="brand-18362" data-initial="X" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E5%B0%8F%E8%BE%A3%E6%A4%92%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,19,71,'品牌::小辣椒')" title="小辣椒">
                                            <i></i><img
                                                src="//img30.360buyimg.com/popshop/jfs/t1/8465/31/13429/3339/5c41d139E0f569651/8109d53385693f46.jpg"
                                                width="102" height="36">小辣椒 </a>
                                    </li>
                                    <li id="brand-8214" data-initial="H" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E9%BB%91%E8%8E%93%EF%BC%88BlackBerry%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,20,71,'品牌::黑莓（BlackBerry）')"
                                            title="黑莓（BlackBerry）">
                                            <i></i><img
                                                src="//img20.360buyimg.com/popshop/jfs/t2815/64/1277517721/2672/ece33803/57396d92N3e802994.png"
                                                width="102" height="36">黑莓（BlackBerry） </a>
                                    </li>
                                    <li id="brand-10640" data-initial="K" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E9%85%B7%E6%B4%BE%EF%BC%88Coolpad%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,21,71,'品牌::酷派（Coolpad）')"
                                            title="酷派（Coolpad）">
                                            <i></i><img
                                                src="//img20.360buyimg.com/popshop/jfs/t2521/347/883897149/3732/91c917ec/5670cf96Ncffa2ae6.jpg"
                                                width="102" height="36">酷派（Coolpad） </a>
                                    </li>
                                    <li id="brand-180213" data-initial="N" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E7%BA%BD%E6%9B%BC%EF%BC%88Newman%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,22,71,'品牌::纽曼（Newman）')"
                                            title="纽曼（Newman）">
                                            <i></i>纽曼（Newman） </a>
                                    </li>
                                    <li id="brand-13066" data-initial="M" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E6%91%A9%E6%89%98%E7%BD%97%E6%8B%89%EF%BC%88Motorola%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,23,71,'品牌::摩托罗拉（Motorola）')"
                                            title="摩托罗拉（Motorola）">
                                            <i></i><img
                                                src="//img30.360buyimg.com/popshop/jfs/t24682/107/1373450238/16268/2827346f/5baddd0eN1b9a7b91.jpg"
                                                width="102" height="36">摩托罗拉（Motorola） </a>
                                    </li>
                                    <li id="brand-16538" data-initial="S" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E7%B4%A2%E5%B0%BC%EF%BC%88SONY%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,24,71,'品牌::索尼（SONY）')"
                                            title="索尼（SONY）">
                                            <i></i><img
                                                src="//img30.360buyimg.com/popshop/jfs/t1/175/26/11602/2671/5bce70a1Ecd95c076/4d7f4f80f80c5a1c.jpg"
                                                width="102" height="36">索尼（SONY） </a>
                                    </li>
                                    <li id="brand-382193" data-initial="D" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E5%A4%9A%E4%BA%B2%EF%BC%88QIN%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,25,71,'品牌::多亲（QIN）')" title="多亲（QIN）">
                                            <i></i>多亲（QIN） </a>
                                    </li>
                                    <li id="brand-233984" data-initial="B" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_8848%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,26,71,'品牌::8848')" title="8848">
                                            <i></i><img
                                                src="//img20.360buyimg.com/popshop/jfs/t1/17462/1/6098/2529/5c46f52cEcf07df42/3f6e36540af3b563.jpg"
                                                width="102" height="36">8848 </a>
                                    </li>
                                    <li id="brand-228280" data-initial="S" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E5%AE%88%E6%8A%A4%E5%AE%9D%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,27,71,'品牌::守护宝')" title="守护宝">
                                            <i></i><img
                                                src="//img20.360buyimg.com/popshop/jfs/t4759/158/117484384/5124/74c314d7/58db2764N71d59f1b.png"
                                                width="102" height="36">守护宝 </a>
                                    </li>
                                    <li id="brand-6522" data-initial="D" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E6%9C%B5%E5%94%AF%EF%BC%88DOOV%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,28,71,'品牌::朵唯（DOOV）')"
                                            title="朵唯（DOOV）">
                                            <i></i>朵唯（DOOV） </a>
                                    </li>
                                    <li id="brand-27306" data-initial="S" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_360%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,29,71,'品牌::360')" title="360">
                                            <i></i><img
                                                src="//img30.360buyimg.com/popshop/jfs/t1/5870/5/9962/7213/5bc93baeEee154554/3544a909fb55f1b1.png"
                                                width="102" height="36">360 </a>
                                    </li>
                                    <li id="brand-398391" data-initial="M" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E9%AD%85%E6%97%8F%EF%BC%88meizu%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,30,71,'品牌::魅族（meizu）')"
                                            title="魅族（meizu）">
                                            <i></i><img
                                                src="//img20.360buyimg.com/popshop/jfs/t1/4170/15/12179/1206/5bd1a525E58f14987/db5d2beeb4bef166.png"
                                                width="102" height="36">魅族（meizu） </a>
                                    </li>
                                    <li id="brand-149070" data-initial="A" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_AGM%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,31,71,'品牌::AGM')" title="AGM">
                                            <i></i><img
                                                src="//img30.360buyimg.com/popshop/jfs/t7672/5/613320372/3853/5bcb2027/59956bc5Na0e765cd.png"
                                                width="102" height="36">AGM </a>
                                    </li>
                                    <li id="brand-198300" data-initial="H" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E6%B5%B7%E4%BF%A1%EF%BC%88Hisense%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,32,71,'品牌::海信（Hisense）')"
                                            title="海信（Hisense）">
                                            <i></i><img
                                                src="//img30.360buyimg.com/popshop/jfs/t19360/352/2305554545/5388/7fed869c/5aefeb9bN1c82297b.jpg"
                                                width="102" height="36">海信（Hisense） </a>
                                    </li>
                                    <li id="brand-253520" data-initial="V" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_VERTU%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,33,71,'品牌::VERTU')" title="VERTU">
                                            <i></i><img
                                                src="//img30.360buyimg.com/popshop/jfs/t5836/31/951952716/2427/77f5df19/5922ce08N0ec247a1.png"
                                                width="102" height="36">VERTU </a>
                                    </li>
                                    <li id="brand-249404" data-initial="C" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E5%88%9B%E6%98%9F%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,34,71,'品牌::创星')" title="创星">
                                            <i></i><img
                                                src="//img30.360buyimg.com/popshop/jfs/t22042/209/1053901270/2983/3a8a25b6/5b1f6474Nae7bf493.png"
                                                width="102" height="36">创星 </a>
                                    </li>
                                    <li id="brand-54347" data-initial="N" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E5%B0%BC%E5%87%AF%E6%81%A9%EF%BC%88neken%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,35,71,'品牌::尼凯恩（neken）')"
                                            title="尼凯恩（neken）">
                                            <i></i><img
                                                src="//img20.360buyimg.com/popshop/g13/M01/11/10/rBEhVFLTwJsIAAAAAACMa1M83DoAAH4hALKkNgAAIyD151.png"
                                                width="102" height="36">尼凯恩（neken） </a>
                                    </li>
                                    <li id="brand-20710" data-initial="C" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E9%95%BF%E8%99%B9%EF%BC%88CHANGHONG%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,36,71,'品牌::长虹（CHANGHONG）')"
                                            title="长虹（CHANGHONG）">
                                            <i></i><img
                                                src="//img30.360buyimg.com/popshop/jfs/t17380/273/1313127713/1697/2349a521/5ac43b77N3610f12d.jpg"
                                                width="102" height="36">长虹（CHANGHONG） </a>
                                    </li>
                                    <li id="brand-95450" data-initial="S" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E7%B4%A2%E7%88%B1%EF%BC%88soaiy%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,37,71,'品牌::索爱（soaiy）')"
                                            title="索爱（soaiy）">
                                            <i></i><img
                                                src="//img20.360buyimg.com/popshop/jfs/t2038/259/119166510/17973/32f59905/55efe697Naf90dce5.jpg"
                                                width="102" height="36">索爱（soaiy） </a>
                                    </li>
                                    <li id="brand-59110" data-initial="N" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_%E8%AF%BA%E4%BA%9A%E4%BF%A1%EF%BC%88NOAIN%EF%BC%89%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,38,71,'品牌::诺亚信（NOAIN）')"
                                            title="诺亚信（NOAIN）">
                                            <i></i><img
                                                src="//img20.360buyimg.com/popshop/jfs/t1/63988/30/9244/13534/5d70b5fcE3e1921ac/fb931837bd6b3ab5.jpg"
                                                width="102" height="36">诺亚信（NOAIN） </a>
                                    </li>
                                    <li id="brand-38605" data-initial="M" style="display:block;">
                                        <a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exbrand_MANN%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,39,71,'品牌::MANN')" title="MANN">
                                            <i></i><img
                                                src="//img20.360buyimg.com/popshop/g14/M0A/09/0F/rBEhVVK6oIIIAAAAAAAIviNGda8AAHWDwND6f8AAAjW195.png"
                                                width="102" height="36">MANN </a>
                                    </li>
                                </ul>
                            </div>
                            <div class="sl-b-selected J_brandSelected"><span class="sl-b-key">已选条件：</span>
                                <ul class="sl-v-list brand-selected"></ul>
                            </div>
                            <div class="sl-btns">
                                <a class="btn btn-primary J_btnsConfirm disabled" href="javascript:;">确定</a>
                                <a class="btn btn-default J_btnsCancel" href="javascript:;">取消</a>
                            </div>
                        </div>
                        <div class="sl-ext">
                            <a class="sl-e-more J_extMore" href="javascript:;"
                                data-url="brand.php?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655"
                                style="visibility: visible;">更多<i></i></a>
                            <a class="sl-e-multiple J_extMultiple" href="javascript:;">多选<i></i></a>
                        </div>
                    </div>
                </div>
                <div class="J_selectorLine s-line">
                    <div class="sl-wrap">
                        <div class="sl-key"><span>屏幕尺寸：</span></div>
                        <div class="sl-value">
                            <div class="sl-v-list">
                                <ul class="J_valueList">
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=244_124095%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow"
                                            onclick="searchlog(1,0,10000,71,'屏幕尺寸::5.0英寸以下')"><i></i>5.0英寸以下</a></li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=244_124094%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow"
                                            onclick="searchlog(1,0,10001,71,'屏幕尺寸::5.0～5.49英寸')"><i></i>5.0～5.49英寸</a>
                                    </li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=244_124093%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow"
                                            onclick="searchlog(1,0,10002,71,'屏幕尺寸::5.5～5.99英寸')"><i></i>5.5～5.99英寸</a>
                                    </li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=244_124092%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow"
                                            onclick="searchlog(1,0,10003,71,'屏幕尺寸::6.0～6.24英寸')"><i></i>6.0～6.24英寸</a>
                                    </li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=244_124091%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow"
                                            onclick="searchlog(1,0,10004,71,'屏幕尺寸::6.25-6.34英寸')"><i></i>6.25-6.34英寸</a>
                                    </li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=244_124098%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow"
                                            onclick="searchlog(1,0,10005,71,'屏幕尺寸::6.35-6.44英寸')"><i></i>6.35-6.44英寸</a>
                                    </li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=244_124090%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow"
                                            onclick="searchlog(1,0,10006,71,'屏幕尺寸::6.45-6.54英寸')"><i></i>6.45-6.54英寸</a>
                                    </li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=244_124089%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow"
                                            onclick="searchlog(1,0,10007,71,'屏幕尺寸::6.55-6.64英寸')"><i></i>6.55-6.64英寸</a>
                                    </li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=244_124088%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow"
                                            onclick="searchlog(1,0,10008,71,'屏幕尺寸::6.65-6.74英寸')"><i></i>6.65-6.74英寸</a>
                                    </li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=244_124087%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow"
                                            onclick="searchlog(1,0,10009,71,'屏幕尺寸::6.75-6.84英寸')"><i></i>6.75-6.84英寸</a>
                                    </li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=244_124085%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow"
                                            onclick="searchlog(1,0,10010,71,'屏幕尺寸::6.95英寸及以上')"><i></i>6.95英寸及以上</a>
                                    </li>
                                </ul>
                            </div>
                            <div class="sl-btns">
                                <a class="btn btn-primary J_btnsConfirm disabled" href="javascript:;">确定</a>
                                <a class="btn btn-default J_btnsCancel" href="javascript:;">取消</a>
                            </div>
                        </div>
                        <div class="sl-ext">
                            <a class="sl-e-more J_extMore" href="javascript:;"
                                style="visibility: visible;">更多<i></i></a>
                            <a class="sl-e-multiple J_extMultiple" href="javascript:;">多选<i></i></a>
                        </div>
                    </div>
                </div>
                <div class="J_selectorLine s-line">
                    <div class="sl-wrap">
                        <div class="sl-key"><span>分辨率：</span></div>
                        <div class="sl-value">
                            <div class="sl-v-list">
                                <ul class="J_valueList">
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3613_122075%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow"
                                            onclick="searchlog(1,0,20000,71,'分辨率::其它分辨率')"><i></i>其它分辨率</a></li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3613_122073%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow"
                                            onclick="searchlog(1,0,20001,71,'分辨率::全高清FHD+')"><i></i>全高清FHD+</a></li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3613_122074%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow"
                                            onclick="searchlog(1,0,20002,71,'分辨率::高清HD+')"><i></i>高清HD+</a></li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3613_103019%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,20003,71,'分辨率::标清SD')"><i></i>标清SD</a>
                                    </li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3613_122072%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow"
                                            onclick="searchlog(1,0,20004,71,'分辨率::QHD+及以上')"><i></i>QHD+及以上</a></li>
                                </ul>
                            </div>
                            <div class="sl-btns">
                                <a class="btn btn-primary J_btnsConfirm disabled" href="javascript:;">确定</a>
                                <a class="btn btn-default J_btnsCancel" href="javascript:;">取消</a>
                            </div>
                        </div>
                        <div class="sl-ext">
                            <a class="sl-e-more J_extMore" href="javascript:;" style="visibility: hidden;">更多<i></i></a>
                            <a class="sl-e-multiple J_extMultiple" href="javascript:;">多选<i></i></a>
                        </div>
                    </div>
                </div>
                <div class="J_selectorLine s-line">
                    <div class="sl-wrap">
                        <div class="sl-key"><span>操作系统：</span></div>
                        <div class="sl-value">
                            <div class="sl-v-list">
                                <ul class="J_valueList">
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=957_122037%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow"
                                            onclick="searchlog(1,0,30000,71,'操作系统::Android(安卓)')"><i></i>Android(安卓)</a>
                                    </li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=957_94165%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow" onclick="searchlog(1,0,30001,71,'操作系统::功能机')"><i></i>功能机</a>
                                    </li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=957_122042%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow"
                                            onclick="searchlog(1,0,30002,71,'操作系统::iOS(Apple)')"><i></i>iOS(Apple)</a>
                                    </li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=957_122041%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow"
                                            onclick="searchlog(1,0,30003,71,'操作系统::其它OS')"><i></i>其它OS</a></li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=957_78587%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow"
                                            onclick="searchlog(1,0,30004,71,'操作系统::YunOS')"><i></i>YunOS</a></li>
                                    <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=957_122040%5E&amp;uc=0#J_searchWrap"
                                            rel="nofollow"
                                            onclick="searchlog(1,0,30005,71,'操作系统::Symbian(塞班)')"><i></i>Symbian(塞班)</a>
                                    </li>
                                </ul>
                            </div>
                            <div class="sl-btns">
                                <a class="btn btn-primary J_btnsConfirm disabled" href="javascript:;">确定</a>
                                <a class="btn btn-default J_btnsCancel" href="javascript:;">取消</a>
                            </div>
                        </div>
                        <div class="sl-ext">
                            <a class="sl-e-more J_extMore" href="javascript:;" style="visibility: hidden;">更多<i></i></a>
                            <a class="sl-e-multiple J_extMultiple" href="javascript:;">多选<i></i></a>
                        </div>
                    </div>
                </div>
                <div id="J_selectorSenior" class="J_selectorLine s-line s-senior">
                    <div class="sl-wrap">
                        <div class="sl-key"><span>高级选项：</span></div>
                        <div class="sl-value">
                            <div class="sl-v-tab">
                                <div class="sl-tab-trigger clearfix">
                                    <a class="trig-item" href="javascript:;"><span class="text">CPU型号</span><i
                                            class="arrow"></i></a>
                                    <a class="trig-item" href="javascript:;"><span class="text">CPU品牌</span><i
                                            class="arrow"></i></a>
                                    <a class="trig-item" href="javascript:;"><span class="text">存储卡</span><i
                                            class="arrow"></i></a>
                                    <a class="trig-item" href="javascript:;"><span class="text">电池容量</span><i
                                            class="arrow"></i></a>
                                    <a class="trig-item" href="javascript:;"><span class="text">机身存储</span><i
                                            class="arrow"></i></a>
                                    <a class="trig-item" href="javascript:;"><span class="text">摄像头数量</span><i
                                            class="arrow"></i></a>
                                </div>
                            </div>
                        </div>
                        <div class="sl-tab-cont">
                            <div class="sl-tab-cont-item" style="display: none;">
                                <div class="sl-v-list">
                                    <ul class="J_valueList clearfix">
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5_125377%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,40000,71,'CPU型号::Helio G90T')"><i></i>Helio
                                                G90T</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5_122872%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,40001,71,'CPU型号::骁龙660')"><i></i>骁龙660</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5_122439%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,40002,71,'CPU型号::骁龙665')"><i></i>骁龙665</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5_117928%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,40003,71,'CPU型号::骁龙675')"><i></i>骁龙675</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5_115329%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,40004,71,'CPU型号::骁龙710')"><i></i>骁龙710</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5_116568%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,40005,71,'CPU型号::骁龙712')"><i></i>骁龙712</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5_121553%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,40006,71,'CPU型号::骁龙730')"><i></i>骁龙730</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5_122671%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,40007,71,'CPU型号::骁龙730G')"><i></i>骁龙730G</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5_122589%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,40008,71,'CPU型号::麒麟810')"><i></i>麒麟810</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5_122870%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,40009,71,'CPU型号::骁龙835')"><i></i>骁龙835</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5_122869%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,40010,71,'CPU型号::骁龙845')"><i></i>骁龙845</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5_116566%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,40011,71,'CPU型号::骁龙855')"><i></i>骁龙855</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5_122548%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,40012,71,'CPU型号::骁龙855plus')"><i></i>骁龙855plus</a>
                                        </li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5_122873%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,40013,71,'CPU型号::麒麟970')"><i></i>麒麟970</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5_113236%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,40014,71,'CPU型号::麒麟980')"><i></i>麒麟980</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5_124168%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,40015,71,'CPU型号::麒麟990')"><i></i>麒麟990</a></li>
                                    </ul>
                                    <a class="btn-multiple J_tabMultiple" href="javascript:;">多选<i></i></a>
                                </div>
                                <div class="sl-btns">
                                    <a class="btn btn-primary J_btnsConfirm disabled" href="javascript:;">确定</a>
                                    <a class="btn btn-default J_tabCancel" href="javascript:;">取消</a>
                                </div>
                            </div>
                            <div class="sl-tab-cont-item" style="display: none;">
                                <div class="sl-v-list">
                                    <ul class="J_valueList clearfix">
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3606_116295%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,50000,71,'CPU品牌::海思(HiSilicon)')"><i></i>海思(HiSilicon)</a>
                                        </li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3606_122085%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,50001,71,'CPU品牌::高通(Qualcomm)')"><i></i>高通(Qualcomm)</a>
                                        </li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3606_116292%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,50002,71,'CPU品牌::联发科(Mtk)')"><i></i>联发科(Mtk)</a>
                                        </li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3606_75964%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,50003,71,'CPU品牌::展讯')"><i></i>展讯</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3606_17109%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,50004,71,'CPU品牌::APPLE')"><i></i>APPLE</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3606_75969%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,50005,71,'CPU品牌::博通')"><i></i>博通</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3606_122086%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,50006,71,'CPU品牌::三星(Exynos)')"><i></i>三星(Exynos)</a>
                                        </li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3606_122087%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,50007,71,'CPU品牌::马威尔(Marvell)')"><i></i>马威尔(Marvell)</a>
                                        </li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3606_488%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,50008,71,'CPU品牌::英特尔(Intel)')"><i></i>英特尔(Intel)</a>
                                        </li>
                                    </ul>
                                    <a class="btn-multiple J_tabMultiple" href="javascript:;">多选<i></i></a>
                                </div>
                                <div class="sl-btns">
                                    <a class="btn btn-primary J_btnsConfirm disabled" href="javascript:;">确定</a>
                                    <a class="btn btn-default J_tabCancel" href="javascript:;">取消</a>
                                </div>
                            </div>
                            <div class="sl-tab-cont-item" style="display: none;">
                                <div class="sl-v-list">
                                    <ul class="J_valueList clearfix">
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=806_122590%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,60000,71,'存储卡::支持MicroSD(TF)')"><i></i>支持MicroSD(TF)</a>
                                        </li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=806_122096%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,60001,71,'存储卡::其它存储卡')"><i></i>其它存储卡</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=806_122095%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,60002,71,'存储卡::不支持存储卡')"><i></i>不支持存储卡</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=806_118847%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,60003,71,'存储卡::NM存储卡')"><i></i>NM存储卡</a></li>
                                    </ul>
                                    <a class="btn-multiple J_tabMultiple" href="javascript:;">多选<i></i></a>
                                </div>
                                <div class="sl-btns">
                                    <a class="btn btn-primary J_btnsConfirm disabled" href="javascript:;">确定</a>
                                    <a class="btn btn-default J_tabCancel" href="javascript:;">取消</a>
                                </div>
                            </div>
                            <div class="sl-tab-cont-item" style="display: none;">
                                <div class="sl-v-list">
                                    <ul class="J_valueList clearfix">
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3803_90184%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,70000,71,'电池容量::1200mAh以下')"><i></i>1200mAh以下</a>
                                        </li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3803_90185%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,70001,71,'电池容量::1200mAh-1999mAh')"><i></i>1200mAh-1999mAh</a>
                                        </li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3803_90187%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,70002,71,'电池容量::2000mAh-2999mAh')"><i></i>2000mAh-2999mAh</a>
                                        </li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3803_122046%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,70003,71,'电池容量::3000mAh-3499mAh')"><i></i>3000mAh-3499mAh</a>
                                        </li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3803_122047%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,70004,71,'电池容量::3500mAh-3749mAh')"><i></i>3500mAh-3749mAh</a>
                                        </li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3803_122048%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,70005,71,'电池容量::3750mAh-3999mAh')"><i></i>3750mAh-3999mAh</a>
                                        </li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3803_122049%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,70006,71,'电池容量::4000mAh-4249mAh')"><i></i>4000mAh-4249mAh</a>
                                        </li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3803_122050%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,70007,71,'电池容量::4250mAh-4449mAh')"><i></i>4250mAh-4449mAh</a>
                                        </li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3803_122051%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,70008,71,'电池容量::4500mAh-5000mAh')"><i></i>4500mAh-5000mAh</a>
                                        </li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=3803_122052%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,70009,71,'电池容量::5000mAh以上')"><i></i>5000mAh以上</a>
                                        </li>
                                    </ul>
                                    <a class="btn-multiple J_tabMultiple" href="javascript:;">多选<i></i></a>
                                </div>
                                <div class="sl-btns">
                                    <a class="btn btn-primary J_btnsConfirm disabled" href="javascript:;">确定</a>
                                    <a class="btn btn-default J_tabCancel" href="javascript:;">取消</a>
                                </div>
                            </div>
                            <div class="sl-tab-cont-item" style="display: none;">
                                <div class="sl-v-list">
                                    <ul class="J_valueList clearfix">
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=13519_85088%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,80000,71,'机身存储::8GB以下')"><i></i>8GB以下</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=13519_76033%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,80001,71,'机身存储::8GB')"><i></i>8GB</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=13519_76034%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,80002,71,'机身存储::16GB')"><i></i>16GB</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=13519_76035%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,80003,71,'机身存储::32GB')"><i></i>32GB</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=13519_76036%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,80004,71,'机身存储::64GB')"><i></i>64GB</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=13519_73965%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,80005,71,'机身存储::128GB')"><i></i>128GB</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=13519_88228%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,80006,71,'机身存储::256GB')"><i></i>256GB</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=13519_90887%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,80007,71,'机身存储::512GB')"><i></i>512GB</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=13519_122044%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,80008,71,'机身存储::其它存储')"><i></i>其它存储</a></li>
                                    </ul>
                                    <a class="btn-multiple J_tabMultiple" href="javascript:;">多选<i></i></a>
                                </div>
                                <div class="sl-btns">
                                    <a class="btn btn-primary J_btnsConfirm disabled" href="javascript:;">确定</a>
                                    <a class="btn btn-default J_tabCancel" href="javascript:;">取消</a>
                                </div>
                            </div>
                            <div class="sl-tab-cont-item" style="display: none;">
                                <div class="sl-v-list">
                                    <ul class="J_valueList clearfix">
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5147_122302%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,90000,71,'摄像头数量::后置双摄')"><i></i>后置双摄</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5147_115495%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,90001,71,'摄像头数量::后置三摄')"><i></i>后置三摄</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5147_122301%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,90002,71,'摄像头数量::后置单摄')"><i></i>后置单摄</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5147_122305%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,90003,71,'摄像头数量::后置四摄')"><i></i>后置四摄</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5147_122303%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,90004,71,'摄像头数量::无后置摄像头')"><i></i>无后置摄像头</a></li>
                                        <li><a href="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=5147_122306%5E&amp;uc=0#J_searchWrap"
                                                rel="nofollow"
                                                onclick="searchlog(1,0,90005,71,'摄像头数量::后置五摄')"><i></i>后置五摄</a></li>
                                    </ul>
                                    <a class="btn-multiple J_tabMultiple" href="javascript:;">多选<i></i></a>
                                </div>
                                <div class="sl-btns">
                                    <a class="btn btn-primary J_btnsConfirm disabled" href="javascript:;">确定</a>
                                    <a class="btn btn-default J_tabCancel" href="javascript:;">取消</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div id="J_main" class="g-main2" source-data-lazy-advertisement-install="1" data-lazy-img-install="1">
                <div class="m-list">
                    <div class="ml-wrap">
                        <div id="J_filter" class="filter">
                            <div class="f-line top">
                                <div class="f-sort"><a href="javascript:;" class="curr" onclick=""><span
                                            class="fs-tit">综合</span><em class="fs-down"><i class="arrow"></i></em></a><a
                                        href="javascript:;" class="" onclick="SEARCH.sort('3')"><span
                                            class="fs-tit">销量</span><em class="fs-down"><i class="arrow"></i></em></a><a
                                        href="javascript:;" class="" onclick="SEARCH.sort('4')"><span
                                            class="fs-tit">评论数</span><em class="fs-down"><i
                                                class="arrow"></i></em></a><a href="javascript:;" class=""
                                        onclick="SEARCH.sort('5')"><span class="fs-tit">新品</span><em class="fs-down"><i
                                                class="arrow"></i></em></a><a href="javascript:;" class=""
                                        onclick="SEARCH.sort('2')"><span class="fs-tit">价格</span><em class="fs-up"><i
                                                class="arrow-top"></i><i class="arrow-bottom"></i></em></a></div>
                                <div class="f-datagrid"><a href="javascript:;" class="fdg-item" data-range="0-349"
                                        data-tips="8%的用户喜欢的价位"><span class="def-bar" style="height:16%"></span></a><a
                                        href="javascript:;" class="fdg-item" data-range="349-1362"
                                        data-tips="29%的用户喜欢的价位"><span class="def-bar" style="height:57%"></span></a><a
                                        href="javascript:;" class="fdg-item" data-range="1362-3573"
                                        data-tips="43%的用户喜欢的价位"><span class="def-bar" style="height:85%"></span></a><a
                                        href="javascript:;" class="fdg-item" data-range="3573-8096"
                                        data-tips="15%的用户喜欢的价位"><span class="def-bar" style="height:30%"></span></a><a
                                        href="javascript:;" class="fdg-item" data-range="8096-¥"
                                        data-tips="5%的用户喜欢的价位"><span class="def-bar" style="height:10%"></span></a>
                                </div>
                                <div id="J_selectorPrice" class="f-price">
                                    <div class="f-price-set">
                                        <div class="fl"><input type="text" class="input-txt" autocomplete="off"
                                                style="color:#ccc" value="¥"></div>
                                        <em>-</em>
                                        <div class="fl"><input type="text" class="input-txt" autocomplete="off"
                                                style="color:#ccc" value="¥"></div>
                                    </div>
                                    <div class="f-price-edit">
                                        <a href="javascript:;" class="item1 J-price-cancle">清空</a>
                                        <a href="javascript:;" class="item2 J-price-confirm"
                                            data-url="search?keyword=%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;qrst=1&amp;rt=1&amp;stop=1&amp;vt=2&amp;wq=%E6%89%8B%E6%9C%BA&amp;cid2=653&amp;cid3=655&amp;ev=exprice_%7Bmin%7D-%7Bmax%7D%5E&amp;uc=0#J_searchWrap">确定</a>
                                    </div>
                                </div>
                                <div id="J_topPage" class="f-pager"><span
                                        class="fp-text"><b>1</b><em>/</em><i>97</i></span><a class="fp-prev disabled"
                                        href="javascript:;">&lt;</a><a class="fp-next" onclick="SEARCH.page(3)"
                                        href="javascript:;" title="使用方向键右键也可翻到下一页哦！">&gt;</a></div>
                                <div class="f-result-sum">共<span id="J_resCount" class="num">5700+</span>件商品</div>

                                <span class="clr"></span>
                            </div>
                            <div class="f-line">
                                <div class="f-store">
                                    <div class="fs-cell delivery-location">配送至</div>
                                    <div id="J_store_selector" class="ui-area-wrap ui-area-oversea-mode"
                                        style="float:left;margin-right:10px">
                                        <div class="ui-area-text-wrap">
                                            <div class="ui-area-text" data-id="13-1000-40488" title="山东济南市历城区">山东济南市历城区
                                            </div>
                                            <b></b>
                                        </div>
                                        <div class="ui-area-content-wrap ui-area-w-max">
                                            <div class="ui-area-tab"><a class="ui-switchable-item" data-id="13"
                                                    title="山东"><em>山东</em><i></i></a><a class="ui-switchable-item"
                                                    data-id="1000" title="济南市"><em>济南市</em><i></i></a><a
                                                    class="ui-switchable-item" data-id="40488"
                                                    title="历城区"><em>历城区</em><i></i></a><a
                                                    class="ui-switchable-item ui-area-current" data-id="-1"
                                                    title="请选择"><em>请选择</em><i></i></a></div>
                                            <div class="ui-area-content">
                                                <div style="display: none;" class="ui-switchable-panel" data-index="0">
                                                    <ul class="ui-area-content-list">
                                                        <li><a data-id="1" href="javascript:void(0)">北京</a></li>
                                                        <li><a data-id="2" href="javascript:void(0)">上海</a></li>
                                                        <li><a data-id="3" href="javascript:void(0)">天津</a></li>
                                                        <li><a data-id="4" href="javascript:void(0)">重庆</a></li>
                                                        <li><a data-id="5" href="javascript:void(0)">河北</a></li>
                                                        <li><a data-id="6" href="javascript:void(0)">山西</a></li>
                                                        <li><a data-id="7" href="javascript:void(0)">河南</a></li>
                                                        <li><a data-id="8" href="javascript:void(0)">辽宁</a></li>
                                                        <li><a data-id="9" href="javascript:void(0)">吉林</a></li>
                                                        <li><a data-id="10" href="javascript:void(0)">黑龙江</a></li>
                                                        <li><a data-id="11" href="javascript:void(0)">内蒙古</a></li>
                                                        <li><a data-id="12" href="javascript:void(0)">江苏</a></li>
                                                        <li class="ui-area-current"><a data-id="13"
                                                                href="javascript:void(0)">山东</a></li>
                                                        <li><a data-id="14" href="javascript:void(0)">安徽</a></li>
                                                        <li><a data-id="15" href="javascript:void(0)">浙江</a></li>
                                                        <li><a data-id="16" href="javascript:void(0)">福建</a></li>
                                                        <li><a data-id="17" href="javascript:void(0)">湖北</a></li>
                                                        <li><a data-id="18" href="javascript:void(0)">湖南</a></li>
                                                        <li><a data-id="19" href="javascript:void(0)">广东</a></li>
                                                        <li><a data-id="20" href="javascript:void(0)">广西</a></li>
                                                        <li><a data-id="21" href="javascript:void(0)">江西</a></li>
                                                        <li><a data-id="22" href="javascript:void(0)">四川</a></li>
                                                        <li><a data-id="23" href="javascript:void(0)">海南</a></li>
                                                        <li><a data-id="24" href="javascript:void(0)">贵州</a></li>
                                                        <li><a data-id="25" href="javascript:void(0)">云南</a></li>
                                                        <li><a data-id="26" href="javascript:void(0)">西藏</a></li>
                                                        <li><a data-id="27" href="javascript:void(0)">陕西</a></li>
                                                        <li><a data-id="28" href="javascript:void(0)">甘肃</a></li>
                                                        <li><a data-id="29" href="javascript:void(0)">青海</a></li>
                                                        <li><a data-id="30" href="javascript:void(0)">宁夏</a></li>
                                                        <li><a data-id="31" href="javascript:void(0)">新疆</a></li>
                                                        <li><a data-id="52993" href="javascript:void(0)">港澳</a></li>
                                                        <li><a data-id="32" href="javascript:void(0)">台湾</a></li>
                                                        <li><a data-id="84" href="javascript:void(0)">钓鱼岛</a></li>
                                                        <li><a data-id="53283" href="javascript:void(0)">海外</a></li>
                                                    </ul>
                                                </div>
                                                <div style="display: none;" class="ui-switchable-panel" data-index="1">
                                                    <ul class="ui-area-content-list">
                                                        <li><a data-id="2900" href="javascript:void(0)">济宁市</a></li>
                                                        <li class="ui-area-current"><a data-id="1000"
                                                                href="javascript:void(0)">济南市</a></li>
                                                        <li><a data-id="1007" href="javascript:void(0)">青岛市</a></li>
                                                        <li><a data-id="1016" href="javascript:void(0)">淄博市</a></li>
                                                        <li><a data-id="1022" href="javascript:void(0)">枣庄市</a></li>
                                                        <li><a data-id="1025" href="javascript:void(0)">东营市</a></li>
                                                        <li><a data-id="1032" href="javascript:void(0)">潍坊市</a></li>
                                                        <li><a data-id="1042" href="javascript:void(0)">烟台市</a></li>
                                                        <li><a data-id="1053" href="javascript:void(0)">威海市</a></li>
                                                        <li><a data-id="1058" href="javascript:void(0)">莱芜市</a></li>
                                                        <li><a data-id="1060" href="javascript:void(0)">德州市</a></li>
                                                        <li><a data-id="1072" href="javascript:void(0)">临沂市</a></li>
                                                        <li><a data-id="1081" href="javascript:void(0)">聊城市</a></li>
                                                        <li><a data-id="1090" href="javascript:void(0)">滨州市</a></li>
                                                        <li><a data-id="1099" href="javascript:void(0)">菏泽市</a></li>
                                                        <li><a data-id="1108" href="javascript:void(0)">日照市</a></li>
                                                        <li><a data-id="1112" href="javascript:void(0)">泰安市</a></li>
                                                    </ul>
                                                </div>
                                                <div style="display: none;" class="ui-switchable-panel" data-index="2">
                                                    <ul class="ui-area-content-list">
                                                        <li><a data-id="1002" href="javascript:void(0)">长清区</a></li>
                                                        <li><a data-id="1003" href="javascript:void(0)">平阴县</a></li>
                                                        <li><a data-id="1004" href="javascript:void(0)">济阳县</a></li>
                                                        <li><a data-id="1005" href="javascript:void(0)">商河县</a></li>
                                                        <li><a data-id="4277" href="javascript:void(0)">高新区</a></li>
                                                        <li class="ui-area-current"><a data-id="40488"
                                                                href="javascript:void(0)">历城区</a></li>
                                                        <li><a data-id="40489" href="javascript:void(0)">天桥区</a></li>
                                                        <li><a data-id="40490" href="javascript:void(0)">槐荫区</a></li>
                                                        <li><a data-id="40491" href="javascript:void(0)">历下区</a></li>
                                                        <li><a data-id="40492" href="javascript:void(0)">市中区</a></li>
                                                        <li><a data-id="40493" href="javascript:void(0)">章丘区</a></li>
                                                    </ul>
                                                </div>
                                                <div style="" class="ui-switchable-panel ui-switchable-panel-selected"
                                                    data-index="3">
                                                    <ul class="ui-area-content-list">
                                                        <li><a data-id="40562" href="javascript:void(0)">仲宫镇</a></li>
                                                        <li><a data-id="40563" href="javascript:void(0)">西营镇</a></li>
                                                        <li><a data-id="40564" href="javascript:void(0)">柳埠镇</a></li>
                                                        <li><a data-id="40565" href="javascript:void(0)">彩石镇</a></li>
                                                        <li><a data-id="40566" href="javascript:void(0)">董家镇</a></li>
                                                        <li><a data-id="40567" href="javascript:void(0)">唐王镇</a></li>
                                                        <li><a data-id="40568" href="javascript:void(0)">孙村镇</a></li>
                                                        <li><a data-id="51328" href="javascript:void(0)">城区</a></li>
                                                        <li><a data-id="54433" href="javascript:void(0)">遥墙街道</a></li>
                                                        <li><a data-id="54434" href="javascript:void(0)">王舍人街道</a></li>
                                                        <li><a data-id="54435" href="javascript:void(0)">唐冶街道</a></li>
                                                        <li><a data-id="54436" href="javascript:void(0)">山大路街道</a></li>
                                                        <li><a data-id="54437" href="javascript:void(0)">全福街道</a></li>
                                                        <li><a data-id="54438" href="javascript:void(0)">华山街道</a></li>
                                                        <li><a data-id="54439" href="javascript:void(0)">洪家楼街道</a></li>
                                                        <li><a data-id="54440" href="javascript:void(0)">荷花路街道</a></li>
                                                        <li><a data-id="54441" href="javascript:void(0)">郭店街道</a></li>
                                                        <li><a data-id="54442" href="javascript:void(0)">港沟街道</a></li>
                                                        <li><a data-id="54443" href="javascript:void(0)">东风街道</a></li>
                                                        <li><a data-id="54444" href="javascript:void(0)">鲍山街道</a></li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div id="J_feature" class="f-feature">
                                    <ul>
                                        <li><a data-field="wtype" data-val="1" class="" href="javascript:;"
                                                onclick="searchlog(1,0,0,43)"><i></i>京东物流</a></li>
                                        <li><a data-field="cod" data-val="1" class="" href="javascript:;"
                                                onclick="searchlog(1,0,0,34)"><i></i>货到付款</a></li>
                                        <li><a data-field="stock" data-val="1" class="" href="javascript:;"
                                                onclick="searchlog(1,0,0,41)"><i></i>仅显示有货</a></li>
                                        <li><a data-field="gp" data-val="1" class="" href="javascript:;"
                                                onclick="searchlog(1,0,0,39)"><i></i>海囤全球</a></li>
                                        <li><a data-field="gp" data-val="2" class="" href="javascript:;"
                                                onclick="searchlog(1,0,0,87)"><i></i>可配送全球</a></li>
                                        <li><a data-field="zx" data-val="2" class="" href="javascript:;"
                                                onclick="searchlog(1,0,0,85)"><i></i>新品</a></li>
                                        <li><a data-field="plus" data-val="1" class="" href="javascript:;"
                                                onclick=""><i></i>PLUS专享</a></li>
                                    </ul>
                                </div>
                                <div class="f-search">
                                    <input type="text" value="在结果中搜索" class="input-txt">
                                    <a class="btn btn-default" href="javascript:;">确定</a>
                                </div>
                                <span class="clr"></span>
                            </div>
                        </div>
                        <div id="J_goodsList" class="goods-list-v2 gl-type-3 J-goods-list">
                            <ul class="gl-warp clearfix" data-tpl="3">
                                <li class="gl-item" data-sku="100006635632" data-spu="100006635632"
                                    data-pid="100006635632">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank" title="麒麟810，4800万超清双摄，升降式全面屏！荣耀爆品特惠，选品质，购荣耀~"
                                                href="//item.jd.com/100004069421.html"
                                                onclick="searchlog(1,100006635632,0,2,'','flagsClk=557847176')">
                                                <img width="220" height="220" class="" data-img="1"
                                                    source-data-lazy-img="" data-lazy-img="done"
                                                    src="//img11.360buyimg.com/n7/jfs/t1/84119/30/7021/372939/5d53b55aE12f17b5a/5619ee1ae96c3cd8.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000000904" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="" title="魅海蓝"><img
                                                                data-presale="" data-sku="100006635632" data-img="1"
                                                                data-lazy-img="done" class="" width="25" height="25"
                                                                data-done="1"
                                                                src="//img12.360buyimg.com/n9/jfs/t1/38376/31/12243/397999/5d36c0b0E4fe67576/ad031fec5819110f.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="幻夜黑" class=""><img
                                                                data-presale="" data-sku="100004069505" data-img="1"
                                                                width="25" height="25" data-lazy-img="done" class=""
                                                                data-done="1"
                                                                src="//img10.360buyimg.com/n9/jfs/t1/64468/1/5252/214483/5d36a5b7E1b13e7dc/67711c7137af161b.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="魅焰红"
                                                            class="curr"><img data-presale="" data-sku="100004069421"
                                                                data-img="1" width="25" height="25" data-lazy-img="done"
                                                                class="" data-done="1"
                                                                src="//img11.360buyimg.com/n9/jfs/t1/84119/30/7021/372939/5d53b55aE12f17b5a/5619ee1ae96c3cd8.jpg"></a>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100006635632"
                                                data-done="1"><em>￥</em><i>1399.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank" title="麒麟810，4800万超清双摄，升降式全面屏！荣耀爆品特惠，选品质，购荣耀~"
                                                href="//item.jd.com/100004069421.html"
                                                onclick="searchlog(1,100006635632,0,1,'','flagsClk=557847176')">
                                                <em>荣耀9X 麒麟810 4000mAh超强续航 4800万超清夜拍 6.59英寸升降全面屏 全网通4GB+64GB 魅海蓝</em>
                                                <i class="promo-words"
                                                    id="J_AD_100006635632">麒麟810，4800万超清双摄，升降式全面屏！荣耀爆品特惠，选品质，购荣耀~</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <strong><a id="J_comment_100006635632" target="_blank"
                                                    href="//item.jd.com/100004069421.html#comment"
                                                    onclick="searchlog(1,100006635632,0,3,'','flagsClk=557847176')">32万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100004069421"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100006635632,0,5,'','flagsClk=557847176')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="97"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000000904,0,58)"
                                                    href="//mall.jd.com/index-1000000904.html"
                                                    title="荣耀京东自营旗舰店">荣耀京东自营旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000000904,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100006635632" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                        </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100000177760" data-spu="100000177756"
                                    data-pid="100000177756">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="【iPhoneXR限时特惠！】6.1英寸视网膜显示屏，A12仿生芯片，面容识别，无线充电，支持双卡！更多优惠点击！"
                                                href="//item.jd.com/100000287115.html"
                                                onclick="searchlog(1,100000177760,1,2,'','flagsClk=1631589000')">
                                                <img width="220" height="220" class="" data-img="1"
                                                    source-data-lazy-img="" data-lazy-img="done"
                                                    src="//img10.360buyimg.com/n7/jfs/t1/1695/39/3482/70556/5b997bf7Ed2d65519/749d8efdff062fb0.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000000127" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="" title="黑色"><img
                                                                data-presale="" data-sku="100000177760" data-img="1"
                                                                data-lazy-img="done" class="" width="25" height="25"
                                                                data-done="1"
                                                                src="//img10.360buyimg.com/n9/jfs/t1/3405/18/3537/69901/5b997c0aE5dc8ed9f/a2c208410ae84d1f.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="白色"
                                                            class="curr"><img data-presale="" data-sku="100000287115"
                                                                data-img="1" width="25" height="25" data-lazy-img="done"
                                                                class="" data-done="1"
                                                                src="//img10.360buyimg.com/n9/jfs/t1/1695/39/3482/70556/5b997bf7Ed2d65519/749d8efdff062fb0.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="红色" class=""><img
                                                                data-presale="" data-sku="100000287163" data-img="1"
                                                                width="25" height="25" data-lazy-img="done" class=""
                                                                data-done="1"
                                                                src="//img13.360buyimg.com/n9/jfs/t1/842/9/3723/77573/5b997bedE4f438e5b/ccd1077b985c7150.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="蓝色" class=""><img
                                                                data-presale="" data-sku="100000287141" data-img="1"
                                                                width="25" height="25" data-lazy-img="done" class=""
                                                                data-done="1"
                                                                src="//img11.360buyimg.com/n9/jfs/t1/2267/5/3518/83121/5b997bf1E6409d7b2/378263542aab44a0.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="珊瑚色" class=""><img
                                                                data-presale="" data-sku="100000177770" data-img="1"
                                                                width="25" height="25" data-lazy-img="done" class=""
                                                                data-done="1"
                                                                src="//img10.360buyimg.com/n9/jfs/t1/3398/4/3488/86713/5b997c05Ef8001f1a/d1cbeecd11a2ef3b.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="黄色"><img
                                                                data-presale="" data-sku="100000177782" data-img="1"
                                                                width="25" height="25" data-lazy-img="done" class=""
                                                                data-done="1"
                                                                src="//img12.360buyimg.com/n9/jfs/t1/966/3/3746/82542/5b997c01E2a0b6915/2946c53c7a2f137f.jpg"></a>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100000177760"
                                                data-done="1"><em>￥</em><i>5099.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="【iPhoneXR限时特惠！】6.1英寸视网膜显示屏，A12仿生芯片，面容识别，无线充电，支持双卡！更多优惠点击！"
                                                href="//item.jd.com/100000287115.html"
                                                onclick="searchlog(1,100000177760,1,1,'','flagsClk=1631589000')">
                                                <em><span class="p-tag"
                                                        style="background-color:#c81623">京品手机</span>Apple iPhone XR
                                                    (A2108) 128GB 黑色 移动联通电信4G<font class="skcolor_ljg">手机</font>
                                                    双卡双待</em>
                                                <i class="promo-words"
                                                    id="J_AD_100000177760">【iPhoneXR限时特惠！】6.1英寸视网膜显示屏，A12仿生芯片，面容识别，无线充电，支持双卡！更多优惠点击！</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <a target="_blank" href="//paipai.jd.com/pc/list.html?pid=100000177760"
                                                class="spu-link">二手有售</a>
                                            <strong><a id="J_comment_100000177760" target="_blank"
                                                    href="//paipai.jd.com/pc/list.html?pid=100000177760"
                                                    onclick="searchlog(1,100000177760,1,3,'','flagsClk=1631589000')">186万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100000287115"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100000177760,1,5,'','flagsClk=1631589000')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="97"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000000127,0,58)"
                                                    href="//mall.jd.com/index-1000000127.html"
                                                    title="Apple产品京东自营旗舰店">Apple产品京东自营旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000000127,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100000177760" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                            <i class="goods-icons4 J-picon-tips" data-tips="购买本商品送赠品">赠</i> </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100002749549" data-spu="100002795955"
                                    data-pid="100002795955">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="【优惠300！到手价3988！加赠大额礼品券（含大闸蟹）】一站式以旧换新至高享500元补贴，5倍混合变焦；畅享10P预售送大额礼品卡》"
                                                href="//item.jd.com/100004404918.html"
                                                onclick="searchlog(1,100002749549,2,2,'','flagsClk=1631589000')">
                                                <img width="220" height="220" class="" data-img="1"
                                                    source-data-lazy-img="" data-lazy-img="done"
                                                    src="//img13.360buyimg.com/n7/jfs/t1/74426/16/7673/368712/5d5b506bE30738f4a/eae4991a129e6591.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000004259" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class=""
                                                            title="天空之境"><img data-presale="" data-sku="100002749549"
                                                                data-img="1" data-lazy-img="done" class="" width="25"
                                                                height="25" data-done="1"
                                                                src="//img14.360buyimg.com/n9/jfs/t1/50018/39/8127/229510/5d5b5043E66769ff0/8907776f7bd66d57.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="亮黑色" class=""><img
                                                                data-presale="" data-sku="100004404920" data-img="1"
                                                                width="25" height="25" data-lazy-img="done" class=""
                                                                data-done="1"
                                                                src="//img10.360buyimg.com/n9/jfs/t1/54694/19/8183/332089/5d5b5058Ece46a837/a10c1f3b8cdca326.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="珠光贝母"><img
                                                                data-presale="" data-sku="100004404916" data-img="1"
                                                                width="25" height="25" data-lazy-img="done" class=""
                                                                data-done="1"
                                                                src="//img11.360buyimg.com/n9/jfs/t1/76506/35/7715/193234/5d5b5091Ea0e8c700/12c1e03b26abf46f.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="极光色"
                                                            class="curr"><img data-presale="" data-sku="100004404918"
                                                                data-img="1" width="25" height="25" data-lazy-img="done"
                                                                class="" data-done="1"
                                                                src="//img13.360buyimg.com/n9/jfs/t1/74426/16/7673/368712/5d5b506bE30738f4a/eae4991a129e6591.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="赤茶橘"><img
                                                                data-presale="" data-sku="100002795955" data-img="1"
                                                                width="25" height="25" data-lazy-img="done" class=""
                                                                data-done="1"
                                                                src="//img10.360buyimg.com/n9/jfs/t1/84566/14/7747/113156/5d5b507fE98b97996/a2fd4fb1d05d1fe6.jpg"></a>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100002749549"
                                                data-done="1"><em>￥</em><i>3988.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="【优惠300！到手价3988！加赠大额礼品券（含大闸蟹）】一站式以旧换新至高享500元补贴，5倍混合变焦；畅享10P预售送大额礼品卡》"
                                                href="//item.jd.com/100004404918.html"
                                                onclick="searchlog(1,100002749549,2,1,'','flagsClk=1631589000')">
                                                <em><img class="p-tag3"
                                                        src="//img14.360buyimg.com/uba/jfs/t6919/268/501386350/1257/92e5fb39/5976fcf9Nd915775f.png">华为
                                                    HUAWEI P30 超感光徕卡三摄麒麟980AI智能芯片全面屏屏内指纹版<font class="skcolor_ljg">手机
                                                    </font>8GB+128GB天空之境全网通双4G<font class="skcolor_ljg">手机</font></em>
                                                <i class="promo-words"
                                                    id="J_AD_100002749549">【优惠300！到手价3988！加赠大额礼品券（含大闸蟹）】一站式以旧换新至高享500元补贴，5倍混合变焦；畅享10P预售送大额礼品卡》</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <a target="_blank" href="//paipai.jd.com/pc/list.html?pid=100002749549"
                                                class="spu-link">二手有售</a>
                                            <strong><a id="J_comment_100002749549" target="_blank"
                                                    href="//paipai.jd.com/pc/list.html?pid=100002749549"
                                                    onclick="searchlog(1,100002749549,2,3,'','flagsClk=1631589000')">43万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100004404918"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100002749549,2,5,'','flagsClk=1631589000')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="97"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000004259,0,58)"
                                                    href="//mall.jd.com/index-1000004259.html"
                                                    title="华为京东自营官方旗舰店">华为京东自营官方旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000004259,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100002749549" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                            <i class="goods-icons4 J-picon-tips"
                                                style="border-color:#4d88ff;color:#4d88ff;" data-idx="1"
                                                data-tips="品质服务，放心购物">放心购</i>
                                            <i class="goods-icons4 J-picon-tips" data-tips="购买本商品送赠品">赠</i> </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100001550349" data-spu="100001467225"
                                    data-pid="100001467225">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="限时优惠999！2400万AI高清自拍，麒麟710处理器，炫光渐变色！荣耀9X系列1399起，麒麟810，4800万超清双摄！"
                                                href="//item.jd.com/100001550349.html"
                                                onclick="searchlog(1,100001550349,3,2,'','flagsClk=1631589000')">
                                                <img width="220" height="220" class="" data-img="1"
                                                    source-data-lazy-img="" data-lazy-img="done"
                                                    src="//img14.360buyimg.com/n7/jfs/t1/22718/1/12601/168068/5caedd41E05e879b0/865565d919219154.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000000904" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="渐变蓝"><img data-presale="" data-sku="100001550349"
                                                                data-img="1" data-lazy-img="done" class="" width="25"
                                                                height="25" data-done="1"
                                                                src="//img14.360buyimg.com/n9/jfs/t1/22718/1/12601/168068/5caedd41E05e879b0/865565d919219154.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="幻夜黑"><img
                                                                data-presale="" data-sku="100001467225" data-img="1"
                                                                width="25" height="25" data-lazy-img="done" class=""
                                                                data-done="1"
                                                                src="//img10.360buyimg.com/n9/jfs/t1/27161/33/15211/149602/5caedc4dEdb9e08b0/794519c5c5924524.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="铃兰白"><img
                                                                data-presale="" data-sku="100002380994" data-img="1"
                                                                width="25" height="25" data-lazy-img="done" class=""
                                                                data-done="1"
                                                                src="//img14.360buyimg.com/n9/jfs/t1/33777/1/2378/138249/5caee098E6ac49e11/b63b74e47be77911.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="渐变红"><img
                                                                data-presale="" data-sku="100001550347" data-img="1"
                                                                width="25" height="25" data-lazy-img="done" class=""
                                                                data-done="1"
                                                                src="//img12.360buyimg.com/n9/jfs/t1/24961/31/15129/171030/5caee71eE1de3edd7/2e5e07e00b0e3b75.jpg"></a>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100001550349"
                                                data-done="1"><em>￥</em><i>999.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="限时优惠999！2400万AI高清自拍，麒麟710处理器，炫光渐变色！荣耀9X系列1399起，麒麟810，4800万超清双摄！"
                                                href="//item.jd.com/100001550349.html"
                                                onclick="searchlog(1,100001550349,3,1,'','flagsClk=1631589000')">
                                                <em>荣耀10青春版 幻彩渐变 2400万AI自拍 全网通版4GB+64GB 渐变蓝 移动联通电信4G全面屏<font
                                                        class="skcolor_ljg">手机</font> 双卡双待</em>
                                                <i class="promo-words"
                                                    id="J_AD_100001550349">限时优惠999！2400万AI高清自拍，麒麟710处理器，炫光渐变色！荣耀9X系列1399起，麒麟810，4800万超清双摄！</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <strong><a id="J_comment_100001550349" target="_blank"
                                                    href="//item.jd.com/100001550349.html#comment"
                                                    onclick="searchlog(1,100001550349,3,3,'','flagsClk=1631589000')">94万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100001550349"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100001550349,3,5,'','flagsClk=1631589000')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="98"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000000904,0,58)"
                                                    href="//mall.jd.com/index-1000000904.html"
                                                    title="荣耀京东自营旗舰店">荣耀京东自营旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000000904,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100001550349" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                            <i class="goods-icons4 J-picon-tips"
                                                style="border-color:#4d88ff;color:#4d88ff;" data-idx="1"
                                                data-tips="品质服务，放心购物">放心购</i>
                                        </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="8735304" data-spu="8735304" data-pid="8735304">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="限时优惠1099！2000万AI双摄，人脸+指纹双识别！荣耀9X系列1399起，麒麟810，4800万超清双摄！"
                                                href="//item.jd.com/100000304401.html"
                                                onclick="searchlog(1,8735304,4,2,'','flagsClk=1631589000')">
                                                <img width="220" height="220" class="" data-img="1"
                                                    source-data-lazy-img="" data-lazy-img="done"
                                                    src="//img11.360buyimg.com/n7/jfs/t1/15754/23/5665/358122/5c41229aE112fdfdb/aa9e8675d4a214a6.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000000904" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="" title="幻夜黑"><img
                                                                data-presale="" data-sku="8735304" data-img="1"
                                                                data-lazy-img="done" class="" width="25" height="25"
                                                                data-done="1"
                                                                src="//img14.360buyimg.com/n9/jfs/t1/21333/14/5246/180334/5c3ad7b6Ef7d727c0/c16e93d0bf77a31f.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="幻影蓝"><img
                                                                data-presale="" data-sku="100001270083" data-img="1"
                                                                width="25" height="25" data-lazy-img="done" class=""
                                                                data-done="1"
                                                                src="//img13.360buyimg.com/n9/jfs/t1/15311/16/6377/388816/5c53a7a2Ec6521c3b/0a5f5e008d032291.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="魅海蓝"
                                                            class="curr"><img data-presale="" data-sku="100000304401"
                                                                data-img="1" width="25" height="25" data-lazy-img="done"
                                                                class="" data-done="1"
                                                                src="//img11.360buyimg.com/n9/jfs/t1/15754/23/5665/358122/5c41229aE112fdfdb/aa9e8675d4a214a6.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="魅焰红" class=""><img
                                                                data-presale="" data-sku="100000508193" data-img="1"
                                                                width="25" height="25" data-lazy-img="done" class=""
                                                                data-done="1"
                                                                src="//img13.360buyimg.com/n9/jfs/t1/26415/25/5655/360553/5c41239eE10fa2ab6/690787e91e05a398.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="梦幻紫"><img
                                                                data-presale="" data-sku="100000838695" data-img="1"
                                                                width="25" height="25" data-lazy-img="done" class=""
                                                                data-done="1"
                                                                src="//img10.360buyimg.com/n9/jfs/t1/25440/19/5697/338506/5c4125a5E9e80fe96/addf83f4ec77631a.jpg"></a>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_8735304" data-done="1"><em>￥</em><i>1099.00</i></strong>
                                        </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="限时优惠1099！2000万AI双摄，人脸+指纹双识别！荣耀9X系列1399起，麒麟810，4800万超清双摄！"
                                                href="//item.jd.com/100000304401.html"
                                                onclick="searchlog(1,8735304,4,1,'','flagsClk=1631589000')">
                                                <em><span class="p-tag" style="background-color:#c81623">京品手机</span>荣耀8X
                                                    千元屏霸 91%屏占比 2000万AI双摄 4GB+64GB 幻夜黑 移动联通电信4G全面屏<font
                                                        class="skcolor_ljg">手机</font> 双卡双待</em>
                                                <i class="promo-words"
                                                    id="J_AD_8735304">限时优惠1099！2000万AI双摄，人脸+指纹双识别！荣耀9X系列1399起，麒麟810，4800万超清双摄！</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <a target="_blank" href="//paipai.jd.com/pc/list.html?pid=8735304"
                                                class="spu-link">二手有售</a>
                                            <strong><a id="J_comment_8735304" target="_blank"
                                                    href="//paipai.jd.com/pc/list.html?pid=8735304"
                                                    onclick="searchlog(1,8735304,4,3,'','flagsClk=1631589000')">195万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100000304401"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,8735304,4,5,'','flagsClk=1631589000')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="99"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000000904,0,58)"
                                                    href="//mall.jd.com/index-1000000904.html"
                                                    title="荣耀京东自营旗舰店">荣耀京东自营旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000000904,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_8735304" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                            <i class="goods-icons4 J-picon-tips"
                                                style="border-color:#4d88ff;color:#4d88ff;" data-idx="1"
                                                data-tips="品质服务，放心购物">放心购</i>
                                        </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100004418727" data-spu="100004418727"
                                    data-pid="100004418727">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="【实际价格以发布会公布为准】新品预定享12期免息+蓝牙音箱+半年碎屏险！预定新品赢Reno2！OPPO开学换新机，更多优惠"
                                                href="https://item.jd.com/100004418727.html"
                                                onclick="searchlog(1,100004418727,5,2,'','adwClk=1');searchAdvPointReport('https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDQ0MTg3MjcuaHRtbA&amp;log=VuqDEEucP0LvlsuIkout6t92HzcQTX629uB8BI1cCzYVM3DTIxRHKBPcOlhmTC98KQ_k_AIueSQt8w67hHK-9FVr7XNqbuvzvKbtezgodTAW9xLI-LInvmdW99du5nnctY2tWfD7J6Swn5IloIPJXi1yjrIgoLB8SbFuZKRDRV0ZioPjkLNVB1FrfMp_-TzyJPZEa8bQsUIIIlpKKiSyh4addylEEMc3q6Vp9Bu8FF9e1s-iN5sqPG2qGn1q1pnGcsDi3oOJQF3loScXfFvbYS04QQPzspeK4LO0C_mBS6605yso4XbdYP24FOhTf5ahAW3Jdg6pKahpFP-yUOketiLH6F3XHEUN5hifsRiFIyi6kXxban4HGFD0gRwKWPgaWGAXZdwHzGEcdVeSZmcDnK92Q6hicycTxkDEHdVvRvkcrdmm2vSzz8-6STE9snBZ1Xf24iaKCDfh0YicQinjDYOmEFuIrcf_gXT2r5QgmzWwbYIjz1wyZe7Y7cxZDues6rgd3F9F9JqinS0KkJNn6HbTCeg6fLSEk_Y7_Mb2PVMpC_ewflMod2a3mscpyLIUzh1ftqZmroNMdnJ-8v1_r32Kz_JD-qggmfU_6bHDqLmjOFrZ1s-bx1a12_F4bArM_PXBr30vx0TMN985BRqCSYtyH9ZncVjKwCsIvmcnreX0yUBMqrTH2aSIcb-7Dlh8hETbLkAqOOfmQ19nnM7CLA&amp;v=404&amp;clicktype=1');">
                                                <img width="220" height="220" class="" data-img="1"
                                                    source-data-lazy-img="" data-lazy-img="done"
                                                    src="//img12.360buyimg.com/n7/jfs/t1/74098/2/8720/124868/5d68cbacE0b25be85/abc514c2b0c94fea.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000004065" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="深海夜光"><img
                                                                data-url="https://item.jd.com/100004418727.html"
                                                                data-presale="" data-sku="100004418727" data-img="1"
                                                                data-lazy-img="done" class="" width="25" height="25"
                                                                data-done="1"
                                                                src="//img12.360buyimg.com/n9/jfs/t1/74098/2/8720/124868/5d68cbacE0b25be85/abc514c2b0c94fea.jpg"></a>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100004418727"
                                                data-done="1"><em>￥</em><i>9999.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="【实际价格以发布会公布为准】新品预定享12期免息+蓝牙音箱+半年碎屏险！预定新品赢Reno2！OPPO开学换新机，更多优惠"
                                                href="https://item.jd.com/100004418727.html"
                                                onclick="searchlog(1,100004418727,5,1,'','adwClk=1');searchAdvPointReport('https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDQ0MTg3MjcuaHRtbA&amp;log=VuqDEEucP0LvlsuIkout6t92HzcQTX629uB8BI1cCzYVM3DTIxRHKBPcOlhmTC98KQ_k_AIueSQt8w67hHK-9FVr7XNqbuvzvKbtezgodTAW9xLI-LInvmdW99du5nnctY2tWfD7J6Swn5IloIPJXi1yjrIgoLB8SbFuZKRDRV0ZioPjkLNVB1FrfMp_-TzyJPZEa8bQsUIIIlpKKiSyh4addylEEMc3q6Vp9Bu8FF9e1s-iN5sqPG2qGn1q1pnGcsDi3oOJQF3loScXfFvbYS04QQPzspeK4LO0C_mBS6605yso4XbdYP24FOhTf5ahAW3Jdg6pKahpFP-yUOketiLH6F3XHEUN5hifsRiFIyi6kXxban4HGFD0gRwKWPgaWGAXZdwHzGEcdVeSZmcDnK92Q6hicycTxkDEHdVvRvkcrdmm2vSzz8-6STE9snBZ1Xf24iaKCDfh0YicQinjDYOmEFuIrcf_gXT2r5QgmzWwbYIjz1wyZe7Y7cxZDues6rgd3F9F9JqinS0KkJNn6HbTCeg6fLSEk_Y7_Mb2PVMpC_ewflMod2a3mscpyLIUzh1ftqZmroNMdnJ-8v1_r32Kz_JD-qggmfU_6bHDqLmjOFrZ1s-bx1a12_F4bArM_PXBr30vx0TMN985BRqCSYtyH9ZncVjKwCsIvmcnreX0yUBMqrTH2aSIcb-7Dlh8hETbLkAqOOfmQ19nnM7CLA&amp;v=404&amp;clicktype=1');">
                                                <em>【预定】OPPO Reno2 4800万变焦四摄 视频防抖 6.5英寸阳光护眼全面屏 8GB+128GB 深海夜光 拍照游戏智能
                                                    <font class="skcolor_ljg">手机</font></em>
                                                <i class="promo-words"
                                                    id="J_AD_100004418727">【实际价格以发布会公布为准】新品预定享12期免息+蓝牙音箱+半年碎屏险！预定新品赢Reno2！OPPO开学换新机，更多优惠</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <strong><a id="J_comment_100004418727" target="_blank"
                                                    href="https://item.jd.com/100004418727.html"
                                                    onclick="searchlog(1,100004418727,5,3,'','adwClk=1')">0</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100004418727"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100004418727,5,5,'','adwClk=1')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="0" data-reputation=""
                                            data-verderid="1000004065" data-done="1"><span class="J_im_icon"><a
                                                    target="_blank" onclick="searchlog(1,1000004065,0,58)"
                                                    href="//mall.jd.com/index-1000004065.html"
                                                    title="OPPO京东自营官方旗舰店">OPPO京东自营官方旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000004065,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100004418727" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i><i class="goods-icons4 J-picon-tips"
                                                data-tips="购买本商品送赠品">赠</i>
                                        </div>
                                        <span class="p-promo-flag">广告</span>

                                        <img source-data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=VuqDEEucP0LvlsuIkout6t92HzcQTX629uB8BI1cCzYVM3DTIxRHKBPcOlhmTC98KQ_k_AIueSQt8w67hHK-9FVr7XNqbuvzvKbtezgodTAW9xLI-LInvmdW99du5nnctY2tWfD7J6Swn5IloIPJXi1yjrIgoLB8SbFuZKRDRV0ZioPjkLNVB1FrfMp_-TzyJPZEa8bQsUIIIlpKKiSyhxEhlfUT5PWUPxi5dB3WOqoYqwWZmcD2qCfXrdKBSW8grhHECQiDbIp8kBKArGI0pjtN1MZs0XEOsakqVwNbnShgIrTNyXTj04P2xm3d-niGkMslfQTRhz9Ns38tBWrijbQY1h1ggAsZlrkSeQwikaB4qM29caWtgncSxDLfjPeWQ-0BBJ7oxLQkyP5IjJkmZ5zgpm7T2VeJ_aYhsLcOIMW7OXWyC5BAL_UFAt3cKkeJHudlafAlbraJRuJe3E8EUHRnJnz6OU-fsUX4uP67zXA14jd2md0uybDIZiAQ1PE1AE3AtHA9XCYvDa_s60orOxa2CVI4gkThowWvd5GnswpOgFQtsCj9ZYPs1iNbPdJZFS3yzJFjzbaH0c_EDo_TpCcJZhojHfPBmRnaLjVtxiNEIUXMsJ19qifondIqUhrewx43yoP6FD7ZsT0rNx2U1vTNrKack1thH8bv0SHXfudfqeEVZ_yAGCrK6naoNMEqwDQtC3QNQ6TU0FWv6KAiDw&amp;v=404&amp;rt=3"
                                            style="">
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100003464635" data-spu="100003464635"
                                    data-pid="100003464635">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank" title="【以旧换新满1000再返500】杜比全景声，UFS3.0，4800万超清双摄猛戳更多精彩！"
                                                href="//item.jd.com/100003464635.html"
                                                onclick="searchlog(1,100003464635,6,2,'','flagsClk=1633686152')">
                                                <img width="220" height="220" class="" data-img="1"
                                                    source-data-lazy-img="" data-lazy-img="done"
                                                    src="//img10.360buyimg.com/n7/jfs/t1/35032/13/9593/102096/5cf0c2ccE77dc890e/abde5c9a60044485.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000001947" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="曜岩灰"><img data-presale="" data-sku="100003464635"
                                                                data-img="1" data-lazy-img="done" class="" width="25"
                                                                height="25" data-done="1"
                                                                src="//img10.360buyimg.com/n9/jfs/t1/35032/13/9593/102096/5cf0c2ccE77dc890e/abde5c9a60044485.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="珐琅红"><img
                                                                data-presale="" data-sku="100005741508" data-img="1"
                                                                width="25" height="25" data-lazy-img="done" class=""
                                                                data-done="1"
                                                                src="//img13.360buyimg.com/n9/jfs/t1/74767/1/827/258672/5cf0c304E264ae29f/fed0b23aa7d3eaf8.jpg"></a>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100003464635"
                                                data-done="1"><em>￥</em><i>2999.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank" title="【以旧换新满1000再返500】杜比全景声，UFS3.0，4800万超清双摄猛戳更多精彩！"
                                                href="//item.jd.com/100003464635.html"
                                                onclick="searchlog(1,100003464635,6,1,'','flagsClk=1633686152')">
                                                <em><span class="p-tag" style="background-color:#c81623">京品手机</span>一加
                                                    OnePlus 7 骁龙855旗舰性能 4800万超清双摄 8GB+256GB 曜岩灰 全面屏拍照智能游戏<font
                                                        class="skcolor_ljg">手机</font></em>
                                                <i class="promo-words"
                                                    id="J_AD_100003464635">【以旧换新满1000再返500】杜比全景声，UFS3.0，4800万超清双摄猛戳更多精彩！</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <strong><a id="J_comment_100003464635" target="_blank"
                                                    href="//item.jd.com/100003464635.html#comment"
                                                    onclick="searchlog(1,100003464635,6,3,'','flagsClk=1633686152')">14万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100003464635"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100003464635,6,5,'','flagsClk=1633686152')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="95"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000001947,0,58)"
                                                    href="//mall.jd.com/index-1000001947.html"
                                                    title="一加手机京东自营官方旗舰店">一加手机京东自营官方旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000001947,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100003464635" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                            <i class="goods-icons3 J-picon-tips J-picon-fix" data-tips="该商品是当季新品">新品</i>
                                            <i class="goods-icons4 J-picon-tips" data-tips="本商品可领用优惠券">券980-50</i>
                                        </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100000650837" data-spu="100000650837"
                                    data-pid="100000650837">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="限时优惠799！高通6系列芯片+4000mAh大电池+指纹识别+4GB大内存！荣耀爆品特惠，选品质，购荣耀~"
                                                href="//item.jd.com/100000650837.html"
                                                onclick="searchlog(1,100000650837,7,2,'','flagsClk=1631589000')">
                                                <img width="220" height="220" class="" data-img="1"
                                                    source-data-lazy-img="" data-lazy-img="done"
                                                    src="//img12.360buyimg.com/n7/jfs/t25696/183/1719981196/90401/bcf6106c/5bbac3c5N8b0bd22b.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000000904" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="幻夜黑"><img data-presale="" data-sku="100000650837"
                                                                data-img="1" data-lazy-img="done" class="" width="25"
                                                                height="25" data-done="1"
                                                                src="//img12.360buyimg.com/n9/jfs/t25696/183/1719981196/90401/bcf6106c/5bbac3c5N8b0bd22b.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="极光蓝"><img
                                                                data-presale="" data-sku="100000826642" data-img="1"
                                                                width="25" height="25" data-lazy-img="done" class=""
                                                                data-done="1"
                                                                src="//img12.360buyimg.com/n9/jfs/t25963/273/1700722303/109723/13746bcd/5bbad44bN4ec79f17.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="星云紫"><img
                                                                data-presale="" data-sku="100001110773" data-img="1"
                                                                width="25" height="25" data-lazy-img="done" class=""
                                                                data-done="1"
                                                                src="//img13.360buyimg.com/n9/jfs/t1/7378/32/1372/98083/5bcebfe0E16103d3f/e60896d2743a08b8.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="铂光金"><img
                                                                data-presale="" data-sku="100000717327" data-img="1"
                                                                width="25" height="25" data-lazy-img="done" class=""
                                                                data-done="1"
                                                                src="//img12.360buyimg.com/n9/jfs/t25144/341/2595705214/107989/25e23b3f/5beaa50cN4b523767.jpg"></a>
                                                    </li>
                                                    <li class="ps-item"><a href="javascript:;" title="幻影蓝"><img
                                                                data-presale="" data-sku="100005088772" data-img="1"
                                                                width="25" height="25" data-lazy-img="done" class=""
                                                                data-done="1"
                                                                src="//img12.360buyimg.com/n9/jfs/t1/34422/4/2855/103576/5cb6fda0E07db9e12/87d9b86f14387e65.jpg"></a>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100000650837"
                                                data-done="1"><em>￥</em><i>799.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="限时优惠799！高通6系列芯片+4000mAh大电池+指纹识别+4GB大内存！荣耀爆品特惠，选品质，购荣耀~"
                                                href="//item.jd.com/100000650837.html"
                                                onclick="searchlog(1,100000650837,7,1,'','flagsClk=1631589000')">
                                                <em><span class="p-tag"
                                                        style="background-color:#c81623">京品手机</span>荣耀畅玩8C两天一充 莱茵护眼 刘海屏
                                                    全网通版4GB+32GB 幻夜黑 移动联通电信4G全面屏<font class="skcolor_ljg">手机</font>
                                                    双卡双待</em>
                                                <i class="promo-words"
                                                    id="J_AD_100000650837">限时优惠799！高通6系列芯片+4000mAh大电池+指纹识别+4GB大内存！荣耀爆品特惠，选品质，购荣耀~</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <strong><a id="J_comment_100000650837" target="_blank"
                                                    href="//item.jd.com/100000650837.html#comment"
                                                    onclick="searchlog(1,100000650837,7,3,'','flagsClk=1631589000')">69万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100000650837"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100000650837,7,5,'','flagsClk=1631589000')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="99"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000000904,0,58)"
                                                    href="//mall.jd.com/index-1000000904.html"
                                                    title="荣耀京东自营旗舰店">荣耀京东自营旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000000904,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100000650837" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                            <i class="goods-icons4 J-picon-tips"
                                                style="border-color:#4d88ff;color:#4d88ff;" data-idx="1"
                                                data-tips="品质服务，放心购物">放心购</i>
                                        </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100003717483" data-spu="100003717483"
                                    data-pid="100003717483">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank" title="【赠大额购物卡】麒麟980，4800万AI四摄，光学屏内指纹；畅享10P预售送大额礼品卡》"
                                                href="//item.jd.com/100003717483.html"
                                                onclick="searchlog(1,100003717483,8,2,'','flagsClk=1633686152')">
                                                <img width="220" height="220" class="" data-img="1"
                                                    source-data-lazy-img="" data-lazy-img="done"
                                                    src="//img13.360buyimg.com/n7/jfs/t1/47193/2/3369/231278/5d11cb39Ef3674059/ba3c0a1d956429e2.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000004259" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="绮境森林"><img data-presale="" data-sku="100003717483"
                                                                data-img="1"
                                                                data-lazy-img="//img13.360buyimg.com/n9/jfs/t1/47193/2/3369/231278/5d11cb39Ef3674059/ba3c0a1d956429e2.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="亮黑色"><img
                                                                data-presale="" data-sku="100003717479" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img14.360buyimg.com/n9/jfs/t1/51336/1/8104/201268/5d5b5213Ec0ea1a1d/ca1e456c486d6ed7.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="仲夏紫"><img
                                                                data-presale="" data-sku="100003717481" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img11.360buyimg.com/n9/jfs/t1/42293/35/12509/226503/5d5b51ffEb5abf8e8/ab88f8b27c092bd2.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="苏音蓝"><img
                                                                data-presale="" data-sku="100004460341" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img11.360buyimg.com/n9/jfs/t1/67964/32/8116/126998/5d5f984aEd235919f/b8cfbffc2e762e4a.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="珊瑚橙"><img
                                                                data-presale="" data-sku="100006249354" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img14.360buyimg.com/n9/jfs/t1/44827/34/8307/228316/5d5b523bE62f6a8a0/9437d4c64a7df075.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="仲夏紫星耀礼盒版"><img
                                                                data-presale="" data-sku="100006273242" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img12.360buyimg.com/n9/jfs/t1/62582/31/2513/104088/5d0c93a3E8667b9b8/39a07d4e6c82f11f.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100003717483"
                                                data-done="1"><em>￥</em><i>2999.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank" title="【赠大额购物卡】麒麟980，4800万AI四摄，光学屏内指纹；畅享10P预售送大额礼品卡》"
                                                href="//item.jd.com/100003717483.html"
                                                onclick="searchlog(1,100003717483,8,1,'','flagsClk=1633686152')">
                                                <em>华为 HUAWEI nova 5 Pro
                                                    前置3200万人像超级夜景4800万AI四摄麒麟980芯片8GB+128GB绮境森林全网通双4G<font
                                                        class="skcolor_ljg">手机</font></em>
                                                <i class="promo-words"
                                                    id="J_AD_100003717483">【赠大额购物卡】麒麟980，4800万AI四摄，光学屏内指纹；畅享10P预售送大额礼品卡》</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <strong><a id="J_comment_100003717483" target="_blank"
                                                    href="//item.jd.com/100003717483.html#comment"
                                                    onclick="searchlog(1,100003717483,8,3,'','flagsClk=1633686152')">18万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100003717483"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100003717483,8,5,'','flagsClk=1633686152')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="96"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000004259,0,58)"
                                                    href="//mall.jd.com/index-1000004259.html"
                                                    title="华为京东自营官方旗舰店">华为京东自营官方旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000004259,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100003717483" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                            <i class="goods-icons4 J-picon-tips"
                                                style="border-color:#4d88ff;color:#4d88ff;" data-idx="1"
                                                data-tips="品质服务，放心购物">放心购</i>
                                            <i class="goods-icons3 J-picon-tips J-picon-fix" data-tips="该商品是当季新品">新品</i>
                                            <i class="goods-icons4 J-picon-tips" data-tips="购买本商品送赠品">赠</i> </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100003060627" data-spu="100003062377"
                                    data-pid="100003062377">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="限时优惠1299！前置3200万AI相机，后置2400万AI三摄，3D炫光渐变机身！荣耀爆品特惠，选品质，购荣耀~"
                                                href="//item.jd.com/100003060627.html"
                                                onclick="searchlog(1,100003060627,9,2,'','flagsClk=1631589000')">
                                                <img width="220" height="220" class="" data-img="1"
                                                    source-data-lazy-img="" data-lazy-img="done"
                                                    src="//img12.360buyimg.com/n7/jfs/t30031/152/1332312785/300863/cdf3a03d/5cdd233eN69626d85.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000000904" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="渐变蓝"><img data-presale="" data-sku="100003060627"
                                                                data-img="1"
                                                                data-lazy-img="//img12.360buyimg.com/n9/jfs/t30031/152/1332312785/300863/cdf3a03d/5cdd233eN69626d85.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="幻夜黑"><img
                                                                data-presale="" data-sku="100002962227" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img12.360buyimg.com/n9/jfs/t11467/256/2884845812/267100/493ed21c/5cdd1018N977740e5.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="渐变红"><img
                                                                data-presale="" data-sku="100004934254" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img14.360buyimg.com/n9/jfs/t10504/98/2941711404/297005/d2998272/5cdd24b3N465495f7.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100003060627"
                                                data-done="1"><em>￥</em><i>1299.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="限时优惠1299！前置3200万AI相机，后置2400万AI三摄，3D炫光渐变机身！荣耀爆品特惠，选品质，购荣耀~"
                                                href="//item.jd.com/100003060627.html"
                                                onclick="searchlog(1,100003060627,9,1,'','flagsClk=1631589000')">
                                                <em>荣耀20i 3200万AI自拍 超广角三摄 全网通版6GB+64GB 渐变蓝 移动联通电信4G全面屏<font
                                                        class="skcolor_ljg">手机</font> 双卡双待</em>
                                                <i class="promo-words"
                                                    id="J_AD_100003060627">限时优惠1299！前置3200万AI相机，后置2400万AI三摄，3D炫光渐变机身！荣耀爆品特惠，选品质，购荣耀~</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <strong><a id="J_comment_100003060627" target="_blank"
                                                    href="//item.jd.com/100003060627.html#comment"
                                                    onclick="searchlog(1,100003060627,9,3,'','flagsClk=1631589000')">40万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100003060627"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100003060627,9,5,'','flagsClk=1631589000')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="96"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000000904,0,58)"
                                                    href="//mall.jd.com/index-1000000904.html"
                                                    title="荣耀京东自营旗舰店">荣耀京东自营旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000000904,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100003060627" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                        </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100002881193" data-spu="100002642218"
                                    data-pid="100002642218">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="白条6期免息！限时优惠2099！麒麟980芯片，魅眼全视屏，4800万AI超清摄影！荣耀爆品特惠，选品质，购荣耀~"
                                                href="//item.jd.com/100002881193.html"
                                                onclick="searchlog(1,100002881193,10,2,'','flagsClk=1631589000')">
                                                <img width="220" height="220" class="" data-img="1"
                                                    source-data-lazy-img="" data-lazy-img="done"
                                                    src="//img13.360buyimg.com/n7/jfs/t1/16446/33/13283/339849/5c9eca5bE06fce1b2/500f99a976998161.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000000904" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="幻影蓝"><img data-presale="" data-sku="100002881193"
                                                                data-img="1"
                                                                data-lazy-img="//img13.360buyimg.com/n9/jfs/t1/16446/33/13283/339849/5c9eca5bE06fce1b2/500f99a976998161.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="幻夜黑"><img
                                                                data-presale="" data-sku="100002544828" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img13.360buyimg.com/n9/jfs/t1/27653/36/12572/346766/5c99ef63E81a8de14/5a38e39b2975e837.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="魅海蓝"><img
                                                                data-presale="" data-sku="100001364160" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img10.360buyimg.com/n9/jfs/t1/26070/26/12789/383055/5c99ecb9Ecd4e6bb9/4494127f19776033.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="魅丽红"><img
                                                                data-presale="" data-sku="100002642218" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img13.360buyimg.com/n9/jfs/t1/16813/39/12659/358796/5c99f002Ee7721cc6/a25a0116a081b6e6.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="幻影红"><img
                                                                data-presale="" data-sku="100004772462" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img12.360buyimg.com/n9/jfs/t1/15916/1/15529/313665/5cb0a851E9d979d02/ea7e4bd39906dde1.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100002881193"
                                                data-done="1"><em>￥</em><i>2099.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="白条6期免息！限时优惠2099！麒麟980芯片，魅眼全视屏，4800万AI超清摄影！荣耀爆品特惠，选品质，购荣耀~"
                                                href="//item.jd.com/100002881193.html"
                                                onclick="searchlog(1,100002881193,10,1,'','flagsClk=1631589000')">
                                                <em><img class="p-tag3"
                                                        src="//img14.360buyimg.com/uba/jfs/t6919/268/501386350/1257/92e5fb39/5976fcf9Nd915775f.png">荣耀V20
                                                    游戏<font class="skcolor_ljg">手机</font> 麒麟980芯片 魅眼全视屏 4800万深感相机
                                                    6GB+128GB 幻影蓝 移动联通电信4G全面屏<font class="skcolor_ljg">手机</font></em>
                                                <i class="promo-words"
                                                    id="J_AD_100002881193">白条6期免息！限时优惠2099！麒麟980芯片，魅眼全视屏，4800万AI超清摄影！荣耀爆品特惠，选品质，购荣耀~</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <a target="_blank" href="//paipai.jd.com/pc/list.html?pid=100002881193"
                                                class="spu-link">二手有售</a>
                                            <strong><a id="J_comment_100002881193" target="_blank"
                                                    href="//item.jd.com/100002881193.html#comment"
                                                    onclick="searchlog(1,100002881193,10,3,'','flagsClk=1631589000')">53万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100002881193"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100002881193,10,5,'','flagsClk=1631589000')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="97"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000000904,0,58)"
                                                    href="//mall.jd.com/index-1000000904.html"
                                                    title="荣耀京东自营旗舰店">荣耀京东自营旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000000904,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100002881193" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                            <i class="goods-icons4 J-picon-tips" data-tips="购买本商品送赠品">赠</i> </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100000651175" data-spu="100000651175"
                                    data-pid="100000651175">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="【直降100元低至1099元】屏幕指纹解锁手机，前置2500万，AI智慧美颜。50元预定Reno2，4800万变焦四摄"
                                                href="https://item.jd.com/100000651175.html"
                                                onclick="searchlog(1,100000651175,11,2,'','adwClk=1');searchAdvPointReport('https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDA2NTExNzUuaHRtbA&amp;log=VuqDEEucP0LvlsuIkout6t92HzcQTX629uB8BI1cCzYZQ6VmYAssMBXIxzp3LWzo_8q-zZ3cijbOv062wup7KxSlMsvS2HSevYnTO2Ueh2hStrdxtBiliXM-4s4Wupj9tBgFS6jREp8fQrk3BVIPcil_exgO76Q_2zGfK-udS15K0d_precPUBzbnPBJ3BhwCn6pDvJ0S2kExc33Wunqfxm0Xttwm18ovvFGgykX6uXGCnheLMXi_4cgIJjk2IPMDHmpHmqMZ_JuU_hwitTpXGOF2HvSz0a_-X_6L6OK6jTYeGZXbtADQ9Vv12Jyblhy9fSEXgHPHUWyOX2VDoTGAqJ4OPpRJQM-EvnHXkwbcr47ztsxwOIjBqQHOmpRCoNK7Nm9IAKtKEnJuWOZGUV9dT36vN0Y9rBPpRGH6taSSWFkMojn89SI0P43k6Qs0qgYxZu9s8DEdv_h6TfDbMa2EGuNx_mCRTKVTqLcZUzKc2HPRkjN99xOyoR_2s6JQ-oS1q6VWHGvFJMVRxNbs3ysD671dNrDbE_1aTxpvNRuqEI64UtpBERIpY9txN71WaZg20LZMF6x7J84SV7tIo6dTaCHtUoNJrw0Tcl_6oK6RvoIBgOiJZ8gP2Ri8F38ID_4KQx2BddmyRWzNqMsX0u36KXxAY6G2J3FMzQmPf6GPM9VcBmwFaGCqTXN60UA9HaISDW4maiwMRaE-EM4bRt8hw&amp;v=404&amp;clicktype=1');">
                                                <img width="220" height="220" class="" data-img="1"
                                                    source-data-lazy-img="" data-lazy-img="done"
                                                    src="//img10.360buyimg.com/n7/jfs/t1/34591/3/12765/165894/5d0cb6cbE2eb51f7e/6dc5606906c54cad.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000004065" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="梵星蓝"><img
                                                                data-url="https://item.jd.com/100000651175.html"
                                                                data-presale="" data-sku="100000651175" data-img="1"
                                                                data-lazy-img="//img10.360buyimg.com/n9/jfs/t1/34591/3/12765/165894/5d0cb6cbE2eb51f7e/6dc5606906c54cad.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100000651175"
                                                data-done="1"><em>￥</em><i>1099.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="【直降100元低至1099元】屏幕指纹解锁手机，前置2500万，AI智慧美颜。50元预定Reno2，4800万变焦四摄"
                                                href="https://item.jd.com/100000651175.html"
                                                onclick="searchlog(1,100000651175,11,1,'','adwClk=1');searchAdvPointReport('https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDA2NTExNzUuaHRtbA&amp;log=VuqDEEucP0LvlsuIkout6t92HzcQTX629uB8BI1cCzYZQ6VmYAssMBXIxzp3LWzo_8q-zZ3cijbOv062wup7KxSlMsvS2HSevYnTO2Ueh2hStrdxtBiliXM-4s4Wupj9tBgFS6jREp8fQrk3BVIPcil_exgO76Q_2zGfK-udS15K0d_precPUBzbnPBJ3BhwCn6pDvJ0S2kExc33Wunqfxm0Xttwm18ovvFGgykX6uXGCnheLMXi_4cgIJjk2IPMDHmpHmqMZ_JuU_hwitTpXGOF2HvSz0a_-X_6L6OK6jTYeGZXbtADQ9Vv12Jyblhy9fSEXgHPHUWyOX2VDoTGAqJ4OPpRJQM-EvnHXkwbcr47ztsxwOIjBqQHOmpRCoNK7Nm9IAKtKEnJuWOZGUV9dT36vN0Y9rBPpRGH6taSSWFkMojn89SI0P43k6Qs0qgYxZu9s8DEdv_h6TfDbMa2EGuNx_mCRTKVTqLcZUzKc2HPRkjN99xOyoR_2s6JQ-oS1q6VWHGvFJMVRxNbs3ysD671dNrDbE_1aTxpvNRuqEI64UtpBERIpY9txN71WaZg20LZMF6x7J84SV7tIo6dTaCHtUoNJrw0Tcl_6oK6RvoIBgOiJZ8gP2Ri8F38ID_4KQx2BddmyRWzNqMsX0u36KXxAY6G2J3FMzQmPf6GPM9VcBmwFaGCqTXN60UA9HaISDW4maiwMRaE-EM4bRt8hw&amp;v=404&amp;clicktype=1');">
                                                <em>OPPO K1 光感屏幕指纹 水滴屏拍照<font class="skcolor_ljg">手机</font> 4GB+64GB 梵星蓝
                                                    全网通 移动联通电信4G 双卡双待<font class="skcolor_ljg">手机</font></em>
                                                <i class="promo-words"
                                                    id="J_AD_100000651175">【直降100元低至1099元】屏幕指纹解锁手机，前置2500万，AI智慧美颜。50元预定Reno2，4800万变焦四摄</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <strong><a id="J_comment_100000651175" target="_blank"
                                                    href="https://item.jd.com/100000651175.html"
                                                    onclick="searchlog(1,100000651175,11,3,'','adwClk=1')">49万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100000651175"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100000651175,11,5,'','adwClk=1')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="0" data-reputation="63"
                                            data-verderid="1000004065" data-done="1"><span class="J_im_icon"><a
                                                    target="_blank" onclick="searchlog(1,1000004065,0,58)"
                                                    href="//mall.jd.com/index-1000004065.html"
                                                    title="OPPO京东自营官方旗舰店">OPPO京东自营官方旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000004065,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100000651175" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                        </div>
                                        <span class="p-promo-flag">广告</span>

                                        <img source-data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=VuqDEEucP0LvlsuIkout6t92HzcQTX629uB8BI1cCzYZQ6VmYAssMBXIxzp3LWzo_8q-zZ3cijbOv062wup7KxSlMsvS2HSevYnTO2Ueh2hStrdxtBiliXM-4s4Wupj9tBgFS6jREp8fQrk3BVIPcil_exgO76Q_2zGfK-udS15K0d_precPUBzbnPBJ3BhwCn6pDvJ0S2kExc33Wunqf3CUSDNkHWT3ReaypkrJu4ZRf0X6kqto-YLlWUyRRtaoW2r18nmtbvTT8uUd99XOk4J6zCgEId47QDo8WREOYYNwR7IAHE7gIvw8kxLU4y_1tIGeCebAXXKGVG4WmYaTUzMvnPCh3Ixeyvc0dUT-2jk86ACK4SKDukr-2PqYgAHl_R72gl8ogXtDxRcpCw7JH18l9iyZd3LbRo1ezxd-4Xc-peDDQdOhuUAgeOo2-SWSm7zRAwACTsCwvOdiCRvsNihM1b8frQ4STy9XRbwS8urZIzioo7irH9m2IBFtQTY3mphdU-Unnol3J7KCKW2ltkfEnGYMHjJqdSgmSi01d9KnbyfMwgYrmIz76lxR8OKM-0e3JniZoC0p15cfr2sLSVUGlaXHM85JU81gLEVwr82dFc_MMa3xjN09HHcG8LcmAqCC59YS37m1ORpPVvMudT9BNqe0lSPp5_eS5iD55p1tPrsEiHyenR5R3spArW_PNwIvPSpgzxyhV27lmNhziw&amp;v=404&amp;rt=3"
                                            style="">
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100006769698" data-spu="100003395445"
                                    data-pid="100003395445">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="荣耀20 李现同款 4800万超广角AI四摄 3200W美颜自拍 麒麟Kirin980全网通版8GB+128GB 蓝水翡翠 全面屏手机"
                                                href="//item.jd.com/100006769698.html"
                                                onclick="searchlog(1,100006769698,12,2,'','flagsClk=1633686152')">
                                                <img width="220" height="220" class="err-product" data-img="1"
                                                    source-data-lazy-img=""
                                                    data-lazy-img="//img13.360buyimg.com/n7/jfs/t1/35493/30/14545/210121/5d280052E1187c175/e9ad9735fc3f0686.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000000904" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="蓝水翡翠"><img data-presale="" data-sku="100006769698"
                                                                data-img="1"
                                                                data-lazy-img="//img13.360buyimg.com/n9/jfs/t1/35493/30/14545/210121/5d280052E1187c175/e9ad9735fc3f0686.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="幻夜黑"><img
                                                                data-presale="" data-sku="100005603522" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img12.360buyimg.com/n9/jfs/t28906/30/1571661431/255345/986f5fcb/5ce4148aN55586a52.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="冰岛白"><img
                                                                data-presale="" data-sku="100003395467" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img12.360buyimg.com/n9/jfs/t28603/102/1236695962/227407/29d12d49/5ce41500N146e357e.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="幻影蓝"><img
                                                                data-presale="" data-sku="100003395445" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img10.360buyimg.com/n9/jfs/t11266/172/3136897597/311385/898550cb/5ce41430N7bb10f75.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100006769698"
                                                data-done="1"><em>￥</em><i>2699.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="荣耀20 李现同款 4800万超广角AI四摄 3200W美颜自拍 麒麟Kirin980全网通版8GB+128GB 蓝水翡翠 全面屏手机"
                                                href="//item.jd.com/100006769698.html"
                                                onclick="searchlog(1,100006769698,12,1,'','flagsClk=1633686152')">
                                                <em>荣耀20 李现同款 4800万超广角AI四摄 3200W美颜自拍 麒麟Kirin980全网通版8GB+128GB 蓝水翡翠 全面屏
                                                    <font class="skcolor_ljg">手机</font></em>
                                                <i class="promo-words" id="J_AD_100006769698"></i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <strong><a id="J_comment_100006769698" target="_blank"
                                                    href="//item.jd.com/100006769698.html#comment"
                                                    onclick="searchlog(1,100006769698,12,3,'','flagsClk=1633686152')">28万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100006769698"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100006769698,12,5,'','flagsClk=1633686152')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="96"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000000904,0,58)"
                                                    href="//mall.jd.com/index-1000000904.html"
                                                    title="荣耀京东自营旗舰店">荣耀京东自营旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000000904,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100006769698" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                            <i class="goods-icons4 J-picon-tips"
                                                style="border-color:#4d88ff;color:#4d88ff;" data-idx="1"
                                                data-tips="品质服务，放心购物">放心购</i>
                                            <i class="goods-icons3 J-picon-tips J-picon-fix" data-tips="该商品是当季新品">新品</i>
                                        </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100004017011" data-spu="7437710" data-pid="7437710">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="【品质特惠】骁龙675处理器，4000mAh大电量，18个月长质保，标配18W充电器！《6400万四摄小金刚新品，点击预约》"
                                                href="//item.jd.com/100004017011.html"
                                                onclick="searchlog(1,100004017011,13,2,'','flagsClk=1614811784')">
                                                <img width="220" height="220" class="err-product" data-img="1"
                                                    source-data-lazy-img=""
                                                    data-lazy-img="//img11.360buyimg.com/n7/jfs/t1/40924/14/9293/146092/5d2da5c3E80789a10/738b1b7131377b78.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000004123" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="镜花水月"><img data-presale="" data-sku="100004017011"
                                                                data-img="1"
                                                                data-lazy-img="//img11.360buyimg.com/n9/jfs/t1/40924/14/9293/146092/5d2da5c3E80789a10/738b1b7131377b78.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="亮黑色"><img
                                                                data-presale="" data-sku="100004169706" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img11.360buyimg.com/n9/jfs/t1/19699/33/11137/76839/5c8b69acEaa4b91dd/3054e7cd8d3d0e68.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="梦幻蓝"><img
                                                                data-presale="" data-sku="7437710" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img10.360buyimg.com/n9/jfs/t1/22746/35/11162/104085/5c8b6a19Eb8e8f34e/9cd57e3a481c7160.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="暮光金"><img
                                                                data-presale="" data-sku="100004169686" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img11.360buyimg.com/n9/jfs/t1/25890/30/10991/101856/5c8b69e8E1062991c/6eec05206d18d53c.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100004017011"
                                                data-done="1"><em>￥</em><i>1399.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="【品质特惠】骁龙675处理器，4000mAh大电量，18个月长质保，标配18W充电器！《6400万四摄小金刚新品，点击预约》"
                                                href="//item.jd.com/100004017011.html"
                                                onclick="searchlog(1,100004017011,13,1,'','flagsClk=1614811784')">
                                                <em>Redmi Note7pro 索尼4800万超清双摄 骁龙675 18个月超长质保 4000mAh超长续航 6GB+128GB 镜花水月
                                                    游戏智能<font class="skcolor_ljg">手机</font> 小米 红米</em>
                                                <i class="promo-words"
                                                    id="J_AD_100004017011">【品质特惠】骁龙675处理器，4000mAh大电量，18个月长质保，标配18W充电器！《6400万四摄小金刚新品，点击预约》</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <strong><a id="J_comment_100004017011" target="_blank"
                                                    href="//item.jd.com/100004017011.html#comment"
                                                    onclick="searchlog(1,100004017011,13,3,'','flagsClk=1614811784')">43万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100004017011"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100004017011,13,5,'','flagsClk=1614811784')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="95"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000004123,0,58)"
                                                    href="//mall.jd.com/index-1000004123.html"
                                                    title="小米京东自营旗舰店">小米京东自营旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000004123,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100004017011" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                        </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100002795959" data-spu="100004404954"
                                    data-pid="100004404954">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="【优惠500！到手价4988！加赠大额礼品券（含大闸蟹）】一站式以旧换新至高享500元补贴，50倍数字变焦；畅享10P预售送大额礼品卡》"
                                                href="//item.jd.com/100002795959.html"
                                                onclick="searchlog(1,100002795959,14,2,'','flagsClk=1631589000')">
                                                <img width="220" height="220" class="err-product" data-img="1"
                                                    source-data-lazy-img=""
                                                    data-lazy-img="//img14.360buyimg.com/n7/jfs/t1/19261/13/12605/324178/5c98c7bcE63f668de/ca2762256ec6f931.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000004259" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="极光色"><img data-presale="" data-sku="100002795959"
                                                                data-img="1"
                                                                data-lazy-img="//img14.360buyimg.com/n9/jfs/t1/19261/13/12605/324178/5c98c7bcE63f668de/ca2762256ec6f931.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="亮黑色"><img
                                                                data-presale="" data-sku="100004404944" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img14.360buyimg.com/n9/jfs/t1/25813/29/12657/304911/5c98c8e2E6bcf7d2d/25342f237b56fe97.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="天空之境"><img
                                                                data-presale="" data-sku="100004404926" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img11.360buyimg.com/n9/jfs/t1/36796/21/2594/218814/5cb688aaEda49e6a7/2fafed70a0078b59.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="珠光贝母"><img
                                                                data-presale="" data-sku="100004404924" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img14.360buyimg.com/n9/jfs/t1/27385/12/12617/203546/5c98ca37Eff3ca839/b32de2a2d04984c7.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="赤茶橘"><img
                                                                data-presale="" data-sku="100002795957" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img12.360buyimg.com/n9/jfs/t1/19345/10/12598/295682/5c98c724Edb9cbab4/6a62f53984f18318.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100002795959"
                                                data-done="1"><em>￥</em><i>4988.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="【优惠500！到手价4988！加赠大额礼品券（含大闸蟹）】一站式以旧换新至高享500元补贴，50倍数字变焦；畅享10P预售送大额礼品卡》"
                                                href="//item.jd.com/100002795959.html"
                                                onclick="searchlog(1,100002795959,14,1,'','flagsClk=1631589000')">
                                                <em><img class="p-tag3"
                                                        src="//img14.360buyimg.com/uba/jfs/t6919/268/501386350/1257/92e5fb39/5976fcf9Nd915775f.png">华为
                                                    HUAWEI P30 Pro 超感光徕卡四摄10倍混合变焦麒麟980芯片屏内指纹 8GB+128GB极光色全网通版双4G<font
                                                        class="skcolor_ljg">手机</font></em>
                                                <i class="promo-words"
                                                    id="J_AD_100002795959">【优惠500！到手价4988！加赠大额礼品券（含大闸蟹）】一站式以旧换新至高享500元补贴，50倍数字变焦；畅享10P预售送大额礼品卡》</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <a target="_blank" href="//paipai.jd.com/pc/list.html?pid=100002795959"
                                                class="spu-link">二手有售</a>
                                            <strong><a id="J_comment_100002795959" target="_blank"
                                                    href="//item.jd.com/100002795959.html#comment"
                                                    onclick="searchlog(1,100002795959,14,3,'','flagsClk=1631589000')">42万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100002795959"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100002795959,14,5,'','flagsClk=1631589000')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="97"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000004259,0,58)"
                                                    href="//mall.jd.com/index-1000004259.html"
                                                    title="华为京东自营官方旗舰店">华为京东自营官方旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000004259,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100002795959" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                            <i class="goods-icons4 J-picon-tips"
                                                style="border-color:#4d88ff;color:#4d88ff;" data-idx="1"
                                                data-tips="品质服务，放心购物">放心购</i>
                                            <i class="goods-icons4 J-picon-tips" data-tips="购买本商品送赠品">赠</i> </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100003666128" data-spu="100002425279"
                                    data-pid="100002425279">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="【9.8限时直降300+下单再减200，到手价2298！白条6期免息+赠耳机！学生专享12期免息】高通骁龙855！iQOOPro新品上市，速抢！"
                                                href="//item.jd.com/100003666128.html"
                                                onclick="searchlog(1,100003666128,15,2,'','flagsClk=1631589000')">
                                                <img width="220" height="220" class="err-product" data-img="1"
                                                    source-data-lazy-img=""
                                                    data-lazy-img="//img13.360buyimg.com/n7/jfs/t1/26917/29/8819/288174/5c791a3dE6face587/f71f688434d14789.jpg">
                                            </a>
                                            <div id="belt" class="p-act-sign J_belt_box sign-2017083101"
                                                style="background-image: url('https://img30.360buyimg.com/jgsq-productsoa/jfs/t16951/182/417192066/4728/322919ee/5a754dd7N2f64533f.png');">
                                                <div class="sign-title ac">PLUSDAY年度盛典
                                                    <span class="sign-date">(9.5-9.8)</span>
                                                </div>
                                            </div>
                                            <div data-lease="" data-catid="655" data-venid="1000085868" data-presale=""
                                                class="picon"
                                                style="background:url(//img30.360buyimg.com/jgsq-productsoa/jfs/t1/48070/1/8813/2057/5d636656E10ecba6c/f70d1cd376412832.png) no-repeat 0 0;_background-image:none;_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='//img30.360buyimg.com/jgsq-productsoa/jfs/t1/48070/1/8813/2057/5d636656E10ecba6c/f70d1cd376412832.png',sizingMethod='noscale');"
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="熔岩橙"><img data-presale="" data-sku="100003666128"
                                                                data-img="1"
                                                                data-lazy-img="//img13.360buyimg.com/n9/jfs/t1/26917/29/8819/288174/5c791a3dE6face587/f71f688434d14789.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="电光蓝"><img
                                                                data-presale="" data-sku="100002425279" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img14.360buyimg.com/n9/jfs/t1/16938/25/8833/287777/5c791914E6649059c/0e2f0c1d7e74ce0e.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="羽光白"><img
                                                                data-presale="" data-sku="100003785533" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img13.360buyimg.com/n9/jfs/t1/49980/10/3068/357406/5d0ca7f4E060d0278/3cd2f079c7ffe949.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="武士黑"><img
                                                                data-presale="" data-sku="100005236836" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img11.360buyimg.com/n9/jfs/t1/38769/11/2224/318485/5cbfcfaaEfe8197e5/f67f128aef875b28.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="骑士黑"><img
                                                                data-presale="" data-sku="100004323708" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img13.360buyimg.com/n9/jfs/t1/40101/7/2606/165985/5cc16b3cE3ff18f87/a5073ef3e49c1674.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100003666128"
                                                data-done="1"><em>￥</em><i>2498.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="【9.8限时直降300+下单再减200，到手价2298！白条6期免息+赠耳机！学生专享12期免息】高通骁龙855！iQOOPro新品上市，速抢！"
                                                href="//item.jd.com/100003666128.html"
                                                onclick="searchlog(1,100003666128,15,1,'','flagsClk=1631589000')">
                                                <em><span class="p-tag" style="background-color:#c81623">京品手机</span>vivo
                                                    iQOO 6GB+128GB 熔岩橙 高通骁龙855<font class="skcolor_ljg">手机</font>
                                                    4000mAh大电池 全面屏智能拍照 全网通4G<font class="skcolor_ljg">手机</font></em>
                                                <i class="promo-words"
                                                    id="J_AD_100003666128">【9.8限时直降300+下单再减200，到手价2298！白条6期免息+赠耳机！学生专享12期免息】高通骁龙855！iQOOPro新品上市，速抢！</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <a target="_blank" href="//paipai.jd.com/pc/list.html?pid=100003666128"
                                                class="spu-link">二手有售</a>
                                            <strong><a id="J_comment_100003666128" target="_blank"
                                                    href="//item.jd.com/100003666128.html#comment"
                                                    onclick="searchlog(1,100003666128,15,3,'','flagsClk=1631589000')">29万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100003666128"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100003666128,15,5,'','flagsClk=1631589000')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="95"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000085868,0,58)"
                                                    href="//mall.jd.com/index-1000085868.html"
                                                    title="vivo京东自营官方旗舰店">vivo京东自营官方旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000085868,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100003666128" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                            <i class="goods-icons4 J-picon-tips" data-tips="本商品可领用优惠券">券2000-200</i><i
                                                class="goods-icons4 J-picon-tips" data-tips="本商品参与满减促销">满2000-200</i>
                                        </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100000745034" data-spu="100000767811"
                                    data-pid="100000767811">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="【优惠400，到手价1199】7.12英寸大屏，杜比全景声，5000mA超长续航;畅享10P预售送大额礼品卡》"
                                                href="//item.jd.com/100000745034.html"
                                                onclick="searchlog(1,100000745034,16,2,'','flagsClk=1631589000')">
                                                <img width="220" height="220" class="err-product" data-img="1"
                                                    source-data-lazy-img=""
                                                    data-lazy-img="//img14.360buyimg.com/n7/jfs/t25012/345/1827676978/130853/65940865/5bbc6efaNeb227f0b.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000004259" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="幻夜黑"><img data-presale="" data-sku="100000745034"
                                                                data-img="1"
                                                                data-lazy-img="//img14.360buyimg.com/n9/jfs/t25012/345/1827676978/130853/65940865/5bbc6efaNeb227f0b.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="琥珀棕"><img
                                                                data-presale="" data-sku="100000663335" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img10.360buyimg.com/n9/jfs/t27172/83/893681332/128980/dc4ee3e3/5bbc6ed1Nce5ecf65.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="天际白"><img
                                                                data-presale="" data-sku="100000767811" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img11.360buyimg.com/n9/jfs/t25567/298/1850240795/108643/9cdd6f93/5bbc6adcN964c959f.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100000745034"
                                                data-done="1"><em>￥</em><i>1199.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="【优惠400，到手价1199】7.12英寸大屏，杜比全景声，5000mA超长续航;畅享10P预售送大额礼品卡》"
                                                href="//item.jd.com/100000745034.html"
                                                onclick="searchlog(1,100000745034,16,1,'','flagsClk=1631589000')">
                                                <em>华为 HUAWEI 畅享MAX 4GB+64GB 幻夜黑 全网通版 珍珠屏杜比全景声大电池 移动联通电信4G<font
                                                        class="skcolor_ljg">手机</font> 双卡双待</em>
                                                <i class="promo-words"
                                                    id="J_AD_100000745034">【优惠400，到手价1199】7.12英寸大屏，杜比全景声，5000mA超长续航;畅享10P预售送大额礼品卡》</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <strong><a id="J_comment_100000745034" target="_blank"
                                                    href="//item.jd.com/100000745034.html#comment"
                                                    onclick="searchlog(1,100000745034,16,3,'','flagsClk=1631589000')">8.5万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100000745034"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100000745034,16,5,'','flagsClk=1631589000')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="99"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000004259,0,58)"
                                                    href="//mall.jd.com/index-1000004259.html"
                                                    title="华为京东自营官方旗舰店">华为京东自营官方旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000004259,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100000745034" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                            <i class="goods-icons4 J-picon-tips"
                                                style="border-color:#4d88ff;color:#4d88ff;" data-idx="1"
                                                data-tips="品质服务，放心购物">放心购</i>
                                        </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100005088618" data-spu="100005088618"
                                    data-pid="100005088618">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="【6期免息+一年碎屏保】10倍混合光学变焦，60倍数码变焦，高通骁龙855。50元预定Reno2，4800万变焦四摄"
                                                href="https://item.jd.com/100005088618.html"
                                                onclick="searchlog(1,100005088618,17,2,'','adwClk=1');searchAdvPointReport('https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDUwODg2MTguaHRtbA&amp;log=VuqDEEucP0LvlsuIkout6t92HzcQTX629uB8BI1cCzaT1cN54ykQp-uF1id6bI-lNGBUdUUje50HHhCq0pkUnpRcgc1GEQyT8fUmeSeN2RkrOS2Q7GYESaHukAWLzZp1iqagEzJo4Br8qH7zW_1zpGg5PfDFwSVWoMJ74QurhaWucNxl-WRKt9gP9W2u5tyfv1xqghG-HWIvYCRMGyc32xxhUmRVk1BU4XKW7N56nPjMW4uHQVCcfiWjxzA6gZWmWnMdxrVOkea1ghPfUlidsTp9kqS9ZTxxyF5pbIou_7truKsPr8ps-YR6slPODhQGh8v-9WFFQEVNHv49MRipEHatRSL_LB_xQDx8iEmPssbk5_te-7YeUQhK5GZX-q5nU_KUZAd4ccXoUuuBy4CEmzQV_tE6zT39XwuSZEXxWiOE8xfgN7CIXTMzdmXq4x85Lx_-jf8bndqDkHKhzw0SFfULdLvAKbjUS5eIctsjt-EMH1RzURXcVHoNZ2_RcWtKhatoKHtaIvezkcFX0G1SgHfryTioF6kQzMFgnQMaSvrZLeEdJfyS2i5w_5i-6nUkB7ALq9oV5pAmjLh1OKVPFiDWnrqTpBTpB47SWN9KBngeZPy4-egvNfmyFnVzKYEkHnEXXZ-eSwKtFZUpLBPcYZ8rGCEL2x0XHWRMsCGJtIUOjJbdJppLynrRb4u1HKTebbDF8zHNHsST0BtuoWyi5w&amp;v=404&amp;clicktype=1');">
                                                <img width="220" height="220" class="err-product" data-img="1"
                                                    source-data-lazy-img=""
                                                    data-lazy-img="//img13.360buyimg.com/n7/jfs/t1/67127/24/7772/162814/5d5a7c3fE50508764/0aa504c495bb132d.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000004065" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="雾海绿"><img
                                                                data-url="https://item.jd.com/100005088618.html"
                                                                data-presale="" data-sku="100005088618" data-img="1"
                                                                data-lazy-img="//img13.360buyimg.com/n9/jfs/t1/67127/24/7772/162814/5d5a7c3fE50508764/0aa504c495bb132d.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100005088618"
                                                data-done="1"><em>￥</em><i>3699.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="【6期免息+一年碎屏保】10倍混合光学变焦，60倍数码变焦，高通骁龙855。50元预定Reno2，4800万变焦四摄"
                                                href="https://item.jd.com/100005088618.html"
                                                onclick="searchlog(1,100005088618,17,1,'','adwClk=1');searchAdvPointReport('https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDUwODg2MTguaHRtbA&amp;log=VuqDEEucP0LvlsuIkout6t92HzcQTX629uB8BI1cCzaT1cN54ykQp-uF1id6bI-lNGBUdUUje50HHhCq0pkUnpRcgc1GEQyT8fUmeSeN2RkrOS2Q7GYESaHukAWLzZp1iqagEzJo4Br8qH7zW_1zpGg5PfDFwSVWoMJ74QurhaWucNxl-WRKt9gP9W2u5tyfv1xqghG-HWIvYCRMGyc32xxhUmRVk1BU4XKW7N56nPjMW4uHQVCcfiWjxzA6gZWmWnMdxrVOkea1ghPfUlidsTp9kqS9ZTxxyF5pbIou_7truKsPr8ps-YR6slPODhQGh8v-9WFFQEVNHv49MRipEHatRSL_LB_xQDx8iEmPssbk5_te-7YeUQhK5GZX-q5nU_KUZAd4ccXoUuuBy4CEmzQV_tE6zT39XwuSZEXxWiOE8xfgN7CIXTMzdmXq4x85Lx_-jf8bndqDkHKhzw0SFfULdLvAKbjUS5eIctsjt-EMH1RzURXcVHoNZ2_RcWtKhatoKHtaIvezkcFX0G1SgHfryTioF6kQzMFgnQMaSvrZLeEdJfyS2i5w_5i-6nUkB7ALq9oV5pAmjLh1OKVPFiDWnrqTpBTpB47SWN9KBngeZPy4-egvNfmyFnVzKYEkHnEXXZ-eSwKtFZUpLBPcYZ8rGCEL2x0XHWRMsCGJtIUOjJbdJppLynrRb4u1HKTebbDF8zHNHsST0BtuoWyi5w&amp;v=404&amp;clicktype=1');">
                                                <em>OPPO Reno 10倍变焦版 高通骁龙855 4800万超清三摄 6GB+128GB 雾海绿 全网通 全面屏拍照智能游戏<font
                                                        class="skcolor_ljg">手机</font></em>
                                                <i class="promo-words"
                                                    id="J_AD_100005088618">【6期免息+一年碎屏保】10倍混合光学变焦，60倍数码变焦，高通骁龙855。50元预定Reno2，4800万变焦四摄</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <strong><a id="J_comment_100005088618" target="_blank"
                                                    href="https://item.jd.com/100005088618.html"
                                                    onclick="searchlog(1,100005088618,17,3,'','adwClk=1')">3万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100005088618"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100005088618,17,5,'','adwClk=1')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="0" data-reputation="36"
                                            data-verderid="1000004065" data-done="1"><span class="J_im_icon"><a
                                                    target="_blank" onclick="searchlog(1,1000004065,0,58)"
                                                    href="//mall.jd.com/index-1000004065.html"
                                                    title="OPPO京东自营官方旗舰店">OPPO京东自营官方旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000004065,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100005088618" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i><i class="goods-icons4 J-picon-tips"
                                                data-tips="购买本商品送赠品">赠</i>
                                        </div>
                                        <span class="p-promo-flag">广告</span>

                                        <img source-data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=VuqDEEucP0LvlsuIkout6t92HzcQTX629uB8BI1cCzaT1cN54ykQp-uF1id6bI-lNGBUdUUje50HHhCq0pkUnpRcgc1GEQyT8fUmeSeN2RkrOS2Q7GYESaHukAWLzZp1iqagEzJo4Br8qH7zW_1zpGg5PfDFwSVWoMJ74QurhaWucNxl-WRKt9gP9W2u5tyfv1xqghG-HWIvYCRMGyc329z4xud77A8Yk7-w4uuf-lz0f451LECocpEgJ4i7--yzVjYQ6ikJ9vZlnAUI4VE8Q6xF5nSHZDcIGGtFqcwCx-MX_1drxCVooSmGzRRtg9ssi6n0pOKRHTKvijV-Xqdu0ddNLR8hi6CMc7EGHgd1SA-UbxHi2h18tUshQJx1STiZledW0G5frtYLJ7Ybf7eI0r1YX0gZEISA7oYnn9ROZHwBCThN5h6cuq0gibUu79s1E4bCzAw_xubT0c_si8ENPEL53DCbVaO98Qx28Tyh18dEAC9xvAVBZqFA524gryADrqqtww-62QS2OO8mpc617ssTWG3vpiZMbzt2O04s7AqY3pDgsRz0HlJ_DuOQcVVPcDIDisBL4Lqkn3L7_OWgFd7xUrgrmsSVgZlJ2HyJ7hbArCeVJDu6bug53AW6zFt3uRkuVn-VydbdS7XQBDK575AIcCamUwbuczNvcNsyZbT0iVd793wmW5smjsz_-YtuK_P64uyWc-fe9t5MqkwW3A&amp;v=404&amp;rt=3"
                                            style="">
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100004036237" data-spu="100003395443"
                                    data-pid="100003395443">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank" title="白条6期免息！麒麟980，4800万全焦段AI四摄！荣耀20系列2699起，4800万超广角四摄！"
                                                href="//item.jd.com/100004036237.html"
                                                onclick="searchlog(1,100004036237,18,2,'','flagsClk=1633686152')">
                                                <img width="220" height="220" class="err-product" data-img="1"
                                                    source-data-lazy-img=""
                                                    data-lazy-img="//img12.360buyimg.com/n7/jfs/t1/43961/17/9910/200594/5d36d94dE1ccec7c3/2119602452efce60.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000000904" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="冰岛幻境"><img data-presale="" data-sku="100004036237"
                                                                data-img="1"
                                                                data-lazy-img="//img12.360buyimg.com/n9/jfs/t1/43961/17/9910/200594/5d36d94dE1ccec7c3/2119602452efce60.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="蓝水翡翠"><img
                                                                data-presale="" data-sku="100003395443" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img13.360buyimg.com/n9/jfs/t1/45707/34/648/300546/5ce44d8fE72d72070/62cf191f88e41447.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="幻夜星河"><img
                                                                data-presale="" data-sku="100003395441" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img11.360buyimg.com/n9/jfs/t28822/35/1566945199/293949/86cf3f83/5ce44e3cN9f8622b3.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="MOSCHINO联名版"><img
                                                                data-presale="" data-sku="100003856953" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img13.360buyimg.com/n9/jfs/t1/53849/13/3706/186222/5d16bb5eEaa3ae4be/b6f8e1df237f0af9.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100004036237"
                                                data-done="1"><em>￥</em><i>3199.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank" title="白条6期免息！麒麟980，4800万全焦段AI四摄！荣耀20系列2699起，4800万超广角四摄！"
                                                href="//item.jd.com/100004036237.html"
                                                onclick="searchlog(1,100004036237,18,1,'','flagsClk=1633686152')">
                                                <em>荣耀20 PRO 李现同款 4800万全焦段AI四摄 双光学防抖 麒麟980 全网通4G 8GB+128GB 冰岛幻境 拍照<font
                                                        class="skcolor_ljg">手机</font></em>
                                                <i class="promo-words"
                                                    id="J_AD_100004036237">白条6期免息！麒麟980，4800万全焦段AI四摄！荣耀20系列2699起，4800万超广角四摄！</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <strong><a id="J_comment_100004036237" target="_blank"
                                                    href="//item.jd.com/100004036237.html#comment"
                                                    onclick="searchlog(1,100004036237,18,3,'','flagsClk=1633686152')">8.6万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100004036237"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100004036237,18,5,'','flagsClk=1633686152')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="94"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000000904,0,58)"
                                                    href="//mall.jd.com/index-1000000904.html"
                                                    title="荣耀京东自营旗舰店">荣耀京东自营旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000000904,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100004036237" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                            <i class="goods-icons4 J-picon-tips"
                                                style="border-color:#4d88ff;color:#4d88ff;" data-idx="1"
                                                data-tips="品质服务，放心购物">放心购</i>
                                            <i class="goods-icons3 J-picon-tips J-picon-fix" data-tips="该商品是当季新品">新品</i>
                                        </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100003786269" data-spu="100006386682"
                                    data-pid="100006386682">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="【9.8-9.10白条6期免息+赠耳机】高通骁龙845，4500mAh大电池，22.5W闪充！非凡电竞体验！iQOOPro新品上市，速抢！"
                                                href="//item.jd.com/100003786269.html"
                                                onclick="searchlog(1,100003786269,19,2,'','flagsClk=1633686152')">
                                                <img width="220" height="220" class="err-product" data-img="1"
                                                    source-data-lazy-img=""
                                                    data-lazy-img="//img14.360buyimg.com/n7/jfs/t1/66334/6/3571/249336/5d1b3e44Edcaef7fe/6e3dae89f9d9e0cd.jpg">
                                            </a>
                                            <div id="belt" class="p-act-sign J_belt_box sign-2017083101"
                                                style="background-image: url('https://img30.360buyimg.com/jgsq-productsoa/jfs/t16951/182/417192066/4728/322919ee/5a754dd7N2f64533f.png');">
                                                <div class="sign-title ac">PLUSDAY年度盛典
                                                    <span class="sign-date">(9.5-9.8)</span>
                                                </div>
                                            </div>
                                            <div data-lease="" data-catid="655" data-venid="1000085868" data-presale=""
                                                class="picon"
                                                style="background:url(//img30.360buyimg.com/jgsq-productsoa/jfs/t1/48070/1/8813/2057/5d636656E10ecba6c/f70d1cd376412832.png) no-repeat 0 0;_background-image:none;_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='//img30.360buyimg.com/jgsq-productsoa/jfs/t1/48070/1/8813/2057/5d636656E10ecba6c/f70d1cd376412832.png',sizingMethod='noscale');"
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="电光紫"><img data-presale="" data-sku="100003786269"
                                                                data-img="1"
                                                                data-lazy-img="//img14.360buyimg.com/n9/jfs/t1/66334/6/3571/249336/5d1b3e44Edcaef7fe/6e3dae89f9d9e0cd.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="碳纤黑"><img
                                                                data-presale="" data-sku="100006386682" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img12.360buyimg.com/n9/jfs/t1/76415/12/3432/304040/5d1b435aE04901f3c/db75d79d8a32ba44.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100003786269"
                                                data-done="1"><em>￥</em><i>1998.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="【9.8-9.10白条6期免息+赠耳机】高通骁龙845，4500mAh大电池，22.5W闪充！非凡电竞体验！iQOOPro新品上市，速抢！"
                                                href="//item.jd.com/100003786269.html"
                                                onclick="searchlog(1,100003786269,19,1,'','flagsClk=1633686152')">
                                                <em><img class="p-tag3"
                                                        src="//img14.360buyimg.com/uba/jfs/t6919/268/501386350/1257/92e5fb39/5976fcf9Nd915775f.png">vivo
                                                    iQOO Neo 6GB+128GB 电光紫 骁龙845处理器 4500mAh强悍续航<font
                                                        class="skcolor_ljg">手机</font> 22.5W超快闪充 全网通4G<font
                                                        class="skcolor_ljg">手机</font></em>
                                                <i class="promo-words"
                                                    id="J_AD_100003786269">【9.8-9.10白条6期免息+赠耳机】高通骁龙845，4500mAh大电池，22.5W闪充！非凡电竞体验！iQOOPro新品上市，速抢！</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <strong><a id="J_comment_100003786269" target="_blank"
                                                    href="//item.jd.com/100003786269.html#comment"
                                                    onclick="searchlog(1,100003786269,19,3,'','flagsClk=1633686152')">9.9万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100003786269"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100003786269,19,5,'','flagsClk=1633686152')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="95"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000085868,0,58)"
                                                    href="//mall.jd.com/index-1000085868.html"
                                                    title="vivo京东自营官方旗舰店">vivo京东自营官方旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000085868,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100003786269" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                            <i class="goods-icons3 J-picon-tips J-picon-fix" data-tips="该商品是当季新品">新品</i>
                                        </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100006828852" data-spu="100006828852"
                                    data-pid="100006828852">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank" title="白条6期免息！麒麟810,4800万夜拍三摄，升降式全面屏！荣耀爆品特惠，选品质，购荣耀~"
                                                href="//item.jd.com/100006828852.html"
                                                onclick="searchlog(1,100006828852,20,2,'','flagsClk=559944328')">
                                                <img width="220" height="220" class="err-product" data-img="1"
                                                    source-data-lazy-img=""
                                                    data-lazy-img="//img12.360buyimg.com/n7/jfs/t1/84242/16/4683/258994/5d2d24f3Efab954c3/eef9df66700b920e.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000000904" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="幻影紫"><img data-presale="" data-sku="100006828852"
                                                                data-img="1"
                                                                data-lazy-img="//img12.360buyimg.com/n9/jfs/t1/84242/16/4683/258994/5d2d24f3Efab954c3/eef9df66700b920e.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="幻夜黑"><img
                                                                data-presale="" data-sku="100006946970" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img10.360buyimg.com/n9/jfs/t1/39464/17/12055/280975/5d36d3b9E769629e1/e00a86236dd7b270.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100006828852"
                                                data-done="1"><em>￥</em><i>2199.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank" title="白条6期免息！麒麟810,4800万夜拍三摄，升降式全面屏！荣耀爆品特惠，选品质，购荣耀~"
                                                href="//item.jd.com/100006828852.html"
                                                onclick="searchlog(1,100006828852,20,1,'','flagsClk=559944328')">
                                                <em>荣耀9X PRO 麒麟810液冷散热 4000mAh超强续航 4800万超广角夜拍三摄 6.59英寸全网通8GB+128GB
                                                    幻影紫</em>
                                                <i class="promo-words"
                                                    id="J_AD_100006828852">白条6期免息！麒麟810,4800万夜拍三摄，升降式全面屏！荣耀爆品特惠，选品质，购荣耀~</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <strong><a id="J_comment_100006828852" target="_blank"
                                                    href="//item.jd.com/100006828852.html#comment"
                                                    onclick="searchlog(1,100006828852,20,3,'','flagsClk=559944328')">3.1万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100006828852"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100006828852,20,5,'','flagsClk=559944328')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="96"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000000904,0,58)"
                                                    href="//mall.jd.com/index-1000000904.html"
                                                    title="荣耀京东自营旗舰店">荣耀京东自营旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000000904,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100006828852" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                            <i class="goods-icons4 J-picon-tips"
                                                style="border-color:#4d88ff;color:#4d88ff;" data-idx="1"
                                                data-tips="品质服务，放心购物">放心购</i>
                                            <i class="goods-icons3 J-picon-tips J-picon-fix" data-tips="该商品是当季新品">新品</i>
                                        </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="7421462" data-spu="7421462" data-pid="7421462">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="华为 HUAWEI 畅享8e 青春版 2GB+32GB全面屏 金色 全网通版 移动联通电信4G手机 双卡双待"
                                                href="//item.jd.com/7421462.html"
                                                onclick="searchlog(1,7421462,21,2,'','flagsClk=1631589000')">
                                                <img width="220" height="220" class="err-product" data-img="1"
                                                    source-data-lazy-img=""
                                                    data-lazy-img="//img12.360buyimg.com/n7/jfs/t21043/186/220467895/46630/3417464c/5b0517ccN295c6fdb.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000004259" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="金色"><img data-presale="" data-sku="7421462"
                                                                data-img="1"
                                                                data-lazy-img="//img12.360buyimg.com/n9/jfs/t21043/186/220467895/46630/3417464c/5b0517ccN295c6fdb.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="黑色"><img
                                                                data-presale="" data-sku="7635559" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img14.360buyimg.com/n9/jfs/t19822/21/667428507/40291/1aba7a/5b05180aN7bcc1127.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="蓝色"><img
                                                                data-presale="" data-sku="7635543" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img13.360buyimg.com/n9/jfs/t19774/15/2645902231/43345/d4499471/5b05183fNfcf03d14.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_7421462" data-done="1"><em>￥</em><i>549.00</i></strong>
                                        </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="华为 HUAWEI 畅享8e 青春版 2GB+32GB全面屏 金色 全网通版 移动联通电信4G手机 双卡双待"
                                                href="//item.jd.com/7421462.html"
                                                onclick="searchlog(1,7421462,21,1,'','flagsClk=1631589000')">
                                                <em>华为 HUAWEI 畅享8e 青春版 2GB+32GB全面屏 金色 全网通版 移动联通电信4G<font
                                                        class="skcolor_ljg">手机</font> 双卡双待</em>
                                                <i class="promo-words" id="J_AD_7421462"></i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <strong><a id="J_comment_7421462" target="_blank"
                                                    href="//item.jd.com/7421462.html#comment"
                                                    onclick="searchlog(1,7421462,21,3,'','flagsClk=1631589000')">26万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="7421462" href="javascript:;"
                                                title="点击关注"
                                                onclick="searchlog(1,7421462,21,5,'','flagsClk=1631589000')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="98"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000004259,0,58)"
                                                    href="//mall.jd.com/index-1000004259.html"
                                                    title="华为京东自营官方旗舰店">华为京东自营官方旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000004259,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_7421462" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                            <i class="goods-icons4 J-picon-tips"
                                                style="border-color:#4d88ff;color:#4d88ff;" data-idx="1"
                                                data-tips="品质服务，放心购物">放心购</i>
                                        </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100003242371" data-spu="100003242371"
                                    data-pid="100003242371">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="【9.6-9.8号限时优惠100元,到手1699元】骁龙710,升降全面屏；realmeQ全新系列预售，现在付定金至高享100元优惠加送一年碎屏险！"
                                                href="//item.jd.com/100003242371.html"
                                                onclick="searchlog(1,100003242371,22,2,'','flagsClk=1633686152')">
                                                <img width="220" height="220" class="err-product" data-img="1"
                                                    source-data-lazy-img=""
                                                    data-lazy-img="//img11.360buyimg.com/n7/jfs/t30055/157/1561579309/330348/51cda39b/5ce4f888N01ba2454.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000164941" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="朋克蓝"><img data-presale="" data-sku="100003242371"
                                                                data-img="1"
                                                                data-lazy-img="//img11.360buyimg.com/n9/jfs/t30055/157/1561579309/330348/51cda39b/5ce4f888N01ba2454.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="蒸汽白"><img
                                                                data-presale="" data-sku="100005297918" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img13.360buyimg.com/n9/jfs/t1/65369/12/524/294380/5ceb5d9eE1694db95/bc2e7d7aa2a90178.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="大师版白蒜"><img
                                                                data-presale="" data-sku="100003966895" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img10.360buyimg.com/n9/jfs/t1/35261/3/14630/165192/5d26b07bE1bae9c5f/9d45363906f6545d.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="大师版洋葱"><img
                                                                data-presale="" data-sku="100003803335" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img10.360buyimg.com/n9/jfs/t1/71367/1/3095/287604/5d1425f3E6dc43044/fc23eb212982fe9c.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100003242371"
                                                data-done="1"><em>￥</em><i>1799.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="【9.6-9.8号限时优惠100元,到手1699元】骁龙710,升降全面屏；realmeQ全新系列预售，现在付定金至高享100元优惠加送一年碎屏险！"
                                                href="//item.jd.com/100003242371.html"
                                                onclick="searchlog(1,100003242371,22,1,'','flagsClk=1633686152')">
                                                <em><span class="p-tag"
                                                        style="background-color:#c81623">京品手机</span>realme X 4800万双摄
                                                    升降摄像头 屏下指纹 游戏智能<font class="skcolor_ljg">手机</font> 8GB+128GB朋克蓝
                                                    全网通双卡</em>
                                                <i class="promo-words"
                                                    id="J_AD_100003242371">【9.6-9.8号限时优惠100元,到手1699元】骁龙710,升降全面屏；realmeQ全新系列预售，现在付定金至高享100元优惠加送一年碎屏险！</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <strong><a id="J_comment_100003242371" target="_blank"
                                                    href="//item.jd.com/100003242371.html#comment"
                                                    onclick="searchlog(1,100003242371,22,3,'','flagsClk=1633686152')">19万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100003242371"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100003242371,22,5,'','flagsClk=1633686152')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="94"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000164941,0,58)"
                                                    href="//mall.jd.com/index-1000164941.html"
                                                    title="realme京东自营官方旗舰店">realme京东自营官方旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000164941,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100003242371" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                            <i class="goods-icons3 J-picon-tips J-picon-fix" data-tips="该商品是当季新品">新品</i>
                                            <i class="goods-icons4 J-picon-tips" data-tips="本商品可领用优惠券">券980-60</i>
                                        </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100008031596" data-spu="100004619589"
                                    data-pid="100004619589">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="【预售送大额礼品卡】抽奖赢手机，前8000名晒单送耳机，128GB大内存；升降摄像头；抢天空之境稀缺货源》"
                                                href="https://item.jd.com/100008031596.html"
                                                onclick="searchlog(1,100008031596,23,2,'','adwClk=1');searchAdvPointReport('https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDgwMzE1OTYuaHRtbA&amp;log=VuqDEEucP0LvlsuIkout6t92HzcQTX629uB8BI1cCzbQbwb2APV7cS8Tu3CLlGeYvaWpeyppVbS3k0q38DCyU5iMY2JGTIYkOJJlkPFv4YmdMMhttlkNVmYfUlixl97SXTcIQ5_mH4J4JRBHqZOnPZE3wTTGQ-NDb4ociBygW5qucsuJ_gy1rDkTGjkw5nUmM3a6-ejc0mw564HpMRfqbqsbCscVTmVw1UZ57W3y25AQ41KhK7pnAy2DvfvOSBGE3hHPgk41_7Qa0Th5D0JjMI0HThiXWUNAbx2o78tt625aadQI6pmUOJ_2-RZVV-aJnxLYoUyCpUB-OYYAZfSVR3dVjR5py3cJendDJl8HRZ_esKYCHaaodP0jCtKWYDe48CDgDuFX9V25IPW2-V2eErVu0oMJpdyTTpMm0y8CyeW0aKKjXquMGiYKsRdrp8Svw8OTEQcrepN6usLTSKlyg-56JTP5yZUZJaHoSNdpONBmQMR3OzP6qASmWzJa8fu_gXE5T0PfyAuaRLPSSOjCxsWU6Mo6iP8btS5g72ElldPbTjfvi0CJY96rVJFiV-AE9mGZxj0wLwfVwdqgnR1tFxW-y3vWLw8MvAqVT7cvWth4izLG9WhaHuBwXBTsmqLV6uOd1vPGVH9pFaSuvRE_OaAlf54mN9X_Wf211ZXELhVIy0gCvFuQBMgvO2JEuD26Wei3x2BX-W4gT_nzv8ea8GsFfEDvroXGupKClQpLHu0&amp;v=404&amp;clicktype=1');">
                                                <img width="220" height="220" class="err-product" data-img="1"
                                                    source-data-lazy-img=""
                                                    data-lazy-img="//img11.360buyimg.com/n7/jfs/t1/46463/39/9830/239422/5d70d892E48ba5df8/3375049263dc8d11.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000004259" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="翡冷翠"><img
                                                                data-url="https://item.jd.com/100008031596.html"
                                                                data-presale="" data-sku="100008031596" data-img="1"
                                                                data-lazy-img="//img11.360buyimg.com/n9/jfs/t1/46463/39/9830/239422/5d70d892E48ba5df8/3375049263dc8d11.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100008031596"
                                                data-done="1"><em>￥</em><i>1499.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="【预售送大额礼品卡】抽奖赢手机，前8000名晒单送耳机，128GB大内存；升降摄像头；抢天空之境稀缺货源》"
                                                href="https://item.jd.com/100008031596.html"
                                                onclick="searchlog(1,100008031596,23,1,'','adwClk=1');searchAdvPointReport('https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDgwMzE1OTYuaHRtbA&amp;log=VuqDEEucP0LvlsuIkout6t92HzcQTX629uB8BI1cCzbQbwb2APV7cS8Tu3CLlGeYvaWpeyppVbS3k0q38DCyU5iMY2JGTIYkOJJlkPFv4YmdMMhttlkNVmYfUlixl97SXTcIQ5_mH4J4JRBHqZOnPZE3wTTGQ-NDb4ociBygW5qucsuJ_gy1rDkTGjkw5nUmM3a6-ejc0mw564HpMRfqbqsbCscVTmVw1UZ57W3y25AQ41KhK7pnAy2DvfvOSBGE3hHPgk41_7Qa0Th5D0JjMI0HThiXWUNAbx2o78tt625aadQI6pmUOJ_2-RZVV-aJnxLYoUyCpUB-OYYAZfSVR3dVjR5py3cJendDJl8HRZ_esKYCHaaodP0jCtKWYDe48CDgDuFX9V25IPW2-V2eErVu0oMJpdyTTpMm0y8CyeW0aKKjXquMGiYKsRdrp8Svw8OTEQcrepN6usLTSKlyg-56JTP5yZUZJaHoSNdpONBmQMR3OzP6qASmWzJa8fu_gXE5T0PfyAuaRLPSSOjCxsWU6Mo6iP8btS5g72ElldPbTjfvi0CJY96rVJFiV-AE9mGZxj0wLwfVwdqgnR1tFxW-y3vWLw8MvAqVT7cvWth4izLG9WhaHuBwXBTsmqLV6uOd1vPGVH9pFaSuvRE_OaAlf54mN9X_Wf211ZXELhVIy0gCvFuQBMgvO2JEuD26Wei3x2BX-W4gT_nzv8ea8GsFfEDvroXGupKClQpLHu0&amp;v=404&amp;clicktype=1');">
                                                <em>华为 HUAWEI 畅享10 Plus 超高清全视屏前置悬浮式镜头4800万超广角AI三摄 4GB+128GB翡冷翠全网通双4G
                                                    <font class="skcolor_ljg">手机</font></em>
                                                <i class="promo-words"
                                                    id="J_AD_100008031596">【预售送大额礼品卡】抽奖赢手机，前8000名晒单送耳机，128GB大内存；升降摄像头；抢天空之境稀缺货源》</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <strong><a id="J_comment_100008031596" target="_blank"
                                                    href="https://item.jd.com/100008031596.html"
                                                    onclick="searchlog(1,100008031596,23,3,'','adwClk=1')">0</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100008031596"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100008031596,23,5,'','adwClk=1')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="0" data-reputation=""
                                            data-verderid="1000004259" data-done="1"><span class="J_im_icon"><a
                                                    target="_blank" onclick="searchlog(1,1000004259,0,58)"
                                                    href="//mall.jd.com/index-1000004259.html"
                                                    title="华为京东自营官方旗舰店">华为京东自营官方旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000004259,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100008031596" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i><i class="goods-icons4 J-picon-tips"
                                                data-tips="购买本商品送赠品">赠</i>
                                        </div>
                                        <span class="p-promo-flag">广告</span>

                                        <img source-data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=VuqDEEucP0LvlsuIkout6t92HzcQTX629uB8BI1cCzbQbwb2APV7cS8Tu3CLlGeYvaWpeyppVbS3k0q38DCyU5iMY2JGTIYkOJJlkPFv4YmdMMhttlkNVmYfUlixl97SXTcIQ5_mH4J4JRBHqZOnPZE3wTTGQ-NDb4ociBygW5qucsuJ_gy1rDkTGjkw5nUmM3a6-ejc0mw564HpMRfqbrldL1UbwZQsv35CVBvpOAS4u7s47-eyKck9SER06xTHi6dwiWJfQGS1eECbWZEeeBmBge3zvLManYPehJ__yS2mMAwcILVnmX6NKvey-GxdU2kGAUBlxutmehRqUCR1f7zXJSpKy_T5__aMmX3a4U5WA6QUJCRuf5lJcs8k4fJl6m1PJJ68P26JDczs142SprbSnyaIAGQcdgd3zUGfewjwc0elhxA7dZcw_WOV_6CkTD_v-XcLUM0phoE-LYa3cifSk8ecKYmDW6Tj2yyf1wcNA3VupNVylfMHCsb_fY9SQ7JaIyq-8JjL16WynF-UgvaW-OKWyiNxJna5t37YgJr3QYFxOIGORQ8ValhgF7jZLX3JW0j572Gp77Z9a9_NeZSYmIsZclA1-Pr8tpcamz46U_8p8W6Y7l9S1Bmx3RAJCITLjX442GfI5wqfohuvrOkI07bLWtRKYOr_WPbfLR38_0pcgzQ2EB36XTEGt5hJ-sLn9BYZnK8vPW9FCSg3rJTAKxOKqrn5wc9hOkZzAoo&amp;v=404&amp;rt=3"
                                            style="">
                                    </div>
                                </li>
                                <li class="gl-item gl-item-presell" data-sku="100004401679" data-spu="100007411764"
                                    data-pid="100007411764">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="【5G旗舰新品，9月9日0点再次开售！白条12期免息】5G全网通，骁龙855Plus，4800万AI三摄，44W闪充！iQOO至高优惠500，速抢！"
                                                href="//item.jd.com/100004401679.html"
                                                onclick="searchlog(1,100004401679,24,2,'','flagsClk=1631589000')">
                                                <img width="220" height="220" class="err-product" data-img="1"
                                                    source-data-lazy-img=""
                                                    data-lazy-img="//img14.360buyimg.com/n7/jfs/t1/40810/16/12524/254867/5d5e47a5E030ba9fd/9947efb5297ae4d1.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000085868" data-presale="1"
                                                class="picon"
                                                style="background:url(//img30.360buyimg.com/jgsq-productsoa/jfs/t1/48070/1/8813/2057/5d636656E10ecba6c/f70d1cd376412832.png) no-repeat 0 0;_background-image:none;_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='//img30.360buyimg.com/jgsq-productsoa/jfs/t1/48070/1/8813/2057/5d636656E10ecba6c/f70d1cd376412832.png',sizingMethod='noscale');"
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="竞速黑"><img data-presale="1" data-sku="100004401679"
                                                                data-img="1"
                                                                data-lazy-img="//img14.360buyimg.com/n9/jfs/t1/40810/16/12524/254867/5d5e47a5E030ba9fd/9947efb5297ae4d1.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100004401679"
                                                data-done="1"><em>￥</em><i>4098.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="【5G旗舰新品，9月9日0点再次开售！白条12期免息】5G全网通，骁龙855Plus，4800万AI三摄，44W闪充！iQOO至高优惠500，速抢！"
                                                href="//item.jd.com/100004401679.html"
                                                onclick="searchlog(1,100004401679,24,1,'','flagsClk=1631589000')">
                                                <em>vivo iQOO Pro 12GB+128GB 竞速黑 高通骁龙855Plus<font class="skcolor_ljg">手机
                                                    </font> 4800万AI三摄 44W超快闪充 5G全网通<font class="skcolor_ljg">手机</font>
                                                    </em>
                                                <i class="promo-words"
                                                    id="J_AD_100004401679">【5G旗舰新品，9月9日0点再次开售！白条12期免息】5G全网通，骁龙855Plus，4800万AI三摄，44W闪充！iQOO至高优惠500，速抢！</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <strong><a id="J_comment_100004401679" target="_blank"
                                                    href="//item.jd.com/100004401679.html#comment"
                                                    onclick="searchlog(1,100004401679,24,3,'','flagsClk=1631589000')">1万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100004401679"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100004401679,24,5,'','flagsClk=1631589000')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="96"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000085868,0,58)"
                                                    href="//mall.jd.com/index-1000085868.html"
                                                    title="vivo京东自营官方旗舰店">vivo京东自营官方旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000085868,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100004401679" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                        </div>
                                        <div id="presale_show_item" class="p-presell-time" data-time="43222">
                                            <i></i><span>预约中</span><em>剩余12时00分22秒</em></div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100005502446" data-spu="100003344497"
                                    data-pid="100003344497">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="【领券再减，白条3期免息，以旧换新满1000再返500】星雾蓝8+256G，搭载90Hz流体屏,2K+超清分辨率猛戳更多精彩！"
                                                href="//item.jd.com/100005502446.html"
                                                onclick="searchlog(1,100005502446,25,2,'','flagsClk=1633686152')">
                                                <img width="220" height="220" class="err-product" data-img="1"
                                                    source-data-lazy-img=""
                                                    data-lazy-img="//img11.360buyimg.com/n7/jfs/t1/40586/1/11155/200870/5d49255fEa7738b29/b3e5895230af9915.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000001947" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="星雾蓝"><img data-presale="" data-sku="100005502446"
                                                                data-img="1"
                                                                data-lazy-img="//img11.360buyimg.com/n9/jfs/t1/40586/1/11155/200870/5d49255fEa7738b29/b3e5895230af9915.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="曜岩灰"><img
                                                                data-presale="" data-sku="100005502420" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img10.360buyimg.com/n9/jfs/t1/62996/6/6477/112584/5d4925daE990987f2/3abeaf0a55de1fd6.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="皓月金"><img
                                                                data-presale="" data-sku="100005502444" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img14.360buyimg.com/n9/jfs/t1/47320/13/7033/186884/5d4925b1E3452e53c/a95c82b7c278fe1a.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100005502446"
                                                data-done="1"><em>￥</em><i>4499.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="【领券再减，白条3期免息，以旧换新满1000再返500】星雾蓝8+256G，搭载90Hz流体屏,2K+超清分辨率猛戳更多精彩！"
                                                href="//item.jd.com/100005502446.html"
                                                onclick="searchlog(1,100005502446,25,1,'','flagsClk=1633686152')">
                                                <em><span class="p-tag" style="background-color:#c81623">京品手机</span>一加
                                                    OnePlus 7 Pro 2K+90Hz 流体屏 骁龙855旗舰 4800万超广角三摄 8GB+256GB 星雾蓝 全面屏拍照游戏
                                                    <font class="skcolor_ljg">手机</font></em>
                                                <i class="promo-words"
                                                    id="J_AD_100005502446">【领券再减，白条3期免息，以旧换新满1000再返500】星雾蓝8+256G，搭载90Hz流体屏,2K+超清分辨率猛戳更多精彩！</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <a target="_blank" href="//paipai.jd.com/pc/list.html?pid=100005502446"
                                                class="spu-link">二手有售</a>
                                            <strong><a id="J_comment_100005502446" target="_blank"
                                                    href="//item.jd.com/100005502446.html#comment"
                                                    onclick="searchlog(1,100005502446,25,3,'','flagsClk=1633686152')">26万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100005502446"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100005502446,25,5,'','flagsClk=1633686152')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="95"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000001947,0,58)"
                                                    href="//mall.jd.com/index-1000001947.html"
                                                    title="一加手机京东自营官方旗舰店">一加手机京东自营官方旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000001947,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100005502446" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                            <i class="goods-icons3 J-picon-tips J-picon-fix" data-tips="该商品是当季新品">新品</i>
                                            <i class="goods-icons4 J-picon-tips" data-tips="本商品可领用优惠券">券980-50</i>
                                        </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100005088702" data-spu="100004245926"
                                    data-pid="100004245926">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank" title="2400万超广角AI三摄,AI智慧防抖,GPUTurbo2.0；畅享10P预售送大额礼品卡》"
                                                href="//item.jd.com/100005088702.html"
                                                onclick="searchlog(1,100005088702,26,2,'','flagsClk=1631589000')">
                                                <img width="220" height="220" class="err-product" data-img="1"
                                                    source-data-lazy-img=""
                                                    data-lazy-img="//img12.360buyimg.com/n7/jfs/t1/24205/2/14862/179077/5cb6d175E92733807/46e7ace99f41dd41.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000004259" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="幻夜黑"><img data-presale="" data-sku="100005088702"
                                                                data-img="1"
                                                                data-lazy-img="//img12.360buyimg.com/n9/jfs/t1/24205/2/14862/179077/5cb6d175E92733807/46e7ace99f41dd41.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="极光蓝"><img
                                                                data-presale="" data-sku="100005088704" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img14.360buyimg.com/n9/jfs/t1/31642/40/12219/181658/5cb6d0faE26041b4a/f4a0e10a2427b4b1.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="珊瑚红"><img
                                                                data-presale="" data-sku="100005088680" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img10.360buyimg.com/n9/jfs/t1/34888/34/2807/172159/5cb6d0b6Ecce40e87/aa761e9996658177.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100005088702"
                                                data-done="1"><em>￥</em><i>1299.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank" title="2400万超广角AI三摄,AI智慧防抖,GPUTurbo2.0；畅享10P预售送大额礼品卡》"
                                                href="//item.jd.com/100005088702.html"
                                                onclick="searchlog(1,100005088702,26,1,'','flagsClk=1631589000')">
                                                <em>华为 HUAWEI 畅享 9S 6GB+64GB 幻夜黑 全网通 2400万超广角三摄珍珠屏大存储 移动联通电信4G<font
                                                        class="skcolor_ljg">手机</font> 双卡双待</em>
                                                <i class="promo-words"
                                                    id="J_AD_100005088702">2400万超广角AI三摄,AI智慧防抖,GPUTurbo2.0；畅享10P预售送大额礼品卡》</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <strong><a id="J_comment_100005088702" target="_blank"
                                                    href="//item.jd.com/100005088702.html#comment"
                                                    onclick="searchlog(1,100005088702,26,3,'','flagsClk=1631589000')">24万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100005088702"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100005088702,26,5,'','flagsClk=1631589000')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="96"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000004259,0,58)"
                                                    href="//mall.jd.com/index-1000004259.html"
                                                    title="华为京东自营官方旗舰店">华为京东自营官方旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000004259,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100005088702" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                            <i class="goods-icons4 J-picon-tips"
                                                style="border-color:#4d88ff;color:#4d88ff;" data-idx="1"
                                                data-tips="品质服务，放心购物">放心购</i>
                                            <i class="goods-icons4 J-picon-tips" data-tips="购买本商品送赠品">赠</i> </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100000911700" data-spu="100000773875"
                                    data-pid="100000773875">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="【9.8限时直降100+下单立减100，到手价948】骁龙670AIE处理器，指纹人脸双解锁，4D游戏震撼体验！Z5新品上市，速抢！"
                                                href="//item.jd.com/100000911700.html"
                                                onclick="searchlog(1,100000911700,27,2,'','flagsClk=1631589000')">
                                                <img width="220" height="220" class="err-product" data-img="1"
                                                    source-data-lazy-img=""
                                                    data-lazy-img="//img10.360buyimg.com/n7/jfs/t25690/249/2278881791/224805/20c2401e/5bc832ffN19011cce.jpg">
                                            </a>
                                            <div id="belt" class="p-act-sign J_belt_box sign-2017083101"
                                                style="background-image: url('https://img30.360buyimg.com/jgsq-productsoa/jfs/t16951/182/417192066/4728/322919ee/5a754dd7N2f64533f.png');">
                                                <div class="sign-title ac">PLUSDAY年度盛典
                                                    <span class="sign-date">(9.5-9.8)</span>
                                                </div>
                                            </div>
                                            <div data-lease="" data-catid="655" data-venid="1000085868" data-presale=""
                                                class="picon"
                                                style="background:url(//img30.360buyimg.com/jgsq-productsoa/jfs/t1/48070/1/8813/2057/5d636656E10ecba6c/f70d1cd376412832.png) no-repeat 0 0;_background-image:none;_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='//img30.360buyimg.com/jgsq-productsoa/jfs/t1/48070/1/8813/2057/5d636656E10ecba6c/f70d1cd376412832.png',sizingMethod='noscale');"
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="极光蓝"><img data-presale="" data-sku="100000911700"
                                                                data-img="1"
                                                                data-lazy-img="//img10.360buyimg.com/n9/jfs/t25690/249/2278881791/224805/20c2401e/5bc832ffN19011cce.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="星夜黑"><img
                                                                data-presale="" data-sku="100000773875" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img10.360buyimg.com/n9/jfs/t27298/341/1418027848/298328/b12ec565/5bc83164N34528e6e.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="梦幻粉"><img
                                                                data-presale="" data-sku="100000773887" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img12.360buyimg.com/n9/jfs/t26653/114/1434670919/190123/1e51d86f/5bc83394Ndc90e065.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="翡翠色"><img
                                                                data-presale="" data-sku="100003666224" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img14.360buyimg.com/n9/jfs/t1/32758/27/3607/365936/5c76638fEe3a70c6e/03640d9b2cb6ba03.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100000911700"
                                                data-done="1"><em>￥</em><i>1048.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="【9.8限时直降100+下单立减100，到手价948】骁龙670AIE处理器，指纹人脸双解锁，4D游戏震撼体验！Z5新品上市，速抢！"
                                                href="//item.jd.com/100000911700.html"
                                                onclick="searchlog(1,100000911700,27,1,'','flagsClk=1631589000')">
                                                <em><img class="p-tag3"
                                                        src="//img14.360buyimg.com/uba/jfs/t6919/268/501386350/1257/92e5fb39/5976fcf9Nd915775f.png">vivo
                                                    Z3 4GB+64GB 极光蓝 骁龙670处理器 全面屏游戏智能<font class="skcolor_ljg">手机</font>
                                                    移动联通电信全网通4G<font class="skcolor_ljg">手机</font></em>
                                                <i class="promo-words"
                                                    id="J_AD_100000911700">【9.8限时直降100+下单立减100，到手价948】骁龙670AIE处理器，指纹人脸双解锁，4D游戏震撼体验！Z5新品上市，速抢！</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <a target="_blank" href="//paipai.jd.com/pc/list.html?pid=100000911700"
                                                class="spu-link">二手有售</a>
                                            <strong><a id="J_comment_100000911700" target="_blank"
                                                    href="//item.jd.com/100000911700.html#comment"
                                                    onclick="searchlog(1,100000911700,27,3,'','flagsClk=1631589000')">60万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100000911700"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100000911700,27,5,'','flagsClk=1631589000')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="98"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000085868,0,58)"
                                                    href="//mall.jd.com/index-1000085868.html"
                                                    title="vivo京东自营官方旗舰店">vivo京东自营官方旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000085868,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100000911700" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                            <i class="goods-icons4 J-picon-tips"
                                                style="border-color:#4d88ff;color:#4d88ff;" data-idx="1"
                                                data-tips="品质服务，放心购物">放心购</i>
                                            <i class="goods-icons4 J-picon-tips" data-tips="本商品参与满减促销">满800-100</i>
                                        </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100000287113" data-spu="100000287145"
                                    data-pid="100000287145">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="【iPhone焕新季，抢券立减400元】6.5英寸大屏旗舰，A12仿生芯片流畅体验，支持双卡！更多优惠点击！"
                                                href="//item.jd.com/100000287113.html"
                                                onclick="searchlog(1,100000287113,28,2,'','flagsClk=1614811784')">
                                                <img width="220" height="220" class="err-product" data-img="1"
                                                    source-data-lazy-img=""
                                                    data-lazy-img="//img13.360buyimg.com/n7/jfs/t1/3/15/4536/138660/5b997bf8Ed72ebce7/819dcf182d743897.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000000127" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="深空灰色"><img data-presale="" data-sku="100000287113"
                                                                data-img="1"
                                                                data-lazy-img="//img13.360buyimg.com/n9/jfs/t1/3/15/4536/138660/5b997bf8Ed72ebce7/819dcf182d743897.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="银色"><img
                                                                data-presale="" data-sku="100000177784" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img14.360buyimg.com/n9/jfs/t1/4860/25/3563/134740/5b997bffEeb5b5613/0d8dfde177089495.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                    <li class="ps-item"><a href="javascript:;" title="金色"><img
                                                                data-presale="" data-sku="100000287117" data-img="1"
                                                                width="25" height="25"
                                                                data-lazy-img="//img12.360buyimg.com/n9/jfs/t1/4528/10/3590/153299/5b997bf5E4a513949/45ab3dd6c35d981b.jpg"
                                                                class="err-product" data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100000287113"
                                                data-done="1"><em>￥</em><i>8999.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="【iPhone焕新季，抢券立减400元】6.5英寸大屏旗舰，A12仿生芯片流畅体验，支持双卡！更多优惠点击！"
                                                href="//item.jd.com/100000287113.html"
                                                onclick="searchlog(1,100000287113,28,1,'','flagsClk=1614811784')">
                                                <em>Apple iPhone XS Max (A2104) 256GB 深空灰色 移动联通电信4G<font
                                                        class="skcolor_ljg">手机</font> 双卡双待</em>
                                                <i class="promo-words"
                                                    id="J_AD_100000287113">【iPhone焕新季，抢券立减400元】6.5英寸大屏旗舰，A12仿生芯片流畅体验，支持双卡！更多优惠点击！</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <a target="_blank" href="//paipai.jd.com/pc/list.html?pid=100000287113"
                                                class="spu-link">二手有售</a>
                                            <strong><a id="J_comment_100000287113" target="_blank"
                                                    href="//item.jd.com/100000287113.html#comment"
                                                    onclick="searchlog(1,100000287113,28,3,'','flagsClk=1614811784')">83万+</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100000287113"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100000287113,28,5,'','flagsClk=1614811784')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="5" data-reputation="98"
                                            data-done="1">
                                            <span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname"
                                                    onclick="searchlog(1,1000000127,0,58)"
                                                    href="//mall.jd.com/index-1000000127.html"
                                                    title="Apple产品京东自营旗舰店">Apple产品京东自营旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000000127,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100000287113" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i>
                                            <i class="goods-icons4 J-picon-tips" data-tips="本商品可领用优惠券">券980-60</i><i
                                                class="goods-icons4 J-picon-tips" data-tips="购买本商品送赠品">赠</i> </div>
                                    </div>
                                </li>
                                <li class="gl-item" data-sku="100007381674" data-spu="100007381634"
                                    data-pid="100007381634">
                                    <div class="gl-i-wrap">
                                        <div class="p-img">
                                            <a target="_blank"
                                                title="【5G先锋】骁龙855、X50、新一代智能S-Pen、后置四摄、视频实时虚化、变焦麦克风、防抖拍摄了解更多产品》"
                                                href="https://item.jd.com/100007381674.html"
                                                onclick="searchlog(1,100007381674,29,2,'','adwClk=1');searchAdvPointReport('https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDczODE2NzQuaHRtbA&amp;log=VuqDEEucP0LvlsuIkout6t92HzcQTX629uB8BI1cCzbZDWzAg50W154uWGwdrfDhYBX7qi55WOoIyBZX_8pdabPFGPNhaSHXAW0iIwyeRq0jaXj_FqVrPxzdn1sA8B9jqezwb7m-ZXd_pIx2npcCtLan9QCt6YqAn3QBNgf09pW8kqjLN1uXHKlMf_FDNnuqNTkcjfrVZkc5pLSP2XRazFJ7oYmWsysppePOOEDG6PRhht7-K-tJikM4f0QT6WIxvdq-UXRnnqF-hVKk_P0QnMAZdT1nXVjD59FVD578NZq6qF1l8nEMIcy21KXbDlFSXG0x9HyPre7WGvbnTiHXW-ORd5f6A2O_qrvRvKa8aM8y1Pa48xHWzd9DiQDqqGYazROGHzD-mBqU2V9tgQp6zKFw6TFXiQEjEP-cHl03QoQ5aNsEE7j4UtEq3Q3JeGlsdDffMFWj9-XkhGGn5nEw40akjOGuQ4cdRWgSBDGljOsD_Kw8ONi7aTSLIW3E9mxHmCik3tYTgdVf6XApFZcb8BB726JsHrU0fLEr5uC-4uaV875uw7GSt3OuOcFAfnxYdPYGG8uYLnJUVLuoIIfMyuc0zINSAM0QQ_rGKSnhryRa4GDy1pmmfqzXEXFJQmFSDKMUtWSCeqno4x6qrXLtAYuIhLsRcrSMAj1JIbgr-0gu5wHAJto0yFK2AUDJStqvR0IBYTG_P-w4cjrAxIstYhIzQrd98pfb4mxaw0t7dC4&amp;v=404&amp;clicktype=1');">
                                                <img width="220" height="220" class="err-product" data-img="1"
                                                    source-data-lazy-img=""
                                                    data-lazy-img="//img14.360buyimg.com/n7/jfs/t1/57811/13/7162/189455/5d4d208bE358cb1f4/8484d366e37ae548.jpg">
                                            </a>
                                            <div data-lease="" data-catid="655" data-venid="1000003443" data-presale=""
                                                data-done="1"></div>
                                        </div>
                                        <div class="p-scroll">
                                            <span class="ps-prev">&lt;</span>
                                            <span class="ps-next">&gt;</span>
                                            <div class="ps-wrap">
                                                <ul class="ps-main">
                                                    <li class="ps-item"><a href="javascript:;" class="curr"
                                                            title="莫奈彩"><img
                                                                data-url="https://item.jd.com/100007381674.html"
                                                                data-presale="" data-sku="100007381674" data-img="1"
                                                                data-lazy-img="//img14.360buyimg.com/n9/jfs/t1/57811/13/7162/189455/5d4d208bE358cb1f4/8484d366e37ae548.jpg"
                                                                class="err-product" width="25" height="25"
                                                                data-done="1"></a></li>
                                                </ul>
                                            </div>
                                        </div>
                                        <div class="p-price">
                                            <strong class="J_100007381674"
                                                data-done="1"><em>￥</em><i>7999.00</i></strong> </div>
                                        <div class="p-name p-name-type-2">
                                            <a target="_blank"
                                                title="【5G先锋】骁龙855、X50、新一代智能S-Pen、后置四摄、视频实时虚化、变焦麦克风、防抖拍摄了解更多产品》"
                                                href="https://item.jd.com/100007381674.html"
                                                onclick="searchlog(1,100007381674,29,1,'','adwClk=1');searchAdvPointReport('https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDczODE2NzQuaHRtbA&amp;log=VuqDEEucP0LvlsuIkout6t92HzcQTX629uB8BI1cCzbZDWzAg50W154uWGwdrfDhYBX7qi55WOoIyBZX_8pdabPFGPNhaSHXAW0iIwyeRq0jaXj_FqVrPxzdn1sA8B9jqezwb7m-ZXd_pIx2npcCtLan9QCt6YqAn3QBNgf09pW8kqjLN1uXHKlMf_FDNnuqNTkcjfrVZkc5pLSP2XRazFJ7oYmWsysppePOOEDG6PRhht7-K-tJikM4f0QT6WIxvdq-UXRnnqF-hVKk_P0QnMAZdT1nXVjD59FVD578NZq6qF1l8nEMIcy21KXbDlFSXG0x9HyPre7WGvbnTiHXW-ORd5f6A2O_qrvRvKa8aM8y1Pa48xHWzd9DiQDqqGYazROGHzD-mBqU2V9tgQp6zKFw6TFXiQEjEP-cHl03QoQ5aNsEE7j4UtEq3Q3JeGlsdDffMFWj9-XkhGGn5nEw40akjOGuQ4cdRWgSBDGljOsD_Kw8ONi7aTSLIW3E9mxHmCik3tYTgdVf6XApFZcb8BB726JsHrU0fLEr5uC-4uaV875uw7GSt3OuOcFAfnxYdPYGG8uYLnJUVLuoIIfMyuc0zINSAM0QQ_rGKSnhryRa4GDy1pmmfqzXEXFJQmFSDKMUtWSCeqno4x6qrXLtAYuIhLsRcrSMAj1JIbgr-0gu5wHAJto0yFK2AUDJStqvR0IBYTG_P-w4cjrAxIstYhIzQrd98pfb4mxaw0t7dC4&amp;v=404&amp;clicktype=1');">
                                                <em>三星 Galaxy Note10+5G 12GB+256GB 莫奈彩 （SM-N9760）5G<font
                                                        class="skcolor_ljg">手机</font> 骁龙855 智慧型S Pen 双卡双待 游戏<font
                                                        class="skcolor_ljg">手机</font></em>
                                                <i class="promo-words"
                                                    id="J_AD_100007381674">【5G先锋】骁龙855、X50、新一代智能S-Pen、后置四摄、视频实时虚化、变焦麦克风、防抖拍摄了解更多产品》</i>
                                            </a>
                                        </div>
                                        <div class="p-commit" data-done="1">
                                            <strong><a id="J_comment_100007381674" target="_blank"
                                                    href="https://item.jd.com/100007381674.html"
                                                    onclick="searchlog(1,100007381674,29,3,'','adwClk=1')">0</a>条评价</strong>
                                        </div>
                                        <div class="p-focus"><a class="J_focus" data-sku="100007381674"
                                                href="javascript:;" title="点击关注"
                                                onclick="searchlog(1,100007381674,29,5,'','adwClk=1')"><i></i>关注</a>
                                        </div>
                                        <div class="p-shop" data-selfware="1" data-score="0" data-reputation=""
                                            data-verderid="1000003443" data-done="1"><span class="J_im_icon"><a
                                                    target="_blank" onclick="searchlog(1,1000003443,0,58)"
                                                    href="//mall.jd.com/index-1000003443.html"
                                                    title="三星手机京东自营官方旗舰店">三星手机京东自营官方旗舰店</a><b class="im-02"
                                                    style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;"
                                                    title="联系客服" onclick="searchlog(1,1000003443,0,61)"></b></span>
                                        </div>
                                        <div class="p-icons" id="J_pro_100007381674" data-done="1">
                                            <i class="goods-icons J-picon-tips J-picon-fix" data-idx="1"
                                                data-tips="京东自营，品质保障">自营</i><i class="goods-icons4 J-picon-tips"
                                                data-tips="购买本商品送赠品">赠</i>
                                        </div>
                                        <span class="p-promo-flag">广告</span>

                                        <img source-data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=VuqDEEucP0LvlsuIkout6t92HzcQTX629uB8BI1cCzbZDWzAg50W154uWGwdrfDhYBX7qi55WOoIyBZX_8pdabPFGPNhaSHXAW0iIwyeRq0jaXj_FqVrPxzdn1sA8B9jqezwb7m-ZXd_pIx2npcCtLan9QCt6YqAn3QBNgf09pW8kqjLN1uXHKlMf_FDNnuqNTkcjfrVZkc5pLSP2XRazFJ7oYmWsysppePOOEDG6PTH6ESZslqepwvqczRYlX2MQ4vaLRxKxNakHgrCVxzMcSoRqezWcWZwdH_teLzBJWZvRCJRVEpdamXH3l2Xtj9HOeyRO_Gk6AKEIYJrIkWtHxSBfg8bhb0yZpjY3dWPG8GeYSWRGUZSLUw6y9IBnXaHK4U-zZV094OgFpfWa-crir2uGSWf6-rX2J0VXP47jAVPNv_mTqzVwxDikIT1EgV_6LpFjKDSInM-KRXgppBO__YrMt1mtTHV_mvi5imKrux1-HUq6kQ31YN82MLn7KyGGc22BCc2m5lAH8GT5Jb5ANGI84-iS-MR32QtvonlqKqxKG1dNiWtMr8kqDR9ha3xBw1vhlzRMxKeWUtI9SxCsfKwcTKd8S6Adlk5yUlH5XqmpRWuGi2IlnYqZLZaSQg_0B4f8PdaHg8d13uySaY4_z15uL7iX7HjnzFiUhfTaFc6TL9YJrp6M4IBj2tgxbhaOTVR31-LwdbCZ8vBUIKxSLLvBitxgn_H5CwhCrAKT4w&amp;v=404&amp;rt=3"
                                            style="">
                                    </div>
                                </li>
                            </ul><span class="clr"></span>
                        </div>
                        <div id="J_scroll_loading" class="notice-loading-more"><span>正在加载中，请稍后~~</span></div>
                        <div class="page clearfix">
                            <div id="J_bottomPage" class="p-wrap"><span class="p-num"><a
                                        class="pn-prev disabled"><i>&lt;</i><em>上一页</em></a><a href="javascript:;"
                                        class="curr">1</a><a onclick="SEARCH.page(3, true)" href="javascript:;">2</a><a
                                        onclick="SEARCH.page(5, true)" href="javascript:;">3</a><a
                                        onclick="SEARCH.page(7, true)" href="javascript:;">4</a><a
                                        onclick="SEARCH.page(9, true)" href="javascript:;">5</a><a
                                        onclick="SEARCH.page(11, true)" href="javascript:;">6</a><a
                                        onclick="SEARCH.page(13, true)" href="javascript:;">7</a><b
                                        class="pn-break">...</b><a class="pn-next" onclick="SEARCH.page(3, true)"
                                        href="javascript:;"
                                        title="使用方向键右键也可翻到下一页哦！"><em>下一页</em><i>&gt;</i></a></span><span
                                    class="p-skip"><em>共<b>97</b>页&nbsp;&nbsp;到第</em><input class="input-txt"
                                        type="text" value="1"
                                        onkeydown="javascript:if(event.keyCode==13){SEARCH.page_jump(97,1);return false;}"><em>页</em><a
                                        class="btn btn-default" onclick="SEARCH.page_jump(97,1)"
                                        href="javascript:;">确定</a></span></div>
                        </div>
                    </div>
                </div>
                <div class="m-aside">
                    <div class="aside-bar">
                        <div id="J_promGoodsWrap_291" class="ab-goods u-ad-wrap" style="display: block;"
                            data-lazy-img-install="1">
                            <span class="u-ad"></span>
                            <div class="mt">
                                <h3>商品精选</h3>
                            </div>
                            <div class="mc">
                                <ul class="clearfix" data-x="ab">
                                    <li onclick="searchlog(1,8348849, 0, 81)"><img data-lazy-advertisement="done"
                                            src="//misc.360buyimg.com/lib/img/e/blank.gif" class="err-poster"
                                            style="display: none;">
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/8348849.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS84MzQ4ODQ5Lmh0bWw&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjleSGSs8aPsBDq-6qMBgWT6NAE3H66_81dBnP8L-hXIpUUqAkz-wM6EszTFg5GmmjKQ5WSWa-XXGHgafNAwjajaayDgOuMf2753rjTWoA2RS_HZdjU8BEcv-7z58-31cGQQyXpUOyuy2L7Afmk9E4GnOp-Bo2ye5fxBbm898Znx9QZOopsdjvNxjky0X3OtvInmtWEI_j2qFW1P_4kcXUgpUr8r6ratnXLMncBeOZAA_YWN9Mzt8iivomyxQj95gPreBse-4VKRipB9VgC7dqB0v_wxD-TIiQoPNiTqn2z46TbxPQ6A1Vlp7mSERuGJOIeyCky446VV4gdheIB03ezz8PkauYai6NngbzJUtZaTAqGaGn_j_TMBxynr0L9t-fMzhzvtaYP04WQGf9SGK01FqJgFMUajVM4H2gPRwbSXaf3xGxSV7xyp9-_QCq9VaoujUwmeKieBJXrJPk79gIhQqSmMI2yLXB0s1KwJ2bbJryUFyb4ZltWTsIELgj4StciF1lV_QioWDhc-LEVjw4VEwUCfy9hnQbSuY1UtZsMGXDt6jQPcNZqayJq4-mvlWwm85H11gUjF393njIhHPuGbFIUq7xz0uvvNg3bjFfkaU1_jr0oGHz3nKTEaWrKdIPfaF-NgkIRFxS6lQEBLIQiv9-Q0AXgFzOqgBGjn7d1kzOA&amp;v=404&amp;clicktype=1">
                                            <div class="p-img"> <img width="160" height="160" data-img="1"
                                                    src="//img14.360buyimg.com/n2/jfs/t21949/69/2044466680/171928/5301291c/5b45e393N344190f3.jpg"
                                                    class="err-product"> </div>
                                        </div>
                                        <div class="p-price"> <strong><em>¥</em><i
                                                    class="J-prom-p-8348849">499.00</i></strong> </div>
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/8348849.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS84MzQ4ODQ5Lmh0bWw&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjleSGSs8aPsBDq-6qMBgWT6NAE3H66_81dBnP8L-hXIpUUqAkz-wM6EszTFg5GmmjKQ5WSWa-XXGHgafNAwjajaayDgOuMf2753rjTWoA2RS_HZdjU8BEcv-7z58-31cGQQyXpUOyuy2L7Afmk9E4GnOp-Bo2ye5fxBbm898Znx9QZOopsdjvNxjky0X3OtvInmtWEI_j2qFW1P_4kcXUgpUr8r6ratnXLMncBeOZAA_YWN9Mzt8iivomyxQj95gPreBse-4VKRipB9VgC7dqB0v_wxD-TIiQoPNiTqn2z46TbxPQ6A1Vlp7mSERuGJOIeyCky446VV4gdheIB03ezz8PkauYai6NngbzJUtZaTAqGaGn_j_TMBxynr0L9t-fMzhzvtaYP04WQGf9SGK01FqJgFMUajVM4H2gPRwbSXaf3xGxSV7xyp9-_QCq9VaoujUwmeKieBJXrJPk79gIhQqSmMI2yLXB0s1KwJ2bbJryUFyb4ZltWTsIELgj4StciF1lV_QioWDhc-LEVjw4VEwUCfy9hnQbSuY1UtZsMGXDt6jQPcNZqayJq4-mvlWwm85H11gUjF393njIhHPuGbFIUq7xz0uvvNg3bjFfkaU1_jr0oGHz3nKTEaWrKdIPfaF-NgkIRFxS6lQEBLIQiv9-Q0AXgFzOqgBGjn7d1kzOA&amp;v=404&amp;clicktype=1">
                                            <div class="p-name"> <em>诺基亚 NOKIA 8110 移动联通4G<font class="skcolor_ljg">手机
                                                    </font> 黄色 直板按键 双卡双待 经典复刻 炫酷滑盖 4G热点备用功能机</em> </div>
                                        </div>
                                        <div class="p-comm " style="padding:8px 10px 0"> 已有<span style="color:#005aa0"
                                                class="J-p-comm-ss-8348849">5.3万+</span>人评价 </div>
                                    </li>
                                    <li onclick="searchlog(1,100007381674, 1, 81)"><img data-lazy-advertisement="done"
                                            src="//misc.360buyimg.com/lib/img/e/blank.gif" class="err-poster"
                                            style="display: none;">
                                        <div class="p-client-click"
                                            data-clickurl="https://item.jd.com/100007381674.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDczODE2NzQuaHRtbA&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjldhg9-vM3169JzCYjMXvFTiyixJfOl2ufS5KLWQ5fPz3ll92db9-1pqMZr6yRx9B-JgrI--GwxNhf3bChI3b0Ong64dCPbjeb4_va38uP2rEs3nmiYJn8jykP9cTaExiGDVLShATMsW2jPeweZxtrtf2XvjbKrquFXGQsoqiZQp2bH77GdaNo_s272v6qw7e0Fe0d_nh4nbXPsw3h_HTYvTa12h6T-9PsnE-4OJUAZ9OhR3KbwC2KMqHTs0T_M0f7D0duizN3Z19YWgmzLR8MN5w2YrlWlEspb48hvw2yRCN417yTtei7Xsj9-QWep7lWvZBXLQ5uCHrU2W1UZcN7ysCaDIBo0xAAXpjHDmiTUl11PSv_Sl-IV_tY_q_9LTlBjextDYDGjWDuqZy5QT47HiYipEKr_-P2UrujkdqGJ3TBJbyxzV_3f_slXtDV4GDaRMnmXCBX-yMAFYdEvJcu8_elnJZ_XEJlelMOxZB565s6exaJQ6xoyH9za153ebNhAO4Ql95WAufpxfylYGaUlXTa03IfM2KcshVx1TG4FEJL9_STsV5DryevYkN2pE_70DaGj4K5TdXwNivFzqhR68n71Nhh-Bo2NCLBNcihSJP5AV7EdXP8rIRcJwKLXtV6DJIk1dJ9utsXBulhibq9M_ZltePftS7TcagJuQ5Wu63rrwGYesZ4al4lmZRvtqHuA&amp;v=404&amp;clicktype=1">
                                            <div class="p-img"> <img width="160" height="160" data-img="1"
                                                    src="//img14.360buyimg.com/n2/jfs/t1/80038/3/8539/40840/5d67b4a2E4902bffe/a91b0eddcede1bc8.jpg"
                                                    class="err-product"> </div>
                                        </div>
                                        <div class="p-price"> <strong><em>¥</em><i
                                                    class="J-prom-p-100007381674">7999.00</i></strong> </div>
                                        <div class="p-client-click"
                                            data-clickurl="https://item.jd.com/100007381674.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDczODE2NzQuaHRtbA&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjldhg9-vM3169JzCYjMXvFTiyixJfOl2ufS5KLWQ5fPz3ll92db9-1pqMZr6yRx9B-JgrI--GwxNhf3bChI3b0Ong64dCPbjeb4_va38uP2rEs3nmiYJn8jykP9cTaExiGDVLShATMsW2jPeweZxtrtf2XvjbKrquFXGQsoqiZQp2bH77GdaNo_s272v6qw7e0Fe0d_nh4nbXPsw3h_HTYvTa12h6T-9PsnE-4OJUAZ9OhR3KbwC2KMqHTs0T_M0f7D0duizN3Z19YWgmzLR8MN5w2YrlWlEspb48hvw2yRCN417yTtei7Xsj9-QWep7lWvZBXLQ5uCHrU2W1UZcN7ysCaDIBo0xAAXpjHDmiTUl11PSv_Sl-IV_tY_q_9LTlBjextDYDGjWDuqZy5QT47HiYipEKr_-P2UrujkdqGJ3TBJbyxzV_3f_slXtDV4GDaRMnmXCBX-yMAFYdEvJcu8_elnJZ_XEJlelMOxZB565s6exaJQ6xoyH9za153ebNhAO4Ql95WAufpxfylYGaUlXTa03IfM2KcshVx1TG4FEJL9_STsV5DryevYkN2pE_70DaGj4K5TdXwNivFzqhR68n71Nhh-Bo2NCLBNcihSJP5AV7EdXP8rIRcJwKLXtV6DJIk1dJ9utsXBulhibq9M_ZltePftS7TcagJuQ5Wu63rrwGYesZ4al4lmZRvtqHuA&amp;v=404&amp;clicktype=1">
                                            <div class="p-name"> <em>三星 Galaxy Note10+5G 12GB+256GB 莫奈彩 （SM-N9760）5G
                                                    <font class="skcolor_ljg">手机</font> 骁龙855 智慧型S Pen 双卡双待 游戏<font
                                                        class="skcolor_ljg">手机</font></em> </div>
                                        </div>
                                        <div class="p-comm " style="padding:8px 10px 0"> 已有<span style="color:#005aa0"
                                                class="J-p-comm-ss-100007381674">0</span>人评价 </div>
                                    </li>
                                    <li onclick="searchlog(1,55294371632, 2, 81)"><img data-lazy-advertisement="done"
                                            src="//misc.360buyimg.com/lib/img/e/blank.gif" class="err-poster"
                                            style="display: none;">
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/55294371632.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS81NTI5NDM3MTYzMi5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlf_unSRKe8plaVIZ0DkddKAyUo2brr90jiSL_71TJAOLESFUP2NsckA1I4Vq_Isu-SL5jQlMjseJnkuaBH4fwxM3tU5PR-qnLQKftCxG4oYZtctN1NvsoyMTh3jzBJkdMglgMWYeso7tMKleXywLbmutKlAYGh5lWQN07U1l5L3CaST_iM-AoS0yjb1SbTh31i7wN_byJEXGRGhTj4tRPr9_U7prvgs0hFMWOm5d865zbNbFIwd9q3qW9ojc9RWd8--FpFFqHCCQ2dmTEm-JaIpmSYhfG-HWfsE6KOA-3DE5r13mfuP65sMgUDGHMmxkwS0JxmYJM17VJLsNB0KnV2NGOiYEpyx4SMxRHccL_xmrjQkH8q5JBX3gnSY2-haWu8br4ttJaLZWO2ChgQDrUNUc_MlFYGB43trc9uDr5oCo2A3CmTFFa7DV6TQyn-PQQQGqLcecCKpZ8OR0zOr0HsC6M0naHqcL3XW6vgLGVt6hBm5GFZpBGIBHH0U0yiRlp_r2rHkwQBrJ6mgfXmmsksT1n3_vlvQyAc8Uzw0nsMVqQwmDQe6_rcuPNoV4NWBCSV315kpulglxUTR8YL1Snp8R09i1RKvgxce3TZoqX1Ptt5JkpJVd_x9ZhtYaPYmvD4LCRsrwOfCpEb4p_-_xitJD-RXIGzcHPW0Q7EWmC6UQA&amp;v=404&amp;clicktype=1">
                                            <div class="p-img"> <img width="160" height="160" data-img="1"
                                                    src="//img12.360buyimg.com/n2/jfs/t1/78126/2/8662/477756/5d6b2142E06b09b3c/1e92f0199b138228.png"
                                                    class="err-product"> </div>
                                        </div>
                                        <div class="p-price"> <strong><em>¥</em><i
                                                    class="J-prom-p-55294371632">99999.00</i></strong> </div>
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/55294371632.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS81NTI5NDM3MTYzMi5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlf_unSRKe8plaVIZ0DkddKAyUo2brr90jiSL_71TJAOLESFUP2NsckA1I4Vq_Isu-SL5jQlMjseJnkuaBH4fwxM3tU5PR-qnLQKftCxG4oYZtctN1NvsoyMTh3jzBJkdMglgMWYeso7tMKleXywLbmutKlAYGh5lWQN07U1l5L3CaST_iM-AoS0yjb1SbTh31i7wN_byJEXGRGhTj4tRPr9_U7prvgs0hFMWOm5d865zbNbFIwd9q3qW9ojc9RWd8--FpFFqHCCQ2dmTEm-JaIpmSYhfG-HWfsE6KOA-3DE5r13mfuP65sMgUDGHMmxkwS0JxmYJM17VJLsNB0KnV2NGOiYEpyx4SMxRHccL_xmrjQkH8q5JBX3gnSY2-haWu8br4ttJaLZWO2ChgQDrUNUc_MlFYGB43trc9uDr5oCo2A3CmTFFa7DV6TQyn-PQQQGqLcecCKpZ8OR0zOr0HsC6M0naHqcL3XW6vgLGVt6hBm5GFZpBGIBHH0U0yiRlp_r2rHkwQBrJ6mgfXmmsksT1n3_vlvQyAc8Uzw0nsMVqQwmDQe6_rcuPNoV4NWBCSV315kpulglxUTR8YL1Snp8R09i1RKvgxce3TZoqX1Ptt5JkpJVd_x9ZhtYaPYmvD4LCRsrwOfCpEb4p_-_xitJD-RXIGzcHPW0Q7EWmC6UQA&amp;v=404&amp;clicktype=1">
                                            <div class="p-name"> <em>【<font class="skcolor_ljg">新品</font>预约抽奖赢免单】OPPO
                                                    Reno2<font class="skcolor_ljg">手机</font> 4800万变焦四摄 视频防抖 6.5英寸护眼全面屏
                                                    薄雾粉 8G+128G</em> </div>
                                        </div>
                                        <div class="p-comm " style="padding:8px 10px 0"> 已有<span style="color:#005aa0"
                                                class="J-p-comm-ss-55294371632">0</span>人评价 </div>
                                    </li>
                                    <li onclick="searchlog(1,46492972183, 3, 81)"><img data-lazy-advertisement="done"
                                            src="//misc.360buyimg.com/lib/img/e/blank.gif" class="err-poster"
                                            style="display: none;">
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/46492972183.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS80NjQ5Mjk3MjE4My5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlcZlsYOeaTFAipmTW8h4h9LKdGNnPU4QZwhnTzEyOiieVxv_bfQeRa4vFfj_9HuSX7sBEbUNkLz_sz8C8yFr7u4Az3q2BNftOxc0f4-3RoppDB0eTblYpAVV5kjHjlu3zFt9fjXly5FgrAQqYqm1dGWOeHFTs42ynnPAz8PsGFb_Vr7JCsMY7IftNH87fSfcMj0re4xAtkI7wOGepzUOID3gQyIC0gQSNG1YYM-jHKerDfznXOZH1uNbY6IMWtF4uym5By-qH-TX31nvCI3TQknAzHcfBONHQ_kOag27Iwl9V_zgpXiuJpsIHYdpUDYA2ecVxkR2hXjHW8SnMSpvI2od7iUt2Tf7hVTesLxjqRG1JKhcIFHGPfFdDQm_sVKcD3834j60xKEbsJ9vERoq7AVAxAprEXVFZ5JijiV4eJOJkH8H2iv7dlGPRJ2SDugdWQhFuIoaIbfWSO14zfdXzt0T5G8pFY40D95Cqdhrzy3c_CxTW2VXle7nO0Aqf-j1J-ATBIu9gmPvritj7I7Wd42NecwbKKIAbMcwlVeIzYFWph916hqUOrk3OOXHCboJjmi5488wVYc3IDcqFHuQV-60l1HBdqiNXI1ZbYqpSAvP9jmka0z1HGkCjsPyrFx4hI-ZQrdGxjvkhqxZcVKNvIP&amp;v=404&amp;clicktype=1">
                                            <div class="p-img"> <img width="160" height="160" data-img="1"
                                                    data-lazy-img="done" class=""
                                                    src="//img13.360buyimg.com/n2/jfs/t1/56865/3/6537/92557/5d416596E7393a49d/0d70821fdf660e0d.jpg">
                                            </div>
                                        </div>
                                        <div class="p-price"> <strong><em>¥</em><i
                                                    class="J-prom-p-46492972183">8999.00</i></strong> </div>
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/46492972183.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS80NjQ5Mjk3MjE4My5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlcZlsYOeaTFAipmTW8h4h9LKdGNnPU4QZwhnTzEyOiieVxv_bfQeRa4vFfj_9HuSX7sBEbUNkLz_sz8C8yFr7u4Az3q2BNftOxc0f4-3RoppDB0eTblYpAVV5kjHjlu3zFt9fjXly5FgrAQqYqm1dGWOeHFTs42ynnPAz8PsGFb_Vr7JCsMY7IftNH87fSfcMj0re4xAtkI7wOGepzUOID3gQyIC0gQSNG1YYM-jHKerDfznXOZH1uNbY6IMWtF4uym5By-qH-TX31nvCI3TQknAzHcfBONHQ_kOag27Iwl9V_zgpXiuJpsIHYdpUDYA2ecVxkR2hXjHW8SnMSpvI2od7iUt2Tf7hVTesLxjqRG1JKhcIFHGPfFdDQm_sVKcD3834j60xKEbsJ9vERoq7AVAxAprEXVFZ5JijiV4eJOJkH8H2iv7dlGPRJ2SDugdWQhFuIoaIbfWSO14zfdXzt0T5G8pFY40D95Cqdhrzy3c_CxTW2VXle7nO0Aqf-j1J-ATBIu9gmPvritj7I7Wd42NecwbKKIAbMcwlVeIzYFWph916hqUOrk3OOXHCboJjmi5488wVYc3IDcqFHuQV-60l1HBdqiNXI1ZbYqpSAvP9jmka0z1HGkCjsPyrFx4hI-ZQrdGxjvkhqxZcVKNvIP&amp;v=404&amp;clicktype=1">
                                            <div class="p-name"> <em>[六期免息]柔宇科技Royole FlexPai柔派/可折叠柔性屏<font
                                                        class="skcolor_ljg">手机</font>高通骁龙855旗舰折叠<font
                                                        class="skcolor_ljg">手机</font> 深海蓝 6GB+128GB</em> </div>
                                        </div>
                                        <div class="p-comm " style="padding:8px 10px 0"> 已有<span style="color:#005aa0"
                                                class="J-p-comm-ss-46492972183">100+</span>人评价 </div>
                                    </li>
                                    <li onclick="searchlog(1,55245992278, 4, 81)" data-lazy-advertisement-install="1">
                                        <img data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjld1fL_BniyutasT1DduUrNhZJzcevw7oA5sZ1hAEdPx8eWwceHuBGZumR6mqb6dUkCToLKOejVM5i7HEtjZHRXCb7hOuWoXrGLp1vFUmhe0Mgbrw0pmu0Ahqv7WShokh9dgaHrJ2Jb28tNio-yqVJB8kqcKQ2yNnx92-cC4N2hiF3Tze_33uFitGqVHkSNVuKVfF-ePNh0VqL3elJnLt8hzc2vrbBDV9WR0SMx8x5khydRpO4GDGBwAf8BIDarmGdWGml88ipLHLYskpug85uBeQ1RU0hBPHR0Seo1WnWJkT4eDVFoy9k05gkfLSpUZ6ZOid1B-CAvc7y10wlhyOGLc4jwEQNeGU-M6nxyZCSrvAgLKJeVEdXfSi8OldUMNGiC4pb2PEz1IkDkiKQtX9SA_zAcwmHERXbHhCXQ9RddgcvEwKJfaDRye7Qiq_8KZxoTiKKsx7tLaLaPHlAB_pVoDndmgPZ8PYIDlpVIuNzSGElxDJn67dYF_dmt81jtz28dcF1WhVe3gvg2cIGusLj6JuTxlZ4PFK1K-kATQXFmGXhmiwNpNHDEUJJfPfIIXkiKRoeuTnW9Q5nOH_KwrUGk5HU68F3iUeekoZyDLy8_7zfUumvEBOgSsfGM-uMetwDu-BLbpgJObsp7DuYiYBlCMPB32znTR0VqkhkpgJdDHkpGsoF3KH6nlZk5VLZ9efJpvvgevLm9RN9nEfmnrJaAlg1Mp3w0oQ3h43qRu4HHfigHtOcBeV5KQW90_rE60p9MC7iVtvaPELrpn6nBmiqIfzVhxZxr43Pe_QTmQ5ceLVtIHV8JJxY2_taRfVZBxxNk&amp;v=404&amp;rt=3"
                                            style="">
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/55245992278.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS81NTI0NTk5MjI3OC5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjld1fL_BniyutasT1DduUrNhZJzcevw7oA5sZ1hAEdPx8eWwceHuBGZumR6mqb6dUkCToLKOejVM5i7HEtjZHRXCb7hOuWoXrGLp1vFUmhe0Mgbrw0pmu0Ahqv7WShokh9dgaHrJ2Jb28tNio-yqVJB8kqcKQ2yNnx92-cC4N2hiF__rxuvkIypHYMYrZq7385Ftt8ff5JnSFqJsDItG74-6gsSZVjYXay45n7fEwqvoDLlBehpfF7VNBSx6yVWjWrhIz7aN3mgsridYPfZEykCRAPHCzlCQZP3smX_Q9iSvoEeOSTEdpYTg-qEpESLIHvejehvd64K8T4i-QPoAYHN75zf0g7TdhfZJxpRQuBhUOaNd_e5-MvoqUNa3ca49LptbiqRX-th1kqbZYraYH5y5MswZ2rqQS-y-SKfXlXWuXWOp-1pv8AFSxw6FP2c75nKvGmqvXeQOutHmxyJdH6WXF6KzMiN48s112h4iQwWlKrmGCrqTLhIjY9xAyOzdMIJuN9E03lnx_74rWjDyojTLHfaj0DFb778LRjE5uu580dmOtGuIqVLjXBnyJ89BqUdFBiFT08QRKz83S8YHV-KWTRDYR-8q6-uFiSJRsJHmidxLgUKU6rsunInoNMzp6gA&amp;v=404&amp;clicktype=1">
                                            <div class="p-img"> <img width="160" height="160" data-img="1"
                                                    data-lazy-img="//img13.360buyimg.com/n2/jfs/t1/62030/17/9252/70722/5d6f3584E597ef607/1723954f5889156f.jpg"
                                                    class="err-product"> </div>
                                        </div>
                                        <div class="p-price"> <strong><em>¥</em><i
                                                    class="J-prom-p-55245992278">99999.00</i></strong> </div>
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/55245992278.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS81NTI0NTk5MjI3OC5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjld1fL_BniyutasT1DduUrNhZJzcevw7oA5sZ1hAEdPx8eWwceHuBGZumR6mqb6dUkCToLKOejVM5i7HEtjZHRXCb7hOuWoXrGLp1vFUmhe0Mgbrw0pmu0Ahqv7WShokh9dgaHrJ2Jb28tNio-yqVJB8kqcKQ2yNnx92-cC4N2hiF__rxuvkIypHYMYrZq7385Ftt8ff5JnSFqJsDItG74-6gsSZVjYXay45n7fEwqvoDLlBehpfF7VNBSx6yVWjWrhIz7aN3mgsridYPfZEykCRAPHCzlCQZP3smX_Q9iSvoEeOSTEdpYTg-qEpESLIHvejehvd64K8T4i-QPoAYHN75zf0g7TdhfZJxpRQuBhUOaNd_e5-MvoqUNa3ca49LptbiqRX-th1kqbZYraYH5y5MswZ2rqQS-y-SKfXlXWuXWOp-1pv8AFSxw6FP2c75nKvGmqvXeQOutHmxyJdH6WXF6KzMiN48s112h4iQwWlKrmGCrqTLhIjY9xAyOzdMIJuN9E03lnx_74rWjDyojTLHfaj0DFb778LRjE5uu580dmOtGuIqVLjXBnyJ89BqUdFBiFT08QRKz83S8YHV-KWTRDYR-8q6-uFiSJRsJHmidxLgUKU6rsunInoNMzp6gA&amp;v=404&amp;clicktype=1">
                                            <div class="p-name"> <em>OPPO Reno2<font class="skcolor_ljg">手机</font>
                                                    全新旗舰机型 惊艳来袭 全面屏拍照<font class="skcolor_ljg">手机</font> 游戏<font
                                                        class="skcolor_ljg">手机</font> 全网通 8G+128G 海洋之心 双卡双待</em> </div>
                                        </div>
                                        <div class="p-comm " style="padding:8px 10px 0"> 已有<span style="color:#005aa0"
                                                class="J-p-comm-ss-55245992278">0</span>人评价 </div>
                                    </li>
                                    <li onclick="searchlog(1,100008031596, 5, 81)" data-lazy-advertisement-install="1">
                                        <img data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjldmW19JB4f8EFQTqzdp2gYR9lw0fbqNNap0_w0zkJU7D0mbrkGrAm8M6w2WEA5-p45MESZ6d2AAYYurskdDwN8h2SySSPXlcFAJFbnulr5LyMf0njsoAgMC0k4GZ3_jwkh1U0LR9iQdTe0scG03KN9YNuMzaWXttbbRsKF2ZsTvOVB824peuQ5c36lESpCNqTaKOq55Vi8GDqSKY--M6Hg1gCBaRUshD4jtZeWQ9OJ5fWvS1ARXT8frRAWBMZr-_IvUV9J06scBvDOI4ndegTok5NrpxrlWrpm27E7IqLx-IwJ_Wv9_a6FK34XmoRwEvyoByqMEH8rj5vkYjk8qgeiVro_OtZ3qn8cix2rF37ROvqXWucA6Rv-wQyU_VCBdiMwlOswurw0g9mLQwv2txGgvaqEjX_GYEx-7LNWk1tqylf1zCHpXWx2xw9vaRSLGNNcsLGYKOn0LKUECpwWFtblCs0_E41Rk9UtQYhy1TgzGILdJDyU-2n-GUf_GswM15a9meRhdr5l1hDqPFwh-EOZd8Cmg1tttExnb4g5iGigATZI5QQ52zfX9kWRdpMX8-6fdOMBqdv124sw05X8GWSlElcebRySFuTjGJPeDgsUyAyjzLAh-zBJgmlVrg1pnBjlT2HWugxyavV4tpNbB9cbepxt7TnfMjXCxQN8srzgccxWpfyLlOsvDPeRFzBraSq2S0G75HNTLZ2frJHc9mxyuMlJhMjKXZu5pNkyFTs7CjH3nKbaruszQlvlEjCDR4Gd8uTeu15DDcKPOumP-M6mctedBBKK04cKMhdQlJXUOgPH_BH6dPTVGPFbYKrMR-rkoD_wpBtH_0dsaVwQpps_8&amp;v=404&amp;rt=3"
                                            style="">
                                        <div class="p-client-click"
                                            data-clickurl="https://item.jd.com/100008031596.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDgwMzE1OTYuaHRtbA&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjldmW19JB4f8EFQTqzdp2gYR9lw0fbqNNap0_w0zkJU7D0mbrkGrAm8M6w2WEA5-p45MESZ6d2AAYYurskdDwN8h2SySSPXlcFAJFbnulr5LyMf0njsoAgMC0k4GZ3_jwkh1U0LR9iQdTe0scG03KN9YNuMzaWXttbbRsKF2ZsTvOSJUKGVmLy7oNdgp9iCc6r-PhfiI8Xu0uAn1D0Nbz-A47t55cEAlZTHaPt2y07f-fNkL_G0pcIpekny3DfPOS3WXcka98l-yg9Y_LZiw8DEljZRk6Ky-zX9y_M3VPg7gHHcrP5Utks-l5Y0lY71FbIYS-wHsT4mIRigULIcitqoCBJissaM4tf5OIb0Nv53Tp2R4gUlaCVXNCaC39fkSX1Mv6Q2jX0McbvhD-pf2Bh55HYMDe1iAYEApNfpe6o0PSsHJMh0uxS6IAN4MCC1xwo53BSwwDyP3GBA2WLaBgH38pB4_-sSRVgq-Rv7AWZzLsnWbG5mofHpaQiBVhBvh50Dea97dp-D1g_1SnBiUhJ9yTYUW26Amxh_iJIoY_tWnMfy23K5aP3SXjA4-FiJRRrBzkJQZiEQHAEFrhihowN2VBewhXlsXivU6plFj5SGSjVvyOEf6MaFOkSWL7g4_1XjyWwxdK8I_bDSvwLVuueiYzMLZIlLTupaIJys3Y0km-A&amp;v=404&amp;clicktype=1">
                                            <div class="p-img"> <img width="160" height="160" data-img="1"
                                                    data-lazy-img="//img11.360buyimg.com/n2/jfs/t1/46463/39/9830/239422/5d70d892E48ba5df8/3375049263dc8d11.jpg"
                                                    class="err-product"> </div>
                                        </div>
                                        <div class="p-price"> <strong><em>¥</em><i
                                                    class="J-prom-p-100008031596">1499.00</i></strong> </div>
                                        <div class="p-client-click"
                                            data-clickurl="https://item.jd.com/100008031596.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDgwMzE1OTYuaHRtbA&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjldmW19JB4f8EFQTqzdp2gYR9lw0fbqNNap0_w0zkJU7D0mbrkGrAm8M6w2WEA5-p45MESZ6d2AAYYurskdDwN8h2SySSPXlcFAJFbnulr5LyMf0njsoAgMC0k4GZ3_jwkh1U0LR9iQdTe0scG03KN9YNuMzaWXttbbRsKF2ZsTvOSJUKGVmLy7oNdgp9iCc6r-PhfiI8Xu0uAn1D0Nbz-A47t55cEAlZTHaPt2y07f-fNkL_G0pcIpekny3DfPOS3WXcka98l-yg9Y_LZiw8DEljZRk6Ky-zX9y_M3VPg7gHHcrP5Utks-l5Y0lY71FbIYS-wHsT4mIRigULIcitqoCBJissaM4tf5OIb0Nv53Tp2R4gUlaCVXNCaC39fkSX1Mv6Q2jX0McbvhD-pf2Bh55HYMDe1iAYEApNfpe6o0PSsHJMh0uxS6IAN4MCC1xwo53BSwwDyP3GBA2WLaBgH38pB4_-sSRVgq-Rv7AWZzLsnWbG5mofHpaQiBVhBvh50Dea97dp-D1g_1SnBiUhJ9yTYUW26Amxh_iJIoY_tWnMfy23K5aP3SXjA4-FiJRRrBzkJQZiEQHAEFrhihowN2VBewhXlsXivU6plFj5SGSjVvyOEf6MaFOkSWL7g4_1XjyWwxdK8I_bDSvwLVuueiYzMLZIlLTupaIJys3Y0km-A&amp;v=404&amp;clicktype=1">
                                            <div class="p-name"> <em>华为 HUAWEI 畅享10 Plus 超高清全视屏前置悬浮式镜头4800万超广角AI三摄
                                                    4GB+128GB翡冷翠全网通双4G<font class="skcolor_ljg">手机</font></em> </div>
                                        </div>
                                        <div class="p-comm " style="padding:8px 10px 0"> 已有<span style="color:#005aa0"
                                                class="J-p-comm-ss-100008031596">0</span>人评价 </div>
                                    </li>
                                    <li onclick="searchlog(1,100006667574, 6, 81)" data-lazy-advertisement-install="1">
                                        <img data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjle62rQRr-p4UlkqBJz8urCmlKxEMWS2GxX61IIxnpIat9fQqxphN9yQGPiTAvVRgq1rPVG3Nh-nPvhlmuWemswZMxX7cUWRPqCzxIUcow3q5xfSKK0W29sWXS6mhZhCXscgxaqJSdA9Vtb9UOeXBmrxBkTMXsg0bPTP-Jk7ljpYROnllGwtymXNIhG8u-kI4We-LKsBt1jPlbffldS8-NVL50oKiDcSsH6_s_tlniy5HE2mqrdMLm7orzDdxhbc5EuPn4C7mFZu7JSZISPl070_bFYiSKo1_cvRD7fGdC6jIIr6kcwsr8sJUmBKSFL9bgS_yEnhDCrGato_jDlHN0eVucghqQqTWaz-4mnnMwvlLKocpUrR2jVIoxcVYZ7lSu5JkKZTTx-LTTodpNwfs7VTBnERtiOlgATBXxHHcM137lxIGqouZaZliu5xQSIe84W_egIQ4iKMysqFxIGENCxN2Sp2vOli5bTK4rtdvcobflSjwRRSCC4uJl4ltvnY2po4RLKiRGax3Gz51PWlrEaMr6zKhVJUcrt3Dhu-fSpn1nqmmRugQCFz-JncTZTErJnIQ6__liLSOlhqgcA_8iEjb2w1P4OpUexbj4j8kLNBoIqr_zlDJ9f_hBQj6lOWCiJwkbej-qT1IGp2Qt4R9Fi04iHH4uTOCZI3oic5A-S1iItY9RF8z37e9bXTmB5h_5qlVduaOnq64Cj-07KO1T-3ybANWbtJc9wLdby4Ed0PKX9N-_lQy7Lpc2GuNezHwfz3fgUOZMxBBieSlgbvm-ufvwy0EN8mhVpwIMnIZtJ-nI3tQpkBhFurAOYd0W6rxrc&amp;v=404&amp;rt=3"
                                            style="">
                                        <div class="p-client-click"
                                            data-clickurl="https://item.jd.com/100006667574.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDY2Njc1NzQuaHRtbA&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjle62rQRr-p4UlkqBJz8urCmlKxEMWS2GxX61IIxnpIat9fQqxphN9yQGPiTAvVRgq1rPVG3Nh-nPvhlmuWemswZMxX7cUWRPqCzxIUcow3q5xfSKK0W29sWXS6mhZhCXscgxaqJSdA9Vtb9UOeXBmrxBkTMXsg0bPTP-Jk7ljpYRHbst09Qa1CH0w0M0sCaXBCs2LTC_c51pP5wF0YCEeBgaWFQv7OmHKYzo2zkJL5Q5n7HORbOFq84Qy-oDZyBTAoyma3hbnnHAGKbJe-cuj5tKSLDjNNT3M2TswFih2RAbOASSkGQiKGPgN-Y8siGxeyi9KeK2t8BlTH2IhACG880LUV65LUFbcuwuKZXcy_LEoJLx5mzHfJ9a6J9_bFSe0bVSd4Xr8XCzShZhiwNzgWFXmPqFlllbwvI4is_NfXHpkqnizIyJtlJR0GfLFSQfu8OkkgdNWT_5eRvr4Y9mqQyAxMZqpPPULkrw96XYx8tyr79LTh_gABasxuVOYTYultxnrkrTP3lvAkUQYfv48LBsxq7icui_YVMa2wiWH8fYZKtieKIMbxMAvoFDdmpjIm9FPIi-dNcFIayKPaibQfu0bH0Sy--9nVrqixbCi9USofswTDqCIj29i01fdfFC3c&amp;v=404&amp;clicktype=1">
                                            <div class="p-img"> <img width="160" height="160" data-img="1"
                                                    data-lazy-img="//img14.360buyimg.com/n2/jfs/t1/43651/21/8720/332249/5d23454fE54ab1d4a/d0740335667d4f5b.jpg"
                                                    class="err-product"> </div>
                                        </div>
                                        <div class="p-price"> <strong><em>¥</em><i
                                                    class="J-prom-p-100006667574">699.00</i></strong> </div>
                                        <div class="p-client-click"
                                            data-clickurl="https://item.jd.com/100006667574.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDY2Njc1NzQuaHRtbA&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjle62rQRr-p4UlkqBJz8urCmlKxEMWS2GxX61IIxnpIat9fQqxphN9yQGPiTAvVRgq1rPVG3Nh-nPvhlmuWemswZMxX7cUWRPqCzxIUcow3q5xfSKK0W29sWXS6mhZhCXscgxaqJSdA9Vtb9UOeXBmrxBkTMXsg0bPTP-Jk7ljpYRHbst09Qa1CH0w0M0sCaXBCs2LTC_c51pP5wF0YCEeBgaWFQv7OmHKYzo2zkJL5Q5n7HORbOFq84Qy-oDZyBTAoyma3hbnnHAGKbJe-cuj5tKSLDjNNT3M2TswFih2RAbOASSkGQiKGPgN-Y8siGxeyi9KeK2t8BlTH2IhACG880LUV65LUFbcuwuKZXcy_LEoJLx5mzHfJ9a6J9_bFSe0bVSd4Xr8XCzShZhiwNzgWFXmPqFlllbwvI4is_NfXHpkqnizIyJtlJR0GfLFSQfu8OkkgdNWT_5eRvr4Y9mqQyAxMZqpPPULkrw96XYx8tyr79LTh_gABasxuVOYTYultxnrkrTP3lvAkUQYfv48LBsxq7icui_YVMa2wiWH8fYZKtieKIMbxMAvoFDdmpjIm9FPIi-dNcFIayKPaibQfu0bH0Sy--9nVrqixbCi9USofswTDqCIj29i01fdfFC3c&amp;v=404&amp;clicktype=1">
                                            <div class="p-name"> <em>天语（K-TOUCH）i10 迷你智能3GB+64GB 全网通4G移动联通电信双卡双待学生备用小
                                                    <font class="skcolor_ljg">手机</font>卡片机 墨玉黑</em> </div>
                                        </div>
                                        <div class="p-comm " style="padding:8px 10px 0"> 已有<span style="color:#005aa0"
                                                class="J-p-comm-ss-100006667574">50+</span>人评价 </div>
                                    </li>
                                    <li onclick="searchlog(1,100006881012, 7, 81)" data-lazy-advertisement-install="1">
                                        <img data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlcitNDlwQ1_ev-Mr6Fn3J9W4fP6esr5jjG3GqilqYeWe8f3SJM525UH9lSHKIwykkUH4KSyhG4u_Ce3BD9luP8QlDj96hAG6eY_L18xRDVXagroncP8CEZDfHBGlNMm2ayjGTgfw2nzpVCOr-odwJTAV6MBJ50HTYNMDxeABZgW7V8ZBfaKOWTaNJnm3QO4iN2ID7z1eg8yicCmW8ujZQhkEE6O4Cb_F-LxIo5oZPJNPCzOo9lq5ap6d8fkAftzIGXWd6DQtNeNulTGa3JHkOPhJuCdO176Pghz24GHWzaVKFXjGp4aARcIVw1Fp9_uJyiN7f2ENHzwtHHtgk02tkqH4WI4-qrk35wXmJe24eDk7WdFEMZkq0QAKuDzLET5jbTKWFE2OJi_ymFRmD6sIJWmMWGhutvuGI5JhDjM7ME_ofjtIa7c6oOYxct6ARHuoThhGPUYOqlQHEH61sMPPNGvwoP8hxpuvsisOLO1tDXs_lc7ZXQcxM_OK4uN8Kc2fwbP5RyJVoqDEPPhMCyibr7S1QlZ5e9W_5tlqGXqm7XoChk4mCHIBb5rjAbTVyjPvN8FMkbvh05ZGzFeUo7pinE0St-GXTHmGBKTaccn7RZMlIfjK-GaD7gq1BVj4U3PDiSv33WtKCm4AzxLw4e38gw13Pg0vjD2xPVjEU8_RQKCeIcALU6w_9Azw_kgIWr5WN_hnV35szEzHRhRhboAVXCcVfjJbj8Fuat81j-PzEztlI1Rn_UGj7CnvDv2GRjEBjoNYKo_g74twdhBl6GuauWmoyCzuaj7TJ32KoVBU2qeV5HP_hFb97sfYVdwfYLfuaDS0jurHlsybLyXfYjQUzzp&amp;v=404&amp;rt=3"
                                            style="">
                                        <div class="p-client-click"
                                            data-clickurl="https://item.jd.com/100006881012.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDY4ODEwMTIuaHRtbA&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlcitNDlwQ1_ev-Mr6Fn3J9W4fP6esr5jjG3GqilqYeWe8f3SJM525UH9lSHKIwykkUH4KSyhG4u_Ce3BD9luP8QlDj96hAG6eY_L18xRDVXagroncP8CEZDfHBGlNMm2ayjGTgfw2nzpVCOr-odwJTAV6MBJ50HTYNMDxeABZgW7fpsGUSJUQ28Dt43T67U_C02cl90hhuKXo6gpZPGFH4kxAbnZHZ1g0a66KebdZ8DPeOUTT9WprzORaLKGiOMpnkxAylBYX6_7jYrl25Y1lCgZ67BQY553qBi0SySiPrqL7Xf58WkYJbVC9-MFhZkjLsnhW28SKy02Ey09trN46guDfhVPB7Gd6UVTl2jcXL0zycjQpOut3BSp4WgZNmKLxFRg-UyOkUFo-uAHYF2IZ9CEGa9ckM0h2si2VAEqmCvxgxzzw1hV-WYUIke3nGrEi4GCBIJ0qsDotn3FKOBxXX6GepcVcfz1cxnyamSJlDD7EZ1L9tfVxI5iduas172SmSJ96rNeZQ_uMD121URH1JqUeS-gvIXNWSmVO46P0R736_Xt3LEXe1Iq5eZd2T0VdzzQ5JZYhwLjOe0ELXFer-F3fbxK4qhqvs6zQ3c2s-6KTnWoWVnoULcSQBg6cBO1bBOJYlIHcQhYagIG5YX9rZL79OP-I9-TZAb0aNHlw_8ng&amp;v=404&amp;clicktype=1">
                                            <div class="p-img"> <img width="160" height="160" data-img="1"
                                                    data-lazy-img="//img12.360buyimg.com/n2/jfs/t1/57651/10/9758/117221/5d70b247E546b189f/4de8adad8685cbd0.jpg"
                                                    class="err-product"> </div>
                                        </div>
                                        <div class="p-price"> <strong><em>¥</em><i
                                                    class="J-prom-p-100006881012">2999.00</i></strong> </div>
                                        <div class="p-client-click"
                                            data-clickurl="https://item.jd.com/100006881012.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDY4ODEwMTIuaHRtbA&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlcitNDlwQ1_ev-Mr6Fn3J9W4fP6esr5jjG3GqilqYeWe8f3SJM525UH9lSHKIwykkUH4KSyhG4u_Ce3BD9luP8QlDj96hAG6eY_L18xRDVXagroncP8CEZDfHBGlNMm2ayjGTgfw2nzpVCOr-odwJTAV6MBJ50HTYNMDxeABZgW7fpsGUSJUQ28Dt43T67U_C02cl90hhuKXo6gpZPGFH4kxAbnZHZ1g0a66KebdZ8DPeOUTT9WprzORaLKGiOMpnkxAylBYX6_7jYrl25Y1lCgZ67BQY553qBi0SySiPrqL7Xf58WkYJbVC9-MFhZkjLsnhW28SKy02Ey09trN46guDfhVPB7Gd6UVTl2jcXL0zycjQpOut3BSp4WgZNmKLxFRg-UyOkUFo-uAHYF2IZ9CEGa9ckM0h2si2VAEqmCvxgxzzw1hV-WYUIke3nGrEi4GCBIJ0qsDotn3FKOBxXX6GepcVcfz1cxnyamSJlDD7EZ1L9tfVxI5iduas172SmSJ96rNeZQ_uMD121URH1JqUeS-gvIXNWSmVO46P0R736_Xt3LEXe1Iq5eZd2T0VdzzQ5JZYhwLjOe0ELXFer-F3fbxK4qhqvs6zQ3c2s-6KTnWoWVnoULcSQBg6cBO1bBOJYlIHcQhYagIG5YX9rZL79OP-I9-TZAb0aNHlw_8ng&amp;v=404&amp;clicktype=1">
                                            <div class="p-name"> <em>努比亚 nubia 红魔3S电竞游戏<font class="skcolor_ljg">手机
                                                    </font> 8GB+128GB 银色风暴 骁龙855Plus UFS3.0 内置风扇 5000mAh大电池 全面屏</em>
                                            </div>
                                        </div>
                                        <div class="p-comm " style="padding:8px 10px 0"> 已有<span style="color:#005aa0"
                                                class="J-p-comm-ss-100006881012">0</span>人评价 </div>
                                    </li>
                                    <li onclick="searchlog(1,55235391732, 8, 81)" data-lazy-advertisement-install="1">
                                        <img data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlef6t-TA3UzcX4GvaWty-wcvPnxL9gZHcfeVH7Vt6lUryTnPY5XeMPd48rxZAsNTpdnu-aRteKMkq0eAnY6z8XnpOyZsKs7AI1FQ5KO5VbXC-_8Gc70e9FNBiUoyJQn6Pnhk4w9n7sKJV52RTiVWy-fcGnqeazq_saZauBpLZQPfHx2u41TDO2az59hR-W0rwC0zFtYBMrR0sWZKW7Kr58-GND7dWfayahNBoj_vOESKwC1BVaTieP4YetF0OGdK0OanxBm8dkisMpRrnX6zRQKyf1fn4uaIGJ05pNEtYu16u2220iuJY4bGP7Jgdey_ph0r4kS2DPvujlswdkYth50y-Q5d2QxnQ9Tcyxxh0UEuxauTcqoqB8vYi5g9RjhLQFrsEtrHfw_QcnfUs9MoNIDCllMctt20ap-1WSx1EjQA7LGxF5gKDaZqH8iWAh_1hSr3qP8iYvyhb0FLrJXlkceXA4o01PLpQwD03P27s0P4FqXBKOvj_9Is9yFHTaUk4tsaCY7vjDgo3oLFkN4kRSWd7mjapNe6mDOVbxchYMxg0weF3Sfb0CNeGsA3z8FkTUse3mQYPHSJKUNGubFUZV4Njkdgabjn28Zz3pW6jfZLeZYmz-VE3oL3AGuyd6vjqhW62CRg9kPpm5lC1IrErkTM6TGfLVdWY2Wqc6hy9uYoqyXV9KXD_nJnMs2Vm9FC-zhmK6hvyLWJklNPqsHXsW408EAjqQRZI-MeiQn31fe_SvzIQo7D28p6HLGm9qvSWApwaB1C7iSEJGetn95yDaJmgSDZXMmyZETCkAutIzM9UDIAjcfwxaSKgz-l0XpuyYUr6YB4KQFtkFTdAFu-tiV&amp;v=404&amp;rt=3"
                                            style="">
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/55235391732.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS81NTIzNTM5MTczMi5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlef6t-TA3UzcX4GvaWty-wcvPnxL9gZHcfeVH7Vt6lUryTnPY5XeMPd48rxZAsNTpdnu-aRteKMkq0eAnY6z8XnpOyZsKs7AI1FQ5KO5VbXC-_8Gc70e9FNBiUoyJQn6Pnhk4w9n7sKJV52RTiVWy-fcGnqeazq_saZauBpLZQPfFsprvAl4uvk5k9Zyw8wruKs8KbJKbTWgIsqX-FUseUOUXQbDyxTs9rHK0ghA2s3WcQBzFeHcn9AD3_H5oRKq0zR3lguHgnSTDrPuDY3VWYpHF8iYj6DhV1R6knAJwK4i8wTcvXj_DrQzO-I8edUyYhTWEfN0Scq08xEbri2LlSnIiAXXVMXqqs5qy2JRV0Z_IlxZT-Jb4T9D1y5pF_fNnNjLChfMIY_jlPlMVY3D26y0fKKs5M9by9I5VNxDH7p-Zm5zo7Gu7lYPwKAHPYu5UMlRR4VHh-P68Di7AGvFiK7fdIyDDcJeCxMakUTO7cnS0E5KLUfig5ZDGEJC2wOQWCJpBU9Uo8IAbvQIyV6sXSbYGj3NmTiYi0YwRSAkzPLve6B0HR6xeUA3IcOE-DARcKRdmbx94pxg51qtxxK-mtAfOnl9RyAZFhPfXpMtths9cLVnKw_l1YPhoK4HfFGWiiqYYCeMPeNvad5pWo2mGp2pn82O3fTB_NKY7meYSp1yA&amp;v=404&amp;clicktype=1">
                                            <div class="p-img"> <img width="160" height="160" data-img="1"
                                                    data-lazy-img="//img12.360buyimg.com/n2/jfs/t1/74589/26/8953/82632/5d6b80b6E3678f0dd/8a14c740210c78fe.jpg"
                                                    class="err-product"> </div>
                                        </div>
                                        <div class="p-price"> <strong><em>¥</em><i
                                                    class="J-prom-p-55235391732">99999.00</i></strong> </div>
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/55235391732.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS81NTIzNTM5MTczMi5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlef6t-TA3UzcX4GvaWty-wcvPnxL9gZHcfeVH7Vt6lUryTnPY5XeMPd48rxZAsNTpdnu-aRteKMkq0eAnY6z8XnpOyZsKs7AI1FQ5KO5VbXC-_8Gc70e9FNBiUoyJQn6Pnhk4w9n7sKJV52RTiVWy-fcGnqeazq_saZauBpLZQPfFsprvAl4uvk5k9Zyw8wruKs8KbJKbTWgIsqX-FUseUOUXQbDyxTs9rHK0ghA2s3WcQBzFeHcn9AD3_H5oRKq0zR3lguHgnSTDrPuDY3VWYpHF8iYj6DhV1R6knAJwK4i8wTcvXj_DrQzO-I8edUyYhTWEfN0Scq08xEbri2LlSnIiAXXVMXqqs5qy2JRV0Z_IlxZT-Jb4T9D1y5pF_fNnNjLChfMIY_jlPlMVY3D26y0fKKs5M9by9I5VNxDH7p-Zm5zo7Gu7lYPwKAHPYu5UMlRR4VHh-P68Di7AGvFiK7fdIyDDcJeCxMakUTO7cnS0E5KLUfig5ZDGEJC2wOQWCJpBU9Uo8IAbvQIyV6sXSbYGj3NmTiYi0YwRSAkzPLve6B0HR6xeUA3IcOE-DARcKRdmbx94pxg51qtxxK-mtAfOnl9RyAZFhPfXpMtths9cLVnKw_l1YPhoK4HfFGWiiqYYCeMPeNvad5pWo2mGp2pn82O3fTB_NKY7meYSp1yA&amp;v=404&amp;clicktype=1">
                                            <div class="p-name"> <em>OPPO Reno2<font class="skcolor_ljg">新品手机</font>
                                                    【预约抽奖】4800万变焦四摄视频防抖 6.5英寸阳光护眼全面屏全网通 薄雾粉（8G+128G）参与活动 官方标配</em>
                                            </div>
                                        </div>
                                        <div class="p-comm " style="padding:8px 10px 0"> 已有<span style="color:#005aa0"
                                                class="J-p-comm-ss-55235391732">0</span>人评价 </div>
                                    </li>
                                    <li onclick="searchlog(1,47824517783, 9, 81)" data-lazy-advertisement-install="1">
                                        <img data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlckNor1Z7lOZySChGL31SQMXWplxCbbUw8zzgDtAUEdsJ5A2GVU-wD9-2tGRIdovF1mvKbqFR6bm3GbdLKEJ7NrjtdwAS5M0jSKM2WlkMeT1x9J-jMeZM9fC3MkYWNZag3I2uwqofenEXaipD_ZjzaF0bzvMzlqoGOF5k46LkY7APi4v6JSZ_pG2bCOKI960rwSn-Y5vaeWwrMAb3-_aoiVOYffPhSlPmF6eAuZKjQpatAGZxz3sl1gMDQS5sv1mkpYQmDRJ4QLxGD69gM1f54jqeqHPcm2evMjqmp8hzmIX_Q52jc9xQALLEAfKMBGOD5rrvVLWqqxMvN6qpdSeAVmjo2FFtBNncKYNiII_PyviwsAYeoRRSaUSku9D62-0-zZ1L0lzpOGdUOIn-iL1AMCYSkUKUigKs43lMwy_ugAfRQyH3_sM3m0VarKh5EwzuumO4LuamIVHDM8LTM39_AvO6tDRrVoQ3o6c7o_aHAo2uEz2F-WPHcpC2fjciTfGh8wIFNoAIWk-UiOatsrDOH4OlCeO1KQ8dgUyuXOkUdlL4Sshh73j1SrdHV2iNNK2zFDDAWvEhpCoxTVzpWhhW56mKoTL71aAE_Efn_RSeXDqSgkE9l_S8IwDHuS1WusNXJ9r63EDg5ml93XG6Ro3C5F8BczVjFe2zC1666lvKk5wWx8gFU1BaIruIbTACv6nnTabBLfO1EkKQ6fmni3MDPBuFNpM2FLjjd3uT26vFYBTISaTDJUgr165u6Vb08qm6bvIazEyPWspxEPY1fs9GeJcxmkrgsSe_Dv-NjJQThdk3bQ9pB582YRl605jI-NifsF10FTMzI4XzxdpgDe6hUi&amp;v=404&amp;rt=3"
                                            style="">
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/47824517783.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS80NzgyNDUxNzc4My5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlckNor1Z7lOZySChGL31SQMXWplxCbbUw8zzgDtAUEdsJ5A2GVU-wD9-2tGRIdovF1mvKbqFR6bm3GbdLKEJ7NrjtdwAS5M0jSKM2WlkMeT1x9J-jMeZM9fC3MkYWNZag3I2uwqofenEXaipD_ZjzaF0bzvMzlqoGOF5k46LkY7APi4v6JSZ_pG2bCOKI960rwPLnkLbbUYA_afWS3qbnZmMP6sEkMnCd7DEmMXdFCBA2lfGrXK8APzn9I82AcVIX-FNLQkZuHPceS_m6-u0nWijp0N7vE4v3lx1Fu4khPvn5eF8bOAw0B7HdG4htunIHshuclPD79hme3mfh8R4aUKQnnwb41nHe6YqjsNs7CsyYlVCx4eHRXr3fdTv53AiN-HRv3vKCu5mp55_RNJp-IEAmJp9fxixyVXWMzgLu_iAtTyZDeeIaPZASCv_8VpweQEC4cMPum3djj4ofVoi7wKoSRYaCxGo41GkyiWCJlnEj_wyRiaQdkEnQfAFOBXHpdu7Tsy6Q6vjO2WYUNJ4hTnreB1hDbmIXX7E6ttNZKaB0dy8z99t8r5w_EiCHNCsSMq2LBjtB0l_bnqnT7WIJFlJ3LKzBSXb56OH3W9pMWj5UFiyeTugqP15i7m_hQfcs53KSFCx17mTvchuRdbZv6_Ulrdc_NLG449v-xJJQGonA&amp;v=404&amp;clicktype=1">
                                            <div class="p-img"> <img width="160" height="160" data-img="1"
                                                    data-lazy-img="//img13.360buyimg.com/n2/jfs/t1/75209/21/3094/360937/5d147dc8Ef45131f0/1b8b9a938c21f790.png"
                                                    class="err-product"> </div>
                                        </div>
                                        <div class="p-price"> <strong><em>¥</em><i
                                                    class="J-prom-p-47824517783">1499.00</i></strong> </div>
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/47824517783.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS80NzgyNDUxNzc4My5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlckNor1Z7lOZySChGL31SQMXWplxCbbUw8zzgDtAUEdsJ5A2GVU-wD9-2tGRIdovF1mvKbqFR6bm3GbdLKEJ7NrjtdwAS5M0jSKM2WlkMeT1x9J-jMeZM9fC3MkYWNZag3I2uwqofenEXaipD_ZjzaF0bzvMzlqoGOF5k46LkY7APi4v6JSZ_pG2bCOKI960rwPLnkLbbUYA_afWS3qbnZmMP6sEkMnCd7DEmMXdFCBA2lfGrXK8APzn9I82AcVIX-FNLQkZuHPceS_m6-u0nWijp0N7vE4v3lx1Fu4khPvn5eF8bOAw0B7HdG4htunIHshuclPD79hme3mfh8R4aUKQnnwb41nHe6YqjsNs7CsyYlVCx4eHRXr3fdTv53AiN-HRv3vKCu5mp55_RNJp-IEAmJp9fxixyVXWMzgLu_iAtTyZDeeIaPZASCv_8VpweQEC4cMPum3djj4ofVoi7wKoSRYaCxGo41GkyiWCJlnEj_wyRiaQdkEnQfAFOBXHpdu7Tsy6Q6vjO2WYUNJ4hTnreB1hDbmIXX7E6ttNZKaB0dy8z99t8r5w_EiCHNCsSMq2LBjtB0l_bnqnT7WIJFlJ3LKzBSXb56OH3W9pMWj5UFiyeTugqP15i7m_hQfcs53KSFCx17mTvchuRdbZv6_Ulrdc_NLG449v-xJJQGonA&amp;v=404&amp;clicktype=1">
                                            <div class="p-name"> <em>OPPO K3<font class="skcolor_ljg">手机</font>【<font
                                                        class="skcolor_ljg">限时优惠</font>100+耳机】千元机 骁龙710 VOOC闪充 屏幕指纹
                                                    秘境黑（6G+64G） 全网通</em> </div>
                                        </div>
                                        <div class="p-comm " style="padding:8px 10px 0"> 已有<span style="color:#005aa0"
                                                class="J-p-comm-ss-47824517783">2700+</span>人评价 </div>
                                    </li>
                                    <li onclick="searchlog(1,45850490644, 10, 81)" data-lazy-advertisement-install="1">
                                        <img data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlcNtA536l4CHkXm_7glSNCIzToDwfrWOLggEMh98kBi73sS0nOWeaUXh7e5LzfRPWxAZOtDeGxd9Emv3cTw-yOcuB6r60NAHeraa4cjbxlS2KVXKCoDb3CMtjTsA-DBt8SpNlz5cIGQce9E2ilAGBpvbnuBLoUhdEVfDdCz1aFDRUGA3d53FByYWEa9ruc8qAKQkTW-csfR5DSXWj_VdRbr7zm44XNub7wQoVDkJJBjbJeZgpbrVffKog3JQtv7dH1OJ0iUNTBeRz1ZQ-bWrDth4hU-0GTTouVGwbG_x4fne4uUwXvFuqzRvuWpfKxwsDykRkVHqLhjvIpHgWPcJpXRCxJUCnH3O2Un1E5XoxmjqdFKbA89oAlVN4m8CR9U1RorPP98BSvAOpzaWPD3yd5h6ucXJUn_UNn0FMio_by_W1gX4OGFGAPPMdaqgdWxEnhMEMrij0iyR7OKmWNmKoF_EXv04b4rm_cjZ_M80o8EQRuCajXGtmiVP0pWTrlU0mURvyfOVyXGRvVkqOPCxTvtdXStpCZYOYxZvQVHy9i1vKBX8k42Q7A21W1twCxiGd6CwfIkx6MiavRecHT2Xr2Xqf4fyuBpsfo6o8tcyoep2TJxxJ2G85W0Tlo9IZubpKAjxh9VUL_Y0ovrzTa4yKHr8OU_4LrhoA7lvakKtsOpHEwKHEbCHsXm61-px3EMg1k6LW5_XTpQuUSfjgkQd_NwwDI2tRe5-epeBCgKTv7p6LYJvrClNsPZl3sHZRc4Kx2CbjI8RlFgoEzM0R2TxWk0qb5xZYZpW8TfpUjeFM-GHMLDejcxgDRdDKZHjLVuj9BmV2OLlmyjcu74wGg2ddIAyKWvOUZ9w2H79GMNPMY5OWkG4eFQEjEN_nJwEG6Nxlg&amp;v=404&amp;rt=3"
                                            style="">
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/45850490644.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS80NTg1MDQ5MDY0NC5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlcNtA536l4CHkXm_7glSNCIzToDwfrWOLggEMh98kBi73sS0nOWeaUXh7e5LzfRPWxAZOtDeGxd9Emv3cTw-yOcuB6r60NAHeraa4cjbxlS2KVXKCoDb3CMtjTsA-DBt8SpNlz5cIGQce9E2ilAGBpvbnuBLoUhdEVfDdCz1aFDRa9Yvi95VQebhc2HaVkaUpQvt5zWxtSnzRJUPORJkyehqXheryFvyUATALzKIWmb37KjA-l70tkpca42BoMT35DQSqPgpmLpgDOae2Ed8t6nRRlFjPmx7wzh-jF8JlVgWNjLOuqMIEuSr9U4qjBMghdAgYGu-aC42uaEFBUjuxKe-X_mk0pLQim4S8Uv1MEZRNsxssFNp4AHt4bjSsqjy2y28UKeGfbvfUrki2jvKtF4YC8rA-ETbO9j7sbSPIevrO6W9Uk36vb_jUxYovDYK_5x7RhAhrKazIar98cT-6MHy7om0NhtxLOXO9gZnFTPkiB6EqhGvubR-kEShKUbMpWkIsuXTCqUTJJ0Ki1Gi1pd2KF3ELECL565lQGQ3-6g8EqudUZErKNlVwo3O6QxCGBURzVXKmTWUo6NltppjT0_tkb8F7mVeBVmqiG4tTLV54STanidJzZ0OgJ_4RpuafMM4B9eTs2dX__Yl-50TgmNXBHC345crJgbWzHNu9dkLZ4C1k1du-cXXueitpdDd0Q&amp;v=404&amp;clicktype=1">
                                            <div class="p-img"> <img width="160" height="160" data-img="1"
                                                    data-lazy-img="//img14.360buyimg.com/n2/jfs/t1/65190/25/8601/255415/5d67adc8E33752a61/c3cad27a1b132e84.jpg"
                                                    class="err-product"> </div>
                                        </div>
                                        <div class="p-price"> <strong><em>¥</em><i
                                                    class="J-prom-p-45850490644">599.00</i></strong> </div>
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/45850490644.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS80NTg1MDQ5MDY0NC5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlcNtA536l4CHkXm_7glSNCIzToDwfrWOLggEMh98kBi73sS0nOWeaUXh7e5LzfRPWxAZOtDeGxd9Emv3cTw-yOcuB6r60NAHeraa4cjbxlS2KVXKCoDb3CMtjTsA-DBt8SpNlz5cIGQce9E2ilAGBpvbnuBLoUhdEVfDdCz1aFDRa9Yvi95VQebhc2HaVkaUpQvt5zWxtSnzRJUPORJkyehqXheryFvyUATALzKIWmb37KjA-l70tkpca42BoMT35DQSqPgpmLpgDOae2Ed8t6nRRlFjPmx7wzh-jF8JlVgWNjLOuqMIEuSr9U4qjBMghdAgYGu-aC42uaEFBUjuxKe-X_mk0pLQim4S8Uv1MEZRNsxssFNp4AHt4bjSsqjy2y28UKeGfbvfUrki2jvKtF4YC8rA-ETbO9j7sbSPIevrO6W9Uk36vb_jUxYovDYK_5x7RhAhrKazIar98cT-6MHy7om0NhtxLOXO9gZnFTPkiB6EqhGvubR-kEShKUbMpWkIsuXTCqUTJJ0Ki1Gi1pd2KF3ELECL565lQGQ3-6g8EqudUZErKNlVwo3O6QxCGBURzVXKmTWUo6NltppjT0_tkb8F7mVeBVmqiG4tTLV54STanidJzZ0OgJ_4RpuafMM4B9eTs2dX__Yl-50TgmNXBHC345crJgbWzHNu9dkLZ4C1k1du-cXXueitpdDd0Q&amp;v=404&amp;clicktype=1">
                                            <div class="p-name"> <em>
                                                    <font class="skcolor_ljg">新款</font>4G+64G大内存 6.1英寸水滴大屏 小辣椒9e安卓智能
                                                    <font class="skcolor_ljg">手机</font> 全网通4G 学生价超薄指纹一体机 渐变黑 4G+64G
                                                </em> </div>
                                        </div>
                                        <div class="p-comm " style="padding:8px 10px 0"> 已有<span style="color:#005aa0"
                                                class="J-p-comm-ss-45850490644">100+</span>人评价 </div>
                                    </li>
                                    <li onclick="searchlog(1,40230014021, 11, 81)" data-lazy-advertisement-install="1">
                                        <img data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlcBx_WJy_uotkyGZySvsZwpBsgZZ_AetUF60lPK3fY1_25w5neCo-1h89tV69YILC7BW-X3zL_S27b_-5TrKLbta2DKRg1ab-Wyryu4PiDpqbWKbfMM1wpcL8St8qHQz9Pr6LD6A98oOTveMIhgnPCpISTLYLhtuqj47zLHMyhyaGzda9VlHv8-RbPcX-KzxqsLVy2kHRVS2oAZ5uKKjlZX9JaH1H8F59NLRq9npq0FqYniaN31gK_6_OfTol0yrkBJz86yaphaIjkcLBLpCxxXVniCYVJu9uMp5EUueE2ELpVJis69wdnsAJT3F6XqCDwT2XOjxJVmjG_yDRmpHI7I5mlhYxJproqZQNvkBfiu_Zt_smqMiK2_0M2JtMFn2kyJkMD64Nla0CP1ZPyluD-dW7e8W0jpHYm8xgBlUciK_ze6AHWlLK8zLG0BQGz5t76zXYPfGOCpPOH72RC3FL5kMc0JyjJ_ydqiOv6pm2CcvC1xBWVMjBb7_0Cuwke0_7geZlnE3wZAsa_AmTI0G-2B9NerLd26Cx5jNWt9d6FA_S0uUbQ7whsyhN66mT_JOhj0-7hOtsXXGMf3BTlF0rthN0gVGKxmdRTRimI9crQLGKd7hvajZCd1FoGmEr3i7cFEMsO_jFq2CcwgEJrill1Hqo1L9XtTx0Uye3zM4t5vhKCdpgIV9dp4lVY6uutNvp2Z_57quGuA70aBnAyiLcoGdnDedd_595nL9YLoyzEFm2PitPgxIMEUtaVTs2_3cnaCY6Ao_zmTt1LcQbwU_U6fHPuFya2jtAfNQ0qoknwxS4T8UmpX0fyd4VvnHgt9BIw_-WBVmG-L4UHavJ8W7LJh&amp;v=404&amp;rt=3"
                                            style="">
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/40230014021.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS80MDIzMDAxNDAyMS5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlcBx_WJy_uotkyGZySvsZwpBsgZZ_AetUF60lPK3fY1_25w5neCo-1h89tV69YILC7BW-X3zL_S27b_-5TrKLbta2DKRg1ab-Wyryu4PiDpqbWKbfMM1wpcL8St8qHQz9Pr6LD6A98oOTveMIhgnPCpISTLYLhtuqj47zLHMyhyaGzda9VlHv8-RbPcX-Kzxqt2i9IVFo3lrsXVJalWVFoE6YanvbMZqH7P3_UPUa9m4uwIQ1XfOsxAvcu9u-X751BkBNYbjI8vgoFE6wH1RmYKRLeolVgwt4hcVW01NmYudDHHUk5ly4PBFx1gM3kLtuAFS51aS4q1pcQHs28uBLk64-_HKhfsSUy1pnPScGEx9c0tZTVwyHN8vYIB_QTVwdS2adsMOgZa3hIBgSsOOhm4MI51SqxEDE0dpWLcsJ6JnYaZWiNbDh71WQ0QmkNgz_jKA0bfktFJYmOfuwnJO0t0wH7VIjZizmiul_6NONnsPtKbWRIp_8eRxrALCe3uJVb7IQPh0a4ogh2wOqD77q1kjumYPIfX3O91FpfBawowmqCi6vXtGhecImilSbBP2D8rpPR_QLo5s2je8y_1e-UJXGXZKoJsf873lio-FMSfCRwl3a8x4hYVMcRiOSZOh37c-9khyfhAwLWpmxpkEIpdVi2k4d33J4C9gGnmPKT8YQ&amp;v=404&amp;clicktype=1">
                                            <div class="p-img"> <img width="160" height="160" data-img="1"
                                                    data-lazy-img="//img11.360buyimg.com/n2/jfs/t1/18233/24/6805/426512/5c637cf0E8601015f/7d6ebb4df69f62c3.png"
                                                    class="err-product"> </div>
                                        </div>
                                        <div class="p-price"> <strong><em>¥</em><i
                                                    class="J-prom-p-40230014021">799.00</i></strong> </div>
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/40230014021.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS80MDIzMDAxNDAyMS5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlcBx_WJy_uotkyGZySvsZwpBsgZZ_AetUF60lPK3fY1_25w5neCo-1h89tV69YILC7BW-X3zL_S27b_-5TrKLbta2DKRg1ab-Wyryu4PiDpqbWKbfMM1wpcL8St8qHQz9Pr6LD6A98oOTveMIhgnPCpISTLYLhtuqj47zLHMyhyaGzda9VlHv8-RbPcX-Kzxqt2i9IVFo3lrsXVJalWVFoE6YanvbMZqH7P3_UPUa9m4uwIQ1XfOsxAvcu9u-X751BkBNYbjI8vgoFE6wH1RmYKRLeolVgwt4hcVW01NmYudDHHUk5ly4PBFx1gM3kLtuAFS51aS4q1pcQHs28uBLk64-_HKhfsSUy1pnPScGEx9c0tZTVwyHN8vYIB_QTVwdS2adsMOgZa3hIBgSsOOhm4MI51SqxEDE0dpWLcsJ6JnYaZWiNbDh71WQ0QmkNgz_jKA0bfktFJYmOfuwnJO0t0wH7VIjZizmiul_6NONnsPtKbWRIp_8eRxrALCe3uJVb7IQPh0a4ogh2wOqD77q1kjumYPIfX3O91FpfBawowmqCi6vXtGhecImilSbBP2D8rpPR_QLo5s2je8y_1e-UJXGXZKoJsf873lio-FMSfCRwl3a8x4hYVMcRiOSZOh37c-9khyfhAwLWpmxpkEIpdVi2k4d33J4C9gGnmPKT8YQ&amp;v=404&amp;clicktype=1">
                                            <div class="p-name"> <em>【3期免息 】OPPO A5<font class="skcolor_ljg">手机</font>
                                                    千元全面屏 4230mAH大电池 千元旗舰机 珊瑚红（3G+32G） 全网通</em> </div>
                                        </div>
                                        <div class="p-comm " style="padding:8px 10px 0"> 已有<span style="color:#005aa0"
                                                class="J-p-comm-ss-40230014021">7400+</span>人评价 </div>
                                    </li>
                                    <li onclick="searchlog(1,100008037460, 12, 81)" data-lazy-advertisement-install="1">
                                        <img data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjldKG8zIn2E5v45OFc2TihmCrqu-kzItNUapBrn8nY8PrN7LCcecIBEdUBkQr4-56m1DmkF-beHiUcp6OVYDmnd-cXVVPVRXo9xr6n3N-T-r7ucCWHvlhPWU47lN6wcL_PiOi3OsoPIjeG8eSmtDG5SW2SuvGczr6kq_qikVy-ZHOdwXTXSSy7aKy5ukGDf6MpCQtPO3t_4RQIJV19dGyL1RVwCfN9YJ-KNiPdzGqqqe3QXY8YsgYbzTIVbnASfoCyeZAEiYxkq3NHXruo-6Oajv3_f_bbXYmY0p8FglpXE1bVyTWXRhc_VLOVfioVvMauOW77shA2uwAV2bwsuFgVaEco8dWPSamIc1juiOru5nofqFD838iAL15AzDXlWFIE9ntE_j4dWz6dPnC-Q5dNz_-t4QSsc-fzVC8xHbzr1NJmN71RzcOT1DVaRYHxOiafSG_M6rHsNL3cdlbGiVqS7qAVpvYcpD1z7uEe1krgKdPeG7W9RQn37MmvNl2m21y96gDd-d_opI8xmHEtkzMb_1sNvm0QUKwiH0v4gjrLg-aeeCqd_Laa_J8vsopAK-EuHK9301-QZzu30-MsmDkuDa0pNKbcrCfDyWsUHL-dgSB4d6M58xf6NaYXGFTp5ICrngRwa4RZ6ExoZbkzIiH7mnmZ34F4KffAxC4o8ofj99p660dPm74fJhdgulM5Z1GABH-EXEQhImAWw_B_wuE1ugAYkN-zk3ROywvI9ZXRVIoczDKDHpcLcJ0I_UoxaSU8UdCKgkhs25kL7IGawdiaMukM5szD_GCTHGNtMccLh-VUtc_58DauZF5WZGqN_AiHKnYWIT8M-jgFz0L3PUyfnS&amp;v=404&amp;rt=3"
                                            style="">
                                        <div class="p-client-click"
                                            data-clickurl="https://item.jd.com/100008037460.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDgwMzc0NjAuaHRtbA&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjldKG8zIn2E5v45OFc2TihmCrqu-kzItNUapBrn8nY8PrN7LCcecIBEdUBkQr4-56m1DmkF-beHiUcp6OVYDmnd-cXVVPVRXo9xr6n3N-T-r7ucCWHvlhPWU47lN6wcL_PiOi3OsoPIjeG8eSmtDG5SW2SuvGczr6kq_qikVy-ZHOUG2qlzlLO4h6DWMg1w5P15-vrpbDMz-D7ZZOO05UHsf72M-OL3Uuhxs53hx79ukJkWvFDtuuLQVL11LxDYFLxollI64hJGoPEDAHQ-YI1OfM-zHma5e_Lgo3M-2SPsqNkBdFJgVRSLUT-swCMAoSng0xoBNF5R_S1J0WANr4OtXF-Dt7JnJBrRUFUtOZSSEFc1yW5ftslbntEPbAkLwkXqEgYA2uX85TQ2rBm7uHnK5dALj6VmGqbQOBxl5iQHFP9KqS-ueJIGtQNpOKQ8w_8fsxO5pBZEd29U7vVCnBjCpP7XDzk_j4IXD-pOYSFyLaWY9HzPNI-2c_Yr1UJM8a8lFhaz71u2i2Hc3Jazca9JCxGGARl1DMN64QGf4d6UZCb0T9RIotoUWGL8HwkT2wuo1F20u3pYzYFSq8ZVjTyxN2Oo79PrHO8Q5y8V3LQI2I1op8jckqznTPM-MWNziwtbjzVJw66JohZII_C6wdpyz61dI5n_pg7U1dwaa_3YtOw&amp;v=404&amp;clicktype=1">
                                            <div class="p-img"> <img width="160" height="160" data-img="1"
                                                    data-lazy-img="//img10.360buyimg.com/n2/jfs/t1/47787/2/9897/322362/5d7341feE77c51777/d20851334a34906b.jpg"
                                                    class="err-product"> </div>
                                        </div>
                                        <div class="p-price"> <strong><em>¥</em><i
                                                    class="J-prom-p-100008037460">998.00</i></strong> </div>
                                        <div class="p-client-click"
                                            data-clickurl="https://item.jd.com/100008037460.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDgwMzc0NjAuaHRtbA&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjldKG8zIn2E5v45OFc2TihmCrqu-kzItNUapBrn8nY8PrN7LCcecIBEdUBkQr4-56m1DmkF-beHiUcp6OVYDmnd-cXVVPVRXo9xr6n3N-T-r7ucCWHvlhPWU47lN6wcL_PiOi3OsoPIjeG8eSmtDG5SW2SuvGczr6kq_qikVy-ZHOUG2qlzlLO4h6DWMg1w5P15-vrpbDMz-D7ZZOO05UHsf72M-OL3Uuhxs53hx79ukJkWvFDtuuLQVL11LxDYFLxollI64hJGoPEDAHQ-YI1OfM-zHma5e_Lgo3M-2SPsqNkBdFJgVRSLUT-swCMAoSng0xoBNF5R_S1J0WANr4OtXF-Dt7JnJBrRUFUtOZSSEFc1yW5ftslbntEPbAkLwkXqEgYA2uX85TQ2rBm7uHnK5dALj6VmGqbQOBxl5iQHFP9KqS-ueJIGtQNpOKQ8w_8fsxO5pBZEd29U7vVCnBjCpP7XDzk_j4IXD-pOYSFyLaWY9HzPNI-2c_Yr1UJM8a8lFhaz71u2i2Hc3Jazca9JCxGGARl1DMN64QGf4d6UZCb0T9RIotoUWGL8HwkT2wuo1F20u3pYzYFSq8ZVjTyxN2Oo79PrHO8Q5y8V3LQI2I1op8jckqznTPM-MWNziwtbjzVJw66JohZII_C6wdpyz61dI5n_pg7U1dwaa_3YtOw&amp;v=404&amp;clicktype=1">
                                            <div class="p-name"> <em>【预售版】realme Q 4800万超广角四摄 骁龙712AIE 20W VOOC闪充
                                                    4035mAh长续航 4GB+64GB光钻蓝</em> </div>
                                        </div>
                                        <div class="p-comm " style="padding:8px 10px 0"> 已有<span style="color:#005aa0"
                                                class="J-p-comm-ss-100008037460">0</span>人评价 </div>
                                    </li>
                                    <li onclick="searchlog(1,55223318934, 13, 81)" data-lazy-advertisement-install="1">
                                        <img data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlc_VgALbFIJwdBxeZ3sJVs-9jmK-vHTXLXCukPO-os5wE0DgaqGNMxLegkwvJ2GwOqMwkrcHXPvWMBUIxl5vQidMpFT9pR24tDAjb4A_XwwFlCM0fY-Az12no9vHpL5F1BrJMk7aCVXLCcGZlwpoTSmcrfmhxlqBGV0klW9ESVASYuIOCLc3nW9ylaz_LczjGtITobOKNVnFuqUvLfUlmfIfKHWrH36-XygDgxHLTq4sWo88fNY98fT_CE8VuoiwgOPPBZTHaJ3CpV2hJUU6c5c9YHrfhud22f_517OtIHK1QYHl1p-ZHCeXvKCNKmQrMkLqDiqrbWnzI19S_8RTS7IQkJeqkDPztV8J6Hj5Uctoz-2hJA1kuacj3AUkAn2DvUr4-TJGCJxPx7fQviyzwtKJX6mJ7OxBSIwKf_b5QvQCvqiu4JSqwaxQ6_EXYV_N-brX-X-IJkrAw9qG-IVel2XYJeOMRzWlUWEt4mVClTMYatxo5d8rWXgQmBLLaeKLofuNjWtzWLiEEVB4NNa-Ywe63PztEUPZR4bKpXgsr-f7baP_Z4UK0k8tdWaCO2csueuj3AFPsOMNEQV7KsGe5LbqVipkRbMSh7-A435hE1c0eyjDxuKg6FKPLJto7utbKyTyqE8XcS1Ebvl5Cj4Q3k-70ecpUInSljLX-c2YQ5GabxtfI2X2ecQu7t6-wzJe79KGGymmvutbWhTkNf4aoG_1i01z061lzweNryU7RuuvDw20ZcFGt8ZaNrpsoneEK3QxtWtu5TEJpoe24MWyrr474EEU2WDE5lCoVOSGV-kHFTo60Rg09-rfCQcq_VPn_N87sy-Zyk6RYNyr0O43-FA181bx-jxxKrIXp5RpQ8I3Q&amp;v=404&amp;rt=3"
                                            style="">
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/55223318934.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS81NTIyMzMxODkzNC5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlc_VgALbFIJwdBxeZ3sJVs-9jmK-vHTXLXCukPO-os5wE0DgaqGNMxLegkwvJ2GwOqMwkrcHXPvWMBUIxl5vQidMpFT9pR24tDAjb4A_XwwFlCM0fY-Az12no9vHpL5F1BrJMk7aCVXLCcGZlwpoTSmcrfmhxlqBGV0klW9ESVASQLAvOogmK1YrHsJP-Tft9qoIjtlUDguDNUb0MwoaoHRK7TWAGdtO0cUpWYHTxa-wPQUzRXbeP-1Uu381xrKcAvt-j9DyjBpRPDfrCsWXNJhraVRPtCVOX-EjISjcM8che024HHLJr0Kp6D_pAXqeP546dU6bIWVg-UQyAnkHZJo90TJgd5UFiviEQyM32p4cmymyyJgjZrkLiKCCnyzox2hedAGxa0fGHyMAsmYWTs-HQkC8eWqB_6m8R-AnRhYkFE4Zt-tSNiakbOGo77E4t7dNNozVke7rA2Qun5T-r4IsQOUYImsOdpRzYnr4iyVNiZMPeCnu0nZydQIvj3X4wIhlha07IgU4FAvopWec8EEY9_5akHdmqYL4yvghmH5IY6jZcdnzXY11jL-lHcvSakVcC40LIAOgoe2hFv_hk4fNK7DbawY0KBWINDNqHueFqJLqpfSKV_o2zyOfGbbv13FDpjvjBmXFYefiv78LEUDkpg775WeU4UYPS_yu_TkxNFIqC2-_MWjIm4lMffTlgQ&amp;v=404&amp;clicktype=1">
                                            <div class="p-img"> <img width="160" height="160" data-img="1"
                                                    data-lazy-img="//img14.360buyimg.com/n2/jfs/t1/42738/35/12671/138779/5d5e85c5E9dbeee01/f191ddeb0362a68c.jpg"
                                                    class="err-product"> </div>
                                        </div>
                                        <div class="p-price"> <strong><em>¥</em><i
                                                    class="J-prom-p-55223318934">4098.00</i></strong> </div>
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/55223318934.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS81NTIyMzMxODkzNC5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlc_VgALbFIJwdBxeZ3sJVs-9jmK-vHTXLXCukPO-os5wE0DgaqGNMxLegkwvJ2GwOqMwkrcHXPvWMBUIxl5vQidMpFT9pR24tDAjb4A_XwwFlCM0fY-Az12no9vHpL5F1BrJMk7aCVXLCcGZlwpoTSmcrfmhxlqBGV0klW9ESVASQLAvOogmK1YrHsJP-Tft9qoIjtlUDguDNUb0MwoaoHRK7TWAGdtO0cUpWYHTxa-wPQUzRXbeP-1Uu381xrKcAvt-j9DyjBpRPDfrCsWXNJhraVRPtCVOX-EjISjcM8che024HHLJr0Kp6D_pAXqeP546dU6bIWVg-UQyAnkHZJo90TJgd5UFiviEQyM32p4cmymyyJgjZrkLiKCCnyzox2hedAGxa0fGHyMAsmYWTs-HQkC8eWqB_6m8R-AnRhYkFE4Zt-tSNiakbOGo77E4t7dNNozVke7rA2Qun5T-r4IsQOUYImsOdpRzYnr4iyVNiZMPeCnu0nZydQIvj3X4wIhlha07IgU4FAvopWec8EEY9_5akHdmqYL4yvghmH5IY6jZcdnzXY11jL-lHcvSakVcC40LIAOgoe2hFv_hk4fNK7DbawY0KBWINDNqHueFqJLqpfSKV_o2zyOfGbbv13FDpjvjBmXFYefiv78LEUDkpg775WeU4UYPS_yu_TkxNFIqC2-_MWjIm4lMffTlgQ&amp;v=404&amp;clicktype=1">
                                            <div class="p-name"> <em>vivo iQOO Pro 5G全网通高通骁龙855Plus 4800万AI三摄44W超快闪充
                                                    <font class="skcolor_ljg">手机</font> 竞速黑 12GB 128GB</em> </div>
                                        </div>
                                        <div class="p-comm " style="padding:8px 10px 0"> 已有<span style="color:#005aa0"
                                                class="J-p-comm-ss-55223318934">400+</span>人评价 </div>
                                    </li>
                                    <li onclick="searchlog(1,100004404944, 14, 81)" data-lazy-advertisement-install="1">
                                        <img data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjld0DRkP7q-LkK9wFVz3gcwaz5aLwmpkQJ1Oh4yDDcjG_ctIOEXtPEfHvbLohQqe8SN2by34_FV0L3x4s8m969BhhpUlj6KBemJD85DIOoboxoqh2tKz9PIC1GqklT2XoQbo5IGDf3FMfXyrWhtZ-fDfPtLnomQkKt56qb9xeAaXNqwHEtWhySZRNZ-lt6oCl2rxm8jKYTj3BGvmIflf5gcDVZ-12xK8HdlGTV1AfZ1L2VjWawcfVQ7PI8Jfd1-KdFtiXX6WKF2K_mPgipfvhlcGZHBEWA6RVa94ltkBZDdsyRrds3WwymWF1jrfLlPgyiNuqeIs0XXAO9uee_JzMvrJt5ICn0vAXpzOIC9GmoyVN9jy2bMI0tSQLtZjVaWLR1_3BDiOF9K43FnOGFh_FP-YPtizZ__XAn-Eeuc7YdGQUdOpFx17e8gkMot5UWN0UnDr7zwr1qsCUOdpS8N-EuR0-AA5zt-obe7aSGWzLf9Jk__p1O7oheroDWVBiJxiKKdc5zOuEieggx8haJKYKj-fWk3Y5XHnPoTceSjarZ65PygnnPecrYTt1iaHGDvuG-84mwycN1EjydU-ztxUO5NFNqSTyjHzJPH2KDctQUh4APsv9QlKp6AiWkFhHussOVVLcWmIskypA4UbM7ZMV8xn_IUyUnRILL2PcmO3ribDyj168jjMdHxkdr-6NnJGUXsIuWk1w0mOhfPVAHP2FgtFz-rUvAQ3iWx8kcqKl14tsokpReWVevTK5e2l0PGWI6cobW_vDgkfSrztDdi_6XSeWt78JQNoPoV_h5xca-04bfSpIq-gRA8XaIZF5xcAvw2JDqg6GXQjvvtr9gf1bhYf8Umq8BuV3fsZXjsf_291Xw&amp;v=404&amp;rt=3"
                                            style="">
                                        <div class="p-client-click"
                                            data-clickurl="https://item.jd.com/100004404944.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDQ0MDQ5NDQuaHRtbA&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjld0DRkP7q-LkK9wFVz3gcwaz5aLwmpkQJ1Oh4yDDcjG_ctIOEXtPEfHvbLohQqe8SN2by34_FV0L3x4s8m969BhhpUlj6KBemJD85DIOoboxoqh2tKz9PIC1GqklT2XoQbo5IGDf3FMfXyrWhtZ-fDfPtLnomQkKt56qb9xeAaXNshpHzOC3Qhrxbu3NIpvALe_apY-1OjLQvnklHAoWvZZ4qd7vHAVa0T4gewbgSgW8BkyNc09oenRRFhv_1tzGrHV3qfcEmZ9TuUc7d1jrid7Ua5bZqaFmfMKO3pQh9CMtmsWSMTuaTNJKN5puoV91H2mJN-KUM1WdUdxCgHNf5_qT7nicbXCY_8w_d2pcgWg4MmU7IIRz-JbVu7GzlNKv-UImDNtFxzzelBQLh8BM8Y9bzaB5hrkMR7ECpZV0fxCSodVKsGwx9kc2GwxiTNO15IxDctTE0jGakxFC9wz07-SOCCucBKEA1GKRiW3blKoOvS6U2VDzsYSEj34nis59RYH97irTuhChcunZegt9cg9KHcWRygYRkLbTV94AhjCjNpiHeNGwJXrlcr0pzWWescqzS7r1Vb3p_6kYh8ddYWXhxqLZpOV0DaC3nNcLyUPEu6DVH84bNVWFspeW2JuxA_qD-uwiCIS5G1GsiqzooltF381n8we4NFFzDrgY-DzmQ&amp;v=404&amp;clicktype=1">
                                            <div class="p-img"> <img width="160" height="160" data-img="1"
                                                    data-lazy-img="//img14.360buyimg.com/n2/jfs/t1/25813/29/12657/304911/5c98c8e2E6bcf7d2d/25342f237b56fe97.jpg"
                                                    class="err-product"> </div>
                                        </div>
                                        <div class="p-price"> <strong><em>¥</em><i
                                                    class="J-prom-p-100004404944">4988.00</i></strong> </div>
                                        <div class="p-client-click"
                                            data-clickurl="https://item.jd.com/100004404944.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMDAwMDQ0MDQ5NDQuaHRtbA&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjld0DRkP7q-LkK9wFVz3gcwaz5aLwmpkQJ1Oh4yDDcjG_ctIOEXtPEfHvbLohQqe8SN2by34_FV0L3x4s8m969BhhpUlj6KBemJD85DIOoboxoqh2tKz9PIC1GqklT2XoQbo5IGDf3FMfXyrWhtZ-fDfPtLnomQkKt56qb9xeAaXNshpHzOC3Qhrxbu3NIpvALe_apY-1OjLQvnklHAoWvZZ4qd7vHAVa0T4gewbgSgW8BkyNc09oenRRFhv_1tzGrHV3qfcEmZ9TuUc7d1jrid7Ua5bZqaFmfMKO3pQh9CMtmsWSMTuaTNJKN5puoV91H2mJN-KUM1WdUdxCgHNf5_qT7nicbXCY_8w_d2pcgWg4MmU7IIRz-JbVu7GzlNKv-UImDNtFxzzelBQLh8BM8Y9bzaB5hrkMR7ECpZV0fxCSodVKsGwx9kc2GwxiTNO15IxDctTE0jGakxFC9wz07-SOCCucBKEA1GKRiW3blKoOvS6U2VDzsYSEj34nis59RYH97irTuhChcunZegt9cg9KHcWRygYRkLbTV94AhjCjNpiHeNGwJXrlcr0pzWWescqzS7r1Vb3p_6kYh8ddYWXhxqLZpOV0DaC3nNcLyUPEu6DVH84bNVWFspeW2JuxA_qD-uwiCIS5G1GsiqzooltF381n8we4NFFzDrgY-DzmQ&amp;v=404&amp;clicktype=1">
                                            <div class="p-name"> <em>华为 HUAWEI P30 Pro 超感光徕卡四摄10倍混合变焦麒麟980芯片屏内指纹
                                                    8GB+128GB亮黑色全网通版双4G<font class="skcolor_ljg">手机</font></em> </div>
                                        </div>
                                        <div class="p-comm " style="padding:8px 10px 0"> 已有<span style="color:#005aa0"
                                                class="J-p-comm-ss-100004404944">11万+</span>人评价 </div>
                                    </li>
                                    <li onclick="searchlog(1,46141812415, 15, 81)" data-lazy-advertisement-install="1">
                                        <img data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjld7xmksPq9L2aZbeaRLj6NaaZLoOEL99LDHdvFqm0UEgwd793fOQSeqpbeihjxK5TmSzb1JnGVZ8lu6QqcJXTYxsfqDuatjfsaija-rT-I_7QxJJIIuOXzBTI_EisFGo9Cz0ncEa2K0Kt8hiJwSPRIHtYAX9QCoeMj2wOXUH22zGwuB014KdVsLrBPc6XUrCufrDSENE8GJz1DPzmtGlGnqxYcu5sO9qcsLXagN6TlfB3xlXEmJtRz0S7kjxpJfG09rM7ku6Jq6Mv1_PptVozVP3rEfR-WvozGPoaHMaS7sD9efI56wxnR9xq_J1MAQzn-dNiiVzeen5BaNOqSP_ZT9aJCROJpzZlI46I2mW97CpG-Ok5j6dzfTxefwo5pGROi3pS4Y1ezLVaDiOZdcu6iwPM0Ouvqo8rRmXDWdSpBMkpFxORdVoZaBToPWzaclLZIVCYKqqsVWhq8inthqdQws0iDyMA89wanq4BFX1vwwdHtRnsn4DIwzpwg3PiLW01OuIvQMG_h5sbOlsomEOBZbbJwd-FCm6gugOpj4ItA2BBjSW21EcTyFAzJYhO_kLwud-zJVppsSLLKpaSoS8TjHN7GwvgFqY0EnS1G344PemVCsT17MvdfeWUHWON5ntaT5fWj7U4kMBQAmkT4kVSby2YA6c7C4OtEx_Nbz2uCJXiR56-UeX_R5fCap6ODrvX3Bio0h8ZVeWZPXfoJi3pvI-2j7_OovEvC9WZ5lbNtEUwGRnQqkBP9TzcbB09R-3xXi7w_ykiPKE8muLTsvNGWX3mYiFEK_1cQR9NNID0Bm_FBOBTz8Yhc4sFylxkNsHfB0jky_vsgiRssrcfnSalfoMfxR4fDuqwuAuBCYyORfMg&amp;v=404&amp;rt=3"
                                            style="">
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/46141812415.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS80NjE0MTgxMjQxNS5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjld7xmksPq9L2aZbeaRLj6NaaZLoOEL99LDHdvFqm0UEgwd793fOQSeqpbeihjxK5TmSzb1JnGVZ8lu6QqcJXTYxsfqDuatjfsaija-rT-I_7QxJJIIuOXzBTI_EisFGo9Cz0ncEa2K0Kt8hiJwSPRIHtYAX9QCoeMj2wOXUH22zG6Y8Gq0uizQ26eH53CmMDhzdUqAR9eabduCHa-1P0fcOs6-LV3zcCuvHUHBpoF1VZ81aRNA0o-rsG-PMgSh_HhPdBBn0zfh4Q7Sh2N10qTdYF-m_qXBfPHLqCNY0bGs9dhXszsozfulwhPsBtxMECM5Nuoe7j0AB2yNaI7L7dVFztC_jqx6P7-bfGBou1li8mqIyoKFqALductW0pJtSPUNAWwrT4VPXNvD3dNigK_8WkAjC60y71q-vrCHwThi5OSokgwubUx8XI3KZOxuqbQYEqX9VOlX1qTrgZzBrZwOICFlFAS5QSfWTKGz3lSzrEXfDTjAYO8hI1rDnVfox7Qwf_pAILYVD-5ImFqGPtPlo2KjN5lwWkPSw6o-GYI0vcOm4jDyw15bSDDs_T26SfEnmIpb8fT_VMCeeDuwhz0uPp622PRYIfuKWODwQnakljN1m0sJ5DjbNezgMcLar7xVwQqXanFuyikBOq9HscMuTntjV_MJV5NB_4OwTkAwNiWDX_gIe-BpxRID55TvYj2U&amp;v=404&amp;clicktype=1">
                                            <div class="p-img"> <img width="160" height="160" data-img="1"
                                                    data-lazy-img="//img10.360buyimg.com/n2/jfs/t1/67160/40/8761/109213/5d6a90eeE2dac38b9/276a98a48f97d4b9.jpg"
                                                    class="err-product"> </div>
                                        </div>
                                        <div class="p-price"> <strong><em>¥</em><i
                                                    class="J-prom-p-46141812415">5999.00</i></strong> </div>
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/46141812415.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS80NjE0MTgxMjQxNS5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjld7xmksPq9L2aZbeaRLj6NaaZLoOEL99LDHdvFqm0UEgwd793fOQSeqpbeihjxK5TmSzb1JnGVZ8lu6QqcJXTYxsfqDuatjfsaija-rT-I_7QxJJIIuOXzBTI_EisFGo9Cz0ncEa2K0Kt8hiJwSPRIHtYAX9QCoeMj2wOXUH22zG6Y8Gq0uizQ26eH53CmMDhzdUqAR9eabduCHa-1P0fcOs6-LV3zcCuvHUHBpoF1VZ81aRNA0o-rsG-PMgSh_HhPdBBn0zfh4Q7Sh2N10qTdYF-m_qXBfPHLqCNY0bGs9dhXszsozfulwhPsBtxMECM5Nuoe7j0AB2yNaI7L7dVFztC_jqx6P7-bfGBou1li8mqIyoKFqALductW0pJtSPUNAWwrT4VPXNvD3dNigK_8WkAjC60y71q-vrCHwThi5OSokgwubUx8XI3KZOxuqbQYEqX9VOlX1qTrgZzBrZwOICFlFAS5QSfWTKGz3lSzrEXfDTjAYO8hI1rDnVfox7Qwf_pAILYVD-5ImFqGPtPlo2KjN5lwWkPSw6o-GYI0vcOm4jDyw15bSDDs_T26SfEnmIpb8fT_VMCeeDuwhz0uPp622PRYIfuKWODwQnakljN1m0sJ5DjbNezgMcLar7xVwQqXanFuyikBOq9HscMuTntjV_MJV5NB_4OwTkAwNiWDX_gIe-BpxRID55TvYj2U&amp;v=404&amp;clicktype=1">
                                            <div class="p-name"> <em>8848 钛金<font class="skcolor_ljg">手机</font> M4尊享版
                                                    智能商务加密<font class="skcolor_ljg">手机</font> 双卡双待 全网通4G 6G+128G 黑色</em>
                                            </div>
                                        </div>
                                        <div class="p-comm " style="padding:8px 10px 0"> 已有<span style="color:#005aa0"
                                                class="J-p-comm-ss-46141812415">100+</span>人评价 </div>
                                    </li>
                                    <li onclick="searchlog(1,47213371165, 16, 81)" data-lazy-advertisement-install="1">
                                        <img data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlcwIZmfdFEVmH5lFNe5ah6qGSVT7dcNb1Mrk1HLGV0LfRxmiF0Gm5-PazzBwDG31m2SnZr3uv15Yl3N_DJOFuixIy2X687Eyk4i3Vb6_zi3uMpNjEH2gnNqsDoCBFHozYN7OwB7ro1d-NX0Jdu6alYcJE7cxFHgO2_KRZQluxBfkgJDfddgjuqMYBSdKjc3SScO2abEahHXb0WmMb4as1Q8Ii3UaPif7UVbHWwW89F0t6lqwq0WOtfbyS1xMkMbFaNNLdwmpjjuYwjxlsE7oAwJptFU8AnujyIRUA6AcxcLzVELUxv4K8SATEs09U-ESk1-DxnTa9m0TcsORssLUqnaObQtR67F9ZOxSPCr2g6kQzUxuZwB-D-EnJSIVCFGKVFXkvrNZ8aRNs5PUa02GSuwTb7k426Dnwo6GzhA6TzKL88iM23mGuAEehPMRnsipIoVZ5M8E_ReFjV4D6uvEXx4vjaErcwCmvQStxU8w81T2oLnnpKA5GquAa2E7IKZoXmxeLIsjHr7swVAPVBBZlIW6HT8QTCmhRftMywjAZhsIuUzcfB0NLrSnHrOcGUdIkfNjSCUSgIT3s0lLYvCy7sDp3f3ewXQisEbYBu-ti2auwJdaKi-QKzgTPYtWzgjwhuk-J_5v64iTcFObbJ1pu3PrbJ35NItmp02zpIPE4_FNAhBd8a3VNjKOAGIEvOxb19LIn9BVr5YzUW1EHji-TFCpMtSQcEmkCX4S_p99Bcnv4GVz2whzfaWM575ZlZg423AUg0T5HfDlbCoKKhzcwI-W-5HKI1juwLd0b7nyGphmlSAX0ffLe9MwTsjjGpB1SI&amp;v=404&amp;rt=3"
                                            style="">
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/47213371165.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS80NzIxMzM3MTE2NS5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlcwIZmfdFEVmH5lFNe5ah6qGSVT7dcNb1Mrk1HLGV0LfRxmiF0Gm5-PazzBwDG31m2SnZr3uv15Yl3N_DJOFuixIy2X687Eyk4i3Vb6_zi3uMpNjEH2gnNqsDoCBFHozYN7OwB7ro1d-NX0Jdu6alYcJE7cxFHgO2_KRZQluxBfkmhci3V32riF5A4Bi1meRZihwiPEPiEMVwG-URopRThe474agODLWa8LuWVu0MGrXimoDutMyCoAN-F8XsICAdYH6VflRJtTL4lgsjSndOkc_4np-ECQbQquBzt5REboGFWyT9iBXxymQ0hTQYEiH3UZbbtXb_qW4F6kEooSocZ0sRmisjdv3a58VIPkdrvZcffkfudU7cXlfhdDFaqfNvArx5BTOERHfUPAn78VAb5y6nsO0xf4xrwunnY8mG1XS0NaJjCbJDRjLffPAlXNUeSuorZz7qValmr2h3C4Xf6eSO3pKGypD80N4VutsMK0Bc3vzSkBokGO9h_t-p_2OStO1mQcCDBndV7ZFE5GxoVCZnw-UVu4ZAYtk5-bWpUwG0mAtzNXKj24WWjwr5SN7u_erPV0XkRvkWlzf8_pz8-HYqNpJ-IHmCb9qNPMYw4btzVhjzndnI3rWn7o2S6BZIo&amp;v=404&amp;clicktype=1">
                                            <div class="p-img"> <img width="160" height="160" data-img="1"
                                                    data-lazy-img="//img10.360buyimg.com/n2/jfs/t1/38429/6/6657/82913/5cd29aa7E9c9f785d/a1a9e4897f1a512e.jpg"
                                                    class="err-product"> </div>
                                        </div>
                                        <div class="p-price"> <strong><em>¥</em><i
                                                    class="J-prom-p-47213371165">2799.00</i></strong> </div>
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/47213371165.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS80NzIxMzM3MTE2NS5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlcwIZmfdFEVmH5lFNe5ah6qGSVT7dcNb1Mrk1HLGV0LfRxmiF0Gm5-PazzBwDG31m2SnZr3uv15Yl3N_DJOFuixIy2X687Eyk4i3Vb6_zi3uMpNjEH2gnNqsDoCBFHozYN7OwB7ro1d-NX0Jdu6alYcJE7cxFHgO2_KRZQluxBfkmhci3V32riF5A4Bi1meRZihwiPEPiEMVwG-URopRThe474agODLWa8LuWVu0MGrXimoDutMyCoAN-F8XsICAdYH6VflRJtTL4lgsjSndOkc_4np-ECQbQquBzt5REboGFWyT9iBXxymQ0hTQYEiH3UZbbtXb_qW4F6kEooSocZ0sRmisjdv3a58VIPkdrvZcffkfudU7cXlfhdDFaqfNvArx5BTOERHfUPAn78VAb5y6nsO0xf4xrwunnY8mG1XS0NaJjCbJDRjLffPAlXNUeSuorZz7qValmr2h3C4Xf6eSO3pKGypD80N4VutsMK0Bc3vzSkBokGO9h_t-p_2OStO1mQcCDBndV7ZFE5GxoVCZnw-UVu4ZAYtk5-bWpUwG0mAtzNXKj24WWjwr5SN7u_erPV0XkRvkWlzf8_pz8-HYqNpJ-IHmCb9qNPMYw4btzVhjzndnI3rWn7o2S6BZIo&amp;v=404&amp;clicktype=1">
                                            <div class="p-name"> <em>OPPO Reno<font class="skcolor_ljg">手机</font> 【<font
                                                        class="skcolor_ljg">特价</font>到手价2199起+豪礼】 拍照<font
                                                        class="skcolor_ljg">手机</font> 游戏<font class="skcolor_ljg">手机
                                                    </font> 双卡双待 全网通 薄雾粉（8G+256G） 超值套餐</em> </div>
                                        </div>
                                        <div class="p-comm " style="padding:8px 10px 0"> 已有<span style="color:#005aa0"
                                                class="J-p-comm-ss-47213371165">2400+</span>人评价 </div>
                                    </li>
                                    <li onclick="searchlog(1,56228415152, 17, 81)" data-lazy-advertisement-install="1">
                                        <img data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjle8PqbT7rZsL4XeHMbC77De0z12bNeaL_hmurKYt64kr9bXniDkmaKUziXaUGrsHd_xnZMko5Z-b3o6dVFxrLWaMkQcNUE8zFicrr_GhknRVk9VBJPb2bzI_Rm_-bsnxFXdxV-jeeDrca96aKX7BADkOt7wc3CNeILwY5gMX_dExs5II0eudjkmQ78N29i0W6HzZ0xLowbmljDz5l-PYPcE1XTT_1ex5TkkE5NsiTZmCWf39a4h6owRQaBlAiLDpWynaNGL-abIdgnTo3TW03iMsTGnG7PGL6geaZCQ4rywSI9I1edyuCbHhFCEDKZM57-ACmoW2_1Mw8K2waUWSrffmDNUpafBsiCicPzCCOAPvUYOAtyW33eaM9ExKOHb2cCoeOWjFQMtcvv7J4FiqPBBF5AAdOP57FJcdujssj40qvuIMKuPuPo4QgPRcUAquDqdzr2MfDjv6jlWS4TWbqAS7ZDn-9klaojRAMNAw6T-u4an0zv6SlyhfXmEOQRc0QwjBLVDMj6w4mKe87sdCbpcRl2MFKnYl9piG8aXhGAtGnsRHbboh8NqluY4BnMyoP8Nff8b-quw7V7uUorTJL3tR_A3tuHJZVbweRSJsbudHpIVV4-dwpP1OzS5j43ra5GS_ooCEv1NqhxxO5xgtR5Qmyu71qVRe41TFGpyyXd-Ws-GhDD_GxrIcV1iHl9W6suFS8q_Fsxqn98E7teLcNM-S7MFWFhq2SJrcPARWX9y7qkUtd_cGAJ52BwI6tJPtiv6PkmFUz3cYCFEJl6iiO4hduItjmBY61NMvwZpPpkryeyqOdHJtqWrdFCB117GZ2JCWQEX4TEH5gFPa91E9dD_&amp;v=404&amp;rt=3"
                                            style="">
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/56228415152.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS81NjIyODQxNTE1Mi5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjle8PqbT7rZsL4XeHMbC77De0z12bNeaL_hmurKYt64kr9bXniDkmaKUziXaUGrsHd_xnZMko5Z-b3o6dVFxrLWaMkQcNUE8zFicrr_GhknRVk9VBJPb2bzI_Rm_-bsnxFXdxV-jeeDrca96aKX7BADkOt7wc3CNeILwY5gMX_dExs5II0eudjkmQ78N29i0W6EfphJaRQNjFXKQYhYfPp2LLHhxbV9ZS5Ob1EGwAmiiJu-rytcuYdj0bE2LKgzWHRlGqYwqziXUWOVPvAFccWYuh2ExAkJlmYiSD8UqzHberPLdNftWnUXjth24DSwsTRaooQmCJI31BI3PGYtO1BNT4eKGQrm1CLJ1-cSvTARwKYKTkVazH79nhV09EaY3diAAR2oJH6TUhgKTTp1oh1sb8PwBGSRfFaeCFBsQY78TbL-5yEEOK_5xoF9TovJeRsUZPnBml01N_9QqTSgo36oKloFEc5LR8t1MApYdCABKfzvPIH72c4e675FhgfAcjJqFUcqfnJIGZGe7HvWWp92gq9Kgloccc_V1etTqO15j4U1YRjiyCWUjYI3vNK9jDsMcARMWTzIys_MwHyxPN8BFTdqb_6XCwXU7cQI7lQO90DvSLhARcPB3OCDQuJs0TZ7L_miB-n6Y3hWtc9Nq_oOm715w7Zf6fRKidmgsy-PsIw&amp;v=404&amp;clicktype=1">
                                            <div class="p-img"> <img width="160" height="160" data-img="1"
                                                    data-lazy-img="//img12.360buyimg.com/n2/jfs/t1/82485/10/9248/143761/5d70c66eE1d4ef674/0445a58d95fb6a74.jpg"
                                                    class="err-product"> </div>
                                        </div>
                                        <div class="p-price"> <strong><em>¥</em><i
                                                    class="J-prom-p-56228415152">1509.00</i></strong> </div>
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/56228415152.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS81NjIyODQxNTE1Mi5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjle8PqbT7rZsL4XeHMbC77De0z12bNeaL_hmurKYt64kr9bXniDkmaKUziXaUGrsHd_xnZMko5Z-b3o6dVFxrLWaMkQcNUE8zFicrr_GhknRVk9VBJPb2bzI_Rm_-bsnxFXdxV-jeeDrca96aKX7BADkOt7wc3CNeILwY5gMX_dExs5II0eudjkmQ78N29i0W6EfphJaRQNjFXKQYhYfPp2LLHhxbV9ZS5Ob1EGwAmiiJu-rytcuYdj0bE2LKgzWHRlGqYwqziXUWOVPvAFccWYuh2ExAkJlmYiSD8UqzHberPLdNftWnUXjth24DSwsTRaooQmCJI31BI3PGYtO1BNT4eKGQrm1CLJ1-cSvTARwKYKTkVazH79nhV09EaY3diAAR2oJH6TUhgKTTp1oh1sb8PwBGSRfFaeCFBsQY78TbL-5yEEOK_5xoF9TovJeRsUZPnBml01N_9QqTSgo36oKloFEc5LR8t1MApYdCABKfzvPIH72c4e675FhgfAcjJqFUcqfnJIGZGe7HvWWp92gq9Kgloccc_V1etTqO15j4U1YRjiyCWUjYI3vNK9jDsMcARMWTzIys_MwHyxPN8BFTdqb_6XCwXU7cQI7lQO90DvSLhARcPB3OCDQuJs0TZ7L_miB-n6Y3hWtc9Nq_oOm715w7Zf6fRKidmgsy-PsIw&amp;v=404&amp;clicktype=1">
                                            <div class="p-name"> <em>华为畅享10plus 智能<font class="skcolor_ljg">手机</font>
                                                    超高清全视屏 前置悬浮式镜头 4800万超广角AI三摄 全网通4GB+128GB翡冷翠</em> </div>
                                        </div>
                                        <div class="p-comm " style="padding:8px 10px 0"> 已有<span style="color:#005aa0"
                                                class="J-p-comm-ss-56228415152">0</span>人评价 </div>
                                    </li>
                                    <li onclick="searchlog(1,11481305161, 18, 81)" data-lazy-advertisement-install="1">
                                        <img data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlcZVAewjQE57bT7hP2tsKLRw6bTJaFECpq5D9hsgE77ZAQQIGnVhXx_6JDhPpUX2L67NxCvgnAhRU5P8NGiRmh-kRDEoOfRJi5UnT3CsRq5srbQ_414Y8aex3Ye10efyPNkz88xwFTl-51xKmb-M5_i9wCureRnZAP64u59zUkU5EykmcX3o1rwWseoxWauMucejaciJ7Y50wsCFgGSm6Vw4YgsaHEcYKd7D-2LB7MR9N8P63Lz8ZL8LNWoUNJl5iznKDCGm5qjL_Xr4-6WWVNtboA6gIuKtN5K9QbHnBi5bt7Rs9V2dYvGQK73Tx2HwqcQarwsLy6C5y7PJUZ-7LltReJhE_IL9-7EjR5giHMlwFbP8qZ8qEuLbfXE5fyG75Em4xc2SJNY0xfKlWbvGTBJ_Fq-Srx-uocszKVIVo9NLgtd46VHrJE2PL_yZGwA1KeHeI1u7aN-zlFnkFif7d_euEV0BnD2sej4jvl2wcZqQP0RXH3ARvcBdiCqfY31GJ1ZN1XFRpFmstPSrq4h-P6QA4udVgvwclkasxeEjL3PujB0G5pdyN08HgOBud1WTCclHHEQacelc0n5fYNWkF8nWCRsx0PICF3kub0PdllCGLvqWWf1ilrgt8Aosz6Sx96LoZJnU2CKomurkXSv2OAmiQvAhyPhSdyKldvh1wjevaAn6Ttf00ATJjLbi9Lp6zj3SCTPRnEY_KmF2hBgIgqrVfZl0l9OJ13r0f6xCBYJQL0LPUZSyDdGjWAh4xi7QexfgGNTjDZPWjnegtmgE8YJEK4yuyJEiStuLZnjCs8znu89W663JPoD4QZBqP7XQyMQ2sFDSL6s5GIQYMhDGvDR&amp;v=404&amp;rt=3"
                                            style="">
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/11481305161.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMTQ4MTMwNTE2MS5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlcZVAewjQE57bT7hP2tsKLRw6bTJaFECpq5D9hsgE77ZAQQIGnVhXx_6JDhPpUX2L67NxCvgnAhRU5P8NGiRmh-kRDEoOfRJi5UnT3CsRq5srbQ_414Y8aex3Ye10efyPNkz88xwFTl-51xKmb-M5_i9wCureRnZAP64u59zUkU5EykmcX3o1rwWseoxWauMueJhdXDP_CMOOnyDiDOrfbcbGTZWJpusgvPicz1kV5plllVoI_9K66_7ogne-J-9XcGGBMZaGiwtnt_UtkuIbULKd0HhVPYglQxpP_DP9P-kG5K4ouC4irlje21hPmuR32CCPszd3WzQ9Ev2VKZdxoee51kL_5ssThu_CQz5xTBUwqUBl0lu0WQmh_m1_R0gXU08AMCMgKmU3yZ07YNtKDCBjnqe2cYyzbM9YLwDfZaFJZI5OUjKj_CtrKqjZAvsLV05wofbVSL3NC3T7Mm8jaPZe87Q1ShVPE5xkE-TtsxGWXgJ6HTdZ6bkf9fBD_K6oNLmi65k-YEdMvP8W02245AYIU3nDUksZysZoLT44DmixOy-zjw4TZ5rNP7eA40evEEgoJ7oru4lI3RNLqbl-cgeZZt2Rw50imb2LcRf80rF6G9oLgdA5935ykEIYO2k3pdyerwR1ayQY5evA3L1T32&amp;v=404&amp;clicktype=1">
                                            <div class="p-img"> <img width="160" height="160" data-img="1"
                                                    data-lazy-img="//img11.360buyimg.com/n2/jfs/t1/65972/31/9282/124271/5d706ca7E8bb63160/e910485f2a73de67.jpg"
                                                    class="err-product"> </div>
                                        </div>
                                        <div class="p-price"> <strong><em>¥</em><i
                                                    class="J-prom-p-11481305161">99.00</i></strong> </div>
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/11481305161.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS8xMTQ4MTMwNTE2MS5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjlcZVAewjQE57bT7hP2tsKLRw6bTJaFECpq5D9hsgE77ZAQQIGnVhXx_6JDhPpUX2L67NxCvgnAhRU5P8NGiRmh-kRDEoOfRJi5UnT3CsRq5srbQ_414Y8aex3Ye10efyPNkz88xwFTl-51xKmb-M5_i9wCureRnZAP64u59zUkU5EykmcX3o1rwWseoxWauMueJhdXDP_CMOOnyDiDOrfbcbGTZWJpusgvPicz1kV5plllVoI_9K66_7ogne-J-9XcGGBMZaGiwtnt_UtkuIbULKd0HhVPYglQxpP_DP9P-kG5K4ouC4irlje21hPmuR32CCPszd3WzQ9Ev2VKZdxoee51kL_5ssThu_CQz5xTBUwqUBl0lu0WQmh_m1_R0gXU08AMCMgKmU3yZ07YNtKDCBjnqe2cYyzbM9YLwDfZaFJZI5OUjKj_CtrKqjZAvsLV05wofbVSL3NC3T7Mm8jaPZe87Q1ShVPE5xkE-TtsxGWXgJ6HTdZ6bkf9fBD_K6oNLmi65k-YEdMvP8W02245AYIU3nDUksZysZoLT44DmixOy-zjw4TZ5rNP7eA40evEEgoJ7oru4lI3RNLqbl-cgeZZt2Rw50imb2LcRf80rF6G9oLgdA5935ykEIYO2k3pdyerwR1ayQY5evA3L1T32&amp;v=404&amp;clicktype=1">
                                            <div class="p-name"> <em>尼凯恩（neken） EN3 老人机超长待机三防直板老年<font
                                                        class="skcolor_ljg">手机</font>大屏大字大声移动电信版按键男女款老人<font
                                                        class="skcolor_ljg">手机</font> 黑色【移动版】</em> </div>
                                        </div>
                                        <div class="p-comm " style="padding:8px 10px 0"> 已有<span style="color:#005aa0"
                                                class="J-p-comm-ss-11481305161">13万+</span>人评价 </div>
                                    </li>
                                    <li onclick="searchlog(1,47584161597, 19, 81)" data-lazy-advertisement-install="1">
                                        <img data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjleuq96cwG4JqzkfkFlvoMbnU6uX_VgQ2Wk7pkDVwJrYzV91uA90G6rl3fG_mhZyQ8czIfo9Ov1TA4n4uRbSQzXmjPwLpC8pLjYRuP-ytHjzT2QiIT2STdzkiUBNV_bWmkqG3VqJEvLpXM0C0_TwQX5Cw_IhCaIzJ6DwgIB01J-8GJmz0bhwpJVal70RnGwTvpqoj9z-JKZc15KntpeB10AubL0egzS4BAMrV12ppJc0uD4K-IgIEhhva92cOxR4cPhjZmzCzSLjcaQw4__y28g3Kg3RQRXhdGFM5J0louDYOXfJPNhRHnsU1rX8kA5FO9Lt9OysEsf-Xfn3wyTaInmnVslakD8UxHsx8MLikqR80ftUnQF3-I7xOez5tXcmr4uKTqC50I12t6jskks_V4BoE_K4g0xtvB69bROzYT2NrC_PLxDXoOnbKrbI13UJR1pSZRenON2D995Z9DX3-ctNRnQLdriuQdo4Rt0Og1s_DwcLPXCieE4aJWzOA_91Dv5N057aHQOmBBX7ntCXacpyPrscYXqEsQNbyxFTHiRDB-FZtc-IxRhddIzDSykXoMg_Br1iL8JzKoJir0WWgGWABgY_sxbwIvEt2X7DhLEoOxhPkacqN78muT0orL3LBL184a0WplWrL0Wh67q_l0pFfnQ2EunJnuOf3KXYxdV4E5VrYPLBGXbLUO55C0M9eZP3yzJQuit9sRWmZOeBHdhR012YL4bf7GWam22uHXqzZ4g9f-HSvTLJuxWPouFM4f3-FmD1mpFmozqadODPkxuR5WzSfU2qjRwEF9uZowjhJGt0vNLVrfmAqLChY9pDi94&amp;v=404&amp;rt=3"
                                            style="">
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/47584161597.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS80NzU4NDE2MTU5Ny5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjleuq96cwG4JqzkfkFlvoMbnU6uX_VgQ2Wk7pkDVwJrYzV91uA90G6rl3fG_mhZyQ8czIfo9Ov1TA4n4uRbSQzXmjPwLpC8pLjYRuP-ytHjzT2QiIT2STdzkiUBNV_bWmkqG3VqJEvLpXM0C0_TwQX5Cw_IhCaIzJ6DwgIB01J-8GJpvflApvKWILb548TUzkp5mcbfTRaz9TjPrOZLX4g52hoz29t6yEalGYp6MVcm05OE667KfYPo264VLeBSfefIPYtonSUtgjaww9mKPR8FTO4EibLOufK9-Avxs2XQYL3dHBB6CTzHuUxu7JW6ud8poamNT8R3U_AiR9HrAfRe5buF-pdxGT-58aCitAbboQqyH-XzmmGjWLpdQ_pNYn84RsITd-c7DoZTFWa7gnsBmmsj8ScISjaSiBHLlTcOW6_RDYJk1WgOzXQBWzDsTWJBmOVFv9ZJbXF6q6mItnyn40sNa0OfFf6clYq96m9loMuQxRW9aEr3sl_AczoSVu4KQIHxrm8BSYN7TaJyCSl_mtQWaJuKgnyXhVzp8_R3qCb-wcyfmrt_3920gCVuk-BhtK_M4XDUgpwoU-YQv3Wzxv4uqA2qWEiyodJnanb4AWR1mn-4yP5FvMddQMlgdDl-hzs5jUaOepVRyE83AaE7D&amp;v=404&amp;clicktype=1">
                                            <div class="p-img"> <img width="160" height="160" data-img="1"
                                                    data-lazy-img="//img12.360buyimg.com/n2/jfs/t1/68451/12/17/322749/5cd28ca7E80c65425/b94841bb277b9f09.png"
                                                    class="err-product"> </div>
                                        </div>
                                        <div class="p-price"> <strong><em>¥</em><i
                                                    class="J-prom-p-47584161597">999.00</i></strong> </div>
                                        <div class="p-client-click" data-clickurl="https://item.jd.com/47584161597.html"
                                            data-clientclickurl="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9pdGVtLmpkLmNvbS80NzU4NDE2MTU5Ny5odG1s&amp;log=UJRDoYg54F7fyPa-e6GU3JCDJrYsdhONzU10l0apjleuq96cwG4JqzkfkFlvoMbnU6uX_VgQ2Wk7pkDVwJrYzV91uA90G6rl3fG_mhZyQ8czIfo9Ov1TA4n4uRbSQzXmjPwLpC8pLjYRuP-ytHjzT2QiIT2STdzkiUBNV_bWmkqG3VqJEvLpXM0C0_TwQX5Cw_IhCaIzJ6DwgIB01J-8GJpvflApvKWILb548TUzkp5mcbfTRaz9TjPrOZLX4g52hoz29t6yEalGYp6MVcm05OE667KfYPo264VLeBSfefIPYtonSUtgjaww9mKPR8FTO4EibLOufK9-Avxs2XQYL3dHBB6CTzHuUxu7JW6ud8poamNT8R3U_AiR9HrAfRe5buF-pdxGT-58aCitAbboQqyH-XzmmGjWLpdQ_pNYn84RsITd-c7DoZTFWa7gnsBmmsj8ScISjaSiBHLlTcOW6_RDYJk1WgOzXQBWzDsTWJBmOVFv9ZJbXF6q6mItnyn40sNa0OfFf6clYq96m9loMuQxRW9aEr3sl_AczoSVu4KQIHxrm8BSYN7TaJyCSl_mtQWaJuKgnyXhVzp8_R3qCb-wcyfmrt_3920gCVuk-BhtK_M4XDUgpwoU-YQv3Wzxv4uqA2qWEiyodJnanb4AWR1mn-4yP5FvMddQMlgdDl-hzs5jUaOepVRyE83AaE7D&amp;v=404&amp;clicktype=1">
                                            <div class="p-name"> <em>欧奇（OUKI）OKP9 移动联通电信4G 全网通 大屏商务智能<font
                                                        class="skcolor_ljg">手机</font> 超长待机双卡双待 限量版 黑色</em> </div>
                                        </div>
                                        <div class="p-comm " style="padding:8px 10px 0"> 已有<span style="color:#005aa0"
                                                class="J-p-comm-ss-47584161597">20+</span>人评价 </div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <div id="J_recommendGoods" class="ab-goods" style="display: none;">
                            <div class="mt">
                                <h3>精品推荐</h3>
                            </div>
                            <div class="mc"></div>
                        </div>

                        <div class="promo-pic-adbox u-ad-wrap" style="" data-lazy-advertisement-install="1"><span
                                class="u-ad"></span>
                            <h5 class="hd">商家精选</h5>
                            <div class="bd">
                                <div id="J_promWrap_576">
                                    <div class="mc">
                                        <div class="ab-pic"><img
                                                data-lazy-advertisement="https://im-x.jd.com/dsp/np?log=Pih7o3ThIzHBK5Q9B4skiOtim2DcUGtMiYD2mCBEX7iz_bptHkkBHdXpHSi_--zzXjjS6mPYsjXvJ1whmkfDMcNpYazGCpZ3oUadQiA0s8hPHYSZbyS8KSYBV0wbmhUYznwHZWlwZn5p6rEkjCUBAuut_DipWoUrFyZ8_aoJY7-Sm1tY4OUZgiql8yjSvtgltejEmiiHI0YGF72_6qX62obKu8UNlJ11KHNBxCmlI4AaW8ZGzaUoxSYP3_1EU9SYj4ZSIIdzs_l8kbO5zUZQ0K8NZzAmX7yDoSxZBWlT_dDPUj3D3gak7mJTTm17T-Bh2EPA1_v54KpOw3aC9ElBiqpF_Dy2pBear_mZDg4HAF8ESD9OYhFxUerQhPawkEsACrb7rE8mF_7e7d-gVdhch_-KPBmNcUMnaXSOSgbt8as1Nm7SAzOvKo4gFOo_UcQuvHKQ_TCQGSRH_ZXwT_EYJLp_RA3qIQEcwgzr6VI8p1LUSmuB2l36qFJ3Rr9kXK0Y4pegonyVYZfMpWi22Q7FoKuTmHUAMrKcD40Iq7s3XLVBgkXuma7--j-8TKaUo8pQQhomTJ5a0XXESXyHeUq4vhKFZLTqQNtk3Afj2gT-ru7OxEIn9MuR4wnOJHgWTABcohMMrzmnmAhHPY1J9vOXuiBrof9vy20Bbl7DXdSzae6NU9nS7lb8gYkYKAXd-SxGiGf1xoppDTv8XrtLBJhhY0k0tL2BzYrwfLECwBmdITjNyk5fosdxcF862pzM8QL6uyZ6MPLRwSSp4fdwuliDyEsPPDoduAbUaWXsAvJLuXQefab_sz1bdLAlKdcGNlq00oT6vXtg62pk8hg5rNFARqNxR-CIl--dBwO3pMDBZec&amp;v=404"><a
                                                data-exposal="https://im-x.jd.com/dsp/np?log=Pih7o3ThIzHBK5Q9B4skiOtim2DcUGtMiYD2mCBEX7iz_bptHkkBHdXpHSi_--zzXjjS6mPYsjXvJ1whmkfDMcNpYazGCpZ3oUadQiA0s8hPHYSZbyS8KSYBV0wbmhUYznwHZWlwZn5p6rEkjCUBAuut_DipWoUrFyZ8_aoJY7-Sm1tY4OUZgiql8yjSvtgltejEmiiHI0YGF72_6qX62obKu8UNlJ11KHNBxCmlI4AaW8ZGzaUoxSYP3_1EU9SYj4ZSIIdzs_l8kbO5zUZQ0K8NZzAmX7yDoSxZBWlT_dDPUj3D3gak7mJTTm17T-Bh2EPA1_v54KpOw3aC9ElBiqpF_Dy2pBear_mZDg4HAF8ESD9OYhFxUerQhPawkEsACrb7rE8mF_7e7d-gVdhch_-KPBmNcUMnaXSOSgbt8as1Nm7SAzOvKo4gFOo_UcQuvHKQ_TCQGSRH_ZXwT_EYJLp_RA3qIQEcwgzr6VI8p1LUSmuB2l36qFJ3Rr9kXK0Y4pegonyVYZfMpWi22Q7FoKuTmHUAMrKcD40Iq7s3XLVBgkXuma7--j-8TKaUo8pQQhomTJ5a0XXESXyHeUq4vhKFZLTqQNtk3Afj2gT-ru7OxEIn9MuR4wnOJHgWTABcohMMrzmnmAhHPY1J9vOXuiBrof9vy20Bbl7DXdSzae6NU9nS7lb8gYkYKAXd-SxGiGf1xoppDTv8XrtLBJhhY0k0tL2BzYrwfLECwBmdITjNyk5fosdxcF862pzM8QL6uyZ6MPLRwSSp4fdwuliDyEsPPDoduAbUaWXsAvJLuXQefab_sz1bdLAlKdcGNlq00oT6vXtg62pk8hg5rNFARqNxR-CIl--dBwO3pMDBZec&amp;v=404"
                                                onclick="JA.tracker.adclick('4715a5ee5f0e80be^v2.8^SWC^576^^114563055^^261060483^https://oukitel.jd.com/^bca7a4da-aeed-4340-92d7-9ebd005543d4^1^0^663682^')"
                                                target="_blank"
                                                href="https://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9vdWtpdGVsLmpkLmNvbS8&amp;log=Pih7o3ThIzHBK5Q9B4skiOtim2DcUGtMiYD2mCBEX7iz_bptHkkBHdXpHSi_--zzXjjS6mPYsjXvJ1whmkfDMcNpYazGCpZ3oUadQiA0s8hPHYSZbyS8KSYBV0wbmhUYznwHZWlwZn5p6rEkjCUBAuut_DipWoUrFyZ8_aoJY7-Sm1tY4OUZgiql8yjSvtgltejEmiiHI0YGF72_6qX62j32evZik6xrrMITWlitUbOVs6f3Ig84nG1J9Yt8X5KjXuBwPNhsUfGuwyvrP-3uUZdR6T-N9eBQHIqdTO7WkygBnbDyffXcLmjwiYrKjgmeRmYzImQAro8HZgpV9pwWkQaim_R2r2uTIHs3T9d0p9C6sHvkXZYbj2MVS_EPfGW7RqghMZtTP7DNnMQ16jKBmgn-CoRTm9HoRzjafmHr8PZ4aD8ob3MstRO2T1f4CoWkztCm4_Pyd9KIKId4S19qsurfpLTxYmCjhOj7-ObvP3rH_kvcNWNeEcilqVTRP15YtJHA_42ezrCtvjZNGyPZAaaq5_mb7IMOx777FaxjykpiW8zP7GJ4g9Rus-tSZFiNsjYYub3WuSdqe9o_Oy-HUPDajW0bobfjhJxGGAGtemCg_7Cfbblh2lw1gyrUOlsxRkX3dYpAMI5OEmhjqP-y2FS94g_QgG1c3Bg84zzwOMIZHj5ltqYosBpS9Ia1bu_q&amp;v=404">
                                                <img width=""
                                                    src="//img13.360buyimg.com/pop/s180x180_jfs/t25663/341/336165168/533136/f566ed44/5b6bf342N7472161c.png"></a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div id="miaozhen8148" class="ab-pic" style="display: block;"><a
                                href="https://ccc-x.jd.com/dsp/cpd?ext=aHR0cHM6Ly9jaGFvc2hpLmpkLmNvbQ&amp;log=JF5rMUAKXlLMuE_-1qw2RKwu9W82n03RnztIpYfC-NVWZuaHLhAWyfY2fGI8hkyp8V9SnsECqPTeMXyEuwXaBkCBlHIHvrh5F8QqDQ2uoAc7qp-b5F4ejVQOJrpfQSis9xpcBjNqytqksohq0K1nU7HIdnlvrBqmb-9MpiwynWjM5vo3G87QlELrliJPeKBHHFjktw0DN0JDuQCSAT3Vl-iNXNXaFPvjg9At8fDAfejL3IobmXfi6Hqkkm0wuQdYHNPWRpPl77VRxiZ3N3KjCyKZfwmepCo_uS3ww02TIVegulJlKocmSlXZIIq9aoRUg3tdIBiJa6WAlQVVtVwQ5XGpx9iZlQSjuvjeVdM7ZGbN7ATDU0UMyVgXWqf2I-EzIsATB0qmzEYgno3NxbHji1i_Askj49Fb_ZL1ZIPrrTpy998hV1Lqemilu6Djph6XDoEq8_md_72EVryOtcmoYR02ZhVdetAyu_Ezd5iQdcQVxY-4QlzP8bKXheEKOk_xxBdd8luHen1W-DjIc-XbZyORmkjc27XuU_wG-_PrX2N-hRArmc3dwcVM8RnHrj9um7m8xTZzflC5YtDusonWg1-5Vg_sANQQXkrn-xRtVKeSUWjmwsqWUdquGOb_4ASM4dHhR-w8WOhQcEcSoixHUDXqP54TPWpbAgVzHtiIOU_liUPF9-iS-tTqn8rCRAsH"
                                target="_blank" title=""><img
                                    src="//img12.360buyimg.com/da/jfs/t4996/58/289103053/49243/e6acdadd/58de3342Na3c2f0b0.jpg"
                                    width="180" height="240"></a></div>
                    </div>
                </div>
                <span class="clr"></span>
            </div>
            <script>
                LogParm = {
                    result_count: '5787',
                    ab: '0000',
                    front_cost: '599',
                    back_cost: '154',
                    ip: '134.85',
                    cid: 655,
                    psort: 0,
                    page: '1',
                    ekey: '',
                    ev: '0',
                    rec_type: '0',
                    rel_cat2: '653,13767,6880',
                    rel_cat3: '655,13768,6881',
                    log_id: '1567915175.80521',
                    expand: 'adwShow=1$double=1$wq=手机$pvid=c24a5c4a284f400cb3a9e1ab8ed56abe',
                    mtest: 'g_lf,qpv2,qpt8,qpz6,~',
                    word: '',
                    sig: 'HWW+OHo3XWa9EssDUf46QB2M3aMMya7/FTN1vdG1vwh1lz7O4EjQkNvfNQC4sg80qDKs8iqf2DZ2C54OUoNdCNtMBBr8ylG3+uyB5Xa6pPm4T7f8MT9IN60DAor4txw1s/+WQjWVOOQJh7NmofIeECD4cCkG5UmodKHznNwoZg0='
                };
                SEARCH.item_count = 60;
                SEARCH.click = 0;
                SEARCH.adv_param = {
                    page: "1",
                    page_count: "97",
                    psort: 0,
                    cid1: 0,
                    cid2: 653,
                    cid3: 655,
                    lazyload: 1
                };
                SEARCH.base_url =
                    'keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655';
                setTimeout(function () {
                    var b = {};
                    b.i = "1567915175.80521";
                    b.h = "653,13767,6880";
                    b.k = "手机";
                    b.c = "655";
                    b.m = "03a3eb6de923487884437b88d52d5890";
                    var a = [];
                    $("#J_crumbsBar").find("a.crumb-select-item").each(function () {
                        a.push($(this).find("b").html().replace("：", "::") + $(this).attr("title")
                            .replace(/、/g, "||"))
                    });
                    b.s = a.join(";;") + (a.length ? ";;" : "");
                    var c = [];
                    $("#J_selector").find(".J_selectorLine").each(function () {
                        var f = $(this),
                            e = f.find(".sl-key").text().replace("：", "::"),
                            d = [];
                        if (e == "高级选项::") {
                            f.find("a.trig-item").each(function (g) {
                                e = $(this).text() + "::";
                                d = [];
                                f.find(".J_valueList").eq(g).find("a").each(function () {
                                    d.push(e == "颜色::" ? $(this).attr("title") : e ==
                                        "其他分类::" ? $(this).attr("data-v") : $(this)
                                        .text())
                                });
                                c.push(e + d.join(",,"))
                            })
                        } else {
                            if (e == "品牌::") {
                                f.find(".J_valueList li").each(function () {
                                    d.push(this.id.replace("brand-", ""))
                                })
                            } else {
                                if (e == "颜色::") {
                                    f.find(".J_valueList a").each(function () {
                                        d.push($(this).attr("title"))
                                    })
                                } else {
                                    if (f.hasClass("s-category")) {
                                        f.find(".J_valueList a").each(function () {
                                            d.push($(this).attr("data-v"))
                                        })
                                    } else {
                                        f.find(".J_valueList a").each(function () {
                                            d.push($(this).text())
                                        })
                                    }
                                }
                            }
                            c.push(e + d.join(",,"))
                        }
                    });
                    b.u = c.join(";;") + (c.length ? ";;" : "");
                    $.post("attrlog.php", b, function () {})
                }, 500);
            </script>
            <script>
                $.get("im.php?r=1110508747&t=1567915175.7901&cs=136a1e46f818966da14cba096a0d433c");
            </script>
        </div>
    </div>
    <div class="w" data-lazyload-fn="0">
        <div class="m-box-s1 rec-goods-chosen u-ad-wrap hide" id="J_promGoodsWrap_292">
            <span class="u-ad"></span>
            <div class="mt"><strong class="mt-title">商品精选</strong></div>
            <div class="mc"></div>
        </div>
    </div>
    <div class="w">
        <div class="bottom-search">
            <div class="form-group">
                <div class="fg-line search-ext">
                    <div class="fg-line-key"><span>您是不是要找：</span></div>
                    <div class="fg-line-value" clstag="search|keycount|search|qpsearch"><a
                            onclick="searchlog(1,0,0,62,'华为')"
                            href="Search?keyword=%E5%8D%8E%E4%B8%BA&amp;enc=utf-8&amp;spm=2.1.0"
                            class="fore">华为</a><b>|</b><a onclick="searchlog(1,0,1,62,'华为手机')"
                            href="Search?keyword=%E5%8D%8E%E4%B8%BA%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;spm=2.1.1">华为手机</a><b>|</b><a
                            onclick="searchlog(1,0,2,62,'手机自营')"
                            href="Search?keyword=%E6%89%8B%E6%9C%BA%E8%87%AA%E8%90%A5&amp;enc=utf-8&amp;spm=2.1.2">手机自营</a><b>|</b><a
                            onclick="searchlog(1,0,3,62,'小米')"
                            href="Search?keyword=%E5%B0%8F%E7%B1%B3&amp;enc=utf-8&amp;spm=2.1.3">小米</a><b>|</b><a
                            onclick="searchlog(1,0,4,62,'二手手机')"
                            href="Search?keyword=%E4%BA%8C%E6%89%8B%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;spm=2.1.4">二手手机</a><b>|</b><a
                            onclick="searchlog(1,0,5,62,'手机5g手机')"
                            href="Search?keyword=%E6%89%8B%E6%9C%BA5g%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;spm=2.1.5">手机5g手机</a><b>|</b><a
                            onclick="searchlog(1,0,6,62,'荣耀')"
                            href="Search?keyword=%E8%8D%A3%E8%80%80&amp;enc=utf-8&amp;spm=2.1.6">荣耀</a><b>|</b><a
                            onclick="searchlog(1,0,7,62,'苹果')"
                            href="Search?keyword=%E8%8B%B9%E6%9E%9C&amp;enc=utf-8&amp;spm=2.1.7">苹果</a><b>|</b><a
                            onclick="searchlog(1,0,8,62,'苹果手机')"
                            href="Search?keyword=%E8%8B%B9%E6%9E%9C%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;spm=2.1.8">苹果手机</a><b>|</b><a
                            onclick="searchlog(1,0,9,62,'oppo')"
                            href="Search?keyword=oppo&amp;enc=utf-8&amp;spm=2.1.9">oppo</a><b>|</b><a
                            onclick="searchlog(1,0,10,62,'vivo')"
                            href="Search?keyword=vivo&amp;enc=utf-8&amp;spm=2.1.10">vivo</a><b>|</b><a
                            onclick="searchlog(1,0,11,62,'小米9')"
                            href="Search?keyword=%E5%B0%8F%E7%B1%B39&amp;enc=utf-8&amp;spm=2.1.11">小米9</a><b>|</b><a
                            onclick="searchlog(1,0,12,62,'华为p30')"
                            href="Search?keyword=%E5%8D%8E%E4%B8%BAp30&amp;enc=utf-8&amp;spm=2.1.12">华为p30</a><b>|</b><a
                            onclick="searchlog(1,0,13,62,'小米手机')"
                            href="Search?keyword=%E5%B0%8F%E7%B1%B3%E6%89%8B%E6%9C%BA&amp;enc=utf-8&amp;spm=2.1.13">小米手机</a>
                    </div>
                </div>
                <div class="fg-line re-search">
                    <div class="fg-line-key"><b>重新搜索：</b></div>
                    <div class="fg-line-value">
                        <input id="key-re-search" class="input-txt input-XL" type="text" placeholder="搜索" value="手机"
                            onkeydown="javascript:if(event.keyCode==13){searchlog(1,0,0,60);search('key-re-search');}">
                        <a class="btn btn-primary btn-XL" href="javascript:search('key-re-search')"
                            onclick="searchlog(1,0,0,60)">搜索</a>
                        <a class="link" href="javascript:surveyShow()">说说我使用搜索的感受</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="w">
        <div id="footmark" class="footmark" data-lazyload-fn="0"></div>
    </div>
    <div class="w" id="J_bottom-ad">
        <div class="m bottom-ad" id="J_promWrap_230"> <a target="_blank"
                href="http://ccc-x.jd.com/dsp/nc?ext=aHR0cHM6Ly9wcm8uamQuY29tL21hbGwvYWN0aXZlL0s0UHJtc05iZDVSaFJpaUZ0WG1zclBSZ0ZxZC9pbmRleC5odG1s&amp;log=MR48M6_9sphbWNRFbBBQncOEpWq18-Yu28io0MGWNP0uUSICN9roq9BREmJwd4mJKJ93iCYs1AbC6kW1paDswNniBMzupe7Fw0sJCSmhAb3t9j6UkPPA8-iz0D_22CkUvPGQUvcaFqB2AHAWivA5bEBoFmzqHySvvaXWDIwG1Mea_2vsYpVGMPekPa6l4V2VymDYuE5P_HSpNifar4IFDk4mTP2sauWojyPXNJYX5oMPoCVJpFMo28r5IFBdJxNHE3rC7a1CtpH-iPpuzw5ZVYeajqAErl0e1cgDUW83ULZBzyBa-WkBi-Uv-6hEVAeiTFjK_thoOwaWZn5Fk774jDeZu1Nuw7Qi0OYIsZHvJ7eEth54mjSY-ZED5eg3uF1LL-5VZ5sDj1Wp2sksz36RJFKzP_SKwEpT5QAHufn8tZFuFXIrZnQx3LpIB2Way1ITbW0WJPEDOT6uvvVWF9vH4ajXcQ3-5Brk8ExwqhFtIUw&amp;v=404">
                <img width="1390"
                    src="//img30.360buyimg.com/pop/jfs/t1/84279/5/6923/50054/5d52326fEfbd38abd/9ddbb27dc30e1be9.jpg">
            </a></div>
    </div>
    <!--service start-->
    <div id="service-2017">
        <div class="w">
            <ol class="slogen">
                <li class="item fore1">
                    <i>多</i>品类齐全，轻松购物
                </li>
                <li class="item fore2">
                    <i>快</i>多仓直发，极速配送
                </li>
                <li class="item fore3">
                    <i>好</i>正品行货，精致服务
                </li>
                <li class="item fore4">
                    <i>省</i>天天低价，畅选无忧
                </li>
            </ol>
        </div>
        <div class="jd-help">
            <div class="w">
                <div class="wrap">
                    <dl class="fore1">
                        <dt>购物指南</dt>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-29.html">购物流程</a>
                        </dd>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-151.html">会员介绍</a>
                        </dd>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-297.html">生活旅行/团购</a>
                        </dd>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//help.jd.com/user/issue.html">常见问题</a>
                        </dd>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-136.html">大家电</a>
                        </dd>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//help.jd.com/user/custom.html">联系客服</a>
                        </dd>
                    </dl>
                    <dl class="fore2">
                        <dt>配送方式</dt>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-81-100.html">上门自提</a>
                        </dd>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-81.html">211限时达</a>
                        </dd>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/103-983.html">配送服务查询</a>
                        </dd>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/109-188.html">配送费收取标准</a>
                        </dd>
                        <dd>
                            <a target="_blank" href="//help.joybuy.com/help/question-list-201.html">海外配送</a>
                        </dd>
                    </dl>
                    <dl class="fore3">
                        <dt>支付方式</dt>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-172.html">货到付款</a>
                        </dd>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-173.html">在线支付</a>
                        </dd>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-176.html">分期付款</a>
                        </dd>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-174.html">邮局汇款</a>
                        </dd>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-175.html">公司转账</a>
                        </dd>
                    </dl>
                    <dl class="fore4">
                        <dt>售后服务</dt>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/321-981.html">售后政策</a>
                        </dd>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-132.html">价格保护</a>
                        </dd>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/130-978.html">退款说明</a>
                        </dd>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//myjd.jd.com/repair/repairs.action">返修/退换货</a>
                        </dd>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//help.jd.com/user/issue/list-50.html">取消订单</a>
                        </dd>
                    </dl>
                    <dl class="fore5">
                        <dt>特色服务</dt>
                        <dd>
                            <a target="_blank" href="//1paipai.jd.com">夺宝岛</a>
                        </dd>
                        <dd>
                            <a target="_blank" href="//help.jd.com/user/issue/list-134.html">DIY装机</a>
                        </dd>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//fuwu.jd.com/">延保服务</a>
                        </dd>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//o.jd.com/market/index.action">京东E卡</a>
                        </dd>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//mobile.jd.com/">京东通信</a>
                        </dd>
                        <dd>
                            <a rel="nofollow" target="_blank" href="//smart.jd.com/">京鱼座智能</a>
                        </dd>
                    </dl>
                    <span class="clr"></span>
                </div>
            </div>
        </div>
    </div>
    <!--service end-->
    <!--footer start-->
    <div id="footer-2017" includefile_footer_id="1002">
        <div class="w">
            <div class="copyright_links">
                <p>
                    <a href="//about.jd.com" target="_blank">关于我们</a><span class="copyright_split">|</span>
                    <a href="//about.jd.com/contact/" target="_blank">联系我们</a><span class="copyright_split">|</span>
                    <a href="//help.jd.com/user/custom.html" target="_blank">联系客服</a><span
                        class="copyright_split">|</span>
                    <a href="//lai.jd.com" target="_blank">合作招商</a><span class="copyright_split">|</span>
                    <a href="//helpcenter.jd.com/venderportal/index.html" target="_blank">商家帮助</a><span
                        class="copyright_split">|</span>
                    <a href="//jzt.jd.com" target="_blank">营销中心</a><span class="copyright_split">|</span>
                    <a href="//app.jd.com/" target="_blank">手机京东</a><span class="copyright_split">|</span>
                    <a href="//club.jd.com/links.aspx" target="_blank">友情链接</a><span class="copyright_split">|</span>
                    <a href="//media.jd.com/" target="_blank">销售联盟</a><span class="copyright_split">|</span>
                    <a href="//pro.jd.com/mall/active/3WA2zN8wkwc9fL9TxAJXHh5Nj79u/index.html"
                        target="_blank">京东社区</a><span class="copyright_split">|</span>
                    <a href="//pro.jd.com/mall/active/3TF25tMdrnURET8Ez1cW9hzfg3Jt/index.html"
                        target="_blank">风险监测</a><span class="copyright_split">|</span>
                    <a href="//about.jd.com/privacy/" target="_blank">隐私政策</a><span class="copyright_split">|</span>
                    <a href="//gongyi.jd.com" target="_blank">京东公益</a><span class="copyright_split">|</span>
                    <a href="//en.jd.com/" target="_blank">English Site</a><span class="copyright_split">|</span>
                    <a href="//corporate.jd.com/" target="_blank">Media &amp; IR</a>
                </p>
            </div>
            <div class="copyright_info">
                <p>
                    <a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11000002000088"
                        target="_blank">京公网安备 11000002000088号</a><span
                        class="copyright_split">|</span><span>京ICP证070359号</span><span class="copyright_split">|</span>
                    <a href="//img30.360buyimg.com/poprx/jfs/t1/45702/1/7206/3652062/5d4d3f4fE7ea82da4/207332da28ae8230.png"
                        target="_blank">互联网药品信息服务资格证编号(京)-经营性-2014-0008</a><span
                        class="copyright_split">|</span><span>新出发京零 字第大120007号</span></p>
                <p><span>互联网出版许可证编号新出网证(京)字150号</span><span class="copyright_split">|</span>
                    <a href="//pro.jd.com/mall/active/3bVDLXHdwVmdQksGF8TtS7ocq1NY/index.html"
                        target="_blank">出版物经营许可证</a><span class="copyright_split">|</span>
                    <a href="//misc.360buyimg.com/wz/wlwhjyxkz.jpg" target="_blank">网络文化经营许可证京网文[2014]2148-348号</a><span
                        class="copyright_split">|</span><span>违法和不良信息举报电话：4006561155</span></p>
                <p><span class="copyright_text">Copyright © 2004 - <em id="copyright_year">2019</em> 京东JD.com
                        版权所有</span><span class="copyright_split">|</span><span>消费者维权热线：4006067733</span>
                    <a href="//pro.jd.com/mall/active/38PitHBfR7ZopNHRSHnuuWR5AMDL/index.html" target="_blank"
                        class="copyright_license">经营证照</a>
                    <span class="copyright_split">|</span>
                    <span>(京)网械平台备字(2018)第00003号</span>
                    <span class="copyright_split">|</span>
                    <a href="//storage.jd.com/imgtools/cbdaa22553-dccaf290-d1af-11e8-a840-89f99f5f0056.jpeg"
                        target="_blank" class="mod_business_license">营业执照</a>
                </p>
                <p class="mod_copyright_inter">
                    <a class="mod_copyright_inter_lk" href="//www.joybuy.com/?source=1&amp;visitor_from=3"
                        target="_blank" clstag="h|keycount|btm|btmnavi_null0501"><i
                            class="mod_copyright_inter_ico mod_copyright_inter_ico_global"></i><span
                            class="languagefont"></span></a>
                    <span class="copyright_split">|</span>
                    <a class="mod_copyright_inter_lk" href="//www.jd.ru/?source=1&amp;visitor_from=3" target="_blank"
                        clstag="h|keycount|btm|btmnavi_null0502"><i
                            class="mod_copyright_inter_ico mod_copyright_inter_ico_rissia"></i><span
                            class="languagefont"></span></a>
                    <span class="copyright_split">|</span>
                    <a class="mod_copyright_inter_lk" href="//www.jd.id/?source=1&amp;visitor_from=3" target="_blank"
                        clstag="h|keycount|btm|btmnavi_null0503"><i
                            class="mod_copyright_inter_ico mod_copyright_inter_ico_indonesia"></i><span
                            class="languagefont"></span></a>
                    <span class="copyright_split">|</span>
                    <a class="mod_copyright_inter_lk" href="//www.joybuy.es/?source=1&amp;visitor_from=3"
                        target="_blank" clstag="h|keycount|btm|btmnavi_null0504"><i
                            class="mod_copyright_inter_ico mod_copyright_inter_ico_spain"></i><span
                            class="languagefont"></span></a>
                    <span class="copyright_split">|</span>
                    <a class="mod_copyright_inter_lk" href="//www.jd.co.th/?source=1&amp;visitor_from=3" target="_blank"
                        clstag="h|keycount|btm|btmnavi_null0505"><i
                            class="mod_copyright_inter_ico mod_copyright_inter_ico_thailand"></i><span
                            class="languagefont"></span></a>
                </p>
                <p><span>京东旗下网站：</span>
                    <a href="https://www.jdpay.com/" target="_blank">京东钱包</a><span class="copyright_split">|</span>
                    <a href="https://www.jdcloud.com" target="_blank">京东云</a>
                </p>
            </div>
            <p class="copyright_auth">
                <script type="text/JavaScript">function CNNIC_change(eleId){var str= document.getElementById(eleId).href;var str1 =str.substring(0,(str.length-6));str1+=CNNIC_RndNum(6);
                    document.getElementById(eleId).href=str1;}function CNNIC_RndNum(k){var rnd=""; for (var i=0;i
                    < k;i++) rnd+=Math.floor(Math.random()*10); return rnd;};(function(){var d=new Date;document.getElementById(
                     "copyright_year").innerHTML=d.getFullYear()})();</script>
                <a id="urlknet" class="copyright_auth_ico copyright_auth_ico_2" onclick="CNNIC_change('urlknet')"
                    oncontextmenu="return false;" name="CNNIC_seal"
                    href="https://ss.knet.cn/verifyseal.dll?sn=2008070300100000031&amp;ct=df&amp;pa=294005"
                    target="_blank">可信网站信用评估</a>
                <a class="copyright_auth_ico copyright_auth_ico_3" href="http://www.cyberpolice.cn/"
                    target="_blank">网络警察提醒你</a>
                <a class="copyright_auth_ico copyright_auth_ico_4"
                    href="https://search.szfw.org/cert/l/CX20120111001803001836" target="_blank">诚信网站</a>
                <a class="copyright_auth_ico copyright_auth_ico_5" href="http://www.12377.cn"
                    target="_blank">中国互联网举报中心</a>
                <a class="copyright_auth_ico copyright_auth_ico_6" href="http://www.12377.cn/node_548446.htm"
                    target="_blank">网络举报APP下载</a>
            </p>
        </div>
    </div>
    <!--footer end-->
    <script>
        seajs.use('product/search/1.0.7/js/main.js').use('//h5.360buyimg.com/ws_js/jdwebm.js?v=pcSearch').config({
            alias: {
                'search_new': './script/search_new.init.js?2019062419.js'
            }
        }).use('search_new', function (s) {
            s.init(1, 194, "5700+", "0", 1, 0, 26, 1, 0, 0);
        });
    </script>
    <script type="text/javascript">
        (function () {
            var a = document.createElement("script");
            a.type = "text/javascript";
            a.async = true;
            a.src = ("https:" == document.location.protocol ? "https://wlssl" : "//wl") + ".jd.com/wl.js";
            var b = document.getElementsByTagName("script")[0];
            b.parentNode.insertBefore(a, b)
        })();
        window.surveyShow = function () {
            window.open('//surveys.jd.com/index.php?r=survey/index/sid/393283/lang/zh-Hans/search_version/' + (
                readCookie((readCookie('mx') || '').indexOf('_M') > -1 ? 'mtest' : 'xtest') || ''))
        };
    </script>
    <div id="J-global-toolbar">
        <div class="jdm-toolbar-wrap J-wrap">
            <div class="jdm-toolbar J-toolbar">
                <div class="jdm-toolbar-panels J-panel">
                    <div data-name="ad" class="J-content jdm-toolbar-panel jdm-tbar-panel-ad">
                        <h3 class="jdm-tbar-panel-header J-panel-header"> <a> <i></i> <em class="title"></em> </a> <span
                                class="close-panel J-close"></span> </h3>
                        <div class="jdm-tbar-panel-main">
                            <div class="jdm-tbar-panel-content J-panel-content"> </div>
                        </div>
                    </div>
                    <div data-name="jdvip" class="J-content jdm-toolbar-panel jdm-tbar-panel-jdvip">
                        <h3 class="jdm-tbar-panel-header J-panel-header"> <span class="title"
                                clstag="thirdtype|keycount|cebianlan_thirdtype_jdvip|title"> <i></i> <em
                                    class="title">京东会员</em> </span> <span class="close-panel J-close"></span> </h3>
                        <div class="jdm-tbar-panel-main">
                            <div class="jdm-tbar-panel-content J-panel-content" style="overflow:hidden;">
                                <div class="jdm-tbar-tipbox2">
                                    <div class="tip-inner"> <i class="i-loading"></i> </div>
                                </div>
                            </div>
                        </div>
                        <div class="jdm-tbar-panel-footer J-panel-footer"></div>
                    </div>
                    <div data-name="cart" class="J-content jdm-toolbar-panel jdm-tbar-panel-cart">
                        <h3 class="jdm-tbar-panel-header J-panel-header"> <a
                                href="//cart.jd.com/cart.action?r=0.007676708840352209" target="_blank" class="title"
                                clstag="thirdtype|keycount|cebianlan_thirdtype_cart|title"> <i></i> <em
                                    class="title">购物车</em> </a> <span class="close-panel J-close"></span> </h3>
                        <div class="jdm-tbar-panel-main">
                            <div class="jdm-tbar-panel-content J-panel-content">
                                <div class="jdm-tbar-tipbox2">
                                    <div class="tip-inner"> <i class="i-loading"></i> </div>
                                </div>
                            </div>
                        </div>
                        <div class="jdm-tbar-panel-footer J-panel-footer"></div>
                    </div>
                    <div data-name="follow" class="J-content jdm-toolbar-panel jdm-tbar-panel-follow">
                        <h3 class="jdm-tbar-panel-header J-panel-header"> <a href="//t.jd.com/home/follow"
                                target="_blank" class="title"
                                clstag="thirdtype|keycount|cebianlan_thirdtype_follow|title"> <i></i> <em
                                    class="title">我的关注</em> </a> <span class="close-panel J-close"></span> </h3>
                        <div class="jdm-tbar-panel-main">
                            <div class="jdm-tbar-panel-content J-panel-content">
                                <div class="jdm-tbar-tipbox2">
                                    <div class="tip-inner"> <i class="i-loading"></i> </div>
                                </div>
                            </div>
                        </div>
                        <div class="jdm-tbar-panel-footer J-panel-footer"></div>
                    </div>
                </div>
                <div class="jdm-toolbar-header">
                    <div class="jdm-tbar-act J-trigger" data-type="bar" data-name="ad" data-iframe="true"
                        clstag="thirdtype|keycount|cebianlan_thirdtype_header|"> </div>
                </div>
                <div class="jdm-toolbar-tabs J-tab">
                    <div data-type="bar" clstag="thirdtype|keycount|cebianlan_thirdtype_jdvip|btn"
                        class="J-trigger jdm-toolbar-tab jdm-tbar-tab-jdvip" data-name="jdvip" data-login="true"
                        data-iframe="//vip.jd.com/sideBar/index.html"> <i class="tab-tip"></i> <i class="tab-ico"></i>
                        <em class="tab-text"> 京东会员 </em> <span class="tab-sub J-count hide">0</span>
                        <div class="tabs-tip hide"> <span class="ico"></span> <span class="text">成功加入购物车!</span> <b></b>
                        </div>
                    </div>
                    <div data-type="bar" clstag="thirdtype|keycount|cebianlan_thirdtype_cart|btn"
                        class="J-trigger jdm-toolbar-tab jdm-tbar-tab-cart" data-name="cart"> <i class="tab-ico"></i>
                        <em class="tab-text"> 购物车 </em> <span class="tab-sub J-count hide"
                            style="display: none;">0</span>
                        <div class="tabs-tip hide"> <span class="ico"></span> <span class="text">成功加入购物车!</span> <b></b>
                        </div>
                    </div>
                    <div data-type="bar" clstag="thirdtype|keycount|cebianlan_thirdtype_follow|btn"
                        class="J-trigger jdm-toolbar-tab jdm-tbar-tab-follow" data-name="follow" data-login="true"> <i
                            class="tab-ico"></i> <em class="tab-text"> 我的关注 </em> <span
                            class="tab-sub J-count hide">0</span>
                        <div class="tabs-tip hide"> <span class="ico"></span> <span class="text">成功加入购物车!</span> <b></b>
                        </div>
                    </div>
                    <div clstag="thirdtype|keycount|cebianlan_thirdtype_message|btn"
                        class="J-trigger jdm-toolbar-tab jdm-tbar-tab-message" data-name="message"><a target="_blank"
                            href="//joycenter.jd.com/msgCenter/queryHistoryMessage.action"> <i class="tab-ico"></i> <em
                                class="tab-text"> 我的消息 </em> </a> <span class="tab-sub J-count hide">0</span>
                        <div class="tabs-tip hide"> <span class="ico"></span> <span class="text">成功加入购物车!</span> <b></b>
                        </div>
                    </div>
                </div>
                <div class="jdm-toolbar-footer">
                    <div data-type="link" class="J-trigger jdm-toolbar-tab jdm-tbar-tab-qrcode"> <a
                            href="javascript:void(0)" clstag="thirdtype|keycount|cebianlan_thirdtype|qrcode"> <i
                                class="tab-ico"></i> <em class="tab-text"></em> </a>
                        <div class="qrcode-container">
                            <p>去APP上探索你查找的商品~</p><img width="100" height="100">
                        </div>
                    </div>
                    <div data-type="link" class="J-trigger jdm-toolbar-tab jdm-tbar-tab-top"> <a
                            href="javascript:window.scrollTo(0,0);" clstag="thirdtype|keycount|cebianlan_thirdtype|top">
                            <i class="tab-ico"></i> <em class="tab-text">顶部</em> </a> </div>
                    <div data-type="link" class="J-trigger jdm-toolbar-tab jdm-tbar-tab-feedback"> <a
                            href="javascript:surveyShow();" clstag="thirdtype|keycount|cebianlan_thirdtype|feedback"> <i
                                class="tab-ico"></i> <em class="tab-text">反馈</em> </a> </div>
                </div>
                <div class="jdm-toolbar-mini"> </div>
            </div>
            <div id="J-toolbar-load-hook" clstag="thirdtype|keycount|cebianlan_thirdtype|load"></div>
        </div>
    </div>
    <script>
        (function (win) {
            seajs.use('//static.360buyimg.com/devfe/toolbar/1.0.0/js/main', function (Toolbar) {
                var adConfig = {};
                var actName = null;
                if (window.pageConfig && window.pageConfig.actName) {
                    actName = window.pageConfig.actName;
                }

                if (actName == '618') {
                    adConfig = {
                        enabled: true,
                        id: "0_0_7860",
                        startTime: +new Date(2017, 4, 24, 0, 0, 0) / 1000,
                        endTime: +new Date(2017, 5, 21, 23, 59, 59) / 1000
                    };
                }

                pageConfig.toolbar = new Toolbar({
                    pType: 'search',
                    bars: {
                        jimi: {
                            enabled: false
                        },
                        cart: {
                            enabled: true
                        },
                        history: {
                            enabled: false
                        }
                    },
                    links: {
                        qrcode: {
                            index: 0,
                            anchor: "javascript:void(0)"
                        },
                        feedback: {
                            index: 2,
                            anchor: 'javascript:surveyShow();'
                        },
                        top: {
                            index: 1,
                            anchor: "javascript:window.scrollTo(0,0);"
                        }
                    },
                    ad: adConfig
                });
            });

        })(window);
    </script>

    <div id="shSafetyPV" style="display: none;"></div>
    <script src="//payrisk.jd.com/js/td.js"></script>
    <script src="https://gia.jd.com/y.html?v=0.8872231173616143&amp;o=search.jd.com/Search"></script>
</body>

</html>
"""


def find_all():
    # url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=c24a5c4a284f400cb3a9e1ab8ed56abe'
    # page = download(url)

    # print(page)
    soup_all = BeautifulSoup(page, 'lxml')
    sp_all_items = soup_all.find_all('li', attrs={'class': 'gl-item'})
    # print(sp_all_items)

    with open('phone.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        fields = ('id', '名称', '价格', '评价人数', '好评率')
        writer.writerow(fields)

        for soup in sp_all_items:
            print('-' * 50)
            name = soup.find('div', class_='p-name p-name-type-2').find('em').text
            name = ' '.join(name.split())
            print("name: ", name)
            
            item = soup.find('div', class_='p-name p-name-type-2').find('a')
            item_id = re.search(r'(\d+)', item['href']).group()
            print("item_id: ", item_id)

            price = soup.find_all('div', attrs={'class': 'p-price'})
            print('price: ', price[0].i.string)
            # print('price: ', price[0].i.text)

            comment = soup.find_all('div', attrs={'class': 'p-commit'})
            print('comment url:', comment[0].find('a').attrs['href'])

            comment_real_url = f'https://club.jd.com/comment/productCommentSummaries.action?referenceIds={item_id}'
            comment_count, good_rate = get_comment_by_json(comment_real_url)
            print('评价人数：', comment_count)
            print('好评率：', good_rate)
            
            time.sleep(3)

            row = []
            row.append(item_id)
            row.append(name)
            row.append(price[0].i.string)
            row.append(comment_count)
            row.append(good_rate)
            writer.writerow(row)

def get_comment_by_json(url):
    """
        获取网页json数据
    """

    data = requests.get(url).json()
    # print(data)
    comment_count = data['CommentsCount'][0]['CommentCount']
    good_rate = data['CommentsCount'][0]['GoodRate']
    # print('comment_count: ', comment_count)
    # print('good_rate: ', good_rate)
    return comment_count, good_rate


def save_csv_test():
    with open('test.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        fields = ('名称', '价格', 'id')
        writer.writerow(fields)
        writer.writerow(['p10', 1000, 888])
        writer.writerow(['p20', 2000, 788])


def main():
    # save_csv_test()
    find_all()


if __name__ == "__main__":
    main()
