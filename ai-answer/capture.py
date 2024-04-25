# -*- coding: utf-8 -*-
# __author: guo
# @time: 2019-12-03
import tkinter
# import asyncio
from PIL import ImageGrab
from aip import AipOcr
import time
import os
import http.client
import hashlib
import json
import urllib
import random
from tkinter import ttk


# def get_from_lang(self):
#     print(self.from_lang.get())
#     # return
#
#
# def get_to_lang(self):
#     print(self.to_lang.get())
#     # return


class MyCapture:

    def __init__(self):
        # 变量X和Y用来记录鼠标左键按下的位置
        self.X = tkinter.IntVar(value=0)
        self.Y = tkinter.IntVar(value=0)
        self.sel = False
        self.ocr_text = None
        self.capture_png_path = ''
        self.capture_text_box = tkinter.Text(window)  # 创建text容器用于存放截图识别的文字
        self.capture_text_box.place(x=20, y=70, anchor='nw', width=170, height=330)

        self.translate_text_box = tkinter.Text(window)  # 创建text容器用于存放翻译后的文字
        self.translate_text_box.place(x=210, y=70, anchor='nw', width=170, height=330)

        self.capture_btn = tkinter.Button(text='截图', command=self.capture_cmd)  # 创建一个按钮
        self.capture_btn.place(x=80, y=10, anchor='nw', width=60, height=20)  # 在创建的窗口的西北角x=20,y=10处放置按钮
        self.capture_btn.bind("<Control-a>",lambda e: print("Copied!"))

        self.capture_btn = tkinter.Button(text='翻译', command=self.translate_cmd)  # 创建一个按钮
        self.capture_btn.place(x=270, y=10, anchor='nw', width=60, height=20)

        # 下拉选择框
        self.from_lang = 'zh'
        self.to_lang = 'en'
        self.lang_dic = {'自动识别': 'auto', '中文': 'zh', '英语': 'en', '日语': 'jp'}
        self.from_lang_L = tkinter.Label(window, text='原语言：')
        self.from_lang_box = ttk.Combobox(window, state="readonly")
        self.from_lang_box['value'] = ('自动识别', '中文', '英语', '日语')
        self.from_lang_box.current(1)
        self.from_lang_L.place(x=20, y=40, anchor='nw')
        self.from_lang_box.place(x=80, y=40, anchor='nw', width=80, height=20)
        self.from_lang_box.bind("<<ComboboxSelected>>", self.get_from_lang)

        self.to_lang_L = tkinter.Label(window, text='目标语言：')
        self.to_lang_box = ttk.Combobox(window,state="readonly")
        self.to_lang_box['value'] = ('中文', '英语', '日语')
        self.to_lang_box.current(1)
        self.to_lang_L.place(x=210, y=40, anchor='nw')
        self.to_lang_box.place(x=270, y=40, anchor='nw', width=60, height=20)
        self.to_lang_box.bind("<<ComboboxSelected>>", self.get_to_lang)

        # 屏幕尺寸
        self.screenWidth = window.winfo_screenwidth()
        self.screenHeight = window.winfo_screenheight()
        self.temp_png = 'temp.png'
        # self.create_canvas()

    def create_canvas(self):
        time.sleep(0.2)
        im = ImageGrab.grab()
        im.save(self.temp_png)
        im.close()
        # 创建顶级组件容器
        self.top = tkinter.Toplevel(window, width=self.screenWidth, height=self.screenHeight)
        # 不显示最大化、最小化按钮
        self.top.overrideredirect(True)
        self.canvas = tkinter.Canvas(self.top, bg='white', width=self.screenWidth, height=self.screenHeight)
        # 显示全屏截图，在全屏截图上进行区域截图
        self.image = tkinter.PhotoImage(file=self.temp_png)
        self.canvas.create_image(self.screenWidth, self.screenHeight, image=self.image)

        # 鼠标左键按下的位置
        self.canvas.bind('<Button-1>', self.mouse_left_down)
        # 鼠标左键移动，显示选取的区域
        self.canvas.bind('<B1-Motion>', self.mouse_move)
        # 获取鼠标左键抬起的位置，保存区域截图
        self.canvas.bind('<ButtonRelease-1>', self.mouse_left_up)

        self.canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)

    def mouse_left_down(self, event):
        """鼠标左键按下的位置"""
        self.X.set(event.x)
        self.Y.set(event.y)
        self.sel = True  # 开始截图

    # 鼠标左键移动，显示选取的区域
    def mouse_move(self, event):
        if not self.sel:
            return
        try:
            # 删除刚画完的图形，要不然鼠标移动的时候是黑乎乎的一片矩形
            self.canvas.delete(self.lastDraw)
        except Exception as e:
            pass
        self.lastDraw = self.canvas.create_rectangle(self.X.get(), self.Y.get(), event.x, event.y, outline='green')

    def mouse_left_up(self, event):
        """获取鼠标左键抬起的位置，保存区域截图"""
        self.sel = False
        try:
            self.canvas.delete(self.lastDraw)
        except Exception as e:
            pass
        # 考虑鼠标左键从右下方按下而从左上方抬起的截图
        x1, x2 = sorted([self.X.get(), event.x])  # tkinter记录的坐标点
        y1, y2 = sorted([self.Y.get(), event.y])

        pic = ImageGrab.grab((x1+1, y1+1, x2, y2))
        # pic.show()
        self.capture_png_path = 'capture_png.png'
        pic.save(self.capture_png_path)

        # 关闭当前窗口
        self.top.destroy()

    def capture_cmd(self):
        """点击截图按钮触发函数"""
        window.iconify()  # 窗口最小化
        # 显示全屏幕截图
        self.create_canvas()
        self.capture_btn.wait_window(self.top)
        os.remove(self.temp_png)
        self.ocr_text = self.baidu_ocr(self.capture_png_path)
        print(self.ocr_text)
        if self.ocr_text:
            self.capture_text_box.delete('1.0', tkinter.END)   # 清空文本框
            self.translate_text_box.delete('1.0', tkinter.END)
            self.capture_text_box.insert('end', self.ocr_text)
            window.deiconify()  # 窗口显示
            os.remove(self.capture_png_path)

    def translate_cmd(self):
        """点击翻译按钮触发函数"""
        if self.ocr_text:
            self.translate_text = self.baidu_translate(self.ocr_text)
            self.translate_text_box.delete('1.0', tkinter.END)
            if self.translate_text:
                self.translate_text_box.insert('end', self.translate_text)

    def baidu_ocr(self, file_path):
        """ 调用通用文字识别, 图片参数为本地图片 """
        app_id = '你自己的appid'
        api_key = '你自己的api_key'
        secret_key = '你自己的secret_key'
        ocr_text = ''
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as fp:
                image = fp.read()
            ocr_ret = AipOcr(app_id, api_key, secret_key).basicGeneral(image)
            words = ocr_ret.get('words_result')
            if words is not None and len(words):
                for word in words:
                    # print(word['words'], end='\n')
                    ocr_text += word['words'] + '\n'
                return ocr_text
            else:
                return None
        else:
            return None

    def baidu_translate(self, content):
        app_id = '你自己的appid'
        secret_key = '你自己的secretkey'
        http_client = None
        myurl = '/api/trans/vip/translate'
        q = content
        # from_lang = 'zh'  # 源语言
        from_lang = self.from_lang  # 源语言
        to_lang = self.to_lang  # 翻译后的语言
        # to_lang = 'en'  # 翻译后的语言
        salt = random.randint(32768, 65536)
        sign = app_id + q + str(salt) + secret_key
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = myurl + '?appid=' + app_id + '&q=' + urllib.parse.quote(
            q) + '&from=' + from_lang + '&to=' + to_lang + '&salt=' + str(
            salt) + '&sign=' + sign

        try:
            http_client = http.client.HTTPConnection('api.fanyi.baidu.com')
            http_client.request('GET', myurl)
            # response是HTTPResponse对象
            response = http_client.getresponse()
            json_response = response.read().decode("utf-8")  # 获得返回的结果，结果为json格式
            js = json.loads(json_response)  # 将json格式的结果转换字典结构
            # print(js)
            dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
            # print(dst)  # 打印结果
            return dst
        except Exception as e:
            print(e)
            return None
        finally:
            if http_client:
                http_client.close()

    def get_from_lang(self, event):
        # print(self.from_lang_box.get())
        self.from_lang = self.lang_dic[self.from_lang_box.get()]
        # return

    def get_to_lang(self, event):
        # print(self.to_lang_box.get())
        self.to_lang = self.lang_dic[self.to_lang_box.get()]
        # return


window = tkinter.Tk()
window.title('Capture')
# 创建tkinter主窗口
window.geometry('400x420')  # 指定主窗口位置与大小

capture = MyCapture()

# capture.from_lang.bind("<<ComboboxSelected>>", get_from_lang(capture))
# capture.to_lang.bind("<<ComboboxSelected>>", get_to_lang(capture))
window.mainloop()








