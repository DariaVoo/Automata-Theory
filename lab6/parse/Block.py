class Block:
    def __init__(self, max_cols, max_rows):
        self.max_cols = max_cols
        self.max_rows = max_rows
        self.current_cols = 0
        self.current_rows = 0

    def check_condition_row(self):
        return self.current_rows > self.max_rows

    def check_condition_col(self):
        return self.current_cols > self.max_cols

    def add_rows_cols(self, tag: str):
        if tag == 'column':
            self.current_cols += 1
        elif tag == 'row':
            self.current_rows += 1

        if self.check_condition_row():
            return f'rows! Must be {self.max_rows}, Get: {self.current_rows}'
        elif self.check_condition_col():
            return f'columns! Must be {self.max_cols}, Get: {self.current_cols}'
        return False

    def check_new_rows_cols(self, row, col):
        if col > int(self.max_cols):
            return f'rows! Must be {self.max_rows}, Get: {self.current_rows}'
        elif row > int(self.max_rows):
            return f'columns! Must be {self.max_cols}, Get: {self.current_cols}'
        return False