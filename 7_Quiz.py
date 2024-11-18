#quiz1
import random
def lotto() :
    result = []
    while len(result) <= 5 :
        num = random.randint(1, 45)
        if num not in result :
            result.append(num)
    return result
print(lotto())

#quiz2
class Gugu :
    def __init__(self, num):
        self.num = num
    def output(self):
        for i in range(1, 10) :
            print(f"{self.num}x{i}={self.num * i}")

num = int(input("단을 입력하세요 :"))
gugu = Gugu(num)
gugu.output()

#quiz3
class SafetyEquipment:
    """
    산업 현장에서 사용되는 안전 장비를 모델링한 클래스.
    """

    def __init__(self, name: str, inspection_cycle: int, status: str):
        """
        안전 장비 초기화
        :param name: 장비 이름
        :param inspection_cycle: 점검 주기 (일 단위)
        :param status: 장비 상태 ('양호', '수리 필요', '불량')
        """
        self.name = name
        self.inspection_cycle = inspection_cycle
        self.status = status

    def inspect(self):
        """장비 점검 상태를 갱신."""
        if self.status == "양호":
            print(f"{self.name}: 상태 양호")
        else:
            print(f"{self.name}: 점검 및 수리 필요")

    def update_status(self, new_status: str):
        """장비 상태 업데이트."""
        self.status = new_status
        print(f"{self.name} 상태가 '{new_status}'로 변경되었습니다.")

    def days_until_next_inspection(self, days_since_last: int):
        """다음 점검까지 남은 일수 계산."""
        days_left = max(0, self.inspection_cycle - days_since_last)
        print(f"{self.name}: 다음 점검까지 {days_left}일 남았습니다.")
        return days_left


class Worker:
    """
    산업 현장에서 작업자를 모델링한 클래스.
    """

    def __init__(self, name: str, role: str, training_completed: bool):
        """
        작업자 초기화
        :param name: 작업자 이름
        :param role: 작업자의 역할
        :param training_completed: 안전 교육 이수 여부
        """
        self.name = name
        self.role = role
        self.training_completed = training_completed

    def attend_training(self):
        """안전 교육 참석."""
        self.training_completed = True
        print(f"{self.name}이(가) 안전 교육을 완료했습니다.")

    def is_eligible_for_work(self):
        """작업 가능 여부 확인."""
        if self.training_completed:
            print(f"{self.name}은(는) 작업 가능 상태입니다.")
            return True
        else:
            print(f"{self.name}은(는) 안전 교육 미이수로 작업이 불가능합니다.")
            return False


class Workplace:
    """
    산업 현장의 안전 관리를 모델링한 클래스.
    """

    def __init__(self, name: str):
        """
        산업 현장 초기화
        :param name: 현장 이름
        """
        self.name = name
        self.safety_equipments = []
        self.workers = []

    def add_equipment(self, equipment: SafetyEquipment):
        """안전 장비 추가."""
        self.safety_equipments.append(equipment)
        print(f"{equipment.name}이(가) {self.name}에 추가되었습니다.")

    def add_worker(self, worker: Worker):
        """작업자 추가."""
        self.workers.append(worker)
        print(f"{worker.name}이(가) {self.name}에 추가되었습니다.")

    def conduct_safety_check(self):
        """전체 안전 점검 수행."""
        print(f"\n[{self.name}] 안전 점검 결과:")
        for equipment in self.safety_equipments:
            equipment.inspect()
        for worker in self.workers:
            worker.is_eligible_for_work()


# 테스트 실행
# 1. 안전 장비 생성
helmet = SafetyEquipment("안전모", inspection_cycle=30, status="양호")
harness = SafetyEquipment("안전벨트", inspection_cycle=15, status="수리 필요")

# 2. 작업자 생성
worker1 = Worker("김철수", role="용접 작업자", training_completed=False)
worker2 = Worker("이영희", role="배관 작업자", training_completed=True)

# 3. 작업장 생성
factory = Workplace("철강 공장")

# 4. 장비와 작업자 추가
factory.add_equipment(helmet)
factory.add_equipment(harness)
factory.add_worker(worker1)
factory.add_worker(worker2)

# 5. 안전 점검 및 교육
factory.conduct_safety_check()
worker1.attend_training()
factory.conduct_safety_check()

# 코드설명
# SafetyEquipment 클래스: 안전 장비의 이름, 점검 주기, 상태를 속성으로 관리하며, 상태 점검 및 갱신 기능
# Worker 클래스: 작업자의 이름, 역할, 안전 교육 이수 여부를 관리하며, 교육 참석과 작업 가능 여부를 확인하는 기능
# Workplace 클래스: 현장의 장비와 작업자를 관리하며, 전체 안전 점검을 수행