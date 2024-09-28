document.getElementById("loginForm").addEventListener("submit", function(event) {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Simulação de validação de login (substitua isso pela sua lógica de autenticação)
    if (username === "admin" && password === "12345") {
        alert("Login bem-sucedido!");
    } else {
        alert("Nome de usuário ou senha incorretos.");
        event.preventDefault(); // Impede o envio do formulário se as credenciais estiverem incorretas
    }
});
