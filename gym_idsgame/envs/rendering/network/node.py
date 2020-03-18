#from gym_idsgame.envs.rendering.network.server import Server
#from gym_idsgame.envs.rendering.network.data import Data
from gym_idsgame.envs.rendering.util.render_util import create_circle
from gym_idsgame.envs.rendering.constants import constants
from abc import ABC, abstractmethod

class Node(ABC):
    """
    TODO
    """
    @property
    def size(self):
        return self.size


    def __init__(self, size):
        self.size = size

    @abstractmethod
    def manual_blink_defense(self, i):
        pass
        # if self.resource is not None:
        #     self.resource.manual_blink_defense(i)
        # elif self.circle:
        #     return
        # elif self.data is not None:
        #     self.data.manual_blink_defense(i)

    @abstractmethod
    def manual_blink_attack(self, i, edges=None):
        pass
        # if self.resource is not None:
        #     self.resource.manual_blink_attack(i)
        # elif self.circle:
        #     return
        # elif self.data is not None:
        #     self.data.manual_blink_attack(i, edges=edges)

    @abstractmethod
    def set_state(self, attack_values, defense_values, det_value):
        pass
        # if self.resource is not None:
        #     self.resource.set_state(attack_values, defense_values, det_value)
        # elif self.circle:
        #     return
        # elif self.data is not None:
        #     self.data.set_state(attack_values, defense_values, det_value)

    @abstractmethod
    def defend(self, defense_type):
        pass
        # if self.resource is not None:
        #     self.resource.defend(defense_type)
        # elif self.circle:
        #     return
        # elif self.data is not None:
        #     self.data.defend(defense_type)

    @abstractmethod
    def reset(self):
        pass
        # if self.resource is not None:
        #     self.resource.reset()
        # elif self.circle:
        #     return
        # elif self.data is not None:
        #     self.data.reset()

    @abstractmethod
    def add_in_edge(self, edges):
        pass
        # if self.resource is not None:
        #     self.resource.incoming_edges.append(edges)
        #     return
        # elif self.circle:
        #     return
        # elif self.data is not None:
        #     self.data.incoming_edges.append(edges)
        #     return

    @abstractmethod
    def add_out_edge(self, edges):
        pass
        # if self.resource is not None:
        #     self.resource.outgoing_edges.append(edges)
        #     return
        # elif self.circle is not None:
        #     return
        #
        # elif self.data is not None:
        #     self.data.outgoing_edges.append(edges)
        #     return

    @abstractmethod
    def draw(self, y, x, color, batch, background, foreground, avatar, scale, server = False, data = False,
             start= False, max_value = 10, blink_interval = constants.GAMEFRAME.MANUAL_BLINK_INTERVAL,
             num_blinks = constants.GAMEFRAME.MANUAL_NUM_BLINKS):
        pass
        # if server:
        #     self.resource = Server(avatar, x, y, batch, background, foreground, self.size, scale=scale,
        #                            max_value=max_value, blink_interval=blink_interval, num_blinks=num_blinks)
        # elif start:
        #     create_circle(x * self.size + self.size / 2, y * int(self.size / 1.5) + (self.size / 1.5)/2, self.size / 7,
        #                   batch, background, color)
        #     self.circle = True
        #     self.col = x
        #     self.row = y
        # elif data:
        #     self.data = Data(avatar, x, y, batch, background, foreground, self.size, scale=scale, max_value=max_value,
        #                      blink_interval= blink_interval, num_blinks=num_blinks)

    @abstractmethod
    def get_link_coords(self, upper=True, lower=False):
        pass
        # if self.resource is not None:
        #     if upper:
        #         x = self.resource.col*self.resource.size + self.resource.size/2
        #         y = (self.resource.row+1)*(self.resource.size/1.5) - self.size/6
        #     elif lower:
        #         x = self.resource.col * self.resource.size + self.resource.size / 2
        #         y = (self.resource.row + 1) * (self.resource.size / 1.5) - self.size / 1.75
        #     return x,y,self.resource.col, self.resource.row
        # elif self.circle:
        #     x = self.col * self.size + self.size / 2
        #     y = (self.row + 1) * (self.size / 1.5) - self.size / 1.75
        #     return x,y,self.col,self.row
        # elif self.data is not None:
        #     x = self.data.col * self.data.size + self.data.size / 2
        #     y = (self.data.row + 1) * (self.data.size / 1.5) - self.size / 15
        #     return x, y, self.data.col, self.data.row

    @abstractmethod
    def get_coords(self):
        pass
        # if self.resource is not None:
        #     return self.resource.x, self.resource.y
        #
        # elif self.circle is not None:
        #     return self.col, self.row
        #
        # elif self.data is not None:
        #     return self.data.x, self.data.y


    @abstractmethod
    def get_node(self):
        pass
        # if self.resource is not None:
        #     return self.resource
        # elif self.data is not None:
        #     return self.data