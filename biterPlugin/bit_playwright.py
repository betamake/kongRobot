from bit_api import *
import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    browser = None
    try:
        browser_id = "29771a54297e4b50a6858fbb5c012bf8"  # 替换为你的浏览器ID
        res = openBrowser(browser_id)
        ws = res['data']['ws']
        print(f"WebSocket地址: {ws}")

        chromium = playwright.chromium
        browser = await chromium.connect_over_cdp(ws)
        default_context = browser.contexts[0]
        print('成功连接到浏览器')

        # 创建新页面
        page = await default_context.new_page()
        await page.goto('https://www.okx.com/web3')
        print('页面加载完成')

        # 等待页面完全加载
        await page.wait_for_load_state('networkidle')
        await page.wait_for_timeout(3000)

        # 打印初始页面信息
        pages = default_context.pages
        print(f"初始页面数量: {len(pages)}")
        for p in pages:
            print(f"初始页面URL: {p.url}")

        # 操作OKX钱包扩展
        extension_popup = await operate_okx_wallet(default_context, page)
        if extension_popup:
            print("扩展页面已打开，等待操作...")
            
            # 可以在这里添加具体的钱包操作代码
            # 例如：等待并检查页面元素
            try:
                await extension_popup.wait_for_selector('text=OKX Wallet', timeout=5000)
                print("成功加载钱包界面")
                
                # 在这里可以添加更多钱包操作
                # await extension_popup.click('button:has-text("Connect")')
                # await extension_popup.fill('input[type="password"]', 'your_password')
                
            except Exception as e:
                print(f"钱包界面操作失败: {str(e)}")

            await extension_popup.wait_for_timeout(5000)

        # 打印最终页面信息
        pages = default_context.pages
        print(f"最终页面数量: {len(pages)}")
        for p in pages:
            print(f"最终页面URL: {p.url}")

    except Exception as e:
        print(f"发生错误: {str(e)}")
        
    finally:
        if browser:
            # 确保延迟足够长以便观察结果
            await asyncio.sleep(5)
            await browser.close()
            await asyncio.sleep(2)
            closeBrowser(browser_id)
            print('浏览器已关闭')

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

if __name__ == "__main__":
    asyncio.run(main())
