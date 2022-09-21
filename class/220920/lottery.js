const button = document.querySelector('#lotto-btn')

button.addEventListener('click', function() {

  const ballcontainer = document.createElement('div')
  ballcontainer.classList.add('ball-container')

  const numbers = _.sampleSize(_.range(1, 46), 6)
  numbers.sort((a, b) => (a-b));
  console.log(numbers)
  
  for (let i = 0; i < numbers.length; i++) {
    const ball = document.createElement('div')
    ball.classList.add('ball')
    ball.innerText = numbers[i]
    console.log(numbers[i])
    // 공 색
    if (numbers[i] <= 10) {
      ball.style.backgroundColor = '#FFB400'
    } else if (numbers[i] <= 20) {
      ball.style.backgroundColor = '#3ED0C8'
    } else if (numbers[i] <= 30) {
      ball.style.backgroundColor = '#CD4275'
    } else if (numbers[i] <= 40) {
      ball.style.backgroundColor = '#b4b4b4'
    } else (
      ball.style.backgroundColor = '#40A940'
    )


    ballcontainer.appendChild(ball)
    
    const result = document.querySelector('#result')

    result.appendChild(ballcontainer)
  }
  })