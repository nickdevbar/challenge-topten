$(document).ready(async function () {

    fetch('http://127.0.0.1:5000/historiales')
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));

});