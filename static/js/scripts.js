console.log("Script cargado correctamente");

document.addEventListener('submit', function () {

    const name = document.getElementById('name'.value);
    const message = document.getElementById('message'.value);
    const form = document.getElementById('contact-form');
    console.log(name.value, message.value);
});

