# 旋转矩阵
"""
给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。
不占用额外内存空间能否做到？
给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
"""


# 使用辅助数组
class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        # Python 这里不能 matrix_new = matrix 或 matrix_new = matrix[:] 因为是引用拷贝
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                # 矩阵中的元素matrix[row][col]在旋转后，它的新位置为matrix_new[col][n−row−1]
                matrix_new[j][n - i - 1] = matrix[i][j]
        # 不能写成 matrix = matrix_new
        matrix[:] = matrix_new  # 浅复制


# 原地旋转
# class Solution:
#     def rotate(self, matrix):
#         n = len(matrix)
#         for i in range(n // 2):
#             for j in range((n + 1) // 2):
#                 matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
#                     = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]


# 反转代替旋转
# class Solution:
#     def rotate(self, matrix):
#         n = len(matrix)
#         # 水平翻转
#         for i in range(n // 2):
#             for j in range(n):
#                 matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
#         # 主对角线翻转
#         for i in range(n):
#             for j in range(i):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix)
    print(list(matrix))







