document.getElementById("loginForm").addEventListener("submit", function(event) {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;


    if (username === "admin" && password === "12345") {
        alert("Login bem-sucedido!");
    } else {
        alert("Nome de usuário ou senha incorretos.");
        event.preventDefault();
    }
});
