// 1. 배열 만들기
var shopping = ['bread', 'milk', 'cheese', 'hummus', 'noodles'];
shopping; // (5) ['bread', 'mlik', 'cheese', 'hummus', 'noodle']

// 다양한 데이터 저장 가능
var sequence = [1, 1, 2, 3, 5, 8, 13];
var random = ['tree', 795, [0, 1, 2]];



// 2. 접근과 수정
shopping[0]; // 'bread'
shopping[0] = 'tahini';
shopping; // (5) ['tahini', 'mlik', 'cheese', 'hummus', 'noodle']

// 다중배열
random[2][2]; // 2



// 3. 배열 갯수 알아내기
sequence.length; // 7

var sequence = [1, 1, 2, 3, 5, 8, 13];
for (var i = 0; i < sequence.length; i++) {
  console.log(sequence[i]);
}
/*
1
2
2
3
5
8
13
*/


//4. 문자열 -> 배열 / 배열 -> 문자열

//문자열 -> 배열
var myData = 'Manchester,London,Liverpool,Birmingham,Leeds,Carlisle';
var myArray = myData.split(',');
myArray; // (6) ['Manchester', 'London', 'Liverpool', 'Birmingham', 'Leeds', 'Carlisle']
myArray

// 배열 -> 문자열
var myNewString = myArray.join(',');
myNewString; // 'Manchester,London,Liverpool,Birmingham,Leeds,Carlisle'
// join은 다른 구분자 지정가능

var dogNames = ['Rocket','Flash','Bella','Slugger'];
dogNames.toString(); //Rocket,Flash,Bella,Slugger
// toString은 매개변수가 필요 없어서 간단



//5. 배열에 원소 추가/제거
var myArray = ['Manchester', 'London', 'Liverpool', 'Birmingham', 'Leeds', 'Carlisle'];
myArray.push('Cardiff');
myArray; // (7) ['Manchester', 'London', 'Liverpool', 'Birmingham', 'Leeds', 'Carlisle', 'Cardiff']
myArray.push('Bradford', 'Brighton');
myArray; // (9) ['Manchester', 'London', 'Liverpool', 'Birmingham', 'Leeds', 'Carlisle', 'Cardiff', 'Bradford', 'Brighton']

// 새 배열의 길이를 변수에 저장
var newLength = myArray.push('Bristol');
myArray; // ['Manchester', 'London', 'Liverpool', 'Birmingham', 'Leeds', 'Carlisle', 'Cardiff', 'Bradford', 'Brighton', 'Bristol']
newLength; // 10

// 제거
myArray.pop(); // (9) ['Manchester', 'London', 'Liverpool', 'Birmingham', 'Leeds', 'Carlisle', 'Cardiff', 'Bradford', 'Brighton']

var removedItem = myArray.pop();
myArray;
removedItem;

// unshift(), shift()는 push(), pop()과 동일
myArray.unshift('Edinburgh');
myArray; // (9) ['Edinburgh', 'Manchester', 'London', 'Liverpool', 'Birmingham', 'Leeds', 'Carlisle', 'Cardiff', 'Bradford']

var removedItem = myArray.shift();
myArray; // (8) ['Manchester', 'London', 'Liverpool', 'Birmingham', 'Leeds', 'Carlisle', 'Cardiff', 'Bradford']
removedItem; // 'Edinburgh'