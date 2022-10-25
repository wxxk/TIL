// 1. 문자열의 길이
var browserType = 'mozilla';
browserType.length; // 7



// 2. 특정 문자열 찾기
browserType[0]; // 'm'
browserType[browserType.length - 1]; // 'a'



// 3. 문자열 내부의 하위 문자열 찾기 및 추출
browserType.indexOf('zilla'); // 2
// 'm' 'o' 'zilla'
//  0   1     2

browserType.indexOf('vanilla'); // -1

// slice
// 부분 문자열 
browserType.slice(0, 3); // 'moz'

// 특정 문자 뒤에 문자열의 나머지 문자를 모두 추출
browserType.slice(2); // 'zilla'



// 4. 대/소문자 변경
var radData = 'My NaMe Is MuD';
radData.toLowerCase(); // 'my name is mud'
radData.toUpperCase(); // 'MY NAME IS MUD'


// 5. 문자열 일부 변경
browserType.replace('moz', 'van'); // 'vanilla'