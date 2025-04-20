class Solution(object):
    def spiralOrder(self, A):
        if not A or not A[0]:
            return []

        top, bottom = 0, len(A) - 1
        left, right = 0, len(A[0]) - 1
        S = []

        while top <= bottom and left <= right:
            # Traverse from Left to Right
            for i in range(left, right + 1):
                S.append(A[top][i])
            top += 1

            # Traverse from Top to Bottom
            for i in range(top, bottom + 1):
                S.append(A[i][right])
            right -= 1

            # Traverse from Right to Left (if there's a row left)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    S.append(A[bottom][i])
                bottom -= 1

            # Traverse from Bottom to Top (if there's a column left)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    S.append(A[i][left])
                left += 1

        return S
