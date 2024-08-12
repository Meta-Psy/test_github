database = {}
class Worker:
    def __init__(self, name, job, status=False, worktime=0):
        self.name = name
        self.job = job
        database[name] = job
        self.status = status
        if job == "znahar'":
            self.worktime = 10
        elif job == "streamer":
            self.worktime = 5
    def work(self):
        if self.status == False:
            self.status = True
            print("работает")
        else:
            self.status = False
            print("закочил работу")
class Manager(Worker):
    def __init__(self, name, job, password, status=False):
        super().__init__(name, job, status)
        self.password = password
    def workers_info(self, password):
        if password == self.password:
            for k,v in database.items():
                print(f"Имя: {k}. Должность: {v}")
        else:
            print('нет доступа')
worker1 = Worker("Leha", "znahar'")
worker2 = Worker("Rakhshona", "streamer")
worker3 = Worker("Sardor", "kalyanshik")
manager1 = Manager("Botir", "main manager", "123")

worker1.work()
worker1.work()
manager1.workers_info("12")
manager1.workers_info("123")