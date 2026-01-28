from pympler import asizeof
from typing import List, Optional
import re, sys
from collections import deque, Counter, defaultdict, OrderedDict, ChainMap
from dataclasses import dataclass







### TODO Top Interview 150


# ### TODO БОНУС ЗАДАЧИ



# ### TODO 8. String to Integer (atoi)
# Задача: реализовать myAtoi(s) — преобразовать строку в 32-битное целое.
#
# Алгоритм:
# 1) Whitespace: пропустить ведущие пробелы.
# 2) Signedness: считать знак '+' или '-', если есть.
# 3) Conversion: считать цифры до первого не-цифрового символа.
#    Если цифр нет — вернуть 0.
# 4) Rounding: ограничить результат диапазоном [-2^31, 2^31-1].
#
# Example 1: "42" -> 42
# Example 2: " -042" -> -42
# Example 3: "1337c0d3" -> 1337
# Example 4: "0-1" -> 0
# Example 5: "words and 987" -> 0
#
# Паттерн: парсинг строки + защита от переполнения
#
# Сложность:
# Время: O(n)
# Память: O(1)

# class Solution:
#     def myAtoi(self, s: str) -> int:
#         i = 0
#         n = len(s)
#
#         # 1) пропускаем ведущие пробелы
#         while i < n and s[i] == " ":
#             i += 1
#
#         # 2) знак
#         sign = 1
#         if i < n and s[i] in "+-":
#             if s[i] == "-":
#                 sign = -1
#             i += 1
#
#         # 3) читаем цифры + 4) clamp к 32-bit
#         INT_MIN = -2**31
#         INT_MAX = 2**31 - 1
#         res = 0
#
#         while i < n and "0" <= s[i] <= "9":
#             digit = ord(s[i]) - ord("0")
#
#             # проверка переполнения ДО умножения на 10
#             if res > (INT_MAX - digit) // 10:
#                 return INT_MAX if sign == 1 else INT_MIN
#
#             res = res * 10 + digit
#             i += 1
#
#         return sign * res


# # # ### TODO РЕШИТЬ!   i=0    sign=1   res=0   while  if  while
# def myAtoi(self, s: str) -> int:







# ### TODO 5. Longest Palindromic Substring
# Задача: дана строка s. Нужно вернуть самую длинную палиндромную ПОДСТРОКУ
# (непрерывный фрагмент исходной строки).
#
# Example 1:
# s = "babad" -> "bab" (или "aba")
#
# Example 2:
# s = "cbbd" -> "bb"
#
# Паттерн: Expand Around Center
#
# ============================================================
# 1) Вариант "лучший для собеседования": расширение от центра
#
# Идея:
# Палиндром расширяется от центра.
# Центр бывает:
#  - i,i   (нечётная длина)
#  - i,i+1 (чётная длина)
# Для каждого центра расширяемся влево/вправо и обновляем лучший ответ.
#
# Сложность:
# Время: O(n^2)
# Память: O(1)

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if not s:
#             return ""
#
#         best_l = best_r = 0
#
#         def expand(l: int, r: int) -> None:
#             nonlocal best_l, best_r
#
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 l -= 1
#                 r += 1
#
#             # откат на последнюю валидную пару
#             l += 1
#             r -= 1
#
#             if (r - l + 1) > (best_r - best_l + 1):
#                 best_l, best_r = l, r
#
#         for i in range(len(s)):
#             expand(i, i)       # нечётный центр
#             expand(i, i + 1)   # чётный центр
#
#         return s[best_l:best_r + 1]


# # # ### TODO РЕШИТЬ!               l -= 1  r += 1      if (r - l + 1) > (best_r - best_l + 1):
# def longestPalindrome(self, s: str) -> str:




# ### TODO 409. Longest Palindrome
# Задача: дана строка s из букв (a-z, A-Z). Нужно вернуть длину
# самого длинного палиндрома, который можно собрать из этих букв.
#
# Важно: регистр важен ("Aa" не палиндром).
#
# Example 1:
# s = "abccccdd" -> 7 (например "dccaccd")
#
# Example 2:
# s = "a" -> 1
#
# Паттерн: подсчёт частот (hashmap / Counter)
#
# ============================================================
# 1) Вариант "лучший для собеседования": считаем пары + один центр
#
# Идея:
# - Любую букву с частотой k можно положить по краям палиндрома парами:
#   в длину добавится 2 * (k // 2).
# - Если хотя бы у одной буквы осталась "лишняя" (k нечётное),
#   то можно добавить ровно 1 символ в центр.
#
# Пример:
# c:4 -> берём 4
# d:2 -> берём 2
# a:1,b:1 -> пары 0, но можно взять 1 в центр
#
# Сложность:
# Время: O(n)
# Память: O(кол-во уникальных символов) (макс ~52)

# from collections import Counter
#
# class Solution:
#     def longestPalindrome(self, s: str) -> int:
#         cnt = Counter(s)
#
#         length = 0
#         has_odd = False
#
#         for i in cnt.values():
#             length += (i // 2) * 2   # берём все возможные пары
#             if i % 2 == 1:
#                 has_odd = True         # есть кандидат на центр
#
#         if has_odd:
#             length += 1                # один символ в центр
#
#         return length



# # # ### TODO РЕШИТЬ!   ВЫВОД ДЛИНЫ
# def longestPalindrome(self, s: str) -> int:







# ============================================================
# 1) Вариант "выводим сам палиндром": строим левую половину + центр + зеркалим
#
# Идея:
# - Считаем частоты символов.
# - Для каждой буквы с частотой k берём пары: pairs = k // 2
#   и добавляем (буква * pairs) в левую половину палиндрома.
# - Если осталась хотя бы одна "лишняя" буква (после изъятия пар),
#   её можно положить в центр (ровно 1 символ).
# - Правая половина получается как reverse(левая).
#
# Детерминированность:
# - Идём по символам в sorted порядке, чтобы результат всегда был одинаковым.
# - Центр выбираем также детерминированно: первый (минимальный) оставшийся символ.
#
# Пример:
# s = "abccccdd"
# cnt: a:1, b:1, c:4, d:2
# left: c(2) + d(1) -> "ccd"
# center: "a" (минимальный среди оставшихся нечётных)
# palindrome: "ccd" + "a" + "dcc" -> "ccdadcc"
#
# Сложность:
# Время: O(n + m log m), где m — число уникальных символов
# Память: O(n) (потому что возвращаем строку палиндрома)

# from collections import Counter
#
# class Solution:
#     def buildLongestPalindrome(self, s: str) -> str:
#         cnt = Counter(s)
#
#         left_parts = []
#         center = ""
#
#         # 1) собираем левую половину из пар
#         for ch in sorted(cnt.keys()):
#             pairs = cnt[ch] // 2
#             if pairs:
#                 left_parts.append(ch * pairs)
#                 cnt[ch] -= 2 * pairs
#
#         # 2) выбираем центр (если остался нечётный символ)
#         for ch in sorted(cnt.keys()):
#             if cnt[ch] > 0:
#                 center = ch
#                 break
#
#         left = "".join(left_parts)
#         return left + center + left[::-1]



# # # ### TODO РЕШИТЬ!   ВЫВОД СТРОКИ
# def longestPalindrome(self, s: str) -> int:






### TODO ЗАДАЧИ О РЮКЗАКЕ

# ### TODO 416. Partition Equal Subset Sum
# Задача: дана целочисленная строка nums.
# Нужно вернуть True, если можно разбить nums на 2 подмножества
# с одинаковой суммой.
#
# Example 1:
# nums = [1,5,11,5] -> True (можно [1,5,5] и [11])
#
# Example 2:
# nums = [1,2,3,5] -> False
#
# Паттерн: 0/1 Knapsack (Subset Sum)
#
# ============================================================
# ВАРИАНТ 1: DP (1D boolean массив) — самый “классический”
#
# Идея:
# target = sum(nums)//2
# dp[t] = можно ли набрать сумму t
# Обновляем dp справа налево, чтобы число использовалось только 1 раз.
#
# Сложность:
# Время: O(n * target)
# Память: O(target)

# from typing import List
#
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         total = sum(nums)
#         if total % 2 == 1:
#             return False
#
#         target = total // 2
#         dp = [False] * (target + 1)
#         dp[0] = True
#
#         for i in nums:
#             for j in range(target, i - 1, -1):
#                 dp[j] = dp[j] or dp[j - i]
#
#         return dp[target]



# # # # ### TODO РЕШИТЬ!
# def canPartition(self, nums: List[int]) -> bool:




# ============================================================
# ВАРИАНТ 2: Через set достижимых сумм (часто проще объяснять)
#
# Идея:
# Храним множество sums — суммы, которые можем набрать.
# Для каждого x обновляем: new_sums = sums ∪ {s + x for s in sums}
# Если target появился — можно сразу вернуть True.
#
# Сложность:
# Время: O(n * target) (в худшем)
# Память: O(target)

# class Solution2:
#     def canPartition(self, nums: List[int]) -> bool:
#         total = sum(nums)
#         if total % 2 == 1:
#             return False
#
#         target = total // 2
#         sums = {0}
#
#         for x in nums:
#             new_sums = set(sums)
#             for s in sums:
#                 ns = s + x
#                 if ns == target:
#                     return True
#                 if ns < target:
#                     new_sums.add(ns)
#             sums = new_sums
#
#         return target in sums





# ### TODO Binary Tree General


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


# # # ### TODO РЕШИТЬ!
# def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':







# ### TODO 112. Path Sum
# Задача: дан корень бинарного дерева root и число targetSum.
# Нужно вернуть True, если существует путь root -> leaf (до листа),
# такой что сумма значений на пути равна targetSum.
#
# Лист = узел без детей (left == None и right == None).
#
# Example 1:
# root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22 -> True
#
# Example 2:
# root = [1,2,3], targetSum = 5 -> False
#
# Example 3:
# root = [], targetSum = 0 -> False
#
# Паттерн: DFS (рекурсия/стек)
#
# ============================================================
# 1) Вариант "лучший для собеседования": рекурсивный DFS (O(n) время, O(h) память)
#
# Идея:
# Идём вниз по дереву, уменьшая targetSum на значение текущего узла.
# Когда дошли до листа, проверяем: targetSum == val (или остаток == 0).
#
# Сложность:
# Время: O(n)
# Память: O(h) (глубина рекурсии)

# from typing import Optional
#
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False
#
#         # если лист — проверяем сумму
#         if not root.left and not root.right:
#             return root.val == targetSum
#
#         targetSum -= root.val
#         return (self.hasPathSum(root.left, targetSum) or
#                 self.hasPathSum(root.right, targetSum))



# # # ### TODO РЕШИТЬ!
# def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:



# ============================================================
# 2) Вариант "итеративный": стек (node, remaining_sum) (O(n) время, O(n) память)
#
# Идея:
# Кладём в стек пару (root, targetSum).
# Достаём:
# - если лист и remaining == node.val -> True
# - иначе кладём детей с updated remaining
#
# Сложность:
# Время: O(n)
# Память: O(n) (в худшем случае стек хранит много узлов)

# from typing import Optional, Tuple, List
#
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False
#
#         stack = [(root, root.val)]  # (node, sum_to_node)
#         while stack:
#             node, s = stack.pop()
#
#             if not node.left and not node.right and s == targetSum:
#                 return True
#
#             if node.right:
#                 stack.append((node.right, s + node.right.val))
#             if node.left:
#                 stack.append((node.left, s + node.left.val))
#
#         return False



# ### TODO 101. Symmetric Tree              p.left, q.right     p.right, q.left
# Задача: дан корень бинарного дерева root.
# Нужно проверить, является ли дерево симметричным относительно центра (зеркальным).
#
# Дерево симметрично, если левое и правое поддерево — зеркальные копии:
# - значения в соответствующих узлах равны
# - структура зеркально совпадает:
#   left.left  сравниваем с right.right
#   left.right сравниваем с right.left
#
# Example 1:
# root = [1,2,2,3,4,4,3] -> True
#
# Example 2:
# root = [1,2,2,null,3,null,3] -> False
#
# Паттерн: DFS / BFS (парная проверка зеркала)
#
# ============================================================
# 1) Вариант "лучший для собеседования": рекурсивная проверка mirror (O(n) время, O(h) память)
#
# Идея:
# Функция isMirror(a, b):
# - если оба None -> True
# - если один None -> False
# - если a.val != b.val -> False
# - иначе проверяем:
#   isMirror(a.left, b.right) и isMirror(a.right, b.left)
#
## Сложность: где n — число узлов, h — высота дерева (в худшем O(n), в сбалансированном O(log n)).
# Время: O(n)
# Память: O(h) (глубина рекурсии)

# from typing import Optional
#
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         def mirror(p, q):
#             if not p and not q:
#                 return True
#             if not p or not q:
#                 return False
#             if p.val != q.val:
#                 return False
#             return mirror(p.left, q.right) and mirror(p.right, q.left)
#
#         return mirror(root.left, root.right) if root else True


# # # ### TODO РЕШИТЬ!   def mirror(p, q)   return mirror(p.left, q.right) and mirror(p.right, q.left)
# def isSymmetric(self, root: Optional[TreeNode]) -> bool:




# ============================================================
# 2) Вариант "итеративный": очередь пар (O(n) время, O(n) память)
#
# Идея:
# Кладём в очередь пары узлов, которые должны быть зеркальными.
# Достаём:
# - если оба None -> continue
# - если один None или значения разные -> False
# - иначе добавляем пары детей:
#   (a.left, b.right) и (a.right, b.left)
#
## Сложность: где n — число узлов, w — максимальная ширина дерева (в худшем O(n)).
# Время: O(n)
# Память: O(n)

# from typing import Optional
# from collections import deque
#
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True
#
#         q = deque([(root.left, root.right)])
#
#         while q:
#             a, b = q.popleft()
#
#             if not a and not b:
#                 continue
#             if not a or not b:
#                 return False
#             if a.val != b.val:
#                 return False
#
#             q.append((a.left, b.right))
#             q.append((a.right, b.left))
#
#         return True



# ### TODO 226. Invert Binary Tree
# Задача: дан корень бинарного дерева root.
# Нужно инвертировать дерево (поменять местами left и right у каждого узла) и вернуть root.
#
# Example 1:
# root = [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]
#
# Example 2:
# root = [2,1,3] -> [2,3,1]
#
# Example 3:
# root = [] -> []
#
## Definition for a binary tree node.
## class TreeNode:
##     def __init__(self, val=0, left=None, right=None):
##         self.val = val
##         self.left = left
##         self.right = right
#
#
# Паттерн: DFS / BFS
#
# ============================================================
# 1) Вариант "лучший для собеседования": рекурсивный DFS (O(n) время, O(h) память)
#
# Идея:
# Для каждого узла:
# - меняем местами left и right
# - рекурсивно инвертируем поддеревья
#
# Сложность:
# Время: O(n)
# Память: O(h) (глубина рекурсии)

# from typing import Optional
#
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if not root:
#             return None
#
#         root.left, root.right = root.right, root.left
#         self.invertTree(root.left)
#         self.invertTree(root.right)
#         return root


# # # ### TODO РЕШИТЬ!
# def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:




# ============================================================
# 2) Вариант "итеративный": BFS (O(n) время, O(w) память)
#
# Идея:
# Идём по дереву очередью:
# - для каждого узла меняем left/right
# - добавляем детей в очередь
#
# Сложность:
# Время: O(n)
# Память: O(w), где w — максимальная ширина дерева

# from typing import Optional
# from collections import deque
#
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if not root:
#             return None
#
#         q = deque([root])
#         while q:
#             node = q.popleft()
#             node.left, node.right = node.right, node.left
#
#             if node.left:
#                 q.append(node.left)
#             if node.right:
#                 q.append(node.right)
#
#         return root




# ### TODO 100. Same Tree                               p.left, q.left     p.right, q.right
# Задача: даны корни двух бинарных деревьев p и q.
# Нужно проверить, одинаковые ли они.
# Два дерева одинаковые, если:
# - структура полностью совпадает
# - значения во всех соответствующих узлах равны
#
# Example 1:
# p = [1,2,3], q = [1,2,3] -> True
#
# Example 2:
# p = [1,2], q = [1,null,2] -> False
#
# Example 3:
# p = [1,2,1], q = [1,1,2] -> False
#
#
## Definition for a binary tree node.
## class TreeNode:
##     def __init__(self, val=0, left=None, right=None):
##         self.val = val
##         self.left = left
##         self.right = right
#
#
# Паттерн: DFS / BFS (сравнение двух деревьев)
#
# ============================================================
# 1) Вариант "лучший для собеседования": рекурсивный DFS (O(n) время, O(h) память)
#
# Идея:
# - если оба узла None -> одинаковы
# - если один None, другой нет -> разные
# - если значения разные -> разные
# - иначе рекурсивно сравниваем левое и правое поддеревья
#
# Сложность:
# Время: O(n) (сравниваем каждый узел максимум 1 раз)
# Память: O(h) (глубина рекурсии)

# from typing import Optional
#
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if not p and not q:
#             return True
#         if not p or not q:
#             return False
#         if p.val != q.val:
#             return False
#         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# # # ### TODO РЕШИТЬ!       p.left, q.left     p.right, q.right
# def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


# ============================================================
# 2) Вариант "итеративный": BFS/stack парами узлов (O(n) время, O(n) память)
#
# Идея:
# Кладём в стек пары (p_node, q_node).
# Достаём:
# - если оба None -> продолжаем
# - если один None -> False
# - если значения разные -> False
# - иначе кладём пары детей (left,left) и (right,right)
#
# Сложность:
# Время: O(n)
# Память: O(n) (в худшем случае стек/очередь хранит много пар)

# from typing import Optional
# from collections import deque
#
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         dq = deque([(p, q)])
#
#         while dq:
#             a, b = dq.popleft()
#
#             if not a and not b:
#                 continue
#             if not a or not b:
#                 return False
#             if a.val != b.val:
#                 return False
#
#             dq.append((a.left, b.left))
#             dq.append((a.right, b.right))
#
#         return True



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





# ### TODO 104. Maximum Depth of Binary Tree     1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
# Задача: дан корень бинарного дерева root.
# Нужно вернуть максимальную глубину дерева.
# Глубина = количество узлов на самом длинном пути от root до самого дальнего листа.
#
# Example 1:
# root = [3,9,20,null,null,15,7] -> 3
#
# Example 2:
# root = [1,null,2] -> 2
#
# # --- Definition for a binary tree node ---
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
#
# Паттерн: DFS / BFS
#
# ============================================================
# 1) Вариант "лучший для собеседования": рекурсивный DFS (O(n) время, O(h) память)
# DFS = Depth-First Search — поиск в глубину.
#
# Идея:
# maxDepth(node) = 1 + max(maxDepth(node.left), maxDepth(node.right))
# База: если node == None -> 0
#
# Сложность:
# Время: O(n) (посещаем каждый узел один раз)
# Память: O(h) — стек рекурсии, где h — высота дерева (в худшем O(n), в сбалансированном O(log n)).

# from typing import Optional
#
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# # # ### TODO РЕШИТЬ!              1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
# def maxDepth(self, root: Optional[TreeNode]) -> int:




# ============================================================
# 2) Вариант "итеративный": BFS по уровням (O(n) время, O(w) память)
# BFS = Breadth-First Search — поиск в ширину (по уровням).
#
# Идея:
# Идём по дереву уровнями (очередь).
# Каждый пройденный уровень увеличивает depth на 1.
#
# Сложность:
# Время: O(n)
# Память: O(w) — очередь, где w — максимальная ширина дерева (в худшем O(n)).

# from typing import Optional
# from collections import deque
#
# class Solution:
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



### TODO РЕШИТЬ!  БОНУС     DFS -> root.right  root.left      BFS ->  q = deque([(root, 1)])   [ (root, 1) ]
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




# ### TODO Stack


# ### TODO 150. Evaluate Reverse Polish Notation
# Задача: дан массив строк tokens — арифметическое выражение в обратной польской нотации (RPN).
# Нужно вычислить значение выражения и вернуть int.
#
# Важно:
# - Операторы: '+', '-', '*', '/'
# - Деление двух int всегда "truncate toward zero" (усечение к нулю), например:
#   -3 / 2 -> -1,  3 / -2 -> -1
# - Деления на ноль не будет
# - Выражение корректное
#
# Example 1:
# ["2","1","+","3","*"] -> 9   ( (2 + 1) * 3 )
#
# Example 2:
# ["4","13","5","/","+"] -> 6  ( 4 + (13 / 5) = 4 + 2 )
#
# Example 3:
# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] -> 22
#
# Паттерн: Stack
#


# ============================================================
# 2) Вариант "чуть компактнее": словарь операций (O(n) время, O(n) память)
#
# Идея:
# Храним операции в dict, для '/' отдельно делаем truncate toward zero через int(a / b)
#
# Сложность:
# Время: O(n)
# Память: O(n)

# from typing import List, Callable
#
# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         ops = {
#             "+": lambda a, b: a + b,
#             "-": lambda a, b: a - b,
#             "*": lambda a, b: a * b,
#             "/": lambda a, b: int(a / b),  # truncate toward zero
#         }
#
#         stack: List[int] = []
#         for t in tokens:
#             if t in ops:
#                 b = stack.pop()
#                 a = stack.pop()
#                 stack.append(ops[t](a, b))
#             else:
#                 stack.append(int(t))
#
#         return stack[-1]


# # # ### TODO РЕШИТЬ!
# def evalRPN(self, tokens: List[str]) -> int:




# ============================================================
# 1) Вариант "лучший для собеседования": стек операндов (O(n) время, O(n) память)
#
# Идея:
# Проходим по tokens:
# - если число -> кладём в стек
# - если оператор -> снимаем два числа (b = pop, a = pop), считаем a (op) b,
#   результат кладём обратно
#
# Важно про деление:
# В Python оператор '//' делает floor-деление (округление вниз), это НЕ то, что нужно для отрицательных.
# Нам нужно усечение к нулю, поэтому используем: int(a / b)
#
# Сложность:
# Время: O(n)
# Память: O(n)

# from typing import List
#
# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stack: List[int] = []
#
#         for t in tokens:
#             if t not in {"+", "-", "*", "/"}:
#                 stack.append(int(t))
#                 continue
#
#             b = stack.pop()
#             a = stack.pop()
#
#             if t == "+":
#                 stack.append(a + b)
#             elif t == "-":
#                 stack.append(a - b)
#             elif t == "*":
#                 stack.append(a * b)
#             else:  # "/"
#                 stack.append(int(a / b))  # truncate toward zero
#
#         return stack[-1]









# ### TODO 155. Min Stack
# Задача: реализовать стек, который поддерживает операции:
# - push(val)
# - pop()
# - top()
# - getMin()
# Все операции должны работать за O(1).
#
# Example:
# push(-2), push(0), push(-3)
# getMin() -> -3
# pop()
# top() -> 0
# getMin() -> -2
#
# Паттерн: Stack + дополнительная структура для минимума
#
# ============================================================
# 1) Вариант "лучший для собеседования": два стека (O(1) на все операции)
#
# Идея:
# - stack хранит обычные значения
# - min_stack хранит минимум на каждом уровне
#   min_stack[-1] = min(всех элементов stack)
#
# push(x):
#   stack.push(x)
#   min_stack.push(min(x, min_stack[-1])) или x, если min_stack пуст
#
# pop():
#   stack.pop()
#   min_stack.pop()
#
# top(): stack[-1]
# getMin(): min_stack[-1]
#
# Сложность:
# Время: O(1) на операцию
# Память: O(n)

# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.min_stack = []
#
#     def push(self, val: int) -> None:
#         self.stack.append(val)
#         if not self.min_stack:
#             self.min_stack.append(val)
#         else:
#             self.min_stack.append(min(val, self.min_stack[-1]))
#
#     def pop(self) -> None:
#         self.stack.pop()
#         self.min_stack.pop()
#
#     def top(self) -> int:
#         return self.stack[-1]
#
#     def getMin(self) -> int:
#         return self.min_stack[-1]


# ============================================================
# 2) Вариант "компактный": один стек пар (val, current_min) (O(1) на все операции)
#
# Идея:
# В одном стеке храним кортежи:
# (значение, минимум на момент добавления)
#
# push(x):
#   current_min = x если стек пуст, иначе min(x, stack[-1][1])
#   push((x, current_min))
#
# pop(): pop()
# top(): stack[-1][0]
# getMin(): stack[-1][1]
#
# Сложность:
# Время: O(1) на операцию
# Память: O(n)

# class MinStack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, val: int) -> None:
#         if not self.stack:
#             self.stack.append((val, val))
#         else:
#             cur_min = min(val, self.stack[-1][1])
#             self.stack.append((val, cur_min))
#
#     def pop(self) -> None:
#         self.stack.pop()
#
#     def top(self) -> int:
#         return self.stack[-1][0]
#
#     def getMin(self) -> int:
#         return self.stack[-1][1]



# ### TODO 71. Simplify Path
# Задача: дана абсолютная Unix-путь строка path (всегда начинается с '/').
# Нужно вернуть канонический (упрощённый) путь.
#
# Правила:
# - "."  -> текущая директория (игнорируем)
# - ".." -> перейти к родителю (убираем последний каталог из стека, если он есть)
# - "////" -> считается как один "/"
# - "..." и "...." и любые другие строки — это обычные имена папок/файлов
# Результат:
# - начинается с "/"
# - между директориями ровно один "/"
# - не заканчивается "/" (кроме корня "/")
#
# Паттерн: Stack / String


# ============================================================
# 1) Вариант "лучший для собеседования": стек по компонентам (O(n) время, O(n) память)
#
# Идея:
# Разбиваем по '/', получаем компоненты.
# Для каждой:
# - "" (пустая) или "." -> пропускаем
# - ".." -> pop из стека (если есть)
# - иначе -> push в стек (имя директории)
# В конце собираем: "/" + "/".join(stack) или "/" если стек пуст.
#
# Сложность:
# Время: O(n)
# Память: O(n)

# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         parts = path.split('/')
#         res = []
#
#         for i in parts:
#             if i == "" or i == ".":
#                 continue
#             if i == "..":
#                 if res:
#                     res.pop()
#             else:
#                 res.append(i)
#
#         return "/" + "/".join(res) if res else "/"


# # ### TODO РЕШИТЬ!   if i == "" or i == ".":   if i == "..":
# def simplifyPath(self, path: str) -> str:




# ### TODO 20. Valid Parentheses
# Задача: дана строка s, состоящая из скобок () {} [].
# Нужно проверить, является ли строка корректной:
# - открывающая скобка закрывается той же разновидностью
# - закрытие происходит в правильном порядке
# - у каждой закрывающей есть соответствующая открывающая
#
# Example:
# "()"     -> True
# "()[]{}" -> True
# "(]"     -> False
# "([])"   -> True
# "([)]"   -> False
#
# Паттерн: Stack / String

# ============================================================
# 1) Вариант "лучший для собеседования": Stack + close->open (O(n) время, O(n) память)
#
# Идея:
# - открывающие кладём в стек
# - на закрывающей проверяем верх стека и убираем
# - в конце стек должен быть пуст
#
# Сложность:
# Время: O(n)
# Память: O(n)

# class Solution:
#     def isValid(self, s: str) -> bool:
#         res = {')': '(', ']': '[', '}': '{'}
#         stack = []
#
#         for i in s:
#             if i in res:
#                 if not stack or stack.pop() != res[i]:
#                     return False
#             else:
#                 stack.append(i)
#
#         return not stack


# # # ### TODO РЕШИТЬ!
# def isValid(self, s: str) -> bool:



# ============================================================
# 2) Вариант "простая идея, но хуже по эффективности": replace в цикле (O(n^2) худший случай)
#
# Идея:
# Пока в строке есть пары "()", "[]", "{}" — удаляем их.
# Если в итоге строка пустая -> корректно, иначе нет.
#
# Почему хуже:
# replace создаёт новые строки, и цикл может выполниться много раз -> O(n^2) в худшем.
# Для собеседования обычно лучше стек.
#
# Сложность:
# Время: O(n^2) в худшем
# Память: O(n) (создание новых строк)

# class Solution:
#    def isValid(self, s: str) -> bool:
#        while "()" in s or "[]" in s or "{}" in s:
#            s = s.replace("()", "")
#            s = s.replace("[]", "")
#            s = s.replace("{}", "")
#            # s = s.replace("()", "").replace("[]", "").replace("{}", "")
#        return not s






# ### TODO Intervals


# ### TODO 452. Minimum Number of Arrows to Burst Balloons
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



# # # ### TODO РЕШИТЬ!
# def findMinArrowShots(self, points: List[List[int]]) -> int:






# ### TODO 57. Insert Interval
# Задача: дан массив непересекающихся интервалов intervals, отсортированный по start.
# Дан новый интервал newInterval = [start, end].
# Нужно вставить newInterval так, чтобы:
# - массив остался отсортированным по start
# - интервалы не пересекались (при необходимости слить пересекающиеся)
# Возвращаем новый массив интервалов.
#
# Example 1:
# intervals = [[1,3],[6,9]], newInterval = [2,5] -> [[1,5],[6,9]]
#
# Example 2:
# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# -> [[1,2],[3,10],[12,16]]
#
# Паттерн: One Pass / Merge Intervals
#
# ============================================================
# 1) Вариант "лучший для собеседования": три фазы (O(n) время, O(1) память кроме ответа)
#
# Идея:
# Пусть new = [s,e].
# 1) Добавляем все интервалы, которые строго ДО new: end < s
# 2) Сливаем все интервалы, которые пересекаются с new: start <= e
#    обновляем s = min(s, start), e = max(e, end)
# 3) Добавляем слитый new, затем все интервалы, которые после него
#
# Сложность:
# Время: O(n)
# Память: O(1) дополнительная (кроме ответа)

# from typing import List
#
# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         res: List[List[int]] = []
#         s, e = newInterval
#         i = 0
#         n = len(intervals)
#
#         # 1) интервалы полностью слева
#         while i < n and intervals[i][1] < s:
#             res.append(intervals[i])
#             i += 1
#
#         # 2) пересечения с newInterval
#         while i < n and intervals[i][0] <= e:
#             s = min(s, intervals[i][0])
#             e = max(e, intervals[i][1])
#             i += 1
#
#         res.append([s, e])
#
#         # 3) интервалы справа
#         while i < n:
#             res.append(intervals[i])
#             i += 1
#
#         return res



# # # ### TODO РЕШИТЬ!
# def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:



# ============================================================
# 2) Вариант "универсальный": добавить newInterval и сделать merge (O(n log n) время)
#
# Идея:
# Складываем intervals + [newInterval], сортируем и применяем merge как в задаче 56.
# Просто, но хуже по сложности (сортировка).
#
# Сложность:
# Время: O(n log n)
# Память: O(n)

# from typing import List
#
# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         all_intervals = intervals + [newInterval]
#         all_intervals.sort(key=lambda x: x[0])
#
#         merged: List[List[int]] = []
#         for s, e in all_intervals:
#             if not merged or s > merged[-1][1]:
#                 merged.append([s, e])
#             else:
#                 merged[-1][1] = max(merged[-1][1], e)
#         return merged



# ### TODO 56. Merge Intervals
# Задача: дан массив интервалов intervals, где intervals[i] = [start, end].
# Нужно слить все пересекающиеся интервалы и вернуть список непересекающихся интервалов,
# которые покрывают все исходные интервалы.
#
# Важно:
# Интервалы [1,4] и [4,5] считаются пересекающимися (т.к. граница общая).
#
# Example 1:
# intervals = [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]
#
# Example 2:
# intervals = [[1,4],[4,5]] -> [[1,5]]
#
# Example 3:
# intervals = [[4,7],[1,4]] -> [[1,7]]
#
# Паттерн: Sorting + One Pass
#
# ============================================================
# 1) Вариант "лучший для собеседования": сортировка по start + один проход (O(n log n) время, O(n) память)
#
# Идея:
# 1) Сортируем интервалы по началу (start).
# 2) Идём по отсортированным:
#    - если текущий интервал пересекается с последним в ответе (cur_start <= last_end),
#      то расширяем last_end = max(last_end, cur_end)
#    - иначе добавляем новый интервал в ответ
#
# Сложность:
# Время: O(n log n) (сортировка)
# Память: O(n) (ответ)

# from typing import List
#
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         if not intervals:
#             return []
#
#         intervals.sort(key=lambda x: x[0])
#         merged: List[List[int]] = [intervals[0]]
#
#         for s, e in intervals[1:]:
#             last_s, last_e = merged[-1]
#             if s <= last_e:  # пересечение (включая касание границ)
#                 merged[-1][1] = max(last_e, e)
#             else:
#                 merged.append([s, e])
#
#         return merged


# # # ### TODO РЕШИТЬ!
# def merge(self, intervals: List[List[int]]) -> List[List[int]]:




# ### TODO 228. Summary Ranges  + ВАРИАНТ С СОБЕСЕДОВАНИЯ   nums = sorted(set(nums))  return ", ".join(res)
# Задача: дан отсортированный массив уникальных целых nums.
# Нужно вернуть список диапазонов, которые покрывают все числа ровно один раз.
#
# Диапазон [a,b]:
# - выводим "a->b", если a != b
# - выводим "a", если a == b
#
# Example 1:
# nums = [0,1,2,4,5,7] -> ["0->2","4->5","7"]
#
# Example 2:
# nums = [0,2,3,4,6,8,9] -> ["0","2->4","6","8->9"]
#
# Паттерн: One Pass / Two Pointers
#
# ============================================================
# 1) Вариант "лучший для собеседования": start + prev (O(n) время, O(1) память)
#
# Идея:
# Держим начало текущего диапазона start и предыдущий элемент prev.
# Идём по nums:
# - если текущее число продолжает диапазон (num == prev + 1) -> двигаем prev
# - иначе закрываем диапазон [start..prev], добавляем в ответ и начинаем новый
# В конце обязательно закрываем последний диапазон.
#
# Сложность:
# Время: O(n)
# Память: O(1) дополнительная (кроме ответа)

# from typing import List
#
# class Solution:
#     def summaryRanges(self, nums: List[int]) -> List[str]:
#         if not nums:
#             return []
#
#         res: List[str] = []
#         start = nums[0]
#         # prev = nums[0] # ТОЖЕ САМОЕ  prev = start
#         prev = start
#
#         for i in nums[1:]:
#             if i == prev + 1:
#                 prev = i
#             else:
#                 if start == prev:
#                     res.append(str(start))
#                 else:
#                     res.append(f"{start}->{prev}")
#                     # res.append("{}->{}".format(start, prev))       ### ЧЕРЕЗ ФОРМАТ
#                     # res.append("{a}->{b}".format(a=start, b=prev)) ### ЧЕРЕЗ ФОРМАТ
#                 start = i
#                 prev = i
#
#         # закрываем последний диапазон
#         if start == prev:
#             res.append(str(start))
#         else:
#             res.append(f"{start}->{prev}")
#
#         return res


# # # ### TODO РЕШИТЬ! + ВАРИАНТ С СОБЕСЕДОВАНИЯ   nums = sorted(set(nums))  return ", ".join(res)
# def summaryRanges(self, nums: List[int]) -> List[str]:





# ============================================================
# 2) Вариант "универсальный": сортировка + удаление дублей + one-pass (O(n log n) время, O(n) память)
#
# Важно:
# Это НЕ каноничное решение для LeetCode 228, потому что в 228 вход уже отсортирован и уникален,
# и можно решить за O(n) без сортировки. Здесь вариант именно "универсальный" для произвольного списка.
#
# Example (универсальный вход — может быть не отсортирован и с дубликатами):
# nums = [7, 2, 2, 1, 0, 5, 4, 1] -> "0->2, 4->5, 7"
#
# Идея:
# 1) Приводим вход к нужному виду:
#    nums = sorted(set(nums))   # убираем дубликаты и сортируем
# 2) Дальше тем же алгоритмом (start/prev) сжимаем подряд идущие числа в диапазоны.
# 3) Возвращаем строку ", ".join(res) (как в твоём list_to_ranges).
#
# Сложность:
# Время: O(n log n) (из-за сортировки)
# Память: O(n) (set + сортировка создают новые структуры)

# from typing import List
#
# class Solution:
#     def summaryRanges(self, nums: List[int]) -> str:
#         if not nums:
#             return ""
#
#         nums = sorted(set(nums))
#
#         res: List[str] = []
#         start = nums[0]
#         # prev = nums[0] # ТОЖЕ САМОЕ  prev = start
#         prev = start
#
#         for i in nums[1:]:
#             if i == prev + 1:
#                 prev = i
#             else:
#                 if start == prev:
#                     res.append(str(start))
#                 else:
#                     res.append(f"{start}->{prev}")
#                     # res.append("{}->{}".format(start, prev))       ### ЧЕРЕЗ ФОРМАТ
#                     # res.append("{a}->{b}".format(a=start, b=prev)) ### ЧЕРЕЗ ФОРМАТ
#                 start = i
#                 prev = i
#
#         # закрываем последний диапазон
#         if start == prev:
#             res.append(str(start))
#         else:
#             res.append(f"{start}->{prev}")
#
#         return ", ".join(res)




# ### TODO Hashmap


# ### TODO 128. Longest Consecutive Sequence + ВЫВОД ПОСЛЕДОВАТЕЛЬНОСТИ
# Задача: дан НЕотсортированный массив nums.
# Нужно вернуть длину самой длинной последовательности подряд идущих чисел (consecutive).
# Требование: O(n) по времени.
#
# Example 1:
# nums = [100,4,200,1,3,2] -> 4  (1,2,3,4)
#
# Example 2:
# nums = [0,3,7,2,5,8,4,6,0,1] -> 9  (0..8)
#
# Example 3:
# nums = [1,0,1,2] -> 3  (0,1,2)
#
# Паттерн: HashSet


# ============================================================
# 1) Вариант "лучший для собеседования": HashSet + старт последовательности (O(n), O(n))
#
# Идея:
# - кладём все числа в set
# - число x является началом последовательности, если (x-1) нет в set
# - тогда считаем длину: x, x+1, x+2, ... пока есть в set
# Так каждое число проверяется ограниченное число раз, итог O(n).
#
# Сложность:
# Время: O(n)
# Память: O(n)

# from typing import List
#
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         s = set(nums)
#         best = 0
#
#         for i in s:
#             # стартуем только с начала последовательности
#             if i - 1 not in s:
#                 y = i
#                 while y in s:
#                     y += 1
#                 best = max(best, y - i)
#
#         return best



# # # ### TODO РЕШИТЬ!
# def longestConsecutive(self, nums: List[int]) -> int:




# ============================================================
# 1b) Расширение: вернуть саму последовательность (а не только длину)
#
# Идея:
# То же самое, но дополнительно запоминаем best_start (начало лучшей серии)
# и best_len. После прохода восстанавливаем ответ:
# [best_start, best_start+1, ..., best_start+best_len-1]
#
# Сложность:
# Время: O(n)
# Память: O(n)

# from typing import List
#
# class Solution:
#     def longestConsecutiveSequence(self, nums: List[int]) -> List[int]:
#         if not nums:
#             return []
#
#         s = set(nums)
#         best_len = 0
#         best_start = None
#
#         for i in s:
#             # i — начало последовательности
#             if i - 1 not in s:
#                 y = i
#                 while y in s:
#                     y += 1
#                 length = y - i
#
#                 if length > best_len:
#                     best_len = length
#                     best_start = i
#
#         if best_start is None:
#             return []
#
#         return [best_start + i for i in range(best_len)]


# ============================================================
# 2) Вариант "простой": сортировка (O(n log n), O(1)*)
#
# Идея:
# - сортируем
# - считаем длину текущей подряд идущей серии, пропуская дубликаты
#
# Сложность:
# Время: O(n log n)
# Память: зависит от сортировки в Python (может быть O(n) в худшем)

# from typing import List
#
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#
#         nums.sort()
#         best = 1
#         cur = 1
#
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]:
#                 continue
#             if nums[i] == nums[i - 1] + 1:
#                 cur += 1
#             else:
#                 best = max(best, cur)
#                 cur = 1
#
#         return max(best, cur)



# ### TODO 219. Contains Duplicate II
# Задача: дан массив nums и число k.
# Нужно вернуть True, если существуют разные индексы i и j такие, что:
# - nums[i] == nums[j]
# - |i - j| <= k
#
# Example 1:
# nums = [1,2,3,1], k = 3 -> True (0 и 3)
#
# Example 2:
# nums = [1,0,1,1], k = 1 -> True (2 и 3)
#
# Example 3:
# nums = [1,2,3,1,2,3], k = 2 -> False
#
# Паттерн: HashMap / Sliding Window


# ============================================================
# 1) Вариант "лучший для собеседования": HashMap last_index (O(n) время, O(n) память)
#
# Идея:
# Храним последний индекс появления каждого значения.
# Если встречаем nums[i] и он уже был на позиции prev,
# проверяем i - prev <= k.
#
# Сложность:
# Время: O(n)
# Память: O(n)

# from typing import List
#
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         last = {}
#         for i, v in enumerate(nums):
#             if v in last and i - last[v] <= k:
#                 return True
#             last[v] = i
#         return False


# # # ### TODO РЕШИТЬ!
# def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:



# ============================================================
# 2) Вариант "простой": sliding window set размера k (O(n) время, O(k) память)
#
# Идея:
# Держим множество последних k элементов (окно индексов [i-k .. i-1]).
# Если текущий x уже в set -> есть дубликат на расстоянии <= k.
# Потом добавляем x, и если размер окна превысил k — удаляем nums[i-k].
#
# Сложность:
# Время: O(n)
# Память: O(k)

# from typing import List
#
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         seen = set()
#         for i, v in enumerate(nums):
#             if v in seen:
#                 return True
#             seen.add(v)
#             if len(seen) > k:
#                 seen.remove(nums[i - k])
#         return False



# ### TODO 202. Happy Number
# Задача: определить, является ли число n "счастливым".
# Процесс:
# - заменяем число суммой квадратов его цифр
# - повторяем, пока не получим 1 (счастливое) или не попадём в цикл (несчастливое)
#
# Example 1:
# n = 19 -> True
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
# Example 2:
# n = 2 -> False
#
# Паттерн: HashSet / Fast-Slow Pointers


# ============================================================
# 1) Вариант "лучший для собеседования": Floyd (fast/slow) (O(1) память)
### Floyd — это алгоритм Флойда обнаружения цикла (его ещё называют tortoise and hare — “черепаха и заяц”).
#
# Идея:
# Это задача на обнаружение цикла.
# - slow двигается на 1 шаг: f(n)
# - fast на 2 шага: f(f(n))
# Если есть цикл не содержащий 1, то slow == fast (в какой-то точке).
# Если fast дошёл до 1 — число счастливое.
#
# Сложность:
# Время: O(кол-во шагов до 1/цикла) (по факту очень мало)
# Память: O(1)

# class Solution:
#     def isHappy(self, n: int) -> bool:
#         def nxt(x: int) -> int:
#             s = 0
#             while x > 0:
#                 d = x % 10
#                 s += d * d
#                 x //= 10
#             return s
#
#         slow = n
#         fast = nxt(n)
#         while fast != 1 and slow != fast:
#             slow = nxt(slow)
#             fast = nxt(nxt(fast))
#         return fast == 1


# # # ### TODO РЕШИТЬ!
# def isHappy(self, n: int) -> bool:




# ============================================================
# 2) Вариант "простой": set для посещённых значений (O(k) память)
#
# Идея:
# Запоминаем все встреченные значения n.
# Если n стал 1 -> True.
# Если n повторился -> цикл -> False.
#
# Сложность:
# Время: O(кол-во шагов)
# Память: O(кол-во уникальных значений)

# class Solution:
#     def isHappy(self, n: int) -> bool:
#         def nxt(x: int) -> int:
#             s = 0
#             while x > 0:
#                 d = x % 10
#                 s += d * d
#                 x //= 10
#             return s
#
#         seen = set()
#         while n != 1 and n not in seen:
#             seen.add(n)
#             n = nxt(n)
#         return n == 1




# ### TODO 1. Two Sum
# Задача: дан массив nums и число target.
# Нужно вернуть индексы двух элементов, сумма которых равна target.
# Гарантируется ровно одно решение. Нельзя использовать один и тот же элемент дважды.
# Порядок индексов не важен.
#
# Example 1:
# nums = [2,7,11,15], target = 9 -> [0,1]
#
# Example 2:
# nums = [3,2,4], target = 6 -> [1,2]
#
# Example 3:
# nums = [3,3], target = 6 -> [0,1]
#
# Паттерн: HashMap


# ============================================================
# 1) Вариант "лучший для собеседования": HashMap (O(n) время, O(n) память)
#
# Идея:
# Идём по nums. Для текущего x ищем, есть ли уже (target - x) в словаре.
# В словаре храним: value -> index.
# Если нашли пару — возвращаем [index_of_need, current_index].
#
# Сложность:
# Время: O(n)
# Память: O(n)


# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         seen = {}  # value -> index
#         for i, v in enumerate(nums):
#             need = target - v
#             if need in seen:
#                 return [seen[need], i]
#             seen[v] = i


# # # ### TODO РЕШИТЬ!
# def twoSum(self, nums: list[int], target: int) -> list[int]:






# ============================================================
# 2) Вариант "простой": brute force (O(n^2) время, O(1) память)
#
# Идея:
# Перебираем все пары (i, j), i < j, проверяем сумму.
#
# Сложность:
# Время: O(n^2)
# Память: O(1)


# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []




# ### TODO 49. Group Anagrams
# Задача: дан список строк strs. Нужно сгруппировать анаграммы вместе.
# Анаграммы имеют одинаковые символы в одинаковых количествах (порядок не важен).
# Вернуть список групп в любом порядке.
#
# Example 1:
# Input:  ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Example 2:
# Input:  [""]
# Output: [[""]]
#
# Example 3:
# Input:  ["a"]
# Output: [["a"]]
#
# Паттерн: HashMap / Sorting / Counting


# ============================================================
# 1) Вариант "лучший для собеседования": ключ = отсортированная строка (O(n * k log k))
#
# Идея:
# Для каждой строки строим ключ: ''.join(sorted(word)).
# Все анаграммы дадут одинаковый ключ -> складываем в dict[key].
#
# Сложность:
# Пусть n = кол-во строк, k = средняя длина строки.
# Время: O(n * k log k) (сортировка каждой строки)
# Память: O(n * k) на хранение групп

# from collections import defaultdict
#
# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         groups = defaultdict(list)
#         for w in strs:
#             key = "".join(sorted(w))
#             groups[key].append(w)
#         return list(groups.values())


# # # ### TODO РЕШИТЬ!
# def groupAnagrams(self, strs: list[str]) -> list[list[str]]:



# ============================================================
# 2) Вариант "быстрее для a-z": ключ = частоты 26 букв (O(n * k))
#
# Идея:
# Если строки состоят из lowercase a-z:
# - считаем частоты в массиве из 26
# - используем tuple(freq) как ключ
#
# Сложность:
# Время: O(n * k)
# Память: O(n * k)


# from collections import defaultdict
#
# class Solution:
#     def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         groups = defaultdict(list)
#
#         for w in strs:
#             freq = [0] * 26
#             for ch in w:
#                 freq[ord(ch) - ord('a')] += 1
#             groups[tuple(freq)].append(w)
#
#         return list(groups.values())



# ### TODO 242. Valid Anagram
# Задача: даны строки s и t. Нужно проверить, является ли t анаграммой s
# (т.е. содержит те же символы в тех же количествах, порядок не важен).
#
# Example 1:
# s="anagram", t="nagaram" -> True
#
# Example 2:
# s="rat", t="car" -> False
#
# Паттерн: HashMap / Counting


# ============================================================
# 1) Вариант "лучший для собеседования": подсчёт частот (Counter) (O(n), O(k))
#
# Идея:
# - если длины разные -> False
# - считаем частоты символов и сравниваем
#
# Сложность:
# Время: O(n)
# Память: O(k), k — число разных символов (для lowercase обычно O(1))

# from collections import Counter
#
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         return Counter(s) == Counter(t)


# # # ### TODO РЕШИТЬ!
# def isAnagram(self, s: str, t: str) -> bool:



# ============================================================
# 2) Вариант "быстрый для a-z": массив из 26 (O(n), O(1))
#
# Идея:
# Если гарантировано lowercase английские буквы:
# - увеличиваем счётчик по s
# - уменьшаем по t
# - если где-то ушли в минус -> False
#
# Сложность:
# Время: O(n)
# Память: O(1)

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#
#         freq = [0] * 26
#         for ch in s:
#             freq[ord(ch) - ord('a')] += 1
#         for ch in t:
#             i = ord(ch) - ord('a')
#             freq[i] -= 1
#             if freq[i] < 0:
#                 return False
#         return True



# ### TODO 290. Word Pattern
# Задача: дана строка pattern (буквы) и строка s (слова через пробел).
# Нужно проверить, следует ли s шаблону pattern:
# - каждой букве соответствует ровно одно слово
# - каждому слову соответствует ровно одна буква (bijection)
# - длина pattern должна совпадать с количеством слов
#
# Example 1:
# pattern="abba", s="dog cat cat dog" -> True
#
# Example 2:
# pattern="abba", s="dog cat cat fish" -> False
#
# Example 3:
# pattern="aaaa", s="dog cat cat dog" -> False
#
# Паттерн: HashMap / Bijection


# ============================================================
# 1) Вариант "лучший для собеседования": два словаря (O(n), O(k))
#
# Идея:
# Разбиваем s на слова.
# Держим отображение в обе стороны:
# - p2w[char] = word
# - w2p[word] = char
# На каждой позиции проверяем согласованность.
#
# Сложность:
# Время: O(n)
# Память: O(k)

# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         words = s.split()
#         if len(pattern) != len(words):
#             return False
#
#         p2w = {}
#         w2p = {}
#
#         for p, w in zip(pattern, words):
#             if p in p2w and p2w[p] != w:
#                 return False
#             if w in w2p and w2p[w] != p:
#                 return False
#             p2w[p] = w
#             w2p[w] = p
#
#         return True


# # # ### TODO РЕШИТЬ!
# def wordPattern(self, pattern: str, s: str) -> bool:







# ### TODO 205. Isomorphic Strings
# Задача: даны строки s и t. Определить, изоморфны ли они.
# Строки изоморфны, если можно заменить символы s так, чтобы получить t:
# - каждый символ s всегда заменяется на один и тот же символ t
# - разные символы s не могут перейти в один и тот же символ t (bijection)
# - символ может отображаться в себя
#
# Example 1:
# s="egg", t="add" -> True
#
# Example 2:
# s="foo", t="bar" -> False
#
# Example 3:
# s="paper", t="title" -> True
#
# Паттерн: HashMap / Mapping


# ============================================================
# 1) Вариант "лучший для собеседования": два словаря (O(n) время, O(k) память)
#
# Идея:
# Держим отображения в обе стороны:
# - s_to_t[ch_s] = ch_t
# - t_to_s[ch_t] = ch_s
# На каждой позиции проверяем согласованность.
#
# Сложность:
# Время: O(n)
# Память: O(k), где k — число разных символов

# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#
#         s_to_t = {}
#         t_to_s = {}
#
#         for ct, ts in zip(s, t):
#             if ct in s_to_t and s_to_t[ct] != ts:
#                 return False
#             if ts in t_to_s and t_to_s[ts] != ct:
#                 return False
#             s_to_t[ct] = ts
#             t_to_s[ts] = ct
#
#         return True


# # # ### TODO РЕШИТЬ!
# def isIsomorphic(self, s: str, t: str) -> bool:








# ### TODO 383. Ransom Note
# Задача: даны строки ransomNote и magazine.
# Нужно вернуть True, если ransomNote можно составить из букв magazine,
# причём каждую букву magazine можно использовать не более одного раза.
#
# Example 1:
# ransomNote="a", magazine="b" -> False
# Example 2:
# ransomNote="aa", magazine="ab" -> False
# Example 3:
# ransomNote="aa", magazine="aab" -> True
#
# Паттерн: HashMap / Counting


# ============================================================
# 1) Вариант "лучший для собеседования": подсчёт частот (Counter) (O(n+m), O(k))
#
# Идея:
# Считаем частоты букв в magazine и уменьшаем по буквам ransomNote.
# Если какой-то буквы не хватает — False.
#
# Сложность:
# Время: O(n + m)
# Память: O(k), где k — количество разных символов (для lowercase обычно O(1))

# from collections import Counter
#
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         cnt = Counter(magazine)
#         for i in ransomNote:
#             if cnt[i] == 0:
#                 return False
#             cnt[i] -= 1
#         return True


# # # ### TODO РЕШИТЬ!
# def canConstruct(self, ransomNote: str, magazine: str) -> bool:




# ============================================================
# 2) Вариант "быстрый для алфавита a-z": массив из 26 (O(n+m), O(1))
#
# Идея:
# Если гарантировано lowercase английские буквы:
# - считаем частоты в массиве из 26
# - уменьшаем по ransomNote
#
# Сложность:
# Время: O(n + m)
# Память: O(1)

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         freq = [0] * 26
#         for ch in magazine:
#             freq[ord(ch) - ord('a')] += 1
#
#         for ch in ransomNote:
#             i = ord(ch) - ord('a')
#             if freq[i] == 0:
#                 return False
#             freq[i] -= 1
#
#         return True







# ### TODO Sliding Window


# ### TODO 3. Longest Substring Without Repeating Characters  + ВЫВОД ПОДСТРОКИ
# Задача: дана строка s. Найти длину самой длинной подстроки без повторяющихся символов.
#
# Example 1:
# Input:  "abcabcbb"
# Output: 3  ("abc")
#
# Example 2:
# Input:  "bbbbb"
# Output: 1  ("b")
#
# Example 3:
# Input:  "pwwkew"
# Output: 3  ("wke")
#
# Паттерн: Sliding Window / HashMap


# ============================================================
# 1) Вариант "лучший для собеседования": sliding window + last seen index (O(n), O(k))
#
# Идея:
# Держим левую границу окна l и словарь last, где last[ch] = последний индекс символа ch.
# Идём r слева направо:
# - если символ ch уже встречался и last[ch] >= l, значит он внутри текущего окна,
#   тогда сдвигаем l = last[ch] + 1
# - обновляем last[ch] = r
# - обновляем best = max(best, r - l + 1)
#
# Сложность:
# Время: O(n)
# Память: O(k) (k — кол-во уникальных символов в окне, максимум алфавит)

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         last = {}
#         l = 0
#         best = 0
#
#         for i, v in enumerate(s):
#             if v in last and last[v] >= l:
#                 l = last[v] + 1
#             last[v] = i
#             best = max(best, i - l + 1)
#
#         return best



# # # ### TODO РЕШИТЬ!   + ВЫВОД ПОДСТРОКИ
# def lengthOfLongestSubstring(self, s: str) -> int:




# ============================================================
# 1b) Вариант: вернуть саму подстроку (sliding window + last seen index)
#
# Идея:
# Всё то же самое, но дополнительно запоминаем границы лучшего окна:
# - best_l — старт лучшей подстроки
# - best_len — её длина
# В конце возвращаем s[best_l : best_l + best_len]
#
# Сложность:
# Время: O(n)
# Память: O(k)

# class Solution:
#     def longestSubstring(self, s: str) -> str:
#         last = {}
#         l = 0
#         best_l = 0
#         best_len = 0
#
#         for i, v in enumerate(s):
#             if v in last and last[v] >= l:
#                 l = last[v] + 1
#             last[v] = i
#
#             cur_len = i - l + 1
#             if cur_len > best_len:
#                 best_len = cur_len
#                 best_l = l
#
#         return s[best_l:best_l + best_len]





# ### TODO 209. Minimum Size Subarray Sum
# Задача: дан массив положительных nums и число target.
# Нужно найти минимальную длину подмассива (непустого), сумма которого >= target.
# Если такого подмассива нет — вернуть 0.
#
# Example 1:
# Input:  target = 7, nums = [2,3,1,2,4,3]
# Output: 2  (подмассив [4,3])
#
# Example 2:
# Input:  target = 4, nums = [1,4,4]
# Output: 1
#
# Example 3:
# Input:  target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
#
# Паттерн: Sliding Window / Two Pointers


# ============================================================
# 1) Вариант "лучший для собеседования": Sliding Window (O(n) время, O(1) память)
#
# Идея:
# Так как все числа положительные, можно держать окно [l..r] и его сумму.
# - расширяем r, добавляя nums[r] в sum
# - пока sum >= target, пытаемся сжать окно слева (l++) и обновляем минимум длины
#
# Сложность:
# Время: O(n) (каждый указатель двигается максимум n раз)
# Память: O(1)


# class Solution:
#     def minSubArrayLen(self, target: int, nums: list[int]) -> int:
#         l = 0
#         cur_sum = 0
#         best = float("inf")
#
#         for i, v in enumerate(nums):
#             cur_sum += v
#             while cur_sum >= target:
#                 best = min(best, i - l + 1)
#                 cur_sum -= nums[l]
#                 l += 1
#
#         return 0 if best == float("inf") else best


# # # ### TODO РЕШИТЬ!
# def minSubArrayLen(self, target: int, nums: list[int]) -> int:



# ============================================================
# 2) Вариант "альтернатива": префикс-суммы + бинарный поиск (O(n log n), O(n) память)
#
# Идея:
# Строим prefix, где prefix[i] = сумма nums[0..i-1], prefix[0]=0.
# Для каждого i ищем минимальный j, что prefix[j] - prefix[i] >= target,
# то есть prefix[j] >= prefix[i] + target. Это lower_bound по prefix.
#
# Сложность:
# Время: O(n log n)
# Память: O(n)

# import bisect
#
# class Solution:
#     def minSubArrayLen(self, target: int, nums: list[int]) -> int:
#         n = len(nums)
#         prefix = [0] * (n + 1)
#         for i in range(n):
#             prefix[i + 1] = prefix[i] + nums[i]
#
#         best = float("inf")
#         for i in range(n):
#             need = prefix[i] + target
#             j = bisect.bisect_left(prefix, need, i + 1)
#             if j <= n:
#                 best = min(best, j - i)
#
#         return 0 if best == float("inf") else best





# ### TODO Two Pointers



# ### TODO 15. 3Sum
# Задача: дан массив nums. Нужно вернуть все уникальные тройки [nums[i], nums[j], nums[k]],
# такие что i, j, k различны и nums[i] + nums[j] + nums[k] == 0.
# В ответе не должно быть дубликатов троек.
#
# Example 1:
# Input:  nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#
# Example 2:
# Input:  nums = [0,1,1]
# Output: []
#
# Example 3:
# Input:  nums = [0,0,0]
# Output: [[0,0,0]]
#
# Паттерн: Sorting + Two Pointers


# ============================================================
# 1) Вариант "лучший для собеседования": сортировка + два указателя (O(n^2), O(1) доп. память*)
#
# Идея:
# - сортируем nums
# - фиксируем i (первый элемент)
# - дальше решаем 2Sum на отрезке (i+1..n-1) двумя указателями l/r
# - избегаем дубликатов:
#   * пропускаем одинаковые nums[i]
#   * после нахождения тройки двигаем l и r, пропуская одинаковые значения
#
# Оптимизации:
# - если nums[i] > 0, дальше все будут >= 0 -> сумма не станет 0 -> можно break
#
# Сложность:
# Время: O(n^2)
# Память: O(1) доп. (сортировка в Python может использовать доп. память)

### “Если нельзя модифицировать вход, использую nums = sorted(nums)  — получаю отсортированную копию; это +O(n) память.”

# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         # nums = sorted(nums)          # <-- копия + сортировка
#         nums.sort()
#         n = len(nums)
#         res = []
#
#         for i in range(n - 2):
#             if nums[i] > 0:
#                 break
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#
#             l, r = i + 1, n - 1
#             while l < r:
#                 s = nums[i] + nums[l] + nums[r]
#                 if s == 0:
#                     res.append([nums[i], nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#
#                     while l < r and nums[l] == nums[l - 1]:
#                         l += 1
#                     while l < r and nums[r] == nums[r + 1]:
#                         r -= 1
#
#                 elif s < 0:
#                     l += 1
#                 else:
#                     r -= 1
#
#         return res


# # # ### TODO РЕШИТЬ!
# def threeSum(self, nums: list[int]) -> list[list[int]]:



# ============================================================
# 2) Вариант "простой": hashset для 2Sum внутри (O(n^2), O(n) память)
#
# Идея:
# - фиксируем i
# - для оставшейся части делаем 2Sum через set seen
# - чтобы убрать дубликаты, храним тройки в set как кортежи (после сортировки nums тройка уже упорядочена)
#
# Сложность:
# Время: O(n^2)
# Память: O(n) (seen + set ответов)


# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         nums.sort()
#         n = len(nums)
#         ans = set()
#
#         for i in range(n - 2):
#             seen = set()
#             for j in range(i + 1, n):
#                 need = -nums[i] - nums[j]
#                 if need in seen:
#                     ans.add((nums[i], need, nums[j]))
#                 seen.add(nums[j])
#
#         return [list(t) for t in ans]



# ### TODO 11. Container With Most Water
# Задача: дан массив height, где height[i] — высота вертикальной линии в точке i.
# Нужно выбрать две линии (i, j), чтобы площадь контейнера была максимальной:
# area = (j - i) * min(height[i], height[j])
# Нельзя наклонять контейнер.
#
# Example 1:
# Input:  [1,8,6,2,5,4,8,3,7]
# Output: 49
#
# Example 2:
# Input:  [1,1]
# Output: 1
#
# Паттерн: Two Pointers


# ============================================================
# 1) Вариант "лучший для собеседования": Two Pointers (O(n) время, O(1) память)
#
# Идея:
# - ставим l=0, r=n-1
# - считаем текущую площадь
# - двигаем указатель с меньшей высотой, потому что:
#   ширина уменьшается всегда, а увеличить площадь можно только увеличив min(height[l], height[r]),
#   что возможно лишь подняв меньшую сторону (сдвинув её внутрь).
#
# Сложность:
# Время: O(n)
# Память: O(1)


# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         l, r = 0, len(height) - 1
#         best = 0
#
#         while l < r:
#             h = min(height[l], height[r])
#             best = max(best, (r - l) * h)
#
#             if height[l] < height[r]:
#                 l += 1
#             else:
#                 r -= 1
#
#         return best


# # # ### TODO РЕШИТЬ!
# def maxArea(self, height: list[int]) -> int:




# ### TODO 167. Two Sum II - Input Array Is Sorted
# Задача: дан отсортированный (неубывающий) массив numbers (1-indexed) и target.
# Нужно найти два числа numbers[index1] и numbers[index2], которые в сумме дают target,
# и вернуть индексы [index1, index2] (1 <= index1 < index2 <= n).
# Гарантируется ровно одно решение. Нельзя использовать один и тот же элемент дважды.
# Требование: O(1) доп. память.
#
# Example 1:
# Input:  numbers = [2,7,11,15], target = 9
# Output: [1,2]
#
# Example 2:
# Input:  numbers = [2,3,4], target = 6
# Output: [1,3]
#
# Example 3:
# Input:  numbers = [-1,0], target = -1
# Output: [1,2]
#
# Паттерн: Two Pointers / Sorted Array


# ============================================================
# 1) Вариант "лучший для собеседования": два указателя (O(n) время, O(1) память)
#
# Идея:
# l = 0, r = n-1
# - если numbers[l] + numbers[r] < target -> увеличиваем l
# - если > target -> уменьшаем r
# - иначе нашли ответ
# Возвращаем 1-indexed индексы: [l+1, r+1]
#
# Сложность:
# Время: O(n)
# Память: O(1)


# class Solution:
#     def twoSum(self, numbers: list[int], target: int) -> list[int]:
#         l, r = 0, len(numbers) - 1
#         while l < r:
#             s = numbers[l] + numbers[r]
#             if s == target:
#                 return [l + 1, r + 1]
#             if s < target:
#                 l += 1
#             else:
#                 r -= 1
#         return []  # по условию не понадобится


# # # ### TODO РЕШИТЬ!
# def twoSum(self, numbers: list[int], target: int) -> list[int]:





# ============================================================
# 2) Вариант "простой": для каждого числа искать пару бинпоиском (O(n log n), O(1))
#
# Идея:
# Для i берём need = target - numbers[i], ищем его в правой части (i+1..n-1) бинарным поиском.
#
# Сложность:
# Время: O(n log n)
# Память: O(1)


# class Solution:
#     def twoSum(self, numbers: list[int], target: int) -> list[int]:
#         n = len(numbers)
#
#         for i in range(n):
#             need = target - numbers[i]
#             l, r = i + 1, n - 1
#             while l <= r:
#                 mid = (l + r) // 2
#                 if numbers[mid] == need:
#                     return [i + 1, mid + 1]  # 1-indexed
#                 if numbers[mid] < need:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#
#         return []  # по условию не понадобится




# ### TODO 392. Is Subsequence
# Задача: даны строки s и t. Нужно проверить, является ли s подпоследовательностью t.
# Подпоследовательность получается удалением некоторых символов из t без изменения порядка.
#
# Example 1:
# Input:  s = "abc", t = "ahbgdc"
# Output: True
#
# Example 2:
# Input:  s = "axc", t = "ahbgdc"
# Output: False
#
# Паттерн: Two Pointers


# ============================================================
# 2) Вариант "простой": через итератор (Python-лайфхак) (O(|t|), O(1))
#
# Идея:
# Берём итератор по t и проверяем, что каждый символ s встречается дальше в t.
# Выражение `c in it` двигает итератор вперёд до первого совпадения.
#
# Сложность:
# Время: O(n + m)
# Память: O(1)

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         it = iter(t)
#         return all(ch in it for ch in s)


# # # ### TODO РЕШИТЬ!
# def isSubsequence(self, s: str, t: str) -> bool:



# ============================================================
# 1) Вариант "лучший для собеседования": два указателя (O(|t|), O(1))
#
# Идея:
# Идём по t, указатель i показывает, какой символ из s мы сейчас ищем.
# Когда t[j] == s[i], двигаем i.
# В конце i == len(s) -> True.
#
# Сложность:
# Время: O(n + m) — один проход по t (и по s максимум один раз), где n=len(s), m=len(t).
# Память: O(1) — только индексы.

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         i = 0
#         for ch in t:
#             if i < len(s) and s[i] == ch:
#                 i += 1
#         return i == len(s)




# ### TODO 125. Valid Palindrome
# Задача: дана строка s. Нужно проверить, является ли она палиндромом,
# если:
# - привести все буквы к нижнему регистру
# - удалить все НЕ буквенно-цифровые символы
#
# Alphanumeric: буквы (a-z, A-Z) и цифры (0-9).
#
# Example 1:
# Input:  "A man, a plan, a canal: Panama"
# Output: True
#
# Example 2:
# Input:  "race a car"
# Output: False
#
# Example 3:
# Input:  " "
# Output: True
#
# Паттерн: Two Pointers / String


# ============================================================
# 1) Вариант "лучший для собеседования": two pointers без доп. строки (O(n), O(1))
#
# Идея:
# Два указателя l, r.
# - двигаем l вправо, пока s[l] не alnum
# - двигаем r влево, пока s[r] не alnum
# - сравниваем lower() символы
#
# Сложность:
# Время: O(n)
# Память: O(1)

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l, r = 0, len(s) - 1
#
#         while l < r:
#             while l < r and not s[l].isalnum():
#                 l += 1
#             while l < r and not s[r].isalnum():
#                 r -= 1
#
#             if s[l].lower() != s[r].lower():
#                 return False
#
#             l += 1
#             r -= 1
#
#         return True


# # ### TODO РЕШИТЬ!
# def isPalindrome(self, s: str) -> bool:




# ### TODO Array / String


# ### TODO 28. Find the Index of the First Occurrence in a String
# Задача: даны строки haystack и needle.
# Нужно вернуть индекс первого вхождения needle в haystack, иначе -1.
#
# Example 1:
# Input:  haystack = "sadbutsad", needle = "sad"
# Output: 0
#
# Example 2:
# Input:  haystack = "leetcode", needle = "leeto"
# Output: -1
#
# Паттерн: String / Two Pointers / Substring Search


# ============================================================
# 1) Вариант "лучший для собеседования": прямой поиск (brute force) (O(n*m), O(1))
#
# Идея:
# Пробуем выровнять needle с каждой позицией i в haystack (0..n-m),
# и проверяем посимвольно совпадение.
#
# Edge cases:
# - если needle == "" -> 0 (классическое поведение strStr/Java indexOf)
# - если needle длиннее haystack -> -1
#
# Сложность:
# Время: O(n * m)
# Память: O(1)

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if needle == "":
#             return 0
#         n, m = len(haystack), len(needle)
#         if m > n:
#             return -1
#
#         for i in range(n - m + 1):
#             j = 0
#             while j < m and haystack[i + j] == needle[j]:
#                 j += 1
#             if j == m:
#                 return i
#         return -1


# # ### TODO РЕШИТЬ!
# def strStr(self, haystack: str, needle: str) -> int:



# ============================================================
# 2) Вариант "простой" для Python: встроенный find (обычно O(n), но зависит от реализации)
#
# Идея:
# - используем haystack.find(needle), он возвращает -1 если не найдено
#
# Сложность:
# Время: обычно близко к O(n), зависит от реализации
# Память: O(1)

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         return haystack.find(needle)


# 3) Если хочешь именно через regex (не советую)  без f-string:
# Сложность:
# Время: O(n·m)   (в худшем случае; по сути обычный поиск подстроки)
# Память: O(1)

# def strStr(haystack, needle):
#     """
#     :type haystack: str
#     :type needle: str
#     :rtype: int
#     """
#     import re
#     res = re.search(re.escape(needle), haystack)
#     return res.start() if res else -1
#
#
# print(strStr("sadbutsad", "sad"))   # -> 0
# print(strStr("leetcode", "leeto"))  # -> -1


# 4) МОЙ ВАРИАНТ
# Сложность:
# Время: зависит от needle как regex (может быть очень плохо, вплоть до экспоненциального)
# Память: зависит от regex (обычно O(1) для простых случаев)

# def strStr(haystack, needle):
#     """
#     :type haystack: str
#     :type needle: str
#     :rtype: int
#     """
#     import re
#     res = re.search(rf'{needle}', haystack)
#     return res.start() if res else -1
#
#
# print(strStr("sadbutsad", "sad"))   # -> 0
# print(strStr("leetcode", "leeto"))  # -> -1




# ### TODO 151. Reverse Words in a String
# Задача: дана строка s. Нужно развернуть порядок слов.
#
# Слово — последовательность НЕ-пробельных символов.
# Во входе могут быть ведущие/хвостовые пробелы и несколько пробелов между словами.
# В результате:
# - слова в обратном порядке
# - между словами ровно один пробел
# - без пробелов по краям
#
# Example 1:
# Input:  "the sky is blue"
# Output: "blue is sky the"
#
# Example 2:
# Input:  "  hello world  "
# Output: "world hello"
#
# Example 3:
# Input:  "a good   example"
# Output: "example good a"
#
# Паттерн: String / Two Pointers


# ============================================================
# 1) Вариант "лучший для собеседования" (Python): split + reverse + join
#
# Идея:
# split() без аргументов сам:
# - убирает ведущие/хвостовые пробелы
# - сжимает множественные пробелы
# - возвращает список слов
# Далее разворачиваем и соединяем одним пробелом.
#
# Сложность:
# Время: O(n)
# Память: O(n)

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return " ".join(s.split()[::-1])


# # # ### TODO РЕШИТЬ!
# def reverseWords(self, s: str) -> str:




# ============================================================
# 2) Альтернатива без split: ручной разбор справа налево
#
# Идея:
# Идём с конца строки:
# - пропускаем пробелы
# - находим границы слова [j+1 .. i]
# - добавляем слово в результат
# В конце соединяем слова одним пробелом.
#
# Сложность:
# Время: O(n)
# Память: O(n)

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         res = []
#         i = len(s) - 1
#
#         while i >= 0:
#             # пропускаем пробелы
#             while i >= 0 and s[i] == " ":
#                 i -= 1
#             if i < 0:
#                 break
#
#             # ищем начало слова
#             j = i
#             while j >= 0 and s[j] != " ":
#                 j -= 1
#
#             res.append(s[j + 1:i + 1])
#             i = j - 1
#
#         return " ".join(res)




# ### TODO 14. Longest Common Prefix
# Задача: дан массив строк strs. Нужно найти самый длинный общий префикс
# (одинаковое начало) для всех строк. Если общего префикса нет — вернуть "".
#
# Example 1:
# Input:  strs = ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
# Input:  strs = ["dog","racecar","car"]
# Output: ""
#
# Паттерн: String / Prefix / Iteration


# ============================================================
# 1) Горизонтальное сравнение (самое популярное)
#
# Идея:
# Берём prefix = первая строка.
# Для каждой следующей строки s:
# - пока s не начинается с prefix, укорачиваем prefix на 1 символ справа
# - если prefix стал пустым, значит общего префикса нет -> ""
#
# Плюсы:
# - очень простое и “интервью-дружелюбное”
# Минусы:
# - в худшем может много раз обрезать prefix (но всё равно O(n * L))
#
# Сложность:
# Время: O(n * L), где L — длина общего префикса/длины строк (в худшем)
# Память: O(1)

# from typing import List
#
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#
#         prefix = strs[0]
#         for s in strs[1:]:
#             while not s.startswith(prefix):
#                 prefix = prefix[:-1]
#                 if prefix == "":
#                     return ""
#         return prefix


# # ### TODO РЕШИТЬ!
# def longestCommonPrefix(self, strs: List[str]) -> str:



# ============================================================
# 2) Посимвольное сравнение (чёткая логика)
#
# Идея:
# Находим самую короткую строку (дальше неё префикса быть не может).
# Идём по её символам i:
# - сравниваем этот символ со всеми строками
# - при первом несовпадении возвращаем shortest[:i]
#
# Сложность:
# Время: O(n * L)
# Память: O(1)

# from typing import List
#
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#
#         short = min(strs, key=len)
#         for i, ch in enumerate(short):
#             for s in strs:
#                 if s[i] != ch:
#                     return short[:i]
#         return short


# ============================================================
# 3) Через сортировку: сравниваем первую и последнюю (коротко и красиво)
#
# Идея:
# Если отсортировать строки лексикографически, то общий префикс всех строк
# обязательно будет общим префиксом у первой и последней строки в отсортированном списке
# (они максимально “разные” среди всех по порядку).
#
# Шаги:
# - сортируем (лучше через sorted, чтобы не менять вход)
# - берём a = first, b = last
# - считаем общий префикс у a и b
#
# Сложность:
# Время: O(n log n * K) из-за сортировки и сравнений строк (K ~ средняя длина)
# Память: O(n) (если делаем sorted(strs))

### МЕНЯЕМ ВХОДНОЙ СПИСОК!                                         ### НЕ МЕНЯЕТ ВХОДНОЙ СПИСОК!
# def longestCommonPrefix(strs):                                   def longestCommonPrefix(strs):
#     """                                                              """
#     :type strs: List[str]                                            :type strs: List[str]
#     :rtype: str                                                      :rtype: str
#     """                                                              """
#     if not strs:                                                     if not strs:
#         return ""                                                        return ""
#
#     strs.sort()                                                      s = sorted(strs)
#     a, b = strs[0], strs[-1]                                         a, b = s[0], s[-1]
#
#     i = 0                                                            i = 0
#     while i < len(a) and i < len(b) and a[i] == b[i]:                while i < len(a) and i < len(b) and a[i] == b[i]:
#         i += 1                                                           i += 1
#     return a[:i]                                                     return a[:i]
#
# print(longestCommonPrefix(["dog","racecar","car"])) # -> fl      print(longestCommonPrefix(["dog","racecar","car"])) # -> fl



# ### TODO 58. Length of Last Word
# Задача: дана строка s из слов и пробелов.
# Нужно вернуть длину последнего слова.
# Слово — максимальная подстрока из НЕ-пробельных символов.
#
# Example 1:
# Input: s = "Hello World"
# Output: 5
#
# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
#
# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
#
# Паттерн: String / Two Pointers


# ============================================================
# 1) Вариант "лучший для собеседования": проход с конца (O(n) время, O(1) память)
#
# Идея:
# - пропускаем пробелы в конце
# - считаем длину до следующего пробела или начала строки
#
# Сложность:
# Время: O(n)
# Память: O(1)

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         i = len(s) - 1
#
#         # пропускаем хвостовые пробелы
#         while i >= 0 and s[i] == ' ':
#             i -= 1
#
#         # считаем длину последнего слова
#         length = 0
#         while i >= 0 and s[i] != ' ':
#             length += 1
#             i -= 1
#
#         return length


# ### TODO РЕШИТЬ!
# def lengthOfLastWord(self, s: str) -> int:




# ============================================================
# 2) Вариант "простой": split (O(n) время, O(n) память)
#
# Идея:
# - разбиваем строку по пробелам (split сам игнорирует лишние пробелы)
# - берём последнее слово и его длину
#
# Сложность:
# Время: O(n)
# Память: O(n)

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         parts = s.split()
#         return len(parts[-1]) if parts else 0



# ============================================================
# 3) МОЙ ВАРИАНТ по ПАМЯТИ ХУЖЕ!

# Сложность
# Время: O(n)
# Память: O(n) (так как split() создаёт список слов)

# def lengthOfLastWord(s: str) -> int:
#     return len(s.strip().split()[-1])
#
#
# print(lengthOfLastWord("Hello World",))                  # -> 5
# print(lengthOfLastWord("   fly me   to   the moon  ",))  # -> 4
# print(lengthOfLastWord("luffy is still joyboy",))        # -> 6





# ### TODO 12. Integer to Roman
# Задача: дано целое num (1..3999), нужно перевести в римскую запись.
#
# Римские символы:
# I=1, V=5, X=10, L=50, C=100, D=500, M=1000
# Вычитательные формы:
# IV(4), IX(9), XL(40), XC(90), CD(400), CM(900)
#
# Example 1:
# Input: num = 3749
# Output: "MMMDCCXLIX"
#
# Example 2:
# Input: num = 58
# Output: "LVIII"
#
# Example 3:
# Input: num = 1994
# Output: "MCMXCIV"
#
# Паттерн: Greedy / Mapping



# ============================================================
# 2) Вариант "простой": по разрядам (тысячи/сотни/десятки/единицы)
#
# Идея:
# Предзаготовленные строки для каждого разряда:
# - thousands[0..3]
# - hundreds[0..9]
# - tens[0..9]
# - ones[0..9]
# Потом просто склеиваем.
#
# Сложность:
# Время: O(1)
# Память: O(1)

# class Solution:
#     def intToRoman(self, num: int) -> str:
#         thousands = ["", "M", "MM", "MMM"]
#         hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
#         tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
#         ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
#
#         return (
#             thousands[num // 1000] +
#             hundreds[(num % 1000) // 100] +
#             tens[(num % 100) // 10] +
#             ones[num % 10]
#         )



# ### TODO РЕШИТЬ!  Пустая строка "" - это вариант для цифры 0, чтобы arr[digit] работал без if.
# def intToRoman(self, num: int) -> str:





# ============================================================
# 1) Вариант "лучший для собеседования": жадный по таблице значений (O(1) по факту)
#
# Идея:
# Держим пары (value, symbol) в порядке убывания, включая вычитательные формы.
# Пока num >= value, добавляем symbol и уменьшаем num.
#
# Сложность:
# Время: O(кол-во символов в ответе) ~ O(1)
# Память: O(1)

# class Solution:
#     def intToRoman(self, num: int) -> str:
#         pairs = [
#             (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
#             (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
#             (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
#         ]
#
#         res = []
#         for val, sym in pairs:
#             if num == 0:
#                 break
#             cnt, num = divmod(num, val)
#             if cnt:
#                 res.append(sym * cnt)
#         return "".join(res)




# ### TODO 13. Roman to Integer
# Задача: дана строка s — римское число.
# Нужно преобразовать в целое.
#
# Правило:
# Обычно символы идут по убыванию и складываются.
# Но есть пары "вычитания":
# IV(4), IX(9), XL(40), XC(90), CD(400), CM(900)
#
# Example 1:
# Input: s = "III"
# Output: 3
#
# Example 2:
# Input: s = "LVIII"
# Output: 58
#
# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
#
# Паттерн: String / HashMap


# ============================================================
# 2) Вариант "простой": идти справа налево (O(n), O(1))
#
# Идея:
# Идём с конца, держим previous (значение справа).
# - если текущий < previous -> вычитаем
# - иначе -> прибавляем и обновляем previous
#
# Сложность:
# Время: O(n)
# Память: O(1)

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         res = {
#             'I': 1, 'V': 5, 'X': 10, 'L': 50,
#             'C': 100, 'D': 500, 'M': 1000
#         }
#
#         total = 0
#         prev = 0
#         for i in reversed(s):
#             val = res[i]
#             if val < prev:
#                 total -= val
#             else:
#                 total += val
#             prev = val
#         return total


# ### TODO РЕШИТЬ!
# def romanToInt(self, s: str) -> int:




# ============================================================
# 1) Вариант "лучший для собеседования": один проход слева направо (O(n), O(1))
#
# Идея:
# Смотрим текущий символ и следующий:
# - если value[i] < value[i+1], значит это случай вычитания -> вычитаем
# - иначе -> прибавляем
#
# Сложность:
# Время: O(n)
# Память: O(1)

# ### 2) проход слева направо (по индексу)
# Сложность:
# Время: O(n)
# Память: O(1)

# def romanToInt(s):
#     a = {
#         'I': 1, 'V': 5, 'X': 10, 'L': 50,
#         'C': 100, 'D': 500, 'M': 1000
#     }
#
#     total = 0
#     for i in range(len(s)):
#         val = a[s[i]]
#         # если справа есть символ и он больше — значит это вычитание
#         if i + 1 < len(s) and val < a[s[i + 1]]:
#             total -= val
#         else:
#             total += val
#
#     return total
#
#
# print(romanToInt("III"))       # -> 3
# print(romanToInt("LVIII"))     # -> 58
# print(romanToInt("MCMXCIV"))   # -> 1994







# ### TODO 42. Trapping Rain Water
# Задача: дан массив height — высоты столбиков (ширина каждого = 1).
# Нужно посчитать, сколько воды “запрётся” после дождя.
#
# Example 1:
# Input:  [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
#
# Example 2:
# Input:  [4,2,0,3,2,5]
# Output: 9
#
# Паттерн: Two Pointers / Prefix Max


# ============================================================
# 1) Вариант "лучший для собеседования": two pointers (O(n) время, O(1) память)
#
# Идея:
# Держим два указателя l и r, а также max слева и max справа:
# left_max = max(height[0..l]), right_max = max(height[r..n-1])
#
# Всегда двигаем сторону с меньшим max:
# - если left_max <= right_max, то вода на l зависит только от left_max:
#   water += left_max - height[l] (если >0), затем l++
# - иначе симметрично для r.
#
# Сложность:
# Время: O(n)
# Память: O(1)


# class Solution:
#     def trap(self, height: list[int]) -> int:
#         n = len(height)
#         if n == 0:
#             return 0
#
#         l, r = 0, n - 1
#         left_max, right_max = 0, 0
#         water = 0
#
#         while l < r:
#             if height[l] <= height[r]:
#                 if height[l] >= left_max:
#                     left_max = height[l]
#                 else:
#                     water += left_max - height[l]
#                 l += 1
#             else:
#                 if height[r] >= right_max:
#                     right_max = height[r]
#                 else:
#                     water += right_max - height[r]
#                 r -= 1
#
#         return water


# ### TODO РЕШИТЬ!
# def trap(self, height: list[int]) -> int:





# ============================================================
# 2) Вариант "простой": префикс/суффикс максимумы (O(n) время, O(n) память)
#
# Идея:
# Для каждой позиции i вода = min(max_left[i], max_right[i]) - height[i], если положительно.
# - max_left[i] = максимум слева до i (включительно)
# - max_right[i] = максимум справа от i (включительно)
#
# Сложность:
# Время: O(n)
# Память: O(n)


# class Solution:
#     def trap(self, height: list[int]) -> int:
#         n = len(height)
#         if n == 0:
#             return 0
#
#         max_left = [0] * n
#         max_right = [0] * n
#
#         max_left[0] = height[0]
#         for i in range(1, n):
#             max_left[i] = max(max_left[i - 1], height[i])
#
#         max_right[n - 1] = height[n - 1]
#         for i in range(n - 2, -1, -1):
#             max_right[i] = max(max_right[i + 1], height[i])
#
#         water = 0
#         for i in range(n):
#             level = min(max_left[i], max_right[i])
#             if level > height[i]:
#                 water += level - height[i]
#
#         return water




# ### TODO 135. Candy
# Задача: есть n детей в ряд, ratings[i] — рейтинг.
# Нужно раздать конфеты так, чтобы:
# 1) каждый получил хотя бы 1
# 2) если rating выше соседа, то конфет строго больше, чем у соседа
# Вернуть минимальное общее число конфет.
#
# Example 1:
# Input: ratings = [1,0,2]
# Output: 5
#
# Example 2:
# Input: ratings = [1,2,2]
# Output: 4
#
# Паттерн: Greedy / Two Pass / Slopes


# ============================================================
# 1) Вариант "лучший для собеседования": 2 прохода (O(n) время, O(n) память)
#
# Идея:
# - всем по 1
# - слева направо: если ratings[i] > ratings[i-1], то candies[i] = candies[i-1] + 1
# - справа налево: если ratings[i] > ratings[i+1], то candies[i] = max(candies[i], candies[i+1] + 1)
# - ответ = sum(candies)
#
# Сложность:
# Время: O(n)
# Память: O(n)


# class Solution:
#     def candy(self, ratings: list[int]) -> int:
#         n = len(ratings)
#         if n == 0:
#             return 0
#
#         candies = [1] * n
#
#         for i in range(1, n):
#             if ratings[i] > ratings[i - 1]:
#                 candies[i] = candies[i - 1] + 1
#
#         for i in range(n - 2, -1, -1):
#             if ratings[i] > ratings[i + 1]:
#                 candies[i] = max(candies[i], candies[i + 1] + 1)
#
#         return sum(candies)


# ### TODO РЕШИТЬ!
# def candy(self, ratings: list[int]) -> int:



# ============================================================
# 2) Вариант "усиленный": O(1) память через подсчёт "подъёмов" и "спусков"
#
# Идея (slope approach):
# Рассматриваем изменения рейтингов как последовательность:
# - up: ratings[i] > ratings[i-1]
# - down: ratings[i] < ratings[i-1]
# - flat: равны
#
# Идём слева направо, считаем длину текущего подъёма (up) и спуска (down).
# Для каждой позиции добавляем конфеты как в треугольниках:
# - при подъёме: растёт up -> добавляем 1 + up
# - при спуске: растёт down -> добавляем 1 + down
# - но "пик" должен иметь конфет больше, чем обе стороны,
#   поэтому когда down > up, добавляем ещё 1 (компенсация пика).
#
# Это даёт минимальную сумму без массива candies.
#
# Сложность:
# Время: O(n)
# Память: O(1)


# class Solution:
#     def candy(self, ratings: list[int]) -> int:
#         n = len(ratings)
#         if n == 0:
#             return 0
#
#         total = 1          # первый ребёнок
#         up = 0             # длина текущего подъёма
#         down = 0           # длина текущего спуска
#         peak = 0           # длина последнего подъёма (высота пика)
#
#         for i in range(1, n):
#             if ratings[i] > ratings[i - 1]:
#                 up += 1
#                 peak = up
#                 down = 0
#                 total += 1 + up
#             elif ratings[i] == ratings[i - 1]:
#                 up = down = peak = 0
#                 total += 1
#             else:  # ratings[i] < ratings[i - 1]
#                 down += 1
#                 up = 0
#                 total += 1 + down
#                 # если спуск длиннее подъёма, пику не хватает 1 конфеты
#                 if down > peak:
#                     total += 1
#
#         return total



# ### TODO 134. Gas Station
# Задача: есть n заправок по кругу.
# gas[i] — сколько бензина можно взять на i-й,
# cost[i] — сколько нужно бензина, чтобы доехать с i-й до (i+1)-й.
# Стартуем с пустым баком на одной из заправок.
# Нужно вернуть индекс старта, если можно проехать полный круг, иначе -1.
# Если решение есть — оно единственное.
#
# Паттерн: Greedy / Prefix sum


# ============================================================
# Вариант "лучший для собеседования": жадный O(n)
#
# Ключевые идеи:
# 1) Если суммарно бензина меньше, чем суммарная стоимость, решения нет.
#    (total_gas - total_cost < 0 -> -1)
# 2) Если при движении от candidate_start текущий баланс tank стал < 0,
#    значит стартовать из candidate_start и из любой станции между ним и текущей
#    (включительно) тоже бессмысленно. Тогда новый старт = i + 1,
#    и tank сбрасываем в 0.
#
# Сложность:
# Время: O(n)
# Память: O(1)


# class Solution:
#     def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
#         total = 0      # суммарный баланс по кругу
#         tank = 0       # баланс на текущем отрезке от start
#         start = 0      # кандидат на старт
#
#         for i in range(len(gas)):
#             diff = gas[i] - cost[i]
#             total += diff
#             tank += diff
#
#             # если "не дотянули" до следующей станции, с текущего start не выйдет
#             if tank < 0:
#                 start = i + 1
#                 tank = 0
#
#         return start if total >= 0 else -1


# ### TODO РЕШИТЬ!
# def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:




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


# ### TODO РЕШИТЬ!
# def productExceptSelf(nums: list[int]) -> list[int]:




# ### TODO 380. Insert Delete GetRandom O(1)
# Реализовать структуру RandomizedSet:
# - insert(val): добавить, если нет (avg O(1))
# - remove(val): удалить, если есть (avg O(1))
# - getRandom(): вернуть случайный элемент с равной вероятностью (avg O(1))
#
# Паттерн: Array + HashMap
#
# Идея:
# Держим:
# 1) массив self.arr со значениями
# 2) словарь self.pos: value -> index в массиве
#
# insert:
# - если val уже в pos -> False
# - иначе дописываем в arr, pos[val] = последний индекс -> True
#
# remove:
# - если val нет -> False
# - иначе:
#   idx = pos[val]
#   last = arr[-1]
#   ставим last на место idx (swap-with-last)
#   обновляем pos[last] = idx
#   pop() последний
#   удаляем pos[val]
#
# getRandom:
# - random.choice(arr)
#
# Сложность:
# insert/remove/getRandom: avg O(1)
# память: O(n)

# import random
# from typing import List
#
# class RandomizedSet:
#
#     def __init__(self):
#         self.arr: List[int] = []
#         self.pos = {}  # val -> index in arr
#
#     def insert(self, val: int) -> bool:
#         if val in self.pos:
#             return False
#         self.pos[val] = len(self.arr)
#         self.arr.append(val)
#         return True
#
#     def remove(self, val: int) -> bool:
#         if val not in self.pos:
#             return False
#
#         idx = self.pos[val]
#         last_val = self.arr[-1]
#
#         # переносим последний элемент на место удаляемого
#         self.arr[idx] = last_val
#         self.pos[last_val] = idx
#
#         # удаляем хвост
#         self.arr.pop()
#         del self.pos[val]
#         return True
#
#     def getRandom(self) -> int:
#         return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()



# ### TODO 274. H-Index
# Задача: дан массив citations, где citations[i] — число цитирований i-й статьи.
# Нужно вернуть h-index исследователя.
#
# Определение:
# h-index — максимальное h такое, что есть как минимум h статей,
# каждая из которых процитирована как минимум h раз.

# Мини-шпаргалка для собеса:
# “Базово решаю сортировкой O(n log n). Если нужна линейная сложность — делаю bucket counting, потому что h не больше n.”
#
# Example 1:
# Input: citations = [3,0,6,1,5]
# Output: 3
#
# Example 2:
# Input: citations = [1,3,1]
# Output: 1
#
# Паттерн: Array / Sorting / Counting



# ============================================================
# 2) Вариант "простой": сортировка (O(n log n) время, O(1) доп. память*)
#
# Идея:
# Сортируем по убыванию.
# Для позиции i (1..n) проверяем: citations[i-1] >= i?
# Максимальное i, которое проходит, и есть h-index.
#
# Сложность:
# Время: O(n log n)
# Память: зависит от реализации sort в Python (Timsort), обычно O(n) в худшем.
# (*доп. память вне входа может использоваться сортировкой)

# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         citations.sort(reverse=True)
#         h = 0
#         for i, v in enumerate(citations, start=1):
#             if v >= i:
#                 h = i
#             else:
#                 break
#         return h


### TODO РЕШИТЬ!
# def hIndex(self, citations: List[int]) -> int:




# ============================================================
# 1) Вариант "лучший для собеседования": counting (O(n) время, O(n) память)
#
# Идея:
# h не может быть больше n (кол-ва статей).
# Считаем частоты цитирований, но все значения > n кладём в "n".
# Затем идём с конца: сколько статей имеют >= i цитирований?
# На первом i, где count_ge >= i, это и есть ответ.
#
# Сложность:
# Время: O(n)
# Память: O(n)

# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         n = len(citations)
#         buckets = [0] * (n + 1)
#
#         for c in citations:
#             if c >= n:
#                 buckets[n] += 1
#             else:
#                 buckets[c] += 1
#
#         papers_ge = 0  # сколько статей с цитированиями >= текущего i
#         for i in range(n, -1, -1):
#             papers_ge += buckets[i]
#             if papers_ge >= i:
#                 return i
#         return 0







# ### TODO 45. Jump Game II
# Задача: дан массив nums, где nums[i] — максимальная длина прыжка из позиции i.
# Стартуем с 0. Нужно вернуть минимальное число прыжков, чтобы дойти до n-1.
# Гарантируется, что до конца дойти можно.
#
# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2
#
# Example 2:
# Input: nums = [2,3,0,1,4]
# Output: 2
#
# Паттерн: Greedy / BFS by levels (range expansion)


# ============================================================
# 1) Вариант "лучший для собеседования": greedy (как BFS по уровням)
#
# Идея:
# - Смотрим на прыжки как на уровни BFS:
#   текущий "слой" = диапазон индексов [0..end], до которых можно дойти за jumps прыжков.
# - Идём по индексам и считаем farthest = максимум (i + nums[i]) внутри слоя.
# - Когда дошли до end, значит слой закончился -> делаем jumps += 1 и end = farthest.
# - Как только end >= last_index — можно возвращать jumps.
#
# Сложность:
# Время: O(n)
# Память: O(1)

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n <= 1:
#             return 0
#
#         jumps = 0
#         end = 0        # граница текущего слоя
#         farthest = 0   # самая дальняя достижимая позиция в следующем слое
#
#         for i in range(n - 1):  # до последнего идти не нужно
#             farthest = max(farthest, i + nums[i])
#
#             if i == end:        # закончили текущий слой
#                 jumps += 1
#                 end = farthest
#                 if end >= n - 1:
#                     break
#
#         return jumps



### TODO РЕШИТЬ!
# def jump(self, nums: List[int]) -> int:




# ### TODO 55. Jump Game
# Задача: дан массив nums, где nums[i] — максимальная длина прыжка из позиции i.
# Стартуем с индекса 0. Нужно понять, можно ли добраться до последнего индекса.
#
# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
#
# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
#
# Паттерн: Greedy / One Pass


# ============================================================
# 1) Вариант "лучший для собеседования": greedy — дальность reachable
#
# Идея:
# - Держим farthest — самый дальний индекс, до которого можно добраться.
# - Идём слева направо:
#   если i > farthest, значит мы не можем попасть на i => False.
#   иначе обновляем farthest = max(farthest, i + nums[i]).
# - Если farthest >= last_index => True.
#
# Сложность:
# Время: O(n)
# Память: O(1)

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         farthest = 0
#         last = len(nums) - 1
#
#         for i, jump in enumerate(nums):
#             if i > farthest:
#                 return False
#             farthest = max(farthest, i + jump)
#             if farthest >= last:
#                 return True
#
#         return True


### TODO РЕШИТЬ!
# def canJump(self, nums: List[int]) -> bool:





# ### TODO 122. Best Time to Buy and Sell Stock II
# Задача: дан массив prices, где prices[i] — цена акции в i-й день.
# Можно совершать сколько угодно сделок (покупка/продажа), но держать можно максимум 1 акцию.
# Нужно вернуть максимальную прибыль.
#
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
#
# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
#
# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
#
# Паттерн: Greedy / One Pass


# ============================================================
# 1) Вариант "лучший для собеседования": greedy — суммируем все росты
#
# Идея:
# - Если цена растёт с дня i-1 на день i, то этот рост можно "забрать" в прибыль.
# - Эквивалентно покупке в начале каждого роста и продаже в конце,
#   но проще: добавлять все положительные разницы.
#
# Сложность:
# Время: O(n)
# Память: O(1)

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         for i in range(1, len(prices)):
#             if prices[i] > prices[i - 1]:
#                 profit += prices[i] - prices[i - 1]
#         return profit


### TODO РЕШИТЬ!
# def maxProfit(self, prices: List[int]) -> int:






# ### TODO 121. Best Time to Buy and Sell Stock
# Задача: дан массив prices, где prices[i] — цена акции в i-й день.
# Нужно выбрать один день для покупки и более поздний день для продажи,
# чтобы максимизировать прибыль. Если прибыли нет — вернуть 0.
#
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5  (купить за 1, продать за 6)
#
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
#
# Паттерн: One Pass / Sliding Window (min so far)


# ============================================================
# 1) Вариант "лучший для собеседования": один проход, минимум слева
#
# Идея:
# - держим min_price — минимальную цену, которую видели слева (день покупки)
# - на каждом дне считаем profit = price - min_price и обновляем max_profit
# - обновляем min_price = min(min_price, price)
#
# Сложность:
# Время: O(n)
# Память: O(1)

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_price = float("inf")
#         max_profit = 0
#
#         for price in prices:
#             if price < min_price:
#                 min_price = price
#             else:
#                 max_profit = max(max_profit, price - min_price)
#
#         return max_profit



### TODO РЕШИТЬ!
# def maxProfit(self, prices: List[int]) -> int:






# ### TODO 189. Rotate Array
# Задача: дан массив nums и число k.
# Нужно повернуть массив вправо на k шагов (k >= 0) in-place.
#
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
#
# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
#
# Паттерн: Array / Reverse / Deque


# ============================================================
# 1) Вариант "лучший для собеседования": 3 разворота (O(1) память)
#
# Идея:
# - k %= n
# - reverse(всё), reverse(первые k), reverse(остаток)
#
# Сложность:
# Время: O(n)
# Память: O(1)

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         n = len(nums)
#         if n == 0:
#             return
#         k %= n
#         if k == 0:
#             return
#
#         def rev(l, r):
#             while l < r:
#                 nums[l], nums[r] = nums[r], nums[l]
#                 l += 1
#                 r -= 1
#
#         rev(0, n - 1)
#         rev(0, k - 1)
#         rev(k, n - 1)



### TODO РЕШИТЬ!
# def rotate(self, nums: List[int], k: int) -> None:





# ============================================================
# 2) Вариант "простой": через deque.rotate (O(n) память)
#
# Идея:
# - превращаем nums в deque
# - делаем rotate(k)
# - копируем обратно в nums через nums[:]
#
# Сложность:
# Время: O(n)
# Память: O(n)

# from collections import deque
#
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         d = deque(nums)
#         d.rotate(k)
#         nums[:] = d




# ### TODO 169. Majority Element
# Задача: дан массив nums длины n.
# Нужно найти majority element — элемент, который встречается строго больше floor(n/2) раз.
# Гарантируется, что такой элемент существует.
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
#
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
# Паттерн: Boyer-Moore Voting / HashMap


# ============================================================
# 1) Вариант "лучший для собеседования": Boyer–Moore Voting Algorithm
#
# Идея:
# - Держим candidate и count.
# - Если count == 0 -> назначаем текущий элемент кандидатом.
# - Если элемент равен candidate -> count += 1, иначе count -= 1.
# - Интуиция: пары разных элементов "уничтожают" друг друга, majority выживает.
# - Так как majority гарантирован, в конце candidate и есть ответ.
#
# Сложность:
# Время: O(n)
# Память: O(1)

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         candidate = None
#         count = 0
#
#         for i in nums:
#             if count == 0:
#                 candidate = i
#                 count = 1
#             elif i == candidate:
#                 count += 1
#             else:
#                 count -= 1
#
#         return candidate



### TODO РЕШИТЬ!
# def majorityElement(self, nums: List[int]) -> int:




# ============================================================
# 2) Вариант "простой": HashMap (частоты)
#
# Идея:
# - считаем частоты и возвращаем элемент с частотой > n//2
#
# Сложность:
# Время: O(n)
# Память: O(n)

# from collections import Counter
#
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         need = len(nums) // 2
#         cnt = Counter(nums)
#         for x, f in cnt.items():
#             if f > need:
#                 return x




# ### TODO 80. Remove Duplicates from Sorted Array II
# Задача: дан отсортированный массив nums (неубывающий).
# Нужно удалить дубликаты in-place так, чтобы каждый уникальный элемент встречался НЕ БОЛЕЕ 2 раз.
# Порядок сохраняется. Вернуть k — длину результирующей части.
# Первые k элементов nums должны содержать ответ.
#
# Example 1:
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
#
# Example 2:
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
#
# Паттерн: Two Pointers / In-place


# ============================================================
# 1) Вариант "лучший для собеседования": write pointer + проверка nums[write-2]
#
# Идея:
# - Можно оставлять элемент nums[i], если:
#   * мы записали меньше 2 элементов (write < 2)  -> всегда можно
#   * или текущий nums[i] НЕ равен nums[write-2]
#     (тогда в итоговом массиве этот элемент встретится максимум 2 раза)
#
# Почему работает:
# - Массив отсортирован, значит одинаковые значения идут подряд.
# - Если nums[i] == nums[write-2], то этот элемент уже два раза стоит в результате
#   (на позициях write-2 и write-1), третий раз пропускаем.
#
# Сложность:
# Время: O(n)
# Память: O(1)

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         write = 0
#         for i in nums:
#             if write < 2 or i != nums[write - 2]:
#                 nums[write] = i
#                 write += 1
#         return write


### TODO РЕШИТЬ!
# def removeDuplicates(self, nums: List[int]) -> int:





# ============================================================
# 2) Вариант "универсальный": считать сколько раз подряд встретили текущее число
#
# Идея:
# - Идём слева направо, держим count (сколько раз подряд текущее число уже записали).
# - Если новое число -> count = 1 и записываем.
# - Если то же самое и count < 2 -> записываем и count += 1, иначе пропускаем.
#
# Сложность:
# Время: O(n)
# Память: O(1)

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#
#         write = 1
#         count = 1
#
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]:
#                 if count < 2:
#                     nums[write] = nums[i]
#                     write += 1
#                 count += 1
#             else:
#                 count = 1
#                 nums[write] = nums[i]
#                 write += 1
#
#         return write





# ### TODO 26. Remove Duplicates from Sorted Array
# Задача: дан отсортированный массив nums (неубывающий).
# Нужно удалить дубликаты in-place так, чтобы каждый уникальный элемент встречался один раз,
# при этом относительный порядок сохраняется.
# Вернуть k — количество уникальных элементов.
# Первые k элементов nums должны быть уникальными и отсортированными.
#
# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
#
# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
#
# Паттерн: Two Pointers / In-place



# ============================================================
# 1) Вариант "тоже хороший для собеседования": for x in nums (write pointer) (O(n), O(1))
#
# Идея:
# Тот же write pointer, но идём не по индексам, а по значениям.
# - если write == 0 -> пишем первый элемент
# - иначе пишем x, только если он отличается от последнего записанного nums[write-1]
#
# Сложность:
# Время: O(n)
# Память: O(1)

# from typing import List
#
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         write = 0
#         for i in nums:
#             if write == 0 or i != nums[write - 1]:
#                 nums[write] = i
#                 write += 1
#         return write



### TODO РЕШИТЬ!
# def removeDuplicates(self, nums: List[int]) -> int:




# ============================================================
# 1) Вариант "лучший для собеседования": slow/fast pointers (write pointer)
#
# Идея:
# - Так как массив отсортирован, все дубликаты стоят рядом.
# - write — позиция, куда записываем следующий уникальный элемент.
# - Идём указателем i с 1 до конца:
#   если nums[i] != nums[write-1], значит нашли новый уникальный — пишем nums[write] = nums[i], write += 1
# - Ответ: write
#
# Сложность:
# Время: O(n)
# Память: O(1)

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#
#         write = 1
#         for i in range(1, len(nums)):
#             if nums[i] != nums[write - 1]:
#                 nums[write] = nums[i]
#                 write += 1
#
#         return write




# ============================================================
# 2) Вариант "короче" (но использует доп. память): через set/уникализацию
# Не рекомендуется для интервью, т.к. нужно in-place и без доп. памяти.
#
# Сложность:
# Время: O(n)
# Память: O(n)

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         uniq = sorted(set(nums))
#         nums[:len(uniq)] = uniq
#         return len(uniq)





# ### TODO 27. Remove Element
# Задача: дан массив nums и число val.
# Нужно удалить все вхождения val in-place. Порядок может меняться.
# Вернуть k — количество элементов != val, и первые k элементов nums должны быть != val.
#
# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
#
# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
#
# Паттерн: Two Pointers / In-place






# ============================================================
# 2) Если порядок нужно сохранять (на всякий случай): slow/fast (write pointer)
#
# Идея:
# - write — куда записывать следующий "хороший" элемент (!= val)
# - проходим все элементы, и каждый неравный val записываем в nums[write]
#
# Сложность:
# Время: O(n)
# Память: O(1)

# def removeElement(nums, val):
#     write = 0
#     for i in nums:
#         if i != val:
#             nums[write] = i
#             write += 1
#     return write



### TODO РЕШИТЬ!
# def removeElement(nums, val):




# ============================================================
# 1) “Канонический” вариант (лучше для интервью): swap-with-end (порядок не важен)
#
# Идея:
# - i идёт по массиву, n — текущая "длина" живой части.
# - Если nums[i] == val: заменяем nums[i] последним элементом nums[n-1] и уменьшаем n.
#   i не двигаем, потому что на позицию i пришёл новый элемент — его нужно проверить.
# - Если nums[i] != val: i += 1
#
# Сложность:
# Время: O(n)
# Память: O(1)

# def removeElement(nums, val):
#     i = 0
#     n = len(nums)
#
#     while i < n:
#         if nums[i] == val:
#             nums[i] = nums[n - 1]
#             n -= 1
#         else:
#             i += 1
#
#     return n





# ============================================================
# 3) МОЙ вариант: через list comprehension (не in-place по сути)
#
# Идея:
# - создаём новый список без val и заменяем содержимое nums через nums[:]
# - удобно и коротко, но используется доп. память => не "идеал" для интервью
#
# Сложность:
# Время: O(n)
# Память: O(n)

# def removeElement(nums, val):
#     nums[:] = [x for x in nums if x != val]
#     return len(nums)
#
# print(removeElement([3,2,2,3], 3))          # -> 2
# print(removeElement([0,1,2,2,3,0,4,2], 2))  # -> 5




# ### TODO 88. Merge Sorted Array
# Задача: даны два отсортированных массива nums1 и nums2 (по неубыванию),
# а также числа m и n — сколько реальных элементов в nums1 и nums2.
# Нужно слить nums2 в nums1 так, чтобы итог был отсортирован, и сохранить результат В nums1 (in-place).
# nums1 имеет длину m + n: первые m — данные, последние n — "пустое место" (0), его игнорируем.
#
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
#
# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
#
# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
#
# Паттерн: Two Pointers / Merge (как в merge-sort)


# ============================================================
# 1) Вариант "лучший для собеседования": 3 указателя с конца (in-place)
#
# Идея:
# - Сливать с конца, чтобы не затирать ещё не использованные элементы nums1.
# - i = m-1 (последний реальный элемент nums1)
# - j = n-1 (последний элемент nums2)
# - k = m+n-1 (куда пишем в nums1)
# - На каждом шаге ставим в nums1[k] больший из nums1[i] и nums2[j].
# - Достаточно крутить цикл пока j >= 0 (если nums2 закончился — всё готово).
#
# Сложность:
# Время: O(m + n)
# Память: O(1)

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         i = m - 1
#         j = n - 1
#         k = m + n - 1
#
#         while j >= 0:
#             if i >= 0 and nums1[i] > nums2[j]:
#                 nums1[k] = nums1[i]
#                 i -= 1
#             else:
#                 nums1[k] = nums2[j]
#                 j -= 1
#             k -= 1


### TODO РЕШИТЬ!
# def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:







# ### TODO Math



# ### TODO 66. Plus One
# Задача: дано большое число в виде массива цифр digits (слева направо, без ведущих нулей).
# Нужно увеличить число на 1 и вернуть новый массив цифр.
#
# Example 1:
# digits = [1,2,3] -> [1,2,4]
#
# Example 2:
# digits = [4,3,2,1] -> [4,3,2,2]
#
# Example 3:
# digits = [9] -> [1,0]
#
# Паттерн: Carry (перенос разряда) / In-place
#
# ============================================================
# 1) Вариант "лучший для собеседования": справа налево, обнуляем 9-ки (O(n) время, O(1) память)
#
# Идея:
# Идём с конца массива (с младшего разряда):
# - если digits[i] < 9: увеличиваем digits[i] на 1 и сразу возвращаем (переноса дальше нет)
# - иначе (digits[i] == 9): ставим 0 и продолжаем влево, т.к. перенос = 1
#
# Если дошли до начала и все цифры были 9, то получаем число вида 999...9 + 1 = 1000...0,
# поэтому возвращаем [1] + digits (где digits уже превратился в [0,0,...,0]).
#
# Сложность:
# Время: O(n) (в худшем случае все цифры = 9)
# Память: O(1) дополнительная (новый список создаём только в случае, когда добавляем ведущую 1)

# from typing import List
#
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         for i in range(len(digits) - 1, -1, -1):
#             if digits[i] < 9:
#                 digits[i] += 1
#                 return digits
#             digits[i] = 0
#         return [1] + digits


### TODO РЕШИТЬ!
# def plusOne(self, digits: List[int]) -> List[int]:




# ### TODO 9. Palindrome Number
# Задача: дано целое число x. Нужно проверить, является ли оно палиндромом.
# Палинром читается одинаково слева направо и справа налево.
#
# Важно:
# - отрицательные числа не палиндромы (из-за '-')
# - числа, оканчивающиеся на 0, не палиндромы, кроме 0 (например 10 -> false)
#
# Example 1:
# Input: 121
# Output: True
#
# Example 2:
# Input: -121
# Output: False
#
# Example 3:
# Input: 10
# Output: False
#
# Паттерн: Math / Two Pointers idea (через разворот половины)


# ============================================================
# 1) Вариант "лучший для собеседования": разворачиваем половину числа (O(log10 x), O(1))
#
# Идея:
# Вместо разворота всего числа (риск переполнения в других языках),
# разворачиваем только вторую половину:
# - пока rev < x: переносим последнюю цифру x в rev
# - в конце сравниваем:
#   * x == rev (чётное число цифр)
#   * x == rev // 10 (нечётное число цифр, средняя цифра лишняя)
#
# Сложность:
# Время: O(log n)
# Память: O(1)

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         if x % 10 == 0 and x != 0:
#             return False
#
#         rev = 0
#         while rev < x:
#             rev = rev * 10 + x % 10
#             x //= 10
#
#         return x == rev or x == rev // 10


### TODO РЕШИТЬ!
# def isPalindrome(self, x: int) -> bool:



# ============================================================
# 2) Вариант "простой": через строку (O(n), O(n))
#
# Идея:
# - преобразуем в строку
# - сравниваем со строкой в обратном порядке
#
# Сложность:
# Время: O(n)
# Память: O(n)

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         s = str(x)
#         return s == s[::-1]












