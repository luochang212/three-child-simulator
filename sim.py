# -*- coding: utf-8 -*-

"""n child simulator
    Author: github@luochang212
    Date: 2021-06-05
    Usage: python sim.py
"""


import configparser
import random
import collections
import queue
import ast


Event = collections.namedtuple('Event', ['time', 'ident', 'name', 'gender', 'action'])


class Simulator:

    def __init__(self, config_path):
        self.config_path = config_path
        self.config = None

    def set_config(self):
        config = configparser.ConfigParser()
        config.read(self.config_path)
        self.config = config

    @staticmethod
    def read_config(item: str):
        return ast.literal_eval(item)

    def child_process(self, ident, name, gender, start_time=0):
        time = start_time
        for action, _ in self.read_config(self.config.get('EVENT', 'base_line')):
            time = yield Event(time, ident, name, gender, action)
        yield Event(start_time, ident, name, gender, action)

    def create_generator(self, child_num: int, last_name: str = None, max_size=20):
        if child_num > max_size:  # 因为假设一年只能生一个孩子，所以生育年限和孩子数共用一个max_size
            raise Exception('invalid child_num')

        if last_name is None:
            last_name = random.choices(self.read_config(self.config.get('PROPERTY', 'last_name')))[0]

        first_name_dict = {
            'boy': self.read_config(self.config.get('PROPERTY', 'first_name_boy')),
            'girl': self.read_config(self.config.get('PROPERTY', 'first_name_girl'))
        }

        # 生成孩子的性别
        gender_list = [random.choices(['boy', 'girl'])[0] for _ in range(child_num)]

        # 生成孩子的姓名，不允许重名
        name_list = []
        for gender in gender_list:
            while True:
                child_name = last_name + random.choices(first_name_dict[gender])[0]
                if child_name not in name_list:
                    name_list.append(child_name)
                    break

        # 生成生孩子的时间
        start_time_list = sorted(random.sample(range(max_size), child_num))

        return {i: self.child_process(i, name, gender, start_time) for i, name, gender, start_time in zip(range(child_num), name_list, gender_list, start_time_list)}

    def run(self, end_time: int, child_num: int, last_name: str = None):
        # 挂载配置
        self.set_config()

        # 创建生成器
        generators = self.create_generator(child_num, last_name)

        # 创建事件队列
        events = queue.PriorityQueue()

        # 预激生成器并将事件入队
        for _, generator in generators.items():
            first_event = next(generator)
            events.put(first_event)

        # 主循环
        sim_time = 0
        while sim_time < end_time:
            if events.empty():
                print('*** end of events ***')
                break

            # 从优先队列中获取当前事件
            current_event = events.get()
            sim_time, ident, _, _, action = current_event
            print('    ' * ident + str(current_event))
            duration = [e[1] for e in self.read_config(self.config.get('EVENT', 'base_line')) if e[0] == action][0]

            # 从字典中取出生成器
            current_gen = generators[ident]
            try:
                next_event = current_gen.send(sim_time + duration)
            except StopIteration:
                del generators[ident]
            else:
                events.put(next_event)
        else:
            print(f'*** end of simulation time: {events.qsize()} event(s) pending ***')


if __name__ == '__main__':
    s = Simulator('./conf/config.conf')
    s.run(end_time=30, child_num=3, last_name=None)
