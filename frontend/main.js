function getAllBooks(){
    fetch('http://127.0.0.1:5555/books', {
        method: 'GET',
        headers:{
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        const bookList = document.getElementById('bookList');
        bookList.innerHTML = '';
        data.forEach(book => {
            const li = document.createElement('li');
            li.textContent= `Title: ${book.title}, Author: ${book.author}`;
            bookList.appendChild(li)
        });
    })
    .catch(error => console.error('Error:', error))
}

function submitBook(){
    const title = document.getElementById('newTitle').value;
    const author = document.getElementById('newAuthor').value;

    fetch('http://127.0.0.1:5555/update', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({title, author})
    })
    .then(() => {
        alert('Book submitted succesfully');
        document.getElementById('newTitle').value=''
        document.getElementById('newAuthor').value=''
    })
}

function updateBook(){
    const id = document.getElementById('updateId').value;
    const title = document.getElementById('updateTitle').value;
    const author = document.getElementById('updateAuthor').value;

    fetch(`/books/${id}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({title, author})
    })
    .then(()=>{
        alert('Book updated')
    })
    .catch(error => console.error('Error:', error))
}