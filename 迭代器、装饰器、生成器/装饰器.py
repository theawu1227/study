def decorator(func):
    def demo01():
        func()
        print('执行装饰器')

    return demo01


@decorator
def run():
    print('运行程序')


def dede():
    url = "https://www.mrs.org/meetings-events/spring-meetings-exhibits/past-spring-meetings/2020-mrs-spring-meeting/call-for-papers/symposium-sessions-detail/2020_mrs_spring_meeting/en11"
    import requests
    from lxml import etree

    response = requests.get(url).text
    html = etree.HTML(response)
    # print(html)
    TXT = html.xpath('//*[@id="tab1"]/div[3]/div[1]/div[6]/div/div[3]/div[1]//text()')
    print(TXT)


if __name__ == '__main__':
    run()
