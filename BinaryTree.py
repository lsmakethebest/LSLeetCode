#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple
from io import StringIO
import math


class PrivateNode(object):

    def __init__(self,btNode):
            self.btNode = btNode
            self.left = None
            self.right = None
    

class Printer:

    max_node_width = 0

    def create_node(self,btNode):
            node = PrivateNode(btNode)
            content = str(btNode)
            node.width = len(content)
            node.content = content
            Printer.max_node_width = max(Printer.max_node_width,node.width)
            return node;


    def printTree(self,root,height):
        self.btRoot = root
        if root is None:
            print(root)
            return
        
        root_node = self.create_node(root)

        result = []
        current_level = [root_node]
        cur_height = 0
        while current_level:
            tmp = []
            next_level = []
            for node in current_level:
                tmp.append(node)
                if node is None:
                    next_level.append(None)
                    next_level.append(None)
                else:
                    btNode = node.btNode;
                    if btNode.left:
                        left = self.create_node(btNode.left)
                        left.parent = node
                        node.left = left
                        next_level.append(left)
                    else:
                        next_level.append(None)

                    if btNode.right:
                        right = self.create_node(btNode.right)
                        right.parent = node
                        node.right = right
                        next_level.append(right)
                    else:
                        next_level.append(None)
            current_level = next_level
            result.append(tmp)
            cur_height += 1
            if cur_height >= height:
                break

        # max_level_size = 1
        # for rows in result:
        #     cur_level_size = 0
        #     for i in rows:
        #         if i is not None:
        #             cur_level_size += 1
        #     max_level_size = max(max_level_size,cur_level_size)
        # print(max_level_size)

        left_space = ' '

        for i in range(len(result)):
            rows = result[i]
            w = 2**(height-i)
            for j in range(len(rows)):
                node = rows[j]
                if node:
                    pass
                    # print(left_space*w + str(node.content) + left_space*w,end='  ')
                else:
                    pass
                    # print(left_space*w + 'null' + left_space*w,end='  ')
            # print()
        # print(Printer.max_node_width)
        self.cleanNodes(result)

    def cleanNodes(self,result):
            last_row = result[-1]
            last_row_count = len(last_row)

            # 每个节点之间的间距
            node_space = Printer.max_node_width + 2
            last_row_length = Printer.max_node_width*last_row_count + (last_row_count - 1) * node_space
            print('last_row_length:{}'.format(last_row_length))
            for i in range(len(result)):
                rows = result[i]
                row_length = 0
                all_space = last_row_length - (len(rows) -1)*node_space
                corner_space = all_space // len(rows) - Printer.max_node_width;
                corner_space //= 1
                print("{} {}".format(all_space,corner_space))
                print('---------')
                for j in range(len(rows)):
                    if j != 0:
                        row_length += node_space
                    node = rows[j]
                    row_length += corner_space
                    if node:
                        node.x = row_length + (Printer.max_node_width - node.width)>>1
                        node.y = i
                    row_length += Printer.max_node_width
                    row_length += corner_space
                while None in rows:
                    rows.remove(None)


            # for i in result:
            #     for j in i:
            #         print(j.btNode)
            mid_array = []
            def middle_order(node):
                if Node is None:
                    return
                if node.left:
                    middle_order(node.left)
                mid_array.append(node)
                if node.right:
                    middle_order(node.right)

            middle_order(result[0][0])
            small_x = mid_array[0].x

            for i in result:
                line = ' ' * (i[-1].x+i[-1].width)
                # print(len(line))
                for j in i:
                    j.x -= small_x


            print('*************************')
            lines = []
            for i in result:
                line = ' ' * (i[-1].x+i[-1].width)
                # print(len(line))
                for j in i:
                # i.x -= small_x
                    # print("(x:{} el:{})".format(j.x,j.btNode.element),end=' ')
                    line = line[:j.x] + j.content + line[j.x+j.width:]
                    # print("(x:{} el:{})".format(j.x,j.btNode.element),end=' ')
                # print('')
                lines.append(line)
            # print(mid_array)
            for  i in lines:
                print(i)
            # self.compress_node(result)
    def compress_node(self,result):
        for i in range(len(result)-1,0,-1):
            rows = result[i]


class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, b):
        self.queue.insert(0, b)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        return self.queue == []


class Node(object):
    def __init__(self,element,left,right):
        self.element = element
        self.left = left
        self.right = right
        self.parent = None

    def __str__(self):
        if self.element is None:
            return ''
        return "{}_p({})".format(str(self.element),str(self.parent.element) if self.parent else 'None')

class BinaryTree:

    def __init__(self):
        self.size = 0
        self.root = None

    def depth(self,root):
        if root is None:
            return 0
        return 1 + max(self.depth(root.left),self.depth(root.right))  

    def getheight(self):
        
        def _getHeight(node):
            if node is None:
                return 0
            else:
                return max(_getHeight(node.left),_getHeight(node.right)) + 1
        return _getHeight(self.root)

    def add_padding(self,str, pad_length_value):
        str = str.strip()
        return str.center(pad_length_value, ' ')


    # 打印二叉树
# sotre node , space and slashes in list first, then print out
    def printTree(self):
        output = StringIO()
        pretty_output = StringIO()

        current_level = Queue()
        next_level = Queue()
        current_level.enqueue(self.root)
        depth = 0

        # get the depth of current tree
        # get the tree node data and store in list
        if tree:
            while not current_level.isEmpty():
                current_node = current_level.dequeue()
                output.write('%s ' % current_node.element if current_node else 'N ')
                next_level.enqueue(
                    current_node.left if current_node else current_node)
                next_level.enqueue(
                    current_node.right if current_node else current_node)

                if current_level.isEmpty():
                    if sum([i is not None for i in next_level.queue]
                        ):  # if next level has node
                        current_level, next_level = next_level, current_level
                        depth = depth + 1
                    output.write('\n')
        # print('the tree print level by level is :')
        # print(output.getvalue())
        # print("current tree's depth is %i" % (depth+1))

        # add space to each node
        output.seek(0)
        pad_length = 3
        keys = []
        spaces = int(math.pow(2, depth))

        while spaces > 0:
            skip_start = spaces * pad_length
            skip_mid = (2 * spaces - 1) * pad_length

            key_start_spacing = ' ' * skip_start
            key_mid_spacing = ' ' * skip_mid

            keys = output.readline().split(' ')  # read one level to parse
            padded_keys = (self.add_padding(key, pad_length) for key in keys)
            padded_str = key_mid_spacing.join(padded_keys)
            complete_str = ''.join([key_start_spacing, padded_str])

            pretty_output.write(complete_str)

            # add space and slashes to middle layer
            slashes_depth = spaces
            # print('current slashes depth im_resize:')
            # print(spaces)
            # print("current levle's list is:")
            # print(keys)
            spaces = spaces // 2
            if spaces > 0:
                pretty_output.write('\n')  # print '\n' each level

                cnt = 0
                while cnt < slashes_depth:
                    inter_symbol_spacing = ' ' * (pad_length + 2 * cnt)
                    symbol = ''.join(['/', inter_symbol_spacing, '\\'])
                    # symbol_start_spacing = ' ' * (skip_start-cnt-1)
                    # symbol_mid_spacing = ' ' * (skip_mid-2*(cnt+1))
                    symbol_start_spacing = ' ' * (skip_start-cnt-1)
                    symbol_mid_spacing = ' ' * (skip_mid-2*(cnt+1))
                    pretty_output.write(''.join([symbol_start_spacing, symbol]))
                    for i in keys[1:-1]:
                        pretty_output.write(''.join([symbol_mid_spacing, symbol]))
                    pretty_output.write('\n')
                    cnt = cnt + 1

        print(pretty_output.getvalue())



class BinarySearchTree(BinaryTree):
    def add(self,element):
            node = Node(element,None,None)
            if self.root is None:
                self.root = node;
                self.size += 1
                return

            cur = self.root
            parent = cur
            while(cur):
                parent = cur
                if element > cur.element:
                    cur = cur.right
                elif element < cur.element:
                    cur = cur.left
                else:
                    cur.element = element
                    return
            
            if element < parent.element:
                parent.left = node
            else:
                parent.right = node

            node.parent = parent
            self.size += 1

    def remove(self,element):
        pass

tree = BinarySearchTree()
arr = [29, 36, 72, 33, 19, 4, 26, 22, 5, 17, 42, 44, 31]
for i in arr:
    tree.add(i)

# tree.printTree()
Printer().printTree(tree.root,tree.getheight())
a = [None,None]
# a.append(arr)
# a[0].pop(0)
# a.remove(None)
# print(a)
# print(arr)

'''
                                                 29                                                                                                
                                               /   \
                                              /     \
                         19                                              36                                                
                       /   \                                           /   \
                      /     \                                         /     \
             4                       26                      33                      72                        
           /   \                   /   \                   /   \                   /   \
          /     \                 /     \                 /     \                 /     \
       N           5           22          N           N          10           42          N             
     /   \       /   \       /   \       /   \       /   \       /   \       /   \       /   \
    /     \     /     \     /     \     /     \     /     \     /     \     /     \     /     \
    N     N     N     17    N     N     N     N     N     N     N     11    N     44   N     N  
'''