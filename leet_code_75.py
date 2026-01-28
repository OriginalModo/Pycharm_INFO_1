




from typing import List, Optional
import re
from collections import deque









### TODO LeetCode 75





# ### TODO Intervals



# ### TODO 452. Minimum Number of Arrows to Burst Balloons    больше >
# Задача: даны отрезки points[i] = [xstart, xend] — проекции шариков по оси X.
# Стрела выпускается вертикально вверх из точки x и лопает все шарики, для которых:
# xstart <= x <= xend
# Нужно найти минимальное число стрел, чтобы лопнуть все шарики.
#
# Example 1:
# points = [[10,16],[2,8],[1,6],[7,12]] -> 2
#
# Example 2:
# points = [[1,2],[3,4],[5,6],[7,8]] -> 4
#
# Example 3:
# points = [[1,2],[2,3],[3,4],[4,5]] -> 2
#
# Паттерн: Greedy + Sorting (как интервалы/покрытие точками)
#
# ============================================================
# 1) Вариант "лучший для собеседования": сортировка по правому концу + greedy (O(n log n) время, O(1) память)
#
# Идея:
# Хотим ставить стрелу так, чтобы она покрывала максимум шариков.
# Если отсортировать по xend (по правой границе), то оптимально:
# - первая стрела летит в x = xend первого отрезка
# - далее, если следующий отрезок начинается после позиции стрелы (xstart > arrow_x),
#   нужна новая стрела, и ставим её в x = xend этого отрезка
# - иначе текущая стрела уже лопает этот шарик
#
# Сложность:
# Время: O(n log n) (сортировка)
# Память: O(1) доп. (если не считать сортировку; в Python sort in-place)

# from typing import List
#
# class Solution:
#     def findMinArrowShots(self, points: List[List[int]]) -> int:
#         if not points:
#             return 0
#
#         points.sort(key=lambda x: x[1])  # по правой границе
#         arrows = 1
#         arrow_x = points[0][1]
#
#         for s, e in points[1:]:
#             if s > arrow_x:          # не пересекается с текущей стрелой
#                 arrows += 1
#                 arrow_x = e          # ставим стрелу в конец текущего отрезка
#
#         return arrows


### TODO РЕШИТЬ!   key=lambda x: x[1]   points[0][1]   if s >
# def findMinArrowShots(self, points: List[List[int]]) -> int:







# ### TODO 435. Non-overlapping Intervals    меньше <
# Задача: дан массив интервалов intervals[i] = [start, end].
# Нужно вернуть минимальное количество интервалов, которые нужно удалить,
# чтобы оставшиеся интервалы не пересекались.
#
# Важно:
# Интервалы, которые только касаются границей, НЕ считаются пересекающимися:
# [1,2] и [2,3] — OK (не overlap).
#
# Example 1:
# intervals = [[1,2],[2,3],[3,4],[1,3]] -> 1
#
# Example 2:
# intervals = [[1,2],[1,2],[1,2]] -> 2
#
# Example 3:
# intervals = [[1,2],[2,3]] -> 0
#
# Паттерн: Greedy + Sorting (по правой границе)
#
# ============================================================
# 1) Вариант "лучший для собеседования": жадно выбираем максимум непересекающихся (O(n log n) время, O(1) память)
#
# Идея:
# Это классическая задача "Interval Scheduling":
# - сортируем интервалы по end
# - выбираем интервалы с минимальным end, чтобы оставить как можно больше
# Тогда ответ = всего - выбранные.
#
# Как считаем удаления напрямую:
# - держим last_end выбранного интервала
# - если следующий start < last_end -> пересечение, удаляем его (count++)
# - иначе берём его и обновляем last_end = end
#
# Важно про условие касания:
# overlap только если start < last_end (строго), т.к. start == last_end разрешено.
#
# Сложность:
# Время: O(n log n)
# Память: O(1) доп. (не считая памяти, которую использует сортировка)

# from typing import List
#
# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         if not intervals:
#             return 0
#
#         intervals.sort(key=lambda x: x[1])  # сортируем по end
#         removals = 0
#         last_end = intervals[0][1]
#
#         for s, e in intervals[1:]:
#             if s < last_end:     # пересекается -> удаляем текущий
#                 removals += 1
#             else:                # не пересекается -> оставляем
#                 last_end = e
#
#         return removals


### TODO РЕШИТЬ!  key=lambda x: x[1]   intervals[0][1]   if s <
# def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:





# ============================================================
# 2) Вариант "по start": при пересечении оставляем интервал с меньшим end (O(n log n) время, O(1) память)
#
# Идея:
# - сортируем по start
# - идём слева направо, держим prev_end "оставленного" интервала
# - если пересечение (s < prev_end):
#     удаляем один интервал (count++)
#     и оставляем тот, у кого end меньше: prev_end = min(prev_end, e)
#   иначе:
#     prev_end = e
#
# Сложность:
# Время: O(n log n)
# Память: O(1)

# from typing import List
#
# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         if not intervals:
#             return 0
#
#         intervals.sort(key=lambda x: x[0])  # по start
#         removals = 0
#         prev_end = intervals[0][1]
#
#         for s, e in intervals[1:]:
#             if s < prev_end:
#                 removals += 1
#                 prev_end = min(prev_end, e)
#             else:
#                 prev_end = e
#
#         return removals





# ### TODO Binary Search Tree


# ### TODO 450. Delete Node in a BST
# Задача: дан корень BST root и ключ key.
# Нужно удалить узел со значением key (если он есть) и вернуть (возможно новый) корень.
#
# Удаление в BST:
# 1) Находим узел.
# 2) Удаляем:
#    - если нет детей -> просто None
#    - если один ребёнок -> вернуть этого ребёнка
#    - если два ребёнка ->
#        берём inorder successor (минимум в правом поддереве),
#        копируем его значение в текущий узел,
#        затем удаляем successor из правого поддерева.
#
# Example 1:
# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]  (один из валидных)
#
# Example 2:
# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
#
# Example 3:
# Input: root = [], key = 0
# Output: []
#
# Паттерн: BST / Recursion / Inorder Successor


# ============================================================
# 1) Вариант "лучший для собеседования": рекурсивно + successor (min в правом)
#
# Идея:
# - Рекурсивно спускаемся как в обычном поиске в BST.
# - Когда нашли узел:
#   a) нет левого -> вернуть правого
#   b) нет правого -> вернуть левого
#   c) два ребёнка -> заменить значение на successor и удалить successor справа
#
# Сложность:
# Время: O(h) — высота дерева (в среднем O(log n), в худшем O(n))
# Память: O(h) — стек рекурсии

# class Solution:
#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
#         if not root:
#             return None
#
#         if key < root.val:
#             root.left = self.deleteNode(root.left, key)
#             return root
#         if key > root.val:
#             root.right = self.deleteNode(root.right, key)
#             return root
#
#         # key == root.val -> удаляем этот узел
#         if not root.left:
#             return root.right
#         if not root.right:
#             return root.left
#
#         # два ребёнка: ищем successor (минимум в правом поддереве)
#         succ = root.right
#         while succ.left:
#             succ = succ.left
#
#         root.val = succ.val
#         # удаляем successor из правого поддерева
#         root.right = self.deleteNode(root.right, succ.val)
#         return root


### TODO РЕШИТЬ!
# def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:





# ============================================================
# 2) Вариант "чуть более явный": выделяем helper для поиска минимума
#
# Отличие: та же логика, но код проще читать (helper getMin).
#
# Сложность: такая же O(h) по времени, O(h) по памяти (рекурсия)

# class Solution:
#     def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
#         def getMin(node):
#             while node.left:
#                 node = node.left
#             return node
#
#         if not root:
#             return None
#
#         if key < root.val:
#             root.left = self.deleteNode(root.left, key)
#         elif key > root.val:
#             root.right = self.deleteNode(root.right, key)
#         else:
#             if not root.left:
#                 return root.right
#             if not root.right:
#                 return root.left
#
#             succ = getMin(root.right)
#             root.val = succ.val
#             root.right = self.deleteNode(root.right, succ.val)
#
#         return root




# ### TODO 700. Search in a Binary Search Tree
# Задача: дан корень BST (binary search tree) и число val.
# Нужно найти узел со значением val и вернуть поддерево с корнем в этом узле.
# Если такого узла нет — вернуть None.
#
# Свойство BST:
# - все значения в левом поддереве < node.val
# - все значения в правом поддереве > node.val
#
# Example 1:
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
#
# Example 2:
# Input: root = [4,2,7,1,3], val = 5
# Output: []
#
# Паттерн: BST / Binary Search


# ============================================================
# 1) Вариант "лучший для собеседования": итеративный поиск
#
# Идея:
# - идём от корня вниз
# - если val меньше текущего -> идём влево
# - если больше -> идём вправо
# - если равен -> возвращаем узел
#
# Сложность:
# Время: O(h) — h высота дерева (в среднем O(log n), в худшем O(n))
# Память: O(1)

# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         cur = root
#         while cur:
#             if val == cur.val:
#                 return cur
#             if val < cur.val:
#                 cur = cur.left
#             else:
#                 cur = cur.right
#         return None


### TODO РЕШИТЬ!
# def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:



# ============================================================
# 2) Вариант "короткий": рекурсивный
#
# Сложность:
# Время: O(h)
# Память: O(h) — стек рекурсии

# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         if not root:
#             return None
#         if root.val == val:
#             return root
#         if val < root.val:
#             return self.searchBST(root.left, val)
#         return self.searchBST(root.right, val)




# ### TODO Binary Tree - BFS


# ### TODO 1161. Maximum Level Sum of a Binary Tree
# Задача: дано бинарное дерево root.
# Уровень корня = 1, уровень детей = 2 и т.д.
# Нужно вернуть наименьший уровень x, где сумма значений узлов на уровне максимальна.
#
# Example 1:
# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
#
# Example 2:
# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2
#
# Паттерн: BFS / Level Order Traversal


# ============================================================
# 1) Вариант "DFS": суммируем уровни в массив и потом ищем максимум
#
# Идея:
# - DFS с глубиной depth (0-based).
# - sums[depth] += node.val, при необходимости расширяем sums.
# - После обхода ищем индекс максимума (при равенстве берём меньший).
#
# Сложность:
# Время: O(n)
# Память: O(h) стек + O(k) sums (k — число уровней)

# class Solution:
#     def maxLevelSum(self, root: Optional[TreeNode]) -> int:
#         res = []
#
#         def dfs(node, depth):
#             if not node:
#                 return
#             if depth == len(res):
#                 res.append(0)
#             res[depth] += node.val
#             dfs(node.left, depth + 1)
#             dfs(node.right, depth + 1)
#
#         dfs(root, 0)
#
#         best_idx = 0
#         for i in range(1, len(res)):
#             if res[i] > res[best_idx]:
#                 best_idx = i
#
#         return best_idx + 1  # уровни считаются с 1


### TODO РЕШИТЬ!
# def maxLevelSum(self, root: Optional[TreeNode]) -> int:






# ============================================================
# 2) Вариант "лучший для собеседования": BFS по уровням
#
# Идея:
# - Обходим дерево по уровням очередью.
# - Для каждого уровня считаем сумму.
# - Храним best_sum и best_level (если сумма строго больше — обновляем).
# - Так как нужен минимальный уровень при равенстве, обновляем только при ">".
#
# Сложность:
# Время: O(n)
# Память: O(w) — ширина дерева (очередь), в худшем случае O(n)

# from collections import deque
#
# class Solution:
#     def maxLevelSum(self, root: Optional[TreeNode]) -> int:
#         q = deque([root])
#         level = 1
#         best_level = 1
#         best_sum = float("-inf")
#
#         while q:
#             level_sum = 0
#             for _ in range(len(q)):
#                 node = q.popleft()
#                 level_sum += node.val
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#
#             if level_sum > best_sum:
#                 best_sum = level_sum
#                 best_level = level
#
#             level += 1
#
#         return best_level







# ### TODO 199. Binary Tree Right Side View      right  left
# Задача: дано бинарное дерево root.
# Если смотреть на дерево справа, нужно вернуть значения видимых узлов сверху вниз.
#
# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
#
# Example 2:
# Input: root = [1,2,3,4,null,null,null,5]
# Output: [1,3,4,5]
#
# Example 3:
# Input: root = [1,null,3]
# Output: [1,3]
#
# Example 4:
# Input: root = []
# Output: []
#
# Паттерн: BFS (level order) / DFS (right-first)



# ============================================================
# 1) Вариант "короткий": DFS (сначала вправо), первый узел на глубине = ответ
#
# Идея:
# - Идём DFS: сначала right, потом left.
# - Если мы впервые оказались на глубине depth (depth == len(res)),
#   значит это самый правый узел на этом уровне — добавляем его.
#
# Сложность:
# Время: O(n)
# Память: O(h) — стек рекурсии (в худшем случае O(n))

# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         res = []
#
#         def dfs(node, depth):
#             if not node:
#                 return
#             if depth == len(res):
#                 res.append(node.val)
#             dfs(node.right, depth + 1)
#             dfs(node.left, depth + 1)
#
#         dfs(root, 0)
#         return res


### TODO РЕШИТЬ!     right   left
# def rightSideView(self, root: Optional[TreeNode]) -> List[int]:




# ============================================================
# 2) Вариант "лучший для собеседования": BFS по уровням
#
# Идея:
# - Делаем обход по уровням (очередь).
# - На каждом уровне берём значение последнего узла (самый правый на уровне).
#
# Сложность:
# Время: O(n)
# Память: O(w) — ширина дерева (очередь), в худшем случае O(n)

# from collections import deque
#
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#
#         res = []
#         q = deque([root])
#
#         while q:
#             level_size = len(q)
#             last_val = None
#
#             for _ in range(level_size):
#                 node = q.popleft()
#                 last_val = node.val
#
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#
#             res.append(last_val)
#
#         return res





# ### TODO Binary Tree - DFS



# ### TODO 236. Lowest Common Ancestor of a Binary Tree
# Задача: дано бинарное дерево root и два узла p и q (ссылки на узлы).
# Нужно найти их Lowest Common Ancestor (LCA) — самый “низкий” (ближайший к ним) узел,
# который имеет и p, и q в своём поддереве (узел может быть потомком сам себя).
#
# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p=5, q=1
# Output: 3
#
# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p=5, q=4
# Output: 5
#
# Example 3:
# Input: root = [1,2], p=1, q=2
# Output: 1
#
# Паттерн: DFS / Postorder / Divide & Conquer


# ============================================================
# 1) Вариант "лучший для собеседования": рекурсивный DFS (postorder)
#
# Идея:
# - Рекурсивно ищем p и q в левом и правом поддеревьях.
# - База:
#   - если root == None -> None
#   - если root == p или root == q -> вернуть root (нашли один из узлов)
# - Пусть left = LCA(root.left), right = LCA(root.right)
#   - если left и right оба не None -> p и q лежат в разных ветках => root и есть LCA
#   - иначе возвращаем тот, который не None (оба в одной ветке)
#
# Сложность:
# Время: O(n) — обходим дерево один раз
# Память: O(h) — стек рекурсии (h — высота дерева; в худшем случае O(n))

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if not root or root == p or root == q:
#             return root
#
#         left = self.lowestCommonAncestor(root.left, p, q)
#         right = self.lowestCommonAncestor(root.right, p, q)
#
#         if left and right:
#             return root
#         return left or right


### TODO РЕШИТЬ!
# def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':




# ### TODO 1372. Longest ZigZag Path in a Binary Tree
# Задача: дано бинарное дерево root.
# ZigZag-путь:
# - выбираем стартовый узел и направление (left или right)
# - делаем шаг в выбранную сторону
# - затем каждый шаг меняем направление на противоположное
# Длина ZigZag = кол-во посещённых узлов - 1 (один узел => 0).
# Нужно вернуть максимальную длину ZigZag-пути в дереве.
#
# Example 1:
# Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
# Output: 3
#
# Example 2:
# Input: root = [1,1,1,null,1,null,null,1,1,null,1]
# Output: 4
#
# Example 3:
# Input: root = [1]
# Output: 0
#
# Паттерн: DFS / Backtracking


# ============================================================
# 1) Вариант (как в примере): DFS + "продолжить" / "перезапустить" зигзаг
#
# Идея:
# - dfs(node, goLeft, steps)
#   где:
#   - goLeft: какой шаг должен быть СЛЕДУЮЩИМ
#       True  -> следующий шаг влево
#       False -> следующий шаг вправо
#   - steps: текущая длина ZigZag (число рёбер)
#
# В каждом узле:
# 1) обновляем глобальный максимум self.pathLength = max(self.pathLength, steps)
# 2) делаем два вида переходов:
#    A) Продолжить зигзаг в нужную сторону:
#       - если goLeft=True  -> идём в node.left  с steps+1, дальше ждём вправо (goLeft=False)
#       - если goLeft=False -> идём в node.right с steps+1, дальше ждём влево (goLeft=True)
#    B) Перезапустить зигзаг в противоположную сторону от текущего узла:
#       - если ожидали left, то можем начать вправо: идём в node.right с длиной 1
#       - если ожидали right, то можем начать влево: идём в node.left с длиной 1
#
# Почему работает:
# - "перезапуск" гарантирует, что любой узел может стать стартом пути,
#   поэтому мы найдём максимум по всем возможным ZigZag-путям.
#
# Сложность:
# Время: O(n) — каждый узел обрабатываем константное число раз
# Память: O(h) — стек рекурсии (h — высота дерева; в худшем случае O(n))

# ВАЖНО:
# В исходном коде пользователя в ветке goLeft == False перепутаны переходы.
# Ниже — исправленная версия в том же стиле.

# class Solution:
#     def longestZigZag(self, root: Optional[TreeNode]) -> int:
#         self.pathLength = 0
#
#         def dfs(node, goLeft, steps):
#             if not node:
#                 return
#
#             self.pathLength = max(self.pathLength, steps)
#
#             if goLeft:
#                 # продолжить влево
#                 dfs(node.left, False, steps + 1)
#                 # перезапуск вправо
#                 dfs(node.right, True, 1)
#             else:
#                 # продолжить вправо
#                 dfs(node.right, True, steps + 1)
#                 # перезапуск влево
#                 dfs(node.left, False, 1)
#
#         dfs(root, True, 0)
#         dfs(root, False, 0)   # чтобы стартовать в обе стороны
#         return self.pathLength


### TODO РЕШИТЬ!
# def longestZigZag(self, root: Optional[TreeNode]) -> int:






# ### TODO 437. Path Sum III
# Задача: дано бинарное дерево root и число targetSum.
# Нужно посчитать количество путей, сумма значений на которых равна targetSum.
# Путь должен идти только вниз (parent -> child), но может начинаться и заканчиваться где угодно.
#
# Example 1:
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
#
# Example 2:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3
#
# Паттерн: DFS / Prefix Sum / HashMap


# ============================================================
# 1) Вариант "простой": для каждого узла считаем пути, начинающиеся в нём
#
# Идея:
# - Функция from_node(node, need): сколько путей вниз от node дают сумму need.
# - Ответ = from_node(root, target) + (то же для левого поддерева) + (то же для правого).
#
# Сложность:
# Время: O(n^2) в худшем случае (вытянутое дерево)
# Память: O(h) — стек рекурсии

# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         def from_node(node, need):
#             if not node:
#                 return 0
#             cnt = 1 if node.val == need else 0
#             cnt += from_node(node.left, need - node.val)
#             cnt += from_node(node.right, need - node.val)
#             return cnt
#
#         if not root:
#             return 0
#         return (from_node(root, targetSum) +
#                 self.pathSum(root.left, targetSum) +
#                 self.pathSum(root.right, targetSum))



### TODO РЕШИТЬ!
# def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:






# ============================================================
# 2) Вариант "лучший для собеседования": Prefix Sum + HashMap (O(n))
#
# Идея:
# - Идём DFS от корня и ведём текущую сумму prefix (сумма значений от root до текущего узла).
# - Пусть текущая сумма = prefix. Тогда нам нужен предыдущий prefix_old такой, что:
#     prefix - prefix_old == targetSum  =>  prefix_old == prefix - targetSum
# - Храним в словаре cnt[prefix] сколько раз такой prefix встречался на текущем пути.
# - Когда пришли в узел:
#   1) prefix += node.val
#   2) добавляем к ответу cnt[prefix - targetSum]
#   3) cnt[prefix] += 1
#   4) рекурсивно идём в детей
#   5) откатываем cnt[prefix] -= 1 (backtracking)
#
# Важно:
# - cnt[0] = 1 в начале, чтобы учитывать путь, который начинается "с корня" текущего DFS.
#
# Сложность:
# Время: O(n) — каждый узел обрабатываем один раз
# Память: O(h) — количество prefix на текущем пути (в худшем случае O(n))

# from collections import defaultdict
#
# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         cnt = defaultdict(int)
#         cnt[0] = 1  # пустой префикс
#
#         def dfs(node, prefix):
#             if not node:
#                 return 0
#
#             prefix += node.val
#             res = cnt[prefix - targetSum]
#
#             cnt[prefix] += 1
#             res += dfs(node.left, prefix)
#             res += dfs(node.right, prefix)
#             cnt[prefix] -= 1  # откат
#
#             return res
#
#         return dfs(root, 0)




# ### TODO 1448. Count Good Nodes in Binary Tree
# Задача: дано бинарное дерево root.
# Узел X называется "good", если на пути от root до X нет узла со значением > X.
# (то есть X >= max на всём пути от корня до него)
# Нужно вернуть количество good-узлов.
#
# Example 1:
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
#
# Example 2:
# Input: root = [3,3,null,4,2]
# Output: 3
#
# Example 3:
# Input: root = [1]
# Output: 1
#
# Паттерн: DFS / Tree Traversal / Running Maximum


# ============================================================
# 1) Вариант "простой и очень читаемый" (рекурсивный DFS)
#
# Идея:
# - Идём DFS от корня.
# - Передаём max_so_far — максимальное значение на пути от root до текущего узла.
# - Узел good, если node.val >= max_so_far.
# - Обновляем max_so_far = max(max_so_far, node.val) и идём в детей.
#
# Сложность:
# Время: O(n) — каждый узел посещаем один раз
# Память: O(h) — стек рекурсии (h — высота дерева; в худшем случае O(n))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         def dfs(node, max_so_far):
#             if not node:
#                 return 0
#
#             good = 1 if node.val >= max_so_far else 0
#             new_max = max(max_so_far, node.val)
#
#             good += dfs(node.left, new_max)
#             good += dfs(node.right, new_max)
#             return good
#
#         return dfs(root, root.val)



### TODO РЕШИТЬ!
# def goodNodes(self, root: TreeNode) -> int:




# ============================================================
# 2) Вариант "лучше для собеседования в Python" (итеративный DFS без рекурсии)
#
# Идея:
# - Используем стек: (node, max_so_far).
# - Достаём узел, проверяем good, обновляем max_so_far, кладём детей в стек.
# - Избегаем recursion depth limit.
#
# Сложность:
# Время: O(n)
# Память: O(h) в среднем (стек), в худшем случае O(n)

# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#
#         ans = 0
#         stack = [(root, root.val)]  # (node, max_so_far)
#
#         while stack:
#             node, max_so_far = stack.pop()
#
#             if node.val >= max_so_far:
#                 ans += 1
#
#             new_max = max(max_so_far, node.val)
#
#             if node.right:
#                 stack.append((node.right, new_max))
#             if node.left:
#                 stack.append((node.left, new_max))
#
#         return ans




# ### TODO 872. Leaf-Similar Trees
# Задача: даны два бинарных дерева root1 и root2.
# Листья дерева — это узлы без детей. Если прочитать листья слева направо,
# получим последовательность значений листьев.
# Два дерева leaf-similar, если их последовательности листьев совпадают.
# Нужно вернуть True/False.
#
# Example 1:
# Input:
# root1 = [3,5,1,6,2,9,8,null,null,7,4]
# root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
#
# Example 2:
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false
#
# Паттерн: DFS / Tree Traversal / Generator

# ============================================================
# 1) Вариант "простой и очень читаемый": собрать листья в списки и сравнить
#
# Идея:
# - DFS слева направо генерирует значения листьев (yield).
# - Превращаем генератор в список для каждого дерева и сравниваем списки.

# Сложность:
# Время: O(n + m)
# Память: O(L1 + L2 + h1 + h2)
#   L — число листьев (списки), h — высота дерева (стек рекурсии)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def leafSimilar(self, root1, root2):
#         def dfs(node):
#             if node:
#                 if not node.left and not node.right:
#                     yield node.val
#                 yield from dfs(node.left)
#                 yield from dfs(node.right)
#
#         return list(dfs(root1)) == list(dfs(root2))



### TODO РЕШИТЬ!
# def leafSimilar(self, root1, root2):



# ============================================================
# 2) Вариант "лучше для собеседования": сравнение листьев на лету (без списков)
#
# Идея:
# - делаем генератор, который выдаёт листья слева направо
# - берём следующий лист из обоих деревьев и сравниваем
# - если нашли отличие — сразу False
# - если оба генератора закончились одновременно — True
#
# Почему это сильнее:
# - не храним все листья, можно выйти раньше при первом отличии
#
# Сложность:
# Время: O(n + m)
# Память: O(h1 + h2) — только стек/итерация, без O(L) на списки

# class Solution:
#     def leafSimilar(self, root1, root2):
#         def leaves(root):
#             stack = [root]
#             while stack:
#                 node = stack.pop()
#                 if not node:
#                     continue
#
#                 if not node.left and not node.right:   # лист
#                     yield node.val
#                 else:
#                     # Важно: сначала right, потом left (stack = LIFO),
#                     # чтобы left обработался раньше => порядок слева направо
#                     stack.append(node.right)
#                     stack.append(node.left)
#
#         it1, it2 = leaves(root1), leaves(root2)
#
#         while True:
#             v1 = next(it1, None)
#             v2 = next(it2, None)
#
#             if v1 != v2:
#                 return False
#             if v1 is None:  # значит оба закончились
#                 return True




### TODO БОНУС
# ### TODO 110. Balanced Binary Tree
# Задача: проверить, является ли бинарное дерево сбалансированным по высоте.
# Дерево сбалансировано, если для каждого узла:
# |height(left) - height(right)| <= 1
#
# Example 1:
# [3,9,20,null,null,15,7] -> True
#
# Example 2:
# [1,2,2,3,3,null,null,4,4] -> False
#
# Example 3:
# [] -> True
#
# Паттерн: Tree / DFS (postorder)

# BFS хуже, потому что требует многократного пересчета высот поддеревьев, что может привести к O(n²),    <-----
# в то время как DFS с пост-обходом решает задачу за O(n).
# ============================================================
# 1) Вариант "лучший для собеседования": DFS снизу вверх, возвращаем height или -1 (O(n), O(h))
#
# Идея:
# Функция dfs(node) возвращает:
# - высоту поддерева, если оно сбалансировано
# - -1, если найден дисбаланс (сентинел)
# Тогда при первом дисбалансе можно быстро "протянуть" -1 наверх.
#
# Сложность:
# Время: O(n) (каждый узел посещаем один раз)
# Память: O(h) (стек рекурсии, h — высота дерева)

# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         def dfs(node):
#             if not node:
#                 return 0
#
#             l = dfs(node.left)
#             if l == -1:
#                 return -1
#
#             r = dfs(node.right)
#             if r == -1:
#                 return -1
#
#             if abs(l - r) > 1:
#                 return -1
#
#             return 1 + max(l, r)
#
#         return dfs(root) != -1


# # # ### TODO РЕШИТЬ!  BFS хуже, потому что пересчитывает высоты несколько раз, что может дать O(n²), в отличие от O(n) у DFS.
# def isBalanced(self, root: Optional[TreeNode]) -> bool:




# ### TODO 104. Maximum Depth of Binary Tree
# Задача: вернуть максимальную глубину бинарного дерева.
# Глубина = количество узлов на самом длинном пути от корня до листа.

# Example 1:
# Input: root = [3,9,20,None,None,15,7]
# Output: 3
#
# Example 2:
# Input: root = [1,None,2]
# Output: 2


# --- Definition for a binary tree node ---
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 1) Лучший вариант для собеседования: Рекурсия (DFS)
# DFS = Depth-First Search — поиск в глубину.

# Сложность:
# Время: O(n) — посещаем каждый узел 1 раз.
# Память: O(h) — стек рекурсии, где h — высота дерева (в худшем O(n), в сбалансированном O(log n)).


# class SolutionDFS:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


### TODO РЕШИТЬ!
# def maxDepth(self, root: Optional[TreeNode]) -> int:



# 2) Альтернатива: Итеративно (BFS по уровням)
# BFS = Breadth-First Search — поиск в ширину (по уровням).

# Сложность:
# Время: O(n) — каждый узел попадает в очередь 1 раз.
# Память: O(w) — очередь, где w — максимальная ширина дерева (в худшем O(n)).


# from collections import deque

# class SolutionBFS:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#
#         q = deque([root])
#         depth = 0
#
#         while q:
#             depth += 1
#             for _ in range(len(q)):
#                 node = q.popleft()
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#
#         return depth


### TODO БОНУС
# ### TODO 111. Minimum Depth of Binary Tree


# Input: root = [3,9,20,null,null,15,7]
# Output: 2

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# --- 1) Рекурсия (DFS) — важно правильно обрабатывать "одного ребёнка нет" ---
## DFS = Depth-First Search — поиск в глубину (идём “вниз” по ветке как можно глубже, потом назад).


## Сложность: где n — число узлов, h — высота дерева.
## Время: O(n)
## Память: O(h)

# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#
#         if not root.left:
#             return 1 + self.minDepth(root.right)
#         if not root.right:
#             return 1 + self.minDepth(root.left)
#
#         return 1 + min(self.minDepth(root.left), self.minDepth(root.right))



### TODO РЕШИТЬ!       DFS -> root.right  root.left      BFS ->  q = deque([(root, 1)])
# def minDepth(self, root: Optional[TreeNode]) -> int:




# --- 2) Итеративно (BFS) — лучше для minDepth, можно закончить на первом листе ---
## BFS = Breadth-First Search — поиск в ширину (идём по уровням: сначала корень, потом все дети, потом внуки и т.д.).

## Сложность: где n — число узлов, w — максимальная ширина дерева.
## Время: O(n)
## Память: O(w)  (в худшем O(n))

# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#
#         q = deque([(root, 1)])  # (node, depth)
#         while q:
#             node, d = q.popleft()
#             if not node.left and not node.right:
#                 return d
#             if node.left:
#                 q.append((node.left, d + 1))
#             if node.right:
#                 q.append((node.right, d + 1))
#
#         return 0







# ### TODO Linked List


# ### TODO 2130. Maximum Twin Sum of a Linked List
# Задача: список чётной длины n. "Близнецы" — i-й и (n-1-i)-й узлы.
# Нужно найти максимальную сумму val(i) + val(n-1-i) для i в [0 .. n/2 - 1].

# Example 1:
# Input: head = [5,4,2,1]
# Output: 6
#
# Example 2:
# Input: head = [4,2,2,3]
# Output: 7
#
# Example 3:
# Input: head = [1,100000]
# Output: 100001


# 1) Лучший вариант для собеседования: slow/fast + reverse второй половины
# Идея:
# - находим середину (slow/fast)
# - разворачиваем вторую половину списка
# - идём двумя указателями (с начала и с начала развёрнутой половины) и считаем max суммы
# Паттерн: Two Pointers + Reverse Linked List

# Сложность:
# Время: O(n) — найти середину + развернуть + один проход для подсчёта.
# Память: O(1) — всё делаем на месте.

# from typing import Optional, List

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# def pairSum(head: Optional[ListNode]) -> int:
#     # 1) найти середину
#     slow = head
#     fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#
#     # 2) развернуть вторую половину (начиная с slow)
#     prev = None
#     cur = slow
#     while cur:
#         nxt = cur.next
#         cur.next = prev
#         prev = cur
#         cur = nxt
#     # prev = голова развёрнутой второй половины
#
#     # 3) посчитать максимум twin sum
#     best = 0
#     p1 = head
#     p2 = prev
#     while p2:  # длина второй половины = n/2
#         best = max(best, p1.val + p2.val)
#         p1 = p1.next
#         p2 = p2.next
#
#     return best


# ### TODO РЕШИТЬ!
# def pairSum(head: Optional[ListNode]) -> int:






# ### TODO 206. Reverse Linked List
# Задача: дан head односвязного списка. Нужно развернуть список и вернуть новый head.
#
# Идея (самая популярная): итеративно “переворачиваем” ссылки.
# Держим 3 указателя:
# - prev: уже развернутая часть (сначала None)
# - cur: текущий узел
# - nxt: чтобы не потерять хвост (cur.next)
#
# На каждом шаге:
# 1) сохраняем nxt = cur.next
# 2) разворачиваем cur.next = prev
# 3) двигаем prev = cur, cur = nxt
#
# Когда cur = None — prev и есть новый head.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
# Example 2:
# Input: head = [1,2]
# Output: [2,1]
#
# Example 3:
# Input: head = []
# Output: []

# 1) Лучший вариант для собеседования: итеративный разворот указателей
# Паттерн: Linked List / Two Pointers

# Сложность:
# Время: O(n) — каждый узел посещаем один раз
# Память: O(1) — меняем ссылки на месте


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev = None
#         cur = head
#
#         while cur:
#             nxt = cur.next      # 1) сохранить хвост
#             cur.next = prev     # 2) развернуть ссылку
#             prev = cur          # 3) сдвинуть prev
#             cur = nxt           # 4) сдвинуть cur
#
#         return prev


### TODO РЕШИТЬ!
# def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:





# ### TODO 328. Odd Even Linked List
# Задача: перегруппировать узлы списка так:
# сначала узлы с НЕЧЁТНЫМИ индексами (1-й, 3-й, 5-й...), потом с ЧЁТНЫМИ (2-й, 4-й...).
# Важно: порядок внутри odd-группы и even-группы должен сохраниться.
# Требования: O(n) по времени и O(1) доп. памяти.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
#
# Example 2:
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]


# 1) Лучший вариант для собеседования: 2 указателя (odd/even) + "голова" even
# Паттерн: Two Pointers / In-place Linked List

# Сложность:
# Время: O(n) — один проход по списку.
# Память: O(1) — меняем ссылки на месте (без доп. структур).


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
#     if not head or not head.next:
#         return head
#
#     odd = head                 # текущий odd-узел
#     even = head.next           # текущий even-узел
#     even_head = even           # запомним начало even-цепочки
#
#     while even and even.next:
#         odd.next = even.next   # odd перепрыгивает на следующий odd
#         odd = odd.next
#
#         even.next = odd.next   # even перепрыгивает на следующий even
#         even = even.next
#
#     odd.next = even_head       # приклеиваем even-цепочку в конец odd
#     return head


#### TODO РЕШИТЬ!
# def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:






# ### TODO 2095. Delete the Middle Node of a Linked List
# Задача: удалить "средний" узел списка и вернуть голову.
# middle = floor(n/2) по 0-based индексации.
# Если n = 1 -> после удаления список пустой (None).
#
# Идея (каноническая): Slow/Fast pointers.
# fast идёт по 2 шага, slow по 1 — когда fast дошёл до конца, slow в середине.
# Чтобы удалить middle, нужен prev (узел перед slow).

# Example 1:
# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
#
# Example 2:
# Input: head = [1,2,3,4]
# Output: [1,2,4]
#
# Example 3:
# Input: head = [2,1]
# Output: [2]


# 1) Лучший вариант для собеседования: Slow/Fast + prev
# Паттерн: Two Pointers (slow/fast)

# Сложность:
# Время: O(n) — один проход (fast бежит до конца).
# Память: O(1) — только несколько указателей.


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# from typing import Optional, List
#
# def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
#     if not head or not head.next:
#         return None  # n=0 или n=1
#
#     prev = None
#     slow = head
#     fast = head
#
#     while fast and fast.next:
#         prev = slow
#         slow = slow.next
#         fast = fast.next.next
#
#     # slow сейчас на middle, prev перед ним
#     prev.next = slow.next
#     return head


### TODO РЕШИТЬ!
# def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:




# ### TODO Queue


# ### TODO 649. Dota2 Senate
# Задача: есть сенаторы 'R' и 'D'. По очереди они либо банят противника, либо (когда осталась одна партия)
# объявляют победу. Все играют оптимально. Нужно вернуть "Radiant" или "Dire".
#
# Идея (каноническая): Queue (две очереди индексов).
# Пусть n = len(senate). Запишем индексы всех R в одну очередь, всех D — в другую.
# В каждом шаге сравниваем ближайших (r_idx и d_idx):
# - кто меньше, тот ходит раньше и банит другого
# - победивший возвращается в конец своей очереди с индексом + n (как “следующий раунд”)
# Когда одна очередь пустая — победитель известен.

# Example 1:
# Input: senate = "RD"
# Output: "Radiant"
#
# Example 2:
# Input: senate = "RDD"
# Output: "Dire"


# 1) Лучший вариант для собеседования: две очереди индексов
# Паттерн: Queue / Simulation

# Сложность:
# Время: O(n) амортизированно — каждый сенатор добавляется/удаляется из очереди ограниченное число раз.
# Память: O(n) — храним индексы в очередях.


# from collections import deque

# def predictPartyVictory(senate: str) -> str:
#     n = len(senate)
#     rq = deque()
#     dq = deque()
#
#     for i, ch in enumerate(senate):
#         if ch == 'R':
#             rq.append(i)
#         else:
#             dq.append(i)
#
#     while rq and dq:
#         r = rq.popleft()
#         d = dq.popleft()
#
#         if r < d:
#             # R ходит раньше и банит D
#             rq.append(r + n)
#         else:
#             # D ходит раньше и банит R
#             dq.append(d + n)
#
#     return "Radiant" if rq else "Dire"
#
#
# print(predictPartyVictory("RD"))   # -> Radiant
# print(predictPartyVictory("RDD"))  # -> Dire
# print(predictPartyVictory("RRDDD"))  # -> Dire
# print(predictPartyVictory("RDRDR"))  # -> Radiant


### TODO РЕШИТЬ!
# def predictPartyVictory(senate: str) -> str:




# ### TODO 933. Number of Recent Calls
# Задача: реализовать RecentCounter, который хранит времена запросов.
# ping(t) добавляет запрос в момент t и возвращает количество запросов в диапазоне [t-3000, t].
# Важно: t строго возрастает → можно использовать очередь (deque) и удалять старые запросы слева.

# Example 1:
# Input:
# ["RecentCounter","ping","ping","ping","ping"]
# [[],[1],[100],[3001],[3002]]
# Output:
# [null,1,2,3,3]


# 1) Лучший вариант для собеседования: Queue (deque)
# Паттерн: Queue / Sliding Window

# Сложность:
# Время: O(1) амортизированно на один ping (каждый элемент добавляется и удаляется максимум 1 раз).
# Память: O(w), где w — число запросов в последних 3000 мс (в худшем O(n) по числу вызовов).


# from collections import deque

# class RecentCounter:
#     def __init__(self):
#         self.q = deque()
#
#     def ping(self, t: int) -> int:
#         self.q.append(t)
#
#         left = t - 3000
#         while self.q and self.q[0] < left:
#             self.q.popleft()
#
#         return len(self.q)
#
#
# # --- Local test в стиле “как на LeetCode” ---
# rc = RecentCounter()
# print(rc.ping(1))     # -> 1
# print(rc.ping(100))   # -> 2
# print(rc.ping(3001))  # -> 3
# print(rc.ping(3002))  # -> 3


# 2) Альтернатива: список + указатель (тоже “очередь”, но без popleft)
# Паттерн: Two Pointers / Sliding Window

# Сложность:
# Время: O(1) амортизированно
# Память: O(n) (список растёт, не удаляем элементы физически)


# class RecentCounterList:
#     def __init__(self):
#         self.arr = []
#         self.start = 0  # индекс первого “актуального” запроса
#
#     def ping(self, t: int) -> int:
#         self.arr.append(t)
#
#         left = t - 3000
#         while self.start < len(self.arr) and self.arr[self.start] < left:
#             self.start += 1
#
#         return len(self.arr) - self.start
#
#
# rc2 = RecentCounterList()
# print(rc2.ping(1))     # -> 1
# print(rc2.ping(100))   # -> 2
# print(rc2.ping(3001))  # -> 3
# print(rc2.ping(3002))  # -> 3







# ### TODO Stack


# ### TODO 394. Decode String
# Задача: декодировать строку по правилу k[encoded_string],
# где encoded_string повторяется k раз. Вложенность возможна: "3[a2[c]]".
# Гарантируется валидный ввод.
#
# Идея: Stack — идём слева направо.
# - если цифра: собираем число k
# - если '[': кладём (текущая_строка, k) в стек и обнуляем текущую строку и k
# - если буква: добавляем к текущей строке
# - если ']': достаём (prev, k) и делаем prev + current*k

# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
#
# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
#
# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"


# 1) Лучший вариант для собеседования: Stack
# Паттерн: Stack
#
# Сложность:
# Время: O(n + out) — читаем вход O(n) и строим выход длины out.
# Память: O(out) — результат + стек/промежуточные строки.


# def decodeString(s: str) -> str:
#     stack = []          # (prev_string, repeat_k)
#     cur = []            # текущая строка как список символов
#     k = 0
#
#     for ch in s:
#         if ch.isdigit():
#             k = k * 10 + int(ch)
#
#         elif ch == '[':
#             stack.append(("".join(cur), k))
#             cur = []
#             k = 0
#
#         elif ch == ']':
#             prev, repeat = stack.pop()
#             cur = [prev + ("".join(cur) * repeat)]
#
#         else:  # буква
#             cur.append(ch)
#
#     return "".join(cur)
#
#
# print(decodeString("3[a]2[bc]"))     # -> aaabcbc
# print(decodeString("3[a2[c]]"))      # -> accaccacc
# print(decodeString("2[abc]3[cd]ef")) # -> abcabccdcdcdef


### TODO РЕШИТЬ!
# def decodeString(s: str) -> str:




# 2) Альтернатива: regex (Python-only трюк)
# Важно: regex не умеет нормально парсить вложенные скобки напрямую,
# поэтому делаем повторные замены “самых внутренних” блоков вида k[letters],
# где внутри НЕТ '[' и ']'. Повторяем, пока скобки не исчезнут.
#
# Паттерн: Regex / Simulation
#
# Сложность:
# Время: обычно O(out * depth) — делаем несколько проходов по строке по мере раскрытия вложенности.
# Память: O(out) — создаются промежуточные строки.


# import re
#
# def decodeString_regex(s: str) -> str:
#     pattern = re.compile(r'(\d+)\[([a-zA-Z]+)\]')  # внутри только буквы, без вложенных скобок
#
#     while '[' in s:
#         s = pattern.sub(lambda m: int(m.group(1)) * m.group(2), s)
#
#     return s
#
#
# print(decodeString_regex("3[a]2[bc]"))     # -> aaabcbc
# print(decodeString_regex("3[a2[c]]"))      # -> accaccacc
# print(decodeString_regex("2[abc]3[cd]ef")) # -> abcabccdcdcdef




# ### TODO 735. Asteroid Collision
# Задача: астероиды движутся по линии.
# знак: + вправо, - влево; модуль = размер.
# Столкновение возможно только когда справа летит вправо ( + ), а новый астероид летит влево ( - ).
# Тогда меньший взрывается, если равны — взрываются оба.
# Нужно вернуть состояние после всех столкновений.
#
# Идея: Stack — держим “живые” астероиды слева.
# Когда приходит отрицательный астероид, он может сталкиваться с верхом стека (пока там положительные).

# Example 1:
# Input: asteroids = [5,10,-5]
# Output: [5,10]
#
# Example 2:
# Input: asteroids = [8,-8]
# Output: []
#
# Example 3:
# Input: asteroids = [10,2,-5]
# Output: [10]
#
# Example 4:
# Input: asteroids = [3,5,-6,2,-1,4]
# Output: [-6,2,4]


# 1) Лучший вариант для собеседования: Stack
# Паттерн: Stack / Simulation

# Сложность:
# Время: O(n) — каждый астероид кладётся в стек и удаляется из него максимум один раз.
# Память: O(n) — стек результата.


# def asteroidCollision(asteroids: list[int]) -> list[int]:
#     stack = []
#
#     for a in asteroids:
#         alive = True
#
#         # столкновения: в стеке справа летит вправо ( >0 ), новый летит влево ( <0 )
#         while alive and a < 0 and stack and stack[-1] > 0:
#             if stack[-1] < -a:
#                 # верх стека меньше -> он взрывается, а a продолжает
#                 stack.pop()
#                 continue
#             elif stack[-1] == -a:
#                 # равны -> оба взрываются
#                 stack.pop()
#                 alive = False
#             else:
#                 # верх стека больше -> a взрывается
#                 alive = False
#
#         if alive:
#             stack.append(a)
#
#     return stack
#
#
# print(asteroidCollision([5, 10, -5]))          # -> [5, 10]
# print(asteroidCollision([8, -8]))              # -> []
# print(asteroidCollision([10, 2, -5]))          # -> [10]
# print(asteroidCollision([3, 5, -6, 2, -1, 4])) # -> [-6, 2, 4]


### TODO РЕШИТЬ!
# def asteroidCollision(asteroids: list[int]) -> list[int]:





# ### TODO 2390. Removing Stars From a String
# Задача: для каждой '*' удалить саму звёздочку и ближайший НЕ-звёздный символ слева.
# Гарантируется, что операция всегда возможна, и итоговая строка уникальна.
# Идея: Stack — идём слева направо:
# - если буква → кладём в стек
# - если '*' → убираем последний символ из стека (pop)
# В конце стек = ответ.

# Example 1:
# Input: s = "leet**cod*e"
# Output: "lecoe"

# Example 2:
# Input: s = "erase*****"
# Output: ""


# 1) Лучший вариант для собеседования: Stack
# Паттерн: Stack

# Сложность:
# Время: O(n) — каждый символ добавляется/удаляется из стека максимум 1 раз.
# Память: O(n) — стек для результата.


# def removeStars(s: str) -> str:
#     stack = []
#     for ch in s:
#         if ch == '*':
#             stack.pop()
#         else:
#             stack.append(ch)
#     return ''.join(stack)
#
#
# print(removeStars("leet**cod*e"))  # -> lecoe
# print(removeStars("erase*****"))   # -> ""


### TODO РЕШИТЬ!
# def removeStars(s: str) -> str:




# ### TODO Hash Map / Set


# ### TODO 2352. Equal Row and Column Pairs
# Задача: посчитать количество пар (row_i, col_j), где строка row_i полностью равна столбцу col_j
# (одинаковые элементы в одинаковом порядке).
# Идея: HashMap/Counter — считаем, сколько раз встречается каждая строка (как tuple),
# затем для каждого столбца (тоже tuple) добавляем число совпадающих строк.

# Example 1:
# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1

# Example 2:
# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3


# 1) Лучший вариант для собеседования: Counter строк + проход по столбцам
# Паттерн: Hash Table

# Сложность:
# Время: O(n^2) — строим n строк и n столбцов длины n.
# Память: O(n^2) — храним строки в Counter (в худшем случае все разные).


# from collections import Counter

# def equalPairs(grid: list[list[int]]) -> int:
#     n = len(grid)
#
#     rows = Counter(tuple(r) for r in grid)
#
#     ans = 0
#     for j in range(n):
#         col = tuple(grid[i][j] for i in range(n))
#         ans += rows.get(col, 0)
#
#     return ans
#
#
# print(equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))  # -> 1
# print(equalPairs([[3, 1, 2, 2],
#                   [1, 4, 4, 5],
#                   [2, 4, 2, 2],
#                   [2, 4, 2, 2]]))  # -> 3


### TODO РЕШИТЬ!
# def equalPairs(grid: list[list[int]]) -> int:



# 2) Альтернатива: без Counter (обычный dict частот)
# Паттерн: Hash Table

# Сложность:
# Время: O(n^2)
# Память: O(n^2)


# def equalPairs_manual(grid: list[list[int]]) -> int:
#     n = len(grid)
#     rows = {}
#
#     for r in grid:
#         t = tuple(r)
#         rows[t] = rows.get(t, 0) + 1
#
#     ans = 0
#     for j in range(n):
#         col = tuple(grid[i][j] for i in range(n))
#         ans += rows.get(col, 0)
#
#     return ans
#
#
# print(equalPairs_manual([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))  # -> 1
# print(equalPairs_manual([[3, 1, 2, 2],
#                          [1, 4, 4, 5],
#                          [2, 4, 2, 2],
#                          [2, 4, 2, 2]]))  # -> 3





# ### TODO 1657. Determine if Two Strings Are Close
# Задача: можно ли превратить word1 в word2 с операциями:
# 1) перестановка любых двух символов (т.е. можно получить любую перестановку)
# 2) обмен “имен” двух существующих букв (все a -> b и все b -> a одновременно)
#
# Ключевые условия (и они одновременно достаточны):
# 1) Длины равны.
# 2) Множества символов одинаковы (нельзя “создать” новую букву, только переименовать существующие).
# 3) Мультимножество частот одинаково (частоты можно переставлять между буквами через операцию 2).

# Example 1:
# Input: word1 = "abc", word2 = "bca"
# Output: True
#
# Example 2:
# Input: word1 = "a", word2 = "aa"
# Output: False
#
# Example 3:
# Input: word1 = "cabbba", word2 = "abbccc"
# Output: True


# 1) Лучший вариант для собеседования: Counter + сравнение ключей и отсортированных частот
# Паттерн: Hash Table / Counting

# Сложность:
# Время: O(n + k log k) — подсчёт частот O(n) + сортировка частот (k = число разных букв, <= 26).
# Память: O(k) — Counter.


# from collections import Counter
#
# def closeStrings(word1: str, word2: str) -> bool:
#     if len(word1) != len(word2):
#         return False
#
#     c1 = Counter(word1)
#     c2 = Counter(word2)
#
#     # должны быть одинаковые наборы букв
#     if set(c1.keys()) != set(c2.keys()):
#         return False
#
#     # должны совпадать “наборы частот” (можно перекидывать частоты между буквами)
#     return sorted(c1.values()) == sorted(c2.values())
#
#
# print(closeStrings("abc", "bca"))        # -> True
# print(closeStrings("a", "aa"))           # -> False
# print(closeStrings("cabbba", "abbccc"))  # -> True



### TODO РЕШИТЬ!
# def closeStrings(word1: str, word2: str) -> bool:




# 2) Без Counter (ручной словарь частот)
# Паттерн: Hash Table / Counting

# Сложность:
# Время: O(n + k log k)
# Память: O(k)


# def closeStrings_manual(word1: str, word2: str) -> bool:
#     if len(word1) != len(word2):
#         return False
#
#     c1 = {}
#     c2 = {}
#
#     for ch in word1:
#         c1[ch] = c1.get(ch, 0) + 1
#     for ch in word2:
#         c2[ch] = c2.get(ch, 0) + 1
#
#     if set(c1.keys()) != set(c2.keys()):
#         return False
#
#     return sorted(c1.values()) == sorted(c2.values())
#
#
# print(closeStrings_manual("abc", "bca"))        # -> True
# print(closeStrings_manual("a", "aa"))           # -> False
# print(closeStrings_manual("cabbba", "abbccc"))  # -> True








# ### TODO 1207. Unique Number of Occurrences
# Задача: проверить, что количества вхождений каждого числа в массиве — уникальны
# (никакие два разных числа не встречаются одинаковое число раз).
# Идея: HashMap/Counter — считаем частоты, затем проверяем, что частоты не повторяются
# (через set).

# Example 1:
# Input: arr = [1,2,2,1,1,3]
# Output: True

# Example 2:
# Input: arr = [1,2]
# Output: False

# Example 3:
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: True


# 1) Лучший вариант для собеседования: Counter + set
# Паттерн: Hash Table

# Сложность:
# Время: O(n) — считаем частоты + проверяем уникальность.
# Память: O(n) — словарь частот + set частот.


# from collections import Counter

# def uniqueOccurrences(arr: list[int]) -> bool:
#     freq = Counter(arr)
#     counts = list(freq.values())
#     return len(counts) == len(set(counts))
#
#
# print(uniqueOccurrences([1, 2, 2, 1, 1, 3]))                  # -> True
# print(uniqueOccurrences([1, 2]))                              # -> False
# print(uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))   # -> True



### TODO РЕШИТЬ!
# def uniqueOccurrences(arr: list[int]) -> bool:






# 2) Альтернатива: без Counter (ручной словарь)
# Паттерн: Hash Table

# Сложность:
# Время: O(n)
# Память: O(n)


# def uniqueOccurrences_manual(arr: list[int]) -> bool:
#     freq = {}
#     for x in arr:
#         freq[x] = freq.get(x, 0) + 1
#
#     seen = set()
#     for c in freq.values():
#         if c in seen:
#             return False
#         seen.add(c)
#     return True
#
#
# print(uniqueOccurrences_manual([1, 2, 2, 1, 1, 3]))                  # -> True
# print(uniqueOccurrences_manual([1, 2]))                              # -> False
# print(uniqueOccurrences_manual([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))   # -> True






# ### TODO 2215. Find the Difference of Two Arrays
# Задача: вернуть 2 списка:
# answer[0] — уникальные числа из nums1, которых нет в nums2
# answer[1] — уникальные числа из nums2, которых нет в nums1
# Идея: Hash Set — превращаем в множества и берём разность множеств.

# Example 1:
# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]

# Example 2:
# Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
# Output: [[3],[]]


# 1) Лучший вариант для собеседования: Set difference
# Паттерн: Hash Set

# Сложность:
# Время: O(n + m) — построение множеств и разности.
# Память: O(n + m) — множества.


# def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
#     s1 = set(nums1)
#     s2 = set(nums2)
#
#     # можно так (оператор):
#     return [list(s1 - s2), list(s2 - s1)]
#
#     # или так (встроенная функция):
#     # return [list(s1.difference(s2)), list(s2.difference(s1))]
#
# print(findDifference([1, 2, 3], [2, 4, 6]))        # -> [[1, 3], [4, 6]]
# print(findDifference([1, 2, 3, 3], [1, 1, 2, 2]))  # -> [[3], []]



### TODO РЕШИТЬ!
# def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:





# ### TODO Prefix Sum


# ### TODO 724. Find Pivot Index
# Задача: найти индекс i, где сумма слева (0..i-1) равна сумме справа (i+1..end).
# Вернуть самый левый такой индекс, иначе -1.
# Идея: Prefix Sum — знаем totalSum, идём слева направо и держим leftSum.
# Тогда rightSum = totalSum - leftSum - nums[i].

# Example 1:
# Input: nums = [1,7,3,6,5,6]
# Output: 3

# Example 2:
# Input: nums = [1,2,3]
# Output: -1

# Example 3:
# Input: nums = [2,1,-1]
# Output: 0


# 1) Лучший вариант для собеседования: Prefix Sum (один проход)
# Паттерн: Prefix Sum

# Сложность:
# Время: O(n) — один проход по массиву.
# Память: O(1) — только total и left.


# def pivotIndex(nums: list[int]) -> int:
#     total = sum(nums)
#     left = 0
#
#     for i, v in enumerate(nums):
#         right = total - left - v
#         if left == right:
#             return i
#         left += v
#
#     return -1
#
#
# print(pivotIndex([1, 7, 3, 6, 5, 6]))  # -> 3
# print(pivotIndex([1, 2, 3]))           # -> -1
# print(pivotIndex([2, 1, -1]))          # -> 0
# print(pivotIndex([0, 0, 0]))           # -> 0


### TODO РЕШИТЬ!
# def pivotIndex(nums: list[int]) -> int:





# ### TODO 1732. Find the Highest Altitude
# Задача: дан массив gain, где gain[i] — изменение высоты от точки i к i+1.
# Нужно вернуть максимальную высоту за всю поездку, стартовая высота = 0.
# Идея: Prefix Sum — накапливаем текущую высоту и обновляем максимум.

# Example 1:
# Input: gain = [-5,1,5,0,-7]
# Output: 1

# Example 2:
# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0


# 1) Лучший вариант для собеседования: Prefix Sum (один проход)
# Паттерн: Prefix Sum

# Сложность:
# Время: O(n) — один проход по массиву gain.
# Память: O(1) — только две переменные (cur, best).


# def largestAltitude(gain: list[int]) -> int:
#     cur = 0
#     best = 0
#     for g in gain:
#         cur += g
#         if cur > best:
#             best = cur
#     return best
#
#
# print(largestAltitude([-5, 1, 5, 0, -7]))           # -> 1
# print(largestAltitude([-4, -3, -2, -1, 4, 3, 2]))   # -> 0
# print(largestAltitude([1, 2, 3]))                   # -> 6
# print(largestAltitude([-1, -2, -3]))                # -> 0



### TODO РЕШИТЬ!
# def largestAltitude(gain: list[int]) -> int:






# ### TODO Sliding Window


# ### TODO 1493. Longest Subarray of 1's After Deleting One Element
# Задача: удалить ровно один элемент и получить максимальную длину подмассива из 1.
# Идея: Sliding Window — держим окно, где количество нулей <= 1.
# Тогда ответ = длина окна - 1 (потому что один элемент удаляем: это либо ноль, либо единица).

# Example 1:
# Input: nums = [1,1,0,1]
# Output: 3

# Example 2:
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5

# Example 3:
# Input: nums = [1,1,1]
# Output: 2


# 1) Лучший вариант для собеседования: Sliding Window (zeros <= 1)
# Паттерн: Sliding Window / Two Pointers

# Сложность:
# Время: O(n) — каждый указатель двигается максимум n раз.
# Память: O(1) — только счётчик нулей и переменные.


# def longestSubarray(nums: list[int]) -> int:
#     left = 0
#     zeros = 0
#     best = 0
#
#     for right in range(len(nums)):
#         if nums[right] == 0:
#             zeros += 1
#
#         while zeros > 1:
#             if nums[left] == 0:
#                 zeros -= 1
#             left += 1
#
#         # удаляем один элемент => длина "единиц" = (right-left+1) - 1
#         best = max(best, right - left)
#
#     return best
#
#
# print(longestSubarray([1, 1, 0, 1]))                   # -> 3
# print(longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))    # -> 5
# print(longestSubarray([1, 1, 1]))                      # -> 2
# print(longestSubarray([0, 0, 0]))                      # -> 0


### TODO РЕШИТЬ!    best = max(best, i - left)
# def longestSubarray(nums: list[int]) -> int:




# ### TODO 1004. Max Consecutive Ones III
# Задача: найти максимальную длину подмассива, где можно “перевернуть” (flip) не более k нулей в единицы.
# Идея: Sliding Window — держим окно, в котором количество нулей <= k.
# Если нулей стало больше k — сдвигаем левую границу, пока снова не станет <= k.

# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6

# Example 2:
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10


# 1) Лучший вариант для собеседования: Sliding Window
# Паттерн: Sliding Window / Two Pointers

# Сложность:
# Время: O(n) — каждый указатель двигается максимум n раз.
# Память: O(1) — только счётчик нулей и переменные.


# def longestOnes(nums: list[int], k: int) -> int:
#     left = 0
#     zeros = 0
#     best = 0
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             zeros += 1
#         while zeros > k:
#             if nums[left] == 0:
#                 zeros -= 1
#             left += 1
#         best = max(best, i - left + 1)
#     return best
#
#
# print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))  # -> 6
# print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))  # -> 10
# print(longestOnes([1,1,1,1], 2))  # -> 4
# print(longestOnes([0,0,0], 1))    # -> 1


### TODO РЕШИТЬ!
# def longestOnes(nums: list[int], k: int) -> int:









### TODO БОНУС
# ### TODO 487. Max Consecutive Ones II
# Задача: дан бинарный массив nums. Можно "перевернуть" (flip) максимум один 0 в 1.
# Нужно вернуть максимальную длину подряд идущих единиц после не более чем одного flip.
#
# Example 1:
# nums = [1,0,1,1,0] -> 4
#
# Example 2:
# nums = [1,0,1,1,0,1] -> 4
#
# Паттерн: Sliding Window / Two Pointers


# ============================================================
# 1) Вариант "лучший для собеседования": Sliding Window с <= 1 нулём (O(n), O(1))
#
# Идея:
# Держим окно [l..r], в котором количество нулей <= 1.
# - расширяем r
# - если нулей стало > 1, сдвигаем l, пока снова не станет <= 1
# - ответ = максимум длины окна
#
# Сложность:
# Время: O(n)
# Память: O(1)

# from typing import List
#
# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         k = 1  # можно перевернуть максимум один 0
#         left = 0
#         zeros = 0
#         best = 0
#
#         for right in range(len(nums)):
#             if nums[right] == 0:
#                 zeros += 1
#
#             while zeros > k:
#                 if nums[left] == 0:
#                     zeros -= 1
#                 left += 1
#
#             best = max(best, right - left + 1)
#
#         return best


### TODO РЕШИТЬ!
# def findMaxConsecutiveOnes(self, nums: List[int]) -> int:





### TODO БОНУС
# ### TODO 485. Max Consecutive Ones
# Задача: дан бинарный массив nums (только 0 и 1).
# Нужно вернуть максимальную длину подряд идущих единиц.
#
# Example 1:
# nums = [1,1,0,1,1,1] -> 3
#
# Example 2:
# nums = [1,0,1,1,0,1] -> 2
#
# Паттерн: Array / Sliding Window (по сути простой счётчик)


# ============================================================
# 1) Вариант "лучший для собеседования": один проход (O(n), O(1))
#
# Идея:
# - cur: текущая длина серии 1
# - best: максимум
# Если видим 1 -> cur += 1, иначе cur = 0.
#
# Сложность:
# Время: O(n)
# Память: O(1)

# from typing import List
#
# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         cur = 0
#         best = 0
#         for i in nums:
#             if i == 1:
#                 cur += 1
#                 best = max(best, cur)
#             else:
#                 cur = 0
#         return best


### TODO РЕШИТЬ!
# def findMaxConsecutiveOnes(self, nums: List[int]) -> int:










# ### TODO 1456. Maximum Number of Vowels in a Substring of Given Length   + ВЫВОД ПОДСТРОКИ
# Задача: найти максимум гласных в любой подстроке длины k.
# Идея: Sliding Window — считаем гласные в первом окне, затем двигаем окно на 1:
# добавляем влияние нового символа и убираем влияние ушедшего.

# Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3

# Example 2:
# Input: s = "aeiou", k = 2
# Output: 2

# Example 3:
# Input: s = "leetcode", k = 3
# Output: 2


# 1) Лучший вариант для собеседования: Sliding Window
# Паттерн: Sliding Window

# Сложность:
# Время: O(n) — один проход по строке.
# Память: O(1) — только счётчик и множество гласных.
# TODO ПАМЯТЬ!
# Да, O(1) здесь правильно (по стандартной оценке алгоритмов), потому что:
# vowels = set("aeiou") — множество фиксированного размера 5, оно не растёт с длиной строки n.
# переменные cur, best, i — тоже константное число.
# Значит дополнительная память не зависит от n → O(1).


# def maxVowels(s: str, k: int) -> int:
#     vowels = set("aeiou")
#
#     # гласные в первом окне
#     cur = sum(1 for ch in s[:k] if ch in vowels)
#     best = cur
#
#     # двигаем окно
#     for i in range(k, len(s)):
#         if s[i] in vowels:
#             cur += 1
#         if s[i - k] in vowels:
#             cur -= 1
#         if cur > best:
#             best = cur
#             if best == k:   # максимум возможный, дальше не улучшить
#                 return k
#
#     return best
#
#
# print(maxVowels("abciiidef", 3))  # -> 3
# print(maxVowels("aeiou", 2))      # -> 2
# print(maxVowels("leetcode", 3))   # -> 2



# # # ### TODO РЕШИТЬ!   for i in range(k, len(s)):
# def maxVowels(s: str, k: int) -> int:




### TODO БОНУС
# ### TODO 1456. Maximum Number of Vowels in a Substring of Given Length    ВЫВОД ПОДСТРОКИ!
# 1) Лучший вариант для собеседования: Sliding Window (вернуть именно гласные)
# Паттерн: Sliding Window
#
# Идея:
# Держим окно длины k и считаем, сколько в нём гласных (cur).
# Сдвигаем окно на 1: добавляем вклад нового символа справа и убираем вклад символа слева.
# Если нашли окно с большим числом гласных — запоминаем его старт (best_start).
# В конце берём лучшее окно и возвращаем строку, состоящую только из гласных из этого окна.
#
# Сложность:
# Время: O(n) — один проход по строке + финальная фильтрация окна длины k (это O(k), но k <= n, значит O(n)).
# Память: O(1) — множество гласных фиксированного размера (5) и несколько переменных.
# Примечание: если считать возвращаемую строку результатом, то она занимает O(best) памяти, но доп. память алгоритма — O(1).



# # # ### TODO РЕШИТЬ!   + ВЫВОД ПОДСТРОКИ   for i in range(k, len(s)):  window = s[best_start:best_start + k]
# def maxVowels(s: str, k: int) -> str:




# def maxVowelsOnly(s: str, k: int) -> str:
#     vowels = set("aeiou")
#
#     # гласные в первом окне
#     cur = sum(1 for ch in s[:k] if ch in vowels)
#     best = cur
#     best_start = 0
#
#     # двигаем окно
#     for i in range(k, len(s)):
#         if s[i] in vowels:
#             cur += 1
#         if s[i - k] in vowels:
#             cur -= 1
#
#         start = i - k + 1
#         if cur > best:
#             best = cur
#             best_start = start
#             if best == k:  # максимум возможный, дальше не улучшить
#                 break
#
#     window = s[best_start:best_start + k]
#     return "".join(ch for ch in window if ch in vowels)


# print(maxVowelsOnly("abciiidef", 3))  # -> "iii"
# print(maxVowelsOnly("aeiou", 2))      # -> "ae"
# print(maxVowelsOnly("leetcode", 3))   # -> "ee"






# ### TODO 643. Maximum Average Subarray I
# Задача: найти максимальное среднее значение среди всех подмассивов длины k.
# Идея: Sliding Window — считаем сумму первого окна, затем двигаем окно: прибавляем новый элемент и вычитаем ушедший.

# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75   (max sum = 51, 51/4 = 12.75)

# Example 2:
# Input: nums = [5], k = 1
# Output: 5.0


# 1) Лучший вариант для собеседования: Sliding Window
# Паттерн: Sliding Window

# Сложность:
# Время: O(n) — один проход по массиву.
# Память: O(1) — только переменные суммы.


# def findMaxAverage(nums: list[int], k: int) -> float:
#     window_sum = sum(nums[:k])
#     best_sum = window_sum
#
#     for i in range(k, len(nums)):
#         window_sum += nums[i] - nums[i - k]
#         if window_sum > best_sum:
#             best_sum = window_sum
#
#     return best_sum / k
#
#
# print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))  # -> 12.75
# print(findMaxAverage([5], 1))                      # -> 5.0


# # # ### TODO РЕШИТЬ!    for i in range(k, len(nums))    window_sum += nums[i] - nums[i - k]
# def findMaxAverage(nums: list[int], k: int) -> float:




# ### TODO Two Pointers


# ### TODO 1679. Max Number of K-Sum Pairs
# Идея: нужно максимальное число непересекающихся пар с суммой k.
# Задача: за одну операцию выбрать два числа из nums, сумма которых равна k, и удалить их.
# Нужно вернуть максимальное количество таких операций (пары не должны пересекаться).
# Идея: HashMap (частоты) — идём по nums и для каждого x ищем "пару" need = k - x.
# Если need уже есть в словаре (ждёт пару) — делаем операцию и уменьшаем счётчик.
# Иначе “кладём” x в словарь как число, которое ждёт пару.
# Есть 2 классических решения: HashMap (частоты) или сортировка + Two Pointers.

# Example 1:
# Input: nums = [1,2,3,4], k = 5
# Output: 2

# Example 2:
# Input: nums = [3,1,3,4,3], k = 6
# Output: 1


# 1) Лучший вариант для собеседования: HashMap (частоты) за O(n)
# Паттерн: Hash Table

# Сложность:
# Время: O(n) — один проход по массиву.
# Память: O(n) — словарь частот.


# def maxOperations(nums: list[int], k: int) -> int:
#     seen = {}   # сколько раз встречали число, которое "ждёт пару"
#     ops = 0
#
#     for i in nums:
#         need = k - i
#         if seen.get(need, 0) > 0:
#             ops += 1
#             seen[need] -= 1
#         else:
#             seen[i] = seen.get(i, 0) + 1
#
#     return ops
#
#
# print(maxOperations([1, 2, 3, 4], 5))        # -> 2
# print(maxOperations([3, 1, 3, 4, 3], 6))     # -> 1
# print(maxOperations([2, 2, 2, 2], 4))        # -> 2



# # # ### TODO РЕШИТЬ!
# def maxOperations(nums: list[int], k: int) -> int:




# ### TODO 11. Container With Most Water
# Задача: по массиву height найти две линии (i и j), которые дают максимальную площадь воды.
# Площадь = (j - i) * min(height[i], height[j]).
# Идея: Two Pointers — ставим указатели на края (l, r) и считаем площадь.
# Двигаем указатель с меньшей высотой, потому что:
# ширина (r-l) уменьшается всегда, и “выиграть” можно только если увеличить min(height[l], height[r]),
# а это возможно только подняв меньшую сторону (двигая её внутрь).

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49


# 1) Лучший вариант для собеседования: Two Pointers
# Паттерн: Two Pointers

# Сложность:
# Время: O(n) — один проход двумя указателями.
# Память: O(1) — только несколько переменных.


# def maxArea(height: list[int]) -> int:
#     l, r = 0, len(height) - 1
#     best = 0
#
#     while l < r:
#         h = min(height[l], height[r])
#         best = max(best, (r - l) * h)
#
#         if height[l] < height[r]:
#             l += 1
#         else:
#             r -= 1
#
#     return best
#
#
# print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # -> 49
# print(maxArea([1, 1]))                        # -> 1
# print(maxArea([4, 3, 2, 1, 4]))               # -> 16


# # # ### TODO РЕШИТЬ!
# def maxArea(height: list[int]) -> int:




# ### TODO 392. Is Subsequence
# Задача: проверить, является ли строка s подпоследовательностью строки t.
# Подпоследовательность — это когда символы s можно “найти” в t по порядку,
# возможно с пропусками, но не меняя порядок.
# Идея: Two Pointers — идём по t и двигаем указатель по s, когда нашли нужный символ.


# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: True

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: False


# 1) Лучший вариант для собеседования: Two Pointers
# Паттерн: Two Pointers

# Сложность:
# Время: O(n + m) — один проход по t (и по s максимум один раз), где n=len(s), m=len(t).
# Память: O(1) — только индексы.


# def isSubsequence(s: str, t: str) -> bool:
#     i = 0  # указатель по s
#     for ch in t:
#         if i < len(s) and s[i] == ch:
#             i += 1
#     return i == len(s)
#
#
# print(isSubsequence("abc", "ahbgdc"))  # -> True
# print(isSubsequence("axc", "ahbgdc"))  # -> False
# print(isSubsequence("", "ahbgdc"))     # -> True
# print(isSubsequence("abc", ""))        # -> False


# # # ### TODO РЕШИТЬ!
# def isSubsequence(s: str, t: str) -> bool:




# 2) Альтернатива: через итератор (Python-shortcut)
# Идея: проверяем символы s по очереди, “ищем” их в t через итератор.

# Сложность:
# Время: O(n + m)
# Память: O(1)


# def isSubsequence_iter(s: str, t: str) -> bool:
#     it = iter(t)
#     return all(ch in it for ch in s)
#
#
# print(isSubsequence_iter("abc", "ahbgdc"))  # -> True
# print(isSubsequence_iter("axc", "ahbgdc"))  # -> False
# print(isSubsequence_iter("", "ahbgdc"))     # -> True
# print(isSubsequence_iter("abc", ""))        # -> False





# ### TODO 283. Move Zeroes   НУЛИ в КОНЕЦ
# Задача: переместить все нули в конец массива nums, сохранив относительный порядок ненулевых элементов.
# Нужно сделать это in-place (без копии массива).
# Идея: Two Pointers (write/read) — сначала “сдвигаем” все ненулевые в начало, затем оставшуюся часть заполняем нулями.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]


# 1) Лучший вариант для собеседования: Two Pointers (write/read)
# Паттерн: Two Pointers / In-place

# Сложность:
# Время: O(n) — один проход + дозаполнение нулями.
# Память: O(1) — всё делаем на месте.

                                                           ### ВАРИАНТ ЛУЧШЕ!
# def moveZeroes(nums: list[int]) -> None:                 # def moveZeroes(nums: list[int]) -> None:
#     write = 0  # куда писать следующий ненулевой         #     write = 0  # куда писать следующий ненулевой
#                                                          #
#     # 1) переносим все ненулевые вперёд                  #     # 1) переносим все ненулевые вперёд
#     for read in range(len(nums)):                        #     for i in nums:
#         if nums[read] != 0:                              #         if i != 0:
#             nums[write] = nums[read]                     #             nums[write] = nums[i]
#             write += 1                                   #             write += 1
#                                                          #
#     # 2) остальное заполняем нулями                      #     # 2) остальное заполняем нулями
#     for i in range(write, len(nums)):                    #     for i in range(write, len(nums)):
#         nums[i] = 0                                      #         nums[i] = 0
#
#
# a = [0, 1, 0, 3, 12]
# moveZeroes(a)
# print(a)  # -> [1, 3, 12, 0, 0]
#
# b = [0]
# moveZeroes(b)
# print(b)  # -> [0]


# # # ### TODO РЕШИТЬ!  НУЛИ в КОНЕЦ
# def moveZeroes(nums: list[int]) -> None:







# 2) Альтернатива: swap, когда встречаем ненулевой (тоже in-place)    ТЕКУЩЕЕ РЕШЕНИЕ ЛУЧШЕ И ПРОЩЕ
# Паттерн: Two Pointers (swap)

# Сложность:
# Время: O(n)
# Память: O(1)


# def moveZeroes_swap(nums: list[int]) -> None:                     # def moveZeroes_swap(nums: list[int]) -> None:
#     write = 0                                                     #     write = 0
#     for read in range(len(nums)):                                 #     for i, v in enumerate(nums):
#         if nums[read] != 0:                                       #         if v != 0:
#             nums[write], nums[read] = nums[read], nums[write]     #             nums[write], nums[i] = nums[i], nums[write]
#             write += 1                                            #             write += 1
#
#
# c = [0, 1, 0, 3, 12]
# moveZeroes_swap(c)
# print(c)  # -> [1, 3, 12, 0, 0]



### TODO БОНУС
# # # ### TODO РЕШИТЬ!  НУЛИ в НАЧАЛО   2 ВАРИАНТА НАПИСАТЬ
# def move_zeros_to_start(nums: list[int]) -> None:





# ВАРИАНТ 1) In-place двумя указателями (swap), проход справа налево
# Идея: "write" указывает на позицию, куда нужно поставить следующий ненулевой элемент (с конца).
# Проходим список с конца (i). Если lst[i] != 0 — меняем местами lst[i] и lst[write] (если это разные позиции)
# и сдвигаем write влево. В результате все ненули окажутся справа, а нули — слева.
#
# Время: O(n) — один проход по списку
# Память: O(1) — дополнительные структуры не создаются (работаем в исходном списке)
# Примечание: порядок ненулевых может НЕ сохраняться из-за swap'ов.
# def move_zeros_to_start(nums: list[int]) -> list[int]:
#     write = len(nums) - 1
#     for i in range(len(nums) - 1, -1, -1):
#         if lst[i] != 0:
#             if write != i:
#                 nums[write], nums[i] = nums[i], nums[write]
#             write -= 1
#     return nums


# ВАРИАНТ 2) Через фильтрацию и объединение (создаём новый список)
# Идея: отдельно собираем все нули и все ненули, затем склеиваем: zeros + non_zeros.
# Так проще читать и порядок ненулевых сохраняется (стабильно), но нужна доп. память.
#
# Время: O(n) — два прохода по списку + конкатенация (в сумме линейно)
# Память: O(n) — создаются списки zeros, non_zeros и итоговый список
# def move_zeros_to_start(nums: list[int]) -> list[int]:
#     zeros = [x for x in nums if x == 0]
#     non_zeros = [x for x in nums if x != 0]
#     return zeros + non_zeros




# ### TODO Array / String


# ### TODO 443. String Compression

# Задача: сжать массив символов chars по группам одинаковых подряд идущих символов.
# Для каждой группы:
# - если длина = 1 → пишем только символ
# - если длина > 1 → пишем символ + цифры длины (например 12 → '1','2')
# Нужно изменить chars "на месте" (in-place) и вернуть новую длину.

# Идея: Two Pointers (read/write).
# read идёт по массиву и считает длину группы одинаковых символов,
# write записывает сжатый результат прямо в chars.

# Example 1:
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: 6, chars[:6] = ["a","2","b","2","c","3"]

# Example 2:
# Input: chars = ["a"]
# Output: 1, chars[:1] = ["a"]

# Example 3:
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: 4, chars[:4] = ["a","b","1","2"]


# 1) Лучший вариант для собеседования: in-place (read/write)
# Паттерн: Two Pointers (write/read)

# Сложность:
# Время: O(n) — один проход по массиву.
# Память: O(1) — доп. память константная (пишем прямо в chars).


# def compress(chars: list[str]) -> int:
#     n = len(chars)
#     write = 0
#     read = 0
#
#     while read < n:
#         ch = chars[read]
#         start = read
#
#         # считаем длину группы
#         while read < n and chars[read] == ch:
#             read += 1
#         count = read - start
#
#         # пишем символ
#         chars[write] = ch
#         write += 1
#
#         # пишем количество (если > 1) как отдельные цифры
#         if count > 1:
#             for digit in str(count):
#                 chars[write] = digit
#                 write += 1
#
#     return write
#
# a = ["a","a","b","b","c","c","c"]
# k = compress(a)
# print(k, a[:k])  # -> 6 ['a','2','b','2','c','3']
#
# b = ["a"]
# k = compress(b)
# print(k, b[:k])  # -> 1 ['a']
#
# c = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# k = compress(c)
# print(k, c[:k])  # -> 4 ['a','b','1','2']


# # # ### TODO РЕШИТЬ!
# def compress(chars: list[str]) -> int:





# ### TODO 334. Increasing Triplet Subsequence
# Задача: проверить, существует ли тройка индексов i < j < k такая, что
# nums[i] < nums[j] < nums[k]. Если да — True, иначе False.
# Идея: Greedy за один проход.
# Держим:
# first  — минимальное число, которое видели слева
# second — минимальное число, которое > first
# Если встречаем x > second, значит найдено first < second < x (и индексы по порядку).


# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: True

# Example 2:
# Input: nums = [5,4,3,2,1]
# Output: False

# Example 3:
# Input: nums = [2,1,5,0,4,6]
# Output: True


# 1) Лучший вариант для собеседования: greedy за O(1) памяти
# Паттерн: Greedy / One pass

# Сложность:
# Время: O(n) — один проход по массиву.
# Память: O(1) — только две переменные first и second.


# import math
#
# def increasingTriplet(nums: list[int]) -> bool:
#     first = math.inf
#     second = math.inf
#
#     for x in nums:
#         if x <= first:
#             first = x
#         elif x <= second:
#             second = x
#         else:
#             # x > second -> нашли first < second < x
#             return True
#
#     return False
#
#
# print(increasingTriplet([1, 2, 3, 4, 5]))  # -> True
# print(increasingTriplet([5, 4, 3, 2, 1]))  # -> False
# print(increasingTriplet([2, 1, 5, 0, 4, 6]))  # -> True


# # # ### TODO РЕШИТЬ!
# def increasingTriplet(nums: list[int]) -> bool:




# ### TODO 238. Product of Array Except Self
# Задача: вернуть массив answer, где answer[i] = произведение всех nums[j], j != i.
# Деление использовать нельзя.
# Идея: Prefix/Suffix products — сначала записываем произведение всех элементов слева от i,
# затем вторым проходом домножаем на произведение всех элементов справа от i.


# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


# 1) Лучший вариант для собеседования: Prefix + Suffix (без division)
# Паттерн: Prefix/Suffix products

# Сложность:
# Время: O(n) — два прохода по массиву.
# Память: O(1) доп. память (не считая массива ответа) — используем только prefix и suffix (2 переменные).
# Но если считать всё, включая res, тогда память O(n).


# def productExceptSelf(nums: list[int]) -> list[int]:
#     n = len(nums)
#     res = [1] * n
#
#     # res[i] = произведение всех элементов слева от i
#     prefix = 1
#     for i in range(n):
#         res[i] = prefix
#         prefix *= nums[i]
#
#     # домножаем на произведение всех элементов справа от i
#     suffix = 1
#     for i in range(n - 1, -1, -1):
#         res[i] *= suffix
#         suffix *= nums[i]
#
#     return res
#
#
# print(productExceptSelf([1, 2, 3, 4]))         # -> [24, 12, 8, 6]
# print(productExceptSelf([-1, 1, 0, -3, 3]))    # -> [0, 0, 9, 0, 0]


# # # ### TODO РЕШИТЬ!
# def productExceptSelf(nums: list[int]) -> list[int]:




# ### TODO 151. Reverse Words in a String
# Задача: развернуть порядок слов в строке s.
# Вход может содержать ведущие/хвостовые пробелы и несколько пробелов между словами.
# В ответе слова должны быть разделены ровно одним пробелом, без лишних пробелов по краям.
# Идея: убрать лишние пробелы, разбить на слова и собрать в обратном порядке.
# split() сам убирает лишние пробелы и даёт список слов → разворачиваем → join().

# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"

# Example 3:
# Input: s = "a good   example"
# Output: "example good a"


# 1) Лучший вариант для собеседования (Python): split + reverse + join
# Паттерн: String

# Сложность:
# Время: O(n) — split проходит строку, затем join собирает результат.
# Память: O(n) — список слов + итоговая строка.


# def reverseWords(s: str) -> str:
#     return " ".join(s.split()[::-1])
#
#
# print(reverseWords("the sky is blue"))     # -> "blue is sky the"
# print(reverseWords("  hello world  "))     # -> "world hello"
# print(reverseWords("a good   example"))    # -> "example good a"


# # # ### TODO РЕШИТЬ!
# def reverseWords(s: str) -> str:





# 2) Альтернатива без split (ручной разбор)
# Идея: идём справа налево, вырезаем слова и добавляем в ответ.

# Сложность:
# Время: O(n) — один проход по строке.
# Память: O(n) — храним слова/результат.


# def reverseWords_manual(s: str) -> str:
#     res = []
#     i = len(s) - 1
#
#     while i >= 0:
#         # пропускаем пробелы
#         while i >= 0 and s[i] == " ":
#             i -= 1
#         if i < 0:
#             break
#
#         # нашли конец слова, идём к его началу
#         j = i
#         while j >= 0 and s[j] != " ":
#             j -= 1
#
#         res.append(s[j + 1:i + 1])
#         i = j - 1
#
#     return " ".join(res)
#
#
# print(reverseWords_manual("the sky is blue"))  # -> "blue is sky the"
# print(reverseWords_manual("  hello world  "))  # -> "world hello"
# print(reverseWords_manual("a good   example")) # -> "example good a"




# ### TODO 345. Reverse Vowels of a String
# Задача: развернуть (поменять местами) только гласные буквы в строке s.
# Все остальные символы должны остаться на своих местах.
# Гласные: a, e, i, o, u (и в верхнем регистре тоже).
# Идея: Two Pointers — ищем гласные слева и справа и меняем их местами.


# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"


# 1) Лучший вариант для собеседования: Two Pointers
# Паттерн: Two Pointers

# Сложность:
# Время: O(n)  — каждый указатель проходит строку максимум один раз.
# Память: O(n) — строка неизменяемая, поэтому делаем список символов для swap.


# def reverseVowels(s: str) -> str:
#     vowels = set("aeiouAEIOU")
#     arr = list(s)
#
#     l, r = 0, len(arr) - 1
#     while l < r:
#         while l < r and arr[l] not in vowels:
#             l += 1
#         while l < r and arr[r] not in vowels:
#             r -= 1
#
#         if l < r:
#             arr[l], arr[r] = arr[r], arr[l]
#             l += 1
#             r -= 1
#
#     return "".join(arr)
#
#
# print(reverseVowels("IceCreAm"))  # -> "AceCreIm"
# print(reverseVowels("leetcode"))  # -> "leotcede"
# print(reverseVowels("aA"))        # -> "Aa"
# print(reverseVowels("bcd"))       # -> "bcd"


# # # ### TODO РЕШИТЬ!
# def reverseVowels(s: str) -> str:






# ### TODO 605. Can Place Flowers
# Задача: можно ли посадить n новых цветов в flowerbed так, чтобы не было двух цветов рядом (adjacent).
# flowerbed[i] = 1 — уже есть цветок, 0 — место пустое.
# Идея: Greedy — идём слева направо и сажаем цветок там, где:
# flowerbed[i] == 0 и (слева пусто или граница) и (справа пусто или граница).
# Если посадили — уменьшаем n. Если n стало 0 — сразу True.


# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True

# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False


# 1) Лучший вариант для собеседования: жадно сажаем по месту (Greedy)
# Паттерн: Greedy / Array (один проход)

# Сложность:
# Время: O(L)  — один проход по массиву (L = len(flowerbed)).
# Память: O(1) — кроме входного массива ничего не храним.


# def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
#     if n == 0:
#         return True
#
#     L = len(flowerbed)
#     for i in range(L):
#         if flowerbed[i] == 0:
#             left_empty = (i == 0) or (flowerbed[i - 1] == 0)
#             right_empty = (i == L - 1) or (flowerbed[i + 1] == 0)
#
#             if left_empty and right_empty:
#                 flowerbed[i] = 1
#                 n -= 1
#                 if n == 0:
#                     return True
#
#     return False
#
#
# print(canPlaceFlowers([1, 0, 0, 0, 1], 1))  # -> True
# print(canPlaceFlowers([1, 0, 0, 0, 1], 2))  # -> False
# print(canPlaceFlowers([0, 0, 0, 0, 0], 3))  # -> True
# print(canPlaceFlowers([0], 1))              # -> True
# print(canPlaceFlowers([1], 1))              # -> False


# # # ### TODO РЕШИТЬ!
# def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:





# ### TODO 1431. Kids With the Greatest Number of Candies
# Задача: для каждого ребёнка проверить, станет ли он(а) одним из “самых богатых” по конфетам,
# если дать ему(ей) все extraCandies.
# Вернуть список bool: True, если candies[i] + extraCandies >= max(candies), иначе False.
# Идея: сначала находим максимум mx, потом одним проходом строим ответ.


# Example 1:
# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [True, True, True, False, True]

# Example 2:
# Input: candies = [4,2,1,1,2], extraCandies = 1
# Output: [True, False, False, False, False]

# Example 3:
# Input: candies = [12,1,12], extraCandies = 10
# Output: [True, False, True]


# 1) Лучший вариант для собеседования: один проход за максимумом + один проход за ответом
# Паттерн: Array (просто проход по массиву)

# Сложность:
# Время: O(n)  — находим максимум и строим ответ.
# Память: O(n) — массив результата (его всё равно нужно вернуть).


# def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
#     mx = max(candies)
#     return [c + extraCandies >= mx for c in candies]
#
#
# print(kidsWithCandies([2, 3, 5, 1, 3], 3))   # -> [True, True, True, False, True]
# print(kidsWithCandies([4, 2, 1, 1, 2], 1))   # -> [True, False, False, False, False]
# print(kidsWithCandies([12, 1, 12], 10))      # -> [True, False, True]



# # # ### TODO РЕШИТЬ!
# def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:




# 2) Альтернатива (то же самое, но “вручную” без list comprehension)
# Сложность:
# Время: O(n)
# Память: O(n)


# def kidsWithCandies_loop(candies: List[int], extraCandies: int) -> List[bool]:
#     mx = max(candies)
#     res = []
#     for c in candies:
#         res.append(c + extraCandies >= mx)
#     return res
#
#
# print(kidsWithCandies_loop([2, 3, 5, 1, 3], 3))   # -> [True, True, True, False, True]
# print(kidsWithCandies_loop([4, 2, 1, 1, 2], 1))   # -> [True, False, False, False, False]
# print(kidsWithCandies_loop([12, 1, 12], 10))      # -> [True, False, True]




# ### TODO 1071. Greatest Common Divisor of Strings
# Задача: найти самую большую строку x, которая “делит” обе строки:
# str1 = x + x + ... + x   и   str2 = x + x + ... + x.
# Вернуть эту строку x, если она существует, иначе вернуть "".
# Идея: если общий делитель существует, то должно выполняться:
# str1 + str2 == str2 + str1 (иначе шаблоны несовместимы).
# Тогда ответ — это префикс длины gcd(len(str1), len(str2)).
# Важный трюк: если str1 + str2 != str2 + str1, общего делителя не существует

# Example 1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Example 2:
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Example 3:
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""

# Example 4:
# Input: str1 = "AAAAAB", str2 = "AAA"
# Output: ""


# 1) Лучшее решение для собеседования: проверка (str1+str2 == str2+str1) + gcd длин
# Паттерн: Math / String (gcd)


# Сложность:
# Время: O(n + m) — конкатенация и сравнение строк + один проход при взятии префикса.
# Память: O(n + m) — временно создаются строки str1+str2 и str2+str1.


# from math import gcd
#
# def gcdOfStrings(str1: str, str2: str) -> str:
#     if str1 + str2 != str2 + str1:
#         return ""
#     g = gcd(len(str1), len(str2))
#     return str1[:g]
#
#
# print(gcdOfStrings("ABCABC", "ABC"))   # -> "ABC"
# print(gcdOfStrings("ABABAB", "ABAB"))  # -> "AB"
# print(gcdOfStrings("LEET", "CODE"))    # -> ""
# print(gcdOfStrings("AAAAAB", "AAA"))   # -> ""


# # # ### TODO РЕШИТЬ!
# def gcdOfStrings(str1: str, str2: str) -> str:




# ### TODO 1768. Merge Strings Alternately
# Задача: объединить две строки word1 и word2, чередуя символы: берём 1 символ из word1, потом 1 символ из word2, и так далее.
# Если одна строка закончилась раньше — дописываем оставшуюся часть другой строки в конец.
# Идея: Two Pointers — два индекса i и j по двум строкам, добавляем символы по очереди.
# # O(1) памяти тут обычно нельзя, потому что результат нужно где-то хранить.

# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

# Example 2:
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b
# word2:    p   q   r   s
# merged: a p b q   r   s

# Example 3:
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q
# merged: a p b q c   d



# 1) Два указателя (понятно и по-интервью)
# Это классический паттерн Two Pointers / Two indices (два индекса по двум строкам).

# Сложность:
# Время: O(n + m)  — каждый символ из word1 и word2 добавляется в результат ровно 1 раз.
# Память: O(n + m) — храним результат длины n + m.


# def mergeAlternately(word1: str, word2: str) -> str:
#     i = j = 0
#     res = []
#     while i < len(word1) or j < len(word2):
#         if i < len(word1):
#             res.append(word1[i])
#             i += 1
#         if j < len(word2):
#             res.append(word2[j])
#             j += 1
#     return ''.join(res)
#
#
# print(mergeAlternately('abc', 'pqr')) # -> apbqcr
# print(mergeAlternately('ab', 'pqrs')) # -> apbqrs
# print(mergeAlternately('abcd', 'pq')) # -> apbqcd



# # # ### TODO РЕШИТЬ!
# def mergeAlternately(word1: str, word2: str) -> str:





# 2) Через zip_longest (короче, python-style) - это Python-only shortcut

# Сложность:
# Время: O(n + m)  — проходим по символам обеих строк и формируем результат.
# Память: O(n + m) — храним результат длины n + m.


# from itertools import zip_longest
#
# def mergeAlternately(word1: str, word2: str) -> str:
#     res = []
#     for a, b in zip_longest(word1, word2, fillvalue=''):
#         res.append(a)
#         res.append(b)
#     return ''.join(res)
#
# print(mergeAlternately('abc', 'pqr')) # -> apbqcr
# print(mergeAlternately('ab', 'pqrs')) # -> apbqrs
# print(mergeAlternately('abcd', 'pq')) # -> apbqcd






























