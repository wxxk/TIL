// 1. 문자열 만들기

var string = 'The revolution will not be televised.';
string
// 따옴표로 감싸져 있지 않은 텍스트는 
// 변수 이름, 속성이름, 예약어와 유사하다고 가정하기 때문에 작동하지 않는다.


// 2. 따옴표 vs 쌍따옴표
var sgl = 'Single quotes.';
var dbl = "Bouble quotes";
// 차이점이 거의 없어 편한대로 사용 가능
// 하지만 문자열을 감싸는데 한 종류 따옴표만 사용
var sglDbl = 'Would you eat a "fish supper"?';
var dblSgl = "I'm feeling blue.";
// 다른종류의 따옴표가 감싸고 있어 끝나지 않았다고 인식
sglDbl;
dblSgl;


// 3. 문자열 이스케이프 문자
// error - var bigmouth = 'I've got no right to take my place...';
var bigmouth = 'I\'ve got no right to take my place...';
console.log(bigmouth);


// 4. 문자열 연결하기
// 결합
var one = 'Hello, ';
var two = 'how are you?';
var joined = one + two;
joined

// 원하는 만큼 결합
var multiple = one + one + one + one + two;
multiple;

// 문자열과 결합
var response = one + 'I am fine — ' + two;
response;


// 숫자 vs 문자열
// "Front " + 242; -> 숫자를 문자열로 인식하여 연결 : Front 242
// '19' + '67'; -> 1967

// 문자열로 바꾸고 싶지 않은 경우 Number 객체 사용
var myString = '123'
var myNum = Number(myString);
typeof myNum // 숫자

var myNum = 123;
var myString = myNum.toString();
typeof myString // 문자