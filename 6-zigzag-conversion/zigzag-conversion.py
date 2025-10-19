class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        rows=[]
        current_row=0
        going_down=True
        for i in range(numRows):
            rows.append([])

        for i in range(len(s)):#0 1 2 3 4 5 6 .. 14
            if going_down==True:
                rows[current_row].append(s[i])
                current_row += 1
            else:
                rows[current_row].append(s[i])
                current_row -= 1

            if current_row==0:
                going_down=True

            if current_row==numRows-1:
                going_down=False

        return "".join("".join(row) for row in rows)