document.getElementById('userProfileHide').addEventListener('click', function(){
    console.log('Hello')
    this.style.color = '#F39C11'
    document.getElementById('myOrderHidden').style.color = 'black'
    const profile = document.getElementById('profileHidden')
    profile.classList.remove('d-none')
    const myOrder = document.getElementById('OrderHidden')
    myOrder.classList.add('d-none')


});

document.getElementById('myOrderHidden').addEventListener('click', function(){
    console.log('Hello')
    this.style.color = '#F39C11'
    document.getElementById('userProfileHide').style.color = 'black'
    const myOrder = document.getElementById('OrderHidden')
    myOrder.classList.remove('d-none')

    const profile = document.getElementById('profileHidden')
    profile.classList.add('d-none')
})