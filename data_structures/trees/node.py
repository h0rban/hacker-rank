class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

    def __str__(self):
        left = self.left.info if self.left else 'null'
        right = self.right.info if self.right else 'null'
        return f'{self.info} -> {left}, {right}'

    # todo write my own __str__

    def level_order(self):
        out = []
        queue = [self]
        while queue:
            # print(out, [n.info for n in queue])
            node = queue.pop(0)
            out.append(node.info)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return out

    def display_aux(self):
        """
        Returns list of strings, width, height, and horizontal coordinate of the root.
        taken from: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
        """

        s = str(self.info)
        u = len(s)

        # No child.
        if not self.right and not self.left:
            line = str(self.info)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if not self.right:
            lines, n, p, x = self.left.display_aux()
            first_line = f'{" " * (x + 1)} {"_" * (n - x - 1)}{s}'
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if not self.left:
            lines, n, p, x = self.right.display_aux()
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left.display_aux()
        right, m, q, y = self.right.display_aux()

        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
