import time
import asyncio
import re
import sys
sys.path.append('D:\\code\\kongRobot\\maoRobot\\TaskConfiguration\\Task')
from task1.bit_api import *
from task1.readExcle import get_all_rows
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    browser = None
    try:
        # /browser/open 接口会返回 selenium使用的http地址，以及webdriver的path，直接使用即可
        browser_id = "f7443d76b97f4e5a9421e657f4e6de0b" # 窗口ID从窗口配置界面中复制，或者api创建后返回
        
        # 尝试多次打开浏览器
        max_retries = 3
        for attempt in range(max_retries):
            print(f"尝试打开浏览器 (尝试 {attempt + 1}/{max_retries})")
            res = openBrowser(browser_id)
            print(f"openBrowser 返回结果: {res}")
            
            if res.get('success', False):
                break
            
            if attempt < max_retries - 1:
                print("等待5秒后重试...")
                await asyncio.sleep(5)
        
        # 检查是否成功打开浏览器
        if not res.get('success', False):
            raise ValueError(f"无法打开浏览器: {res.get('msg', '未知错误')}")
            
        # 获取 WebSocket 地址
        if 'data' in res and 'ws' in res['data']:
            ws = res['data']['ws']
        else:
            raise ValueError(f"返回数据格式错误: {res}")
            
        print(f"WebSocket 地址: {ws}")

        # 连接到浏览器
        print("正在连接到浏览器...")
        chromium = playwright.chromium
        browser = await chromium.connect_over_cdp(ws)
        default_context = browser.contexts[0]

        print('创建新页面并访问百度')
        page = await default_context.new_page()
        await page.goto('https://baidu.com')

        await asyncio.sleep(2)

        print('关闭页面')
        await page.close()

        await asyncio.sleep(2)
        
    except Exception as e:
        print(f"执行出错: {str(e)}")
        import traceback
        print(f"错误堆栈: {traceback.format_exc()}")
        raise  # 重新抛出异常以便上层捕获
        
    finally:
        # 确保浏览器被关闭
        if browser:
            try:
                await browser.close()
            except Exception as e:
                print(f"关闭浏览器时出错: {str(e)}")
        
        try:
            print(f"正在关闭浏览器服务，ID: {browser_id}")
            close_result = closeBrowser(browser_id)
            print(f"closeBrowser 返回结果: {close_result}")
        except Exception as e:
            print(f"关闭浏览器服务时出错: {str(e)}")