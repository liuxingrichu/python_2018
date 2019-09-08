"""
	功能：单条记录分析与获取
"""

import re
import time
from bs4 import BeautifulSoup
import requests

html_doc = """
<li class="gl-item" data-sku="100006635632" data-spu="100006635632" data-pid="100006635632">
	<div class="gl-i-wrap">
		<div class="p-img">
			<a target="_blank" title="麒麟810，4800万超清双摄，升降式全面屏！荣耀爆品特惠，选品质，购荣耀~" href="//item.jd.com/100004069421.html" onclick="searchlog(1,100006635632,0,2,'','flagsClk=557847176')">
				<img width="220" height="220" class="" data-img="1" source-data-lazy-img="" data-lazy-img="done" src="//img11.360buyimg.com/n7/jfs/t1/84119/30/7021/372939/5d53b55aE12f17b5a/5619ee1ae96c3cd8.jpg">
</a>			<div data-lease="" data-catid="655" data-venid="1000000904" data-presale="" data-done="1"></div>
		</div>
		<div class="p-scroll">
			<span class="ps-prev">&lt;</span>
			<span class="ps-next">&gt;</span>
			<div class="ps-wrap">
				<ul class="ps-main">
					<li class="ps-item"><a href="javascript:;" class="" title="魅海蓝"><img data-presale="" data-sku="100006635632" data-img="1" data-lazy-img="done" class="" width="25" height="25" data-done="1" src="//img12.360buyimg.com/n9/jfs/t1/38376/31/12243/397999/5d36c0b0E4fe67576/ad031fec5819110f.jpg"></a></li>
										<li class="ps-item"><a href="javascript:;" title="幻夜黑" class=""><img data-presale="" data-sku="100004069505" data-img="1" width="25" height="25" data-lazy-img="done" class="" data-done="1" src="//img10.360buyimg.com/n9/jfs/t1/64468/1/5252/214483/5d36a5b7E1b13e7dc/67711c7137af161b.jpg"></a></li>
										<li class="ps-item"><a href="javascript:;" title="魅焰红" class="curr"><img data-presale="" data-sku="100004069421" data-img="1" width="25" height="25" data-lazy-img="done" class="" data-done="1" src="//img11.360buyimg.com/n9/jfs/t1/84119/30/7021/372939/5d53b55aE12f17b5a/5619ee1ae96c3cd8.jpg"></a></li>
									</ul>
			</div>
		</div>
		<div class="p-price">
<strong class="J_100006635632" data-done="1"><em>￥</em><i>1399.00</i></strong>		</div>
		<div class="p-name p-name-type-2">
			<a target="_blank" title="麒麟810，4800万超清双摄，升降式全面屏！荣耀爆品特惠，选品质，购荣耀~" href="//item.jd.com/100004069421.html" onclick="searchlog(1,100006635632,0,1,'','flagsClk=557847176')">
				<em>荣耀9X 麒麟810 4000mAh超强续航 4800万超清夜拍 6.59英寸升降全面屏 全网通4GB+64GB 魅海蓝</em>
				<i class="promo-words" id="J_AD_100006635632">麒麟810，4800万超清双摄，升降式全面屏！荣耀爆品特惠，选品质，购荣耀~</i>
			</a>
		</div>
		<div class="p-commit" data-done="1">
			<strong><a id="J_comment_100006635632" target="_blank" href="//item.jd.com/100004069421.html#comment" onclick="searchlog(1,100006635632,0,3,'','flagsClk=557847176')">32万+</a>条评价</strong>
		</div>
		<div class="p-focus"><a class="J_focus" data-sku="100004069421" href="javascript:;" title="点击关注" onclick="searchlog(1,100006635632,0,5,'','flagsClk=557847176')"><i></i>关注</a></div>
		<div class="p-shop" data-selfware="1" data-score="5" data-reputation="97" data-done="1">
<span class="J_im_icon"><a target="_blank" class="curr-shop hd-shopname" onclick="searchlog(1,1000000904,0,58)" href="//mall.jd.com/index-1000000904.html" title="荣耀京东自营旗舰店">荣耀京东自营旗舰店</a><b class="im-02" style="background:url(//img14.360buyimg.com/uba/jfs/t26764/156/1205787445/713/9f715eaa/5bc4255bN0776eea6.png) no-repeat;" title="联系客服" onclick="searchlog(1,1000000904,0,61)"></b></span>		</div>		
		<div class="p-icons" id="J_pro_100006635632" data-done="1">
			<i class="goods-icons J-picon-tips J-picon-fix" data-idx="1" data-tips="京东自营，品质保障">自营</i>
		</div>
	</div>
</li>
"""


def test_item():
    soup = BeautifulSoup(html_doc, 'lxml')
    name = soup.find('div', class_='p-name p-name-type-2').find('em').text
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


def main():
    test_item()


if __name__ == "__main__":
    main()
