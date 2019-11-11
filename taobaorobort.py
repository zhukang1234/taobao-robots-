from selenium import webdriver
import datetime
import time
browser = webdriver.Chrome()
def login():
    # 打开淘宝首页，通过扫码登录
    browser.get("https://www.taobao.com")
    time.sleep(0.02)
    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()
        print(f"请尽快扫码登录")
        time.sleep(10)

        
def buy(times):
    while True:
        now = datetime.datetime.now().strftime('%H%M%S')
        te = datetime.datetime.now().strftime('%d')
        # 对比时间，时间到的话就点击结算
        if now >= times:
            # 点击结算按钮
            while True:
                try:
                    if browser.find_element_by_link_text("结 算"):
                        browser.find_element_by_link_text("结 算").click()
                        print(f"结算成功，准备提交订单")
                        break
                except:
                    pass
            # 点击提交订单按钮
            while True:
                try:
                    if browser.find_element_by_link_text('提交订单'):
                        browser.find_element_by_link_text('提交订单').click()
                        print(f"抢购成功，请尽快付款")
                except:
                    print(f"再次尝试提交订单")
            time.sleep(0.01)
def picking(method):
    # 打开购物车列表页面
    browser.get("https://cart.taobao.com/cart.htm")
    time.sleep(0.02)
    while datetime.datetime.now().strftime('%H%M%S')< '125959':
        pass
    # 是否全选购物车
    if method == 0:
        while True:
            try:
                if browser.find_element_by_id("J_SelectAll1"):
                    browser.find_element_by_id("J_SelectAll1").click()
                    break
            except:
                print(f"找不到购买按钮")
    else:
        print(f"请手动勾选需要购买的商品")
        time.sleep(3)
            
'''
times='202000'
now = datetime.datetime.now().strftime('%H%M%S')
te= datetime.datetime.now().strftime('%d')
'''
login()
picking(0)
buy('130000')
