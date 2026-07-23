

class CustomException(Exception):
    def __init__(self, e):
        super().__init__(str(e))

        self.e = e
        self.tb = e.__traceback__

    def __str__(self):
        return (
            f"e occurred in file "
            f"{self.tb.tb_frame.f_code.co_filename} "
            f"at line {self.tb.tb_lineno}: {self.e}"
        )