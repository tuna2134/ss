import discord

from discord.ext import commands

from PIL import Image

from selenium import webdriver

from selenium.webdriver.chrome.options import Options

bot = commands.Bot(command_prefix='!',activity=d.Activity(name='起動中!',type=d.ActivityType.watching))

@bot.event

async def on_ready():

    #ログイン

    print('Login infomation>>>')

    print(bot.user.name)

    print(bot.user.id)

    print('------')

@bot.event

async def on_message(message):

    ctx = await bot.get_context(message)#ctxをとる

    if message.author.bot:

        return #Botには反応しない

    await bot.invoke(ctx)

@bot.command()

async def ss(ctx,web):

    try:

        FILENAME = "screen.png"

        options=Options()

        options.set_headless(True)

        options.add_argument('--disable-dev-shm-usage')

        options.add_argument('start-maximized')

        options.add_argument('disable-infobarse')

        options.add_argument('--disable-extensions')

        options.add_argument('--disable-gpu')

        options.add_argument('--no-sandbox')

        options.binary_location="Chromeがある場所"

        driver=webdriver.Chrome(chrome_options = options,executable_path=r"Chromeドライバーがある場所")

        if not "http" in str(web):

            try:

                driver.get("http://"+str(web))

            except:

                driver.get("https://"+str(web))

        else:

            driver.get(str(web))

        if 'IP addres' in driver.page_source:

            await ctx.send("このWebページにはアクセスできません。")

        else:

            driver.set_window_size(1280, 720)

            driver.save_screenshot('screenshot.png')

            file = discord.File("screenshot.png", filename="image.png")

            embed = d.Embed(title="スクリーンショット", description=f"{web}")

            embed.set_image(url="attachment://image.png")

            await ctx.send(file=file,embed=embed)

            driver.quit()

    except:

        await ctx.send("エラーが発生していたため、アクセスができませんでした。")

bot.run("TOKEN HERE")
