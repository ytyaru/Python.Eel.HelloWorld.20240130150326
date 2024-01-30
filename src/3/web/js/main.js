window.addEventListener('DOMContentLoaded', async(event) => {
    document.querySelector('#save').addEventListener('click', async(event) => {
        eel.save(document.querySelector('#name').value)
    })
})

