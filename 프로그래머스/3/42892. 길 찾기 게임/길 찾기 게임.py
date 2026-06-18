import sys
sys.setrecursionlimit(10**6)


class Node:
    def __init__(self, info, num):
        self.info = info      # [x, y]
        self.num = num        # 노드 번호
        self.left = None
        self.right = None


def make_BT(nodeinfo):
    nodes = [i for i in range(1, len(nodeinfo) + 1)]

    # y 큰 순서, y 같으면 x 작은 순서
    nodes.sort(
        key=lambda x: (nodeinfo[x - 1][1], -nodeinfo[x - 1][0]),
        reverse=True
    )

    root = Node(nodeinfo[nodes[0] - 1], nodes[0])

    for i in range(1, len(nodes)):
        parent = root
        node = Node(nodeinfo[nodes[i] - 1], nodes[i])

        while True:
            # x가 작으면 왼쪽
            if node.info[0] < parent.info[0]:
                if parent.left is not None:
                    parent = parent.left
                else:
                    parent.left = node
                    break

            # x가 크면 오른쪽
            else:
                if parent.right is not None:
                    parent = parent.right
                else:
                    parent.right = node
                    break

    return root


def preorder(node, result):
    if node is None:
        return

    result.append(node.num)
    preorder(node.left, result)
    preorder(node.right, result)


def postorder(node, result):
    if node is None:
        return

    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.num)


def solution(nodeinfo):
    root = make_BT(nodeinfo)

    pre_result = []
    post_result = []

    preorder(root, pre_result)
    postorder(root, post_result)

    return [pre_result, post_result]