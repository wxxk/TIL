// JavaScript 실행 순서

// 이벤트 수신기를 부착
const para = document.querySelector('p');

// 사용자가 문단을 클릭하면 updateName() 코드블록 실행
para.addEventListener('click', updateName);


function updateName() {
  // 이름을 물어보고
  const name = prompt('Enter a new name');
  // 이름을 문단에 삽입해서 화면에 출력
  para.textContent = `Player 1: ${name}`;
}


// ----------------------------------------------

// JavaScript 넣는 법

// 내부 JavaScript
// 닫는 </head> 태그 바로 앞

// 외부 JavaScript
// .js 확장자 파일 생성
// <script scr="[이름].js" defer></script>
// .js 파일 안에 내용 입력

// 인라인 JavaScript 처리기
// 사용하지 않음!
// 대신 addEventListener 사용