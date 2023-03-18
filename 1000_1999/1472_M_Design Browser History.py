class BrowserHistory:

    def __init__(self, homepage: str):
        self.idx = 0
        self.visit_list = [homepage]

    def visit(self, url: str) -> None:
        self.visit_list = self.visit_list[:self.idx+1]
        self.visit_list.append(url)
        self.idx = len(self.visit_list) - 1

        # print(self.idx, self.visit_list)

    def back(self, steps: int) -> str:
        self.idx -= steps
        if self.idx < 0:
            self.idx = 0
        # print(self.idx, self.visit_list)
        return self.visit_list[self.idx]

    def forward(self, steps: int) -> str:
        self.idx += steps
        if self.idx >= len(self.visit_list):
            self.idx = len(self.visit_list) - 1
        # print(self.idx, self.visit_list)
        return self.visit_list[self.idx]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)