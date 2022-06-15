#
# 2022.06.14.
#
# Created by 김성찬.
#

#
# 06 메타클래스와 애트리뷰트
#

# 메타클래스를 사용하면 파이썬의 class 문을 가로채서 클래스가 정의될 때마다 특별한 동작을 제공할 수 있다.

# 동적으로 애트리뷰트 접근을 커스텀화해주는 내장 기능도 있다.
# 파이썬의 객체지향적인 요소와 위 두 기능이 함께 어우러지면 간단한 클래스를 복잡한 클래스로 쉽게 변환할 수 있다.

# 동적인 애트리뷰트로 객체를 오버라이드하면 예기치 못한 부작용이 생길 수 있다.

title = '''44. 세터와 게터 메서드 대신 평범한 애트리뷰트를 사용하라'''

# 다른 언어를 사용하다 파이썬을 접한 프로그래머들은 클래스에 게터와 세터 메서드를 명시적으로 정의하곤 한다.

class OldResistor:
    def __init__(self, ohms):
        self._ohms = ohms
    
    def get_ohms(self):
        return self._ohms
    
    def set_ohms(self, ohms):
        self._ohms = ohms

# 이런 코드는 파이썬답지 않다.

r0 = OldResistor(50e3)
print("Before:", r0.get_ohms())
r0.set_ohms(10e3)
print("After:", r0.get_ohms())

r0.set_ohms(r0.get_ohms() - 4e3)
assert r0.get_ohms() == 6e3

class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0
    
r1 = Resistor(50e3)
r1.ohms = 10e3

r1.ohms += 5e3

class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0
    
    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms

r2 = VoltageResistance(1e3)
print(f"Before: {r2.current:.2f} 암페어")
r2.voltage = 10
print(f"After: {r2.current:.2f} 암페어")

class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms
    
    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError(f'저항 > 0이어야 한다. 실제 값: {ohms}')
        self._ohms = ohms
    
r3 = BoundedResistance(1e3)
r3.ohms = 0

class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError('Ohms는 불변 객체입니다')
        self._ohms = ohms

r4 = FixedResistance(1e3)
r4.ohms = 2e3

title = '''45. 애트리뷰트를 리팩터링하는 대신 @property를 사용하라'''

