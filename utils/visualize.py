import visdom
import time
import numpy as np


class Visualizer(object):
    '''封装了visdom的基本操作，但是你仍然可以通过`self.vis.function`
    调用原生的visdom接口
    比如 
    self.text('hello visdom')
    self.histogram(t.randn(1000))
    self.line(t.arange(0, 10),t.arange(1, 11))'''

    def __init__(self, env='default', **kwargs):
        self.vis = visdom.Visdom(env=env, **kwargs)
        # 画的第几个数，相当于横坐标
        # 保存
        self.index = {}
        self.log_text = ''

    def reinit(self, env='default', **kwargs):
        '''修改visdom的配置'''
        self.vis = visdom.Visdom(env=env, **kwargs)
        return self

    def plot_many(self, d):
        '''一次plot多个
        '''
        # for k, v in d.items():
        # self.
