# baidu_page 使用说明



# 背景

爬取[百度图片](https://image.baidu.com/)的图片



# demo

```python
if __name__ == '__main__':
    baidu_url = input('请输入需要爬取的百度图片的url: ')
    save_path = input('请输入你要将这些图片保存的文件夹地址: ')
    circulate_time = int(input('请输入需要爬取的循环数量(一次循环30张图片):'))
    a = GetPage(url = baidu_url, path = save_path, circulate_time = circulate_time )
    a.get_shufa()
##本程序最终输出即为需要爬取的图片文件
```



# 使用说明

## GetPage类使用

### 1.GetPage参数

`url`:

- **传参形式**：

  str

- **参数说明**：

  传递需要爬取的图片的url

  - **参数获取**：

    下面将以爬取动漫图片为例子

  - ![](https://github.com/Cococonutsu/baudu_page_crawler/blob/main/page/1.png)

  - ![](https://github.com/Cococonutsu/baudu_page_crawler/blob/main/page/2.png)

  - ![](https://github.com/Cococonutsu/baudu_page_crawler/blob/main/page/3.png)

  - ![](https://github.com/Cococonutsu/baudu_page_crawler/blob/main/page/4.png)

  - 到此为止，我们就获得了我们想爬取的图片的url

`path`:

- **传参形式**：

  str

- **参数说明**：

  我们要将这些爬取下来的图片保存到我们电脑的什么位置



`circulate_time`:

- **传参形式**：

  int

- **参数说明**：

  程序循环的次数，输入`1`表示程序循环`1`轮,程序循环`1`轮爬取`30`张图片，输入`2`表示爬取`60`张，以此类推。

  我们可以根据自己需要的图片数量随意更改，不用担心程序会因图片数量不够而中断，如果图片数量不够，循环会自动跳出开始输出图片
