function app(){
    const buttons = document.querySelectorAll('.button')
    const cards = document.querySelectorAll('.card__items')

    function filter (category, items){
        items.forEach  ((item) => {
            const isItemFiltered = !item.classList.contains(category)
            if (isItemFiltered){
                item.classList.add('hide')
            } else{
                item.classList.remove('hide')
            }
        })
    }

    buttons.forEach((button) => {
        button.addEventListener('click',() =>{
            const currentCategory = button.dataset.filter
            filter(currentCategory, cards)
           
        })
    })

}

app()
