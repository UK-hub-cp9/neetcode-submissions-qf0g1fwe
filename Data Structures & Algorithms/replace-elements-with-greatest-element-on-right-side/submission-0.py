class Solution:
    def replaceElements(self, arr):
        max_right = -1

        # traverse from right to left
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]      # save current value
            arr[i] = max_right    # replace with greatest on right
            max_right = max(max_right, current)

        return arr