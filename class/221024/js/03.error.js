// 1. "TypeError: guessSubmit.addeventListener is not a function"
// 호출한 함수를 JavaScript 인터프리터가 인식하지 못했다.
// 보통 오타


// 2. "TypeError: lowOrHi is null"
// 변수에 저장하지 못했다. => console.log([변수])로 값을 확인


// 3. SyntaxError: missing ; before statement
// 보통 줄 끝에 세미콜론을 빠뜨렸을 때 발생

// 4. SyntaxError: missing ) after argument list
// 닫는 괄호 누락

// 5. SyntaxError: missing : after property id
// JavaScript 객체를 잘못된 형태로 작성했을 때 발생

// 6. SyntaxError: missing } after function body
// 함수나 조건문에서 괄호를 누락

// 7. SyntaxError: expected expression, got 'string' 
// 또는 SyntaxError: unterminated string literal
// 따옴표가 빠졌을 경우 발생
// 첫 번째 string 부분에 브라우저가 따옴표 대신 마주친, 예상치 못한 문자 또는 문자열이 들어감
// 두 번째 따옴표로 닫지 않은 문자열이 있다는 의미