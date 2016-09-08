function handleResponse(resp){
  const li = document.createElement('li');
  li.innerHTML = resp;
  document.querySelector('.responses').appendChild(li)
}


function handleClick(event){
  $.ajax({
    url: `hello/${event.target.id}`,
    type: `GET`,
    success(resp){
      handleResponse(resp);
    }
  });
}


document.addEventListener('DOMContentLoaded', () => {
  // document.body.appendChild(document.createElement('p'))
  // let el = document.createElement('p')
  // el.innerHTML = 'JAVASCRIPT'
  // document.body.appendChild(el)
  const buttons = document.getElementsByTagName('button')
  for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', handleClick);
  }

});
