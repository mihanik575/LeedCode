# https://leetcode.com/problems/copy-list-with-random-pointer/?envType=daily-question&envId=2023-09-05

class Solution:
  def copyRandomList(self, head: 'Node') -> 'Node':
    if not head:
      return None
    if head in self.map:
      return self.map[head]

    newNode = Node(head.val)
    self.map[head] = newNode
    newNode.next = self.copyRandomList(head.next)
    newNode.random = self.copyRandomList(head.random)
    return newNode

  map = {}
d=Solution()
d.copyRandomList([[7, 0],[13,0],[11,4],[10,2],[1,0]])