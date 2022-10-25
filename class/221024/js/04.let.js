// 변수


/* html
<button>Pree me</button>
*/

// js
// 버튼을 누르면
const button = document.querySelector('button');

button.onclick = function() {
  // 이름을 입력하도록 요청하고 변수에 값을 지정
  let name = prompt('What is your name?');

  // 변수 값에서 가져욘, 이름이 포함된 환영 메세지가 표시
  alert('Hello ' + name + ', nice to see you!');
}


// 변수 선언
var myName; 
var myAge;

myName; // Result: undefined
myAge; // Result: undefined
scoobydoo; // Result: error — scoobyDoo is not defined



// 변수 초기화

myName = 'Chris';
myAge = 37;
// 선언과 동시에 초기화
// var myName = 'Chris';



// 변수 재지정

// 변수의 다른 값을 지정하여 해당 값 업데이트 가능



// 변수의 종류

// 숫자
var myAge = 17;
//문자열
var dolphinGoodbye = 'So long and thanks for all the fish';
// 불리언
var iAmAlive = true;
var test = 6 < 3;
// 배열
var myNameArray = ['Chris', 'Bob', 'Jim'];
var myNumberArray = [10,15,40];
myNameArray[0]; // should return 'Chris'
myNumberArray[2]; // should return 40
// 객체
var dog = { name : 'Spot', breed : 'Dalmatian' };
dog.name
