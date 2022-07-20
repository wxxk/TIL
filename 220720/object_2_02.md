## 객체 지향의 핵심 개념

### 객체지향의 핵심 4가지

- 추상화: 동작할 수 있는 메서드를 정의한다.
- 상속
- 다형성
- 캡슐화

기능, 정보, 조작을 표현한다.

### 상속

- 클래스 간의 부모-자식 관계를 정립하는 것
- 클래스는 상속이 가능
  - 모든 파이썬 클래스는 object를 상속받음



### 상속 관련 함수와 메서드

- isinstance(object, classinfo)
- issubclass
- super()
  - 자식클래스에서 부모클래스를 사용하고 싶은 경우에 사용한다.

### 상속 정리

- 파이썬의 모든 클래스는 object로부터 상속된다.
- 부모 클래스의 모든 요소가 상속된다.
- **super()**를 통해 부모 클래스의 요소를 호출할 수 있다.
- 메소드 오버라이딩을 통해 자식 클래스에서 정의가 가능하다.

### 다중 상속

- 두개 이상의 클래스를 상속받는 경우
- 상속받은 모든 클래스의 요소

## 

## 다형성 (Polymorphism)

- 여러 모양을 뜻한다.
- 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음을 의미한다.

### 메서드 오버라이딩

- 상속받은 메서드를 재정의 한다.

  즉, 메서드를 덮어쓰기 할 수 있다.

## 캡슐화

실제로 파이썬은 수단과 방법을 써서 접근이 가능하다.

### 접근제어자 종류

- Public Access Modifier: 어디서나 호출이 가능하다.
- Protexted Access Modifier: 부모/자식에서만 접근 가능하다.
- Private Access Modifier: 본인만 접근 가능하다. (클래스 그 자체이다)