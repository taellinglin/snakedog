class BaseAnimation:
    def __init__(
        self, loop=float("Infinity"), func=lambda x: x, running=True, once=False
    ):
        self.clock = 0
        self.loop = loop
        self.func = func
        self.running = running
        self.once = once
        self.value = self.func(0)
        self.update()

    def update(self):
        if not self.running:
            return
        self.clock = (self.clock + 1) % self.loop
        if self.once and self.clock == 0:
            self.running = False
            return
        self.value = self.func(self.clock)
        return self.value

    def stop(self):
        self.running = False

    def start(self):
        self.running = True

    def reset(self, start=False):
        self.clock = 0
        if start:
            self.start()
