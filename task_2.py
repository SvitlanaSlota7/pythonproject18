class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []  # Список робітників

    @property
    def workers(self):
        """Гетер для отримання списку робітників."""
        return self._workers

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            if worker not in self._workers:
                self._workers.append(worker)
        else:
            raise ValueError("Додати до списку можна лише об'єкт класу Worker")

    def __repr__(self):
        return f"Boss(id={self.id}, name='{self.name}')"


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        # Використовуємо сетер для початкового призначення боса
        self.boss = boss

    @property
    def boss(self):
        """Гетер для отримання поточного боса."""
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        """Сетер для призначення нового боса """
        if isinstance(new_boss, Boss):
            self._boss = new_boss
            # Додаємо цього робітника до списку нового боса
            new_boss.add_worker(self)
        else:
            raise ValueError("Босом може бути лише об'єкт класу Boss")

    def __repr__(self):
        return f"Worker(id={self.id}, name='{self.name}')"

boss_1 = Boss(1, "Олександр", "Google")
boss_2 = Boss(2, "Марія", "Apple")

# призначаємо boss_1
worker_1 = Worker(101, "Іван", "Google", boss_1)

print(f"Робочий {worker_1.name}, його бос: {worker_1.boss.name}")
print(f"Список робітників {boss_1.name}: {boss_1.workers}")

# перепризначаємо боса за допомогою сетера
worker_1.boss = boss_2

print(f"\nЗміна боса:")
print(f"Новий бос у {worker_1.name}: {worker_1.boss.name}")
print(f"Список робітників {boss_2.name}: {boss_2.workers}")

try:
    worker_1.boss = "Не Бос"
except ValueError as e:
    print(f"\nПомилка: {e}")